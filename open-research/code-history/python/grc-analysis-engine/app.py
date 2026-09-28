from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from grc_analysis_engine.engine.robustness import RobustnessRequest, RobustnessResult, analyze_robustness
from grc_analysis_engine.engine.topology import TopologyResult, analyze_topology
from grc_analysis_engine.graph.networkx_graph import NetworkXGovernanceGraph
from grc_analysis_engine.models.domain import GovernanceGraphPayload


app = FastAPI(
    title="GRC Analysis Engine",
    version="0.1.0",
    description="Deterministic graph analytics for Governance Intelligence.",
)


class RobustnessEnvelope(BaseModel):
    graph: GovernanceGraphPayload
    analysis: RobustnessRequest


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "engine": "GRC Analysis Engine", "version": "0.1.0"}


@app.post("/analysis/topology", response_model=TopologyResult)
def topology(payload: GovernanceGraphPayload) -> TopologyResult:
    return analyze_topology(NetworkXGovernanceGraph(payload))


@app.post("/analysis/robustness", response_model=RobustnessResult)
def robustness(payload: RobustnessEnvelope) -> RobustnessResult:
    graph = NetworkXGovernanceGraph(payload.graph)
    return analyze_robustness(graph, payload.analysis)
