from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator


class NodeType(str, Enum):
    GOVERNANCE = "GOV"
    RISK = "RSK"
    COMPLIANCE = "CMP"
    REQUIREMENT = "REQ"
    CONTROL = "CTRL"
    EVIDENCE = "EVID"
    STANDARD = "STD"
    ASSURANCE = "ASSR"
    ACTOR = "ACT"
    ASSET = "AST"
    PROCESS = "PROC"
    OTHER = "OTHER"


class GovernanceNode(BaseModel):
    id: str = Field(min_length=1)
    node_type: NodeType = NodeType.OTHER
    name: str = Field(min_length=1)
    attributes: dict[str, Any] = Field(default_factory=dict)


class GovernanceRelationship(BaseModel):
    id: str = Field(min_length=1)
    source: str = Field(min_length=1)
    target: str = Field(min_length=1)
    relationship_type: str = Field(min_length=1)
    strength: float = Field(default=1.0, ge=0.0, le=1.0)
    confidence: float = Field(default=1.0, ge=0.0, le=1.0)
    criticality: float = Field(default=0.5, ge=0.0, le=1.0)
    propagation_potential: float = Field(default=0.5, ge=0.0, le=1.0)
    seam_type: str | None = None
    attributes: dict[str, Any] = Field(default_factory=dict)


class GovernanceGraphPayload(BaseModel):
    nodes: list[GovernanceNode]
    relationships: list[GovernanceRelationship]

    @model_validator(mode="after")
    def references_must_exist(self) -> "GovernanceGraphPayload":
        ids = {node.id for node in self.nodes}
        if len(ids) != len(self.nodes):
            raise ValueError("Node IDs must be unique")
        rel_ids = {rel.id for rel in self.relationships}
        if len(rel_ids) != len(self.relationships):
            raise ValueError("Relationship IDs must be unique")
        missing = {
            endpoint
            for rel in self.relationships
            for endpoint in (rel.source, rel.target)
            if endpoint not in ids
        }
        if missing:
            raise ValueError(f"Relationships reference missing nodes: {sorted(missing)}")
        return self
