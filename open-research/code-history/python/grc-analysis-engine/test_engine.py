import json
from pathlib import Path

from grc_analysis_engine.engine.robustness import RobustnessRequest, analyze_robustness
from grc_analysis_engine.engine.topology import analyze_topology
from grc_analysis_engine.graph.networkx_graph import NetworkXGovernanceGraph
from grc_analysis_engine.models.domain import GovernanceGraphPayload


def sample_graph() -> NetworkXGovernanceGraph:
    path = Path(__file__).parents[1] / "data" / "sample_graph.json"
    payload = GovernanceGraphPayload.model_validate(json.loads(path.read_text()))
    return NetworkXGovernanceGraph(payload)


def test_topology_finds_assurance_chain_articulation_points():
    result = analyze_topology(sample_graph())
    assert result.node_count == 6
    assert result.relationship_count == 6
    assert "CTRL-001" in result.articulation_points
    assert "EVID-001" in result.articulation_points


def test_robustness_detects_fragile_final_assurance_seam():
    graph = sample_graph()
    result = analyze_robustness(
        graph,
        RobustnessRequest(
            source="GOV-001",
            target="ASSR-001",
            relationship_ids=["REL-0001", "REL-0002", "REL-0005", "REL-0006"],
            node_ids=["PROC-001", "PROC-002", "CTRL-001", "EVID-001"],
        ),
    )
    lookup = {r.object_id: r.path_survives for r in result.results}
    assert lookup["REL-0001"] is True
    assert lookup["REL-0002"] is True
    assert lookup["REL-0005"] is False
    assert lookup["REL-0006"] is False
    assert lookup["CTRL-001"] is False
    assert lookup["EVID-001"] is False
    assert result.baseline_path_exists is True
