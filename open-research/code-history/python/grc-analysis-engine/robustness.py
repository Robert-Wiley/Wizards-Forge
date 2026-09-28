from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from grc_analysis_engine.graph.networkx_graph import NetworkXGovernanceGraph


class Fragility(str, Enum):
    STABLE = "stable"
    CONDITIONAL = "conditional"
    FRAGILE = "fragile"
    NO_BASELINE_PATH = "no_baseline_path"


class PerturbationResult(BaseModel):
    object_id: str
    object_type: str
    path_survives: bool


class RobustnessRequest(BaseModel):
    source: str
    target: str
    relationship_ids: list[str] | None = None
    node_ids: list[str] | None = None


class RobustnessResult(BaseModel):
    source: str
    target: str
    baseline_path_exists: bool
    perturbations_tested: int
    surviving_perturbations: int
    survival_ratio: float = Field(ge=0.0, le=1.0)
    fragility: Fragility
    results: list[PerturbationResult]


def _classify(baseline: bool, ratio: float) -> Fragility:
    if not baseline:
        return Fragility.NO_BASELINE_PATH
    if ratio >= 0.80:
        return Fragility.STABLE
    if ratio >= 0.40:
        return Fragility.CONDITIONAL
    return Fragility.FRAGILE


def analyze_robustness(
    graph: NetworkXGovernanceGraph,
    request: RobustnessRequest,
) -> RobustnessResult:
    baseline = graph.has_directed_path(request.source, request.target)
    if not baseline:
        return RobustnessResult(
            source=request.source,
            target=request.target,
            baseline_path_exists=False,
            perturbations_tested=0,
            surviving_perturbations=0,
            survival_ratio=0.0,
            fragility=Fragility.NO_BASELINE_PATH,
            results=[],
        )

    rel_ids = request.relationship_ids or [r.id for r in graph.relationships()]
    node_ids = request.node_ids or [
        n.id for n in graph.nodes() if n.id not in {request.source, request.target}
    ]

    results: list[PerturbationResult] = []
    for rel_id in rel_ids:
        perturbed = graph.copy_without_relationship(rel_id)
        results.append(
            PerturbationResult(
                object_id=rel_id,
                object_type="relationship",
                path_survives=perturbed.has_directed_path(request.source, request.target),
            )
        )

    for node_id in node_ids:
        if node_id in {request.source, request.target}:
            continue
        perturbed = graph.copy_without_node(node_id)
        results.append(
            PerturbationResult(
                object_id=node_id,
                object_type="node",
                path_survives=perturbed.has_directed_path(request.source, request.target),
            )
        )

    tested = len(results)
    surviving = sum(result.path_survives for result in results)
    ratio = surviving / tested if tested else 1.0

    return RobustnessResult(
        source=request.source,
        target=request.target,
        baseline_path_exists=True,
        perturbations_tested=tested,
        surviving_perturbations=surviving,
        survival_ratio=round(ratio, 6),
        fragility=_classify(True, ratio),
        results=results,
    )
