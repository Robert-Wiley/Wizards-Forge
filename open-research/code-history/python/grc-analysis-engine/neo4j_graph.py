"""Neo4j adapter boundary.

The deterministic engine does not depend on this module. The next pass will
implement payload loading/persistence through the official Neo4j driver and
optionally delegate large-scale algorithms to Graph Data Science (GDS).
"""

from __future__ import annotations


class Neo4jGovernanceGraph:
    def __init__(self, uri: str, username: str, password: str):
        self.uri = uri
        self.username = username
        self.password = password
        raise NotImplementedError(
            "Neo4j persistence is intentionally staged for AE-06; use "
            "NetworkXGovernanceGraph for v0.1 deterministic execution."
        )
