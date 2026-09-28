# Computational Research History

This archive preserves executable artifacts as **research history**, not merely source code.

Each snapshot is kept so future readers can see how the research became computational: what the code attempted, what assumptions it encoded, and how later work extended or replaced it.

## Historical source points

- **Wizard's Forge source commit:** `1ef9d97b08e41f3982d210c4123f038ed353463a`
- **GRC Analysis Engine source commit:** `090070f65575874209c9118ad723397ff1fd6c9b`
- Snapshot date: **2026-09-28**

## Archive groups

### Wizard's Forge
Early governed agent/research-loop implementation:
- `main.py` — web/API surface and human approval gate
- `agent.py` — mission entry point and external-observation orchestration
- `external_observer.py` — Crossref scholarly observation adapter
- `research_loop.py` — deterministic candidate governance gate
- `evidence_logger.py` — timestamped evidence record persistence

### GRC Analysis Engine
Early deterministic computational-governance implementation:
- `domain.py` — typed graph ontology and integrity validation
- `networkx_graph.py` — executable directed governance graph
- `topology.py` — connected components, articulation points, bridges, degree centrality
- `robustness.py` — perturbation testing, path survival, and early fragility classification
- `neo4j_graph.py` — explicit future persistence/scale boundary
- `app.py` — FastAPI analysis interface
- `test_engine.py` — early executable assertions about topology and assurance fragility

## Why preserve these files?

The code captures decisions that prose alone cannot:
- what counted as a node or relationship,
- which graph semantics were executable,
- how fragility was initially classified,
- where human approval was inserted,
- what was intentionally deterministic,
- and what capabilities were explicitly deferred.

## Important historical rule

These snapshots are **not silently updated** as production code changes. They are historical evidence.

Current implementations remain in their source repositories.

See also:
- [Obsidian / GRC Mapping Formation Record](FORMATION-GRC-MAPPING-OBSIDIAN.md)
- [Artifact Catalog](CATALOG.md)
