# Governed Research Agent

Governance Research Scout v0.1 is a deliberately small research-agent prototype.

## Purpose

Prove the core governed-agent pattern before adding web search, LLM reasoning, repository writes, or multi-agent orchestration.

Core loop:

Mission -> Observe -> Interpret -> Decide -> Act -> Verify -> Record -> Human Review

## Files

- `charter.json` — machine-readable mission, authority, prohibitions, evidence rules, and escalation threshold.
- `mission.example.json` — first Theory of Governance Dynamics research mission.
- `candidates.example.json` — two sample sources for a dry run.
- `research_loop.py` — deterministic governance gate and research-cycle structure.
- `evidence_logger.py` — immutable-style JSON evidence-log writer.
- `agent.py` — command-line entry point.
- `output/` — generated telemetry/evidence records.

## Run

```bash
python agent.py --mission mission.example.json --candidates candidates.example.json
```

## Version 0.1 design principle

The agent is not yet autonomous. That is intentional. First establish governance, evidence, and escalation behavior; then add model-directed action selection and external observation.

## Next build increments

1. Add public research-source search.
2. Add model-directed relevance scoring and construct extraction.
3. Add citation verification.
4. Add a human approval command that changes state from `awaiting_human_review` to approved/rejected.
5. Add Notion/GRC Atlas write capability only after approval.
6. Add Research Critic as Agent #2.
