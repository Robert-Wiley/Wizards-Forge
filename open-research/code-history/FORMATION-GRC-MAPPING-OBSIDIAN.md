# Obsidian / GRC Mapping Formation Record

This record preserves how the GRC Mapping moved from canonical Atlas data into a navigable Obsidian topology.

It is deliberately explicit about what was actually executed and what did **not** exist as a standalone file.

## Historical truth

The bulk formation of the Obsidian GRC Mapping was orchestrated interactively through connected research tooling and GitHub operations. There was **no original standalone Python generator file** that produced the vault.

For that reason, this archive does not fabricate one after the fact.

A future reproducibility script may be written, but it must be labeled **retrospective reproduction code**, not original formation code.

## Formation sequence

### 1. Private vault scaffold
Repository: `Robert-Wiley/GRC-Atlas-obsidian`

Initial structure established folders for:
- Governance
- Risk
- Compliance
- Relationships
- Frameworks
- Research
- Concepts
- Experiments
- Maps
- Templates

Notion remained canonical; Obsidian was established as the relational discovery layer.

### 2. Pilot topology
The first pilot imported:
- 3 Governance objects
- 3 Risk objects
- 3 Compliance objects
- 4 canonical relationships

Pilot relationship examples included:
- GOV-001 → RSK-001
- GOV-001 → CMP-001
- CMP-001 → CMP-002
- CMP-001 → CMP-003

Pilot completion commit:
`792c1f9f5c945cc7690792f9d9a1d179a2848e18`

The pilot proved that canonical IDs could become Obsidian notes and first-class relationship records without creating ghost nodes.

### 3. Canonical integrity checks
Before bulk expansion:
- 286 total GRC objects
- 286 distinct object IDs
- 0 missing object IDs
- 715 total relationships
- 715 distinct relationship IDs
- 0 missing relationship IDs

Object distribution:
- Governance: 51
- Risk: 103
- Compliance: 132

Relationship confidence distribution:
- Confirmed: 383
- Supported: 64
- Hypothesis: 268

### 4. Full object layer
All 286 canonical GRC objects were represented as lightweight authoritative graph nodes in Markdown.

The graph-first mirror intentionally did not pretend to contain all long-form Notion body content.

Full object layer commit:
`17639c0606240440a02d794b2c59974d0e351fc8`

### 5. Full relationship layer
All 715 governed relationships were represented as first-class Markdown records under `Relationships/`.

Each relationship resolved to actual source and target object files, avoiding unresolved/ghost topology.

Full relationship layer commit:
`333a191a9df336d9cccf6a0715b113744bdcdd5f`

Final tree at that stage:
`2cedd3cdb08bf3c663cb49827a61599da36fe2e8`

### 6. Desktop Obsidian activation
Local vault:
`C:\Obsidian\GRC-Atlas-obsidian`

Obsidian Git was used to pull the repository.

A stale Windows proxy configuration initially blocked Git:
- `HTTP_PROXY=http://localhost:9090`
- `HTTPS_PROXY=http://localhost:9090`

The persistent proxy variables were removed, Obsidian restarted, and Git reported:
**Pull is up to date.**

That was the point at which the complete topology became available as a local interactive Obsidian graph.

### 7. Public visualization
The private 286-object / 715-relationship graph remained the research workbench.

A governed public-review export was created separately and rendered through the live GitHub Pages topology.

The first public visualization contained:
- 280 Review-stage nodes
- 317 Review-stage edges
- 6 held nodes excluded

The resulting Compliance-centered geometry exposed that the currently released edge layer consisted of Compliance-to-Compliance relationships, while Governance and Risk nodes remained isolated in the public export.

That visual anomaly was retained as research history rather than cosmetically hidden.

## Why this formation record matters

The topology did not emerge from a single script.

It emerged from:
1. canonical data governance,
2. integrity checks,
3. pilot representation,
4. bulk object representation,
5. bulk relationship representation,
6. version control,
7. local graph rendering,
8. and later public-safe visualization.

That sequence is part of the research method.

## Future reproducibility work

A future script may automate:
- canonical object extraction,
- relationship validation,
- Markdown generation,
- filename resolution,
- link construction,
- topology integrity checks,
- and publication-safe export.

If created, that code should cite this record and identify itself as a **reproduction implementation**, not the original historical generator.
