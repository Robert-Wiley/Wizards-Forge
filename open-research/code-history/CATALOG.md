# Computational Artifact Catalog

Snapshot date: 2026-09-28

| Snapshot | Original repository/path | Blob SHA | Historical role |
|---|---|---|---|
| `python/wizards-forge/main.py` | Wizards-Forge / `main.py` | `e66db898...` | Human-facing mission submission, execution, approval boundary |
| `python/wizards-forge/agent.py` | Wizards-Forge / `agents/agent_001_research_scout/agent.py` | `c47c2b711...` | Research mission orchestration |
| `python/wizards-forge/external_observer.py` | Wizards-Forge / `.../external_observer.py` | `b6fcc7994...` | External scholarly observation via Crossref |
| `python/wizards-forge/research_loop.py` | Wizards-Forge / `.../research_loop.py` | `fe5d7fd8b...` | Deterministic evidence/source governance gates |
| `python/wizards-forge/evidence_logger.py` | Wizards-Forge / `.../evidence_logger.py` | `773a90e47...` | Evidence persistence and timestamping |
| `python/grc-analysis-engine/domain.py` | GRC-Analysis-Engine / `src/.../models/domain.py` | `be07adc35...` | Executable graph ontology and referential integrity |
| `python/grc-analysis-engine/networkx_graph.py` | GRC-Analysis-Engine / `src/.../graph/networkx_graph.py` | `b1973f8e0...` | Directed graph implementation |
| `python/grc-analysis-engine/topology.py` | GRC-Analysis-Engine / `src/.../engine/topology.py` | `e171d9af0...` | Structural graph metrics |
| `python/grc-analysis-engine/robustness.py` | GRC-Analysis-Engine / `src/.../engine/robustness.py` | `2acf72fca...` | Perturbation and early assurance-fragility logic |
| `python/grc-analysis-engine/neo4j_graph.py` | GRC-Analysis-Engine / `src/.../graph/neo4j_graph.py` | `4dcdef800...` | Explicit future scale/persistence boundary |
| `python/grc-analysis-engine/app.py` | GRC-Analysis-Engine / `src/.../api/app.py` | `7dbf524db...` | API surface for deterministic analysis |
| `python/grc-analysis-engine/test_engine.py` | GRC-Analysis-Engine / `tests/test_engine.py` | `4070a9118...` | Executable assertions for topology and fragility |

## Reading rule

The SHA is part of the artifact identity. If a current source file later changes, this archive remains a record of the state represented here.
