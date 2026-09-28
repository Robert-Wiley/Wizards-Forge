from __future__ import annotations

from pydantic import BaseModel
import networkx as nx

from grc_analysis_engine.graph.networkx_graph import NetworkXGovernanceGraph


class CentralityScore(BaseModel):
    node_id: str
    degree_centrality: float


class TopologyResult(BaseModel):
    node_count: int
    relationship_count: int
    connected_components: int
    articulation_points: list[str]
    bridges: list[tuple[str, str]]
    centrality: list[CentralityScore]


def analyze_topology(graph: NetworkXGovernanceGraph) -> TopologyResult:
    undirected = graph.simple_undirected()
    articulation_points = sorted(nx.articulation_points(undirected))
    bridges = sorted(tuple(sorted(edge)) for edge in nx.bridges(undirected))
    degree = nx.degree_centrality(undirected)
    centrality = [
        CentralityScore(node_id=node_id, degree_centrality=score)
        for node_id, score in sorted(degree.items(), key=lambda item: (-item[1], item[0]))
    ]
    return TopologyResult(
        node_count=graph.node_count(),
        relationship_count=graph.relationship_count(),
        connected_components=nx.number_connected_components(undirected),
        articulation_points=articulation_points,
        bridges=bridges,
        centrality=centrality,
    )
