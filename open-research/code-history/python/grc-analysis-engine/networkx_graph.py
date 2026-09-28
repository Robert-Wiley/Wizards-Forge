from __future__ import annotations

import networkx as nx

from grc_analysis_engine.graph.base import GovernanceGraph
from grc_analysis_engine.models.domain import GovernanceGraphPayload, GovernanceNode, GovernanceRelationship


class NetworkXGovernanceGraph(GovernanceGraph):
    def __init__(self, payload: GovernanceGraphPayload):
        self.payload = payload
        self.graph = nx.MultiDiGraph()
        self._node_index = {node.id: node for node in payload.nodes}
        self._rel_index = {rel.id: rel for rel in payload.relationships}

        for node in payload.nodes:
            self.graph.add_node(node.id, model=node)
        for rel in payload.relationships:
            self.graph.add_edge(rel.source, rel.target, key=rel.id, model=rel)

    def nodes(self):
        return self._node_index.values()

    def relationships(self):
        return self._rel_index.values()

    def node_count(self) -> int:
        return self.graph.number_of_nodes()

    def relationship_count(self) -> int:
        return self.graph.number_of_edges()

    def copy_without_relationship(self, relationship_id: str) -> "NetworkXGovernanceGraph":
        relationships = [r for r in self.payload.relationships if r.id != relationship_id]
        return NetworkXGovernanceGraph(
            GovernanceGraphPayload(nodes=self.payload.nodes, relationships=relationships)
        )

    def copy_without_node(self, node_id: str) -> "NetworkXGovernanceGraph":
        nodes = [n for n in self.payload.nodes if n.id != node_id]
        relationships = [
            r for r in self.payload.relationships
            if r.source != node_id and r.target != node_id
        ]
        return NetworkXGovernanceGraph(
            GovernanceGraphPayload(nodes=nodes, relationships=relationships)
        )

    def has_directed_path(self, source: str, target: str) -> bool:
        if source not in self.graph or target not in self.graph:
            return False
        return nx.has_path(self.graph, source, target)

    def simple_undirected(self) -> nx.Graph:
        graph = nx.Graph()
        graph.add_nodes_from(self.graph.nodes)
        graph.add_edges_from((u, v) for u, v, _ in self.graph.edges(keys=True))
        return graph
