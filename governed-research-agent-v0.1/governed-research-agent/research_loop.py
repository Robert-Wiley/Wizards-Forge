from evidence_logger import utc_now


def evaluate_candidate(candidate: dict, charter: dict) -> dict:
    """Governance gate for a candidate source.

    Version 0.1 uses deterministic checks only. A later version can add
    model-directed evaluation while preserving this gate as a control.
    """
    required = ["title", "source_type", "citation", "relevance_summary", "confidence"]
    missing = [field for field in required if not candidate.get(field)]

    decision = "accept"
    rationale = []

    if missing:
        decision = "reject"
        rationale.append(f"Missing required fields: {', '.join(missing)}")

    approved = charter.get("approved_source_types", [])
    if candidate.get("source_type") not in approved:
        decision = "reject"
        rationale.append("Source type is not on the approved-source list.")

    threshold = charter.get("escalation", {}).get("confidence_threshold", 0.70)
    confidence = float(candidate.get("confidence", 0.0) or 0.0)
    if confidence < threshold and decision != "reject":
        decision = "escalate"
        rationale.append(f"Confidence {confidence:.2f} is below threshold {threshold:.2f}.")

    if not rationale:
        rationale.append("Candidate satisfies version 0.1 governance gates.")

    return {
        **candidate,
        "decision": decision,
        "decision_rationale": rationale,
        "evaluated_at": utc_now()
    }


def run_research_cycle(mission: dict, charter: dict, candidates: list[dict]) -> dict:
    evaluated = [evaluate_candidate(c, charter) for c in candidates]
    accepted = [c for c in evaluated if c["decision"] == "accept"]
    escalated = [c for c in evaluated if c["decision"] == "escalate"]
    rejected = [c for c in evaluated if c["decision"] == "reject"]

    return {
        "mission_id": mission["mission_id"],
        "research_question": mission["research_question"],
        "cycle_started_at": utc_now(),
        "agent": charter["agent_name"],
        "agent_version": charter["version"],
        "status": "awaiting_human_review",
        "counts": {
            "considered": len(evaluated),
            "accepted": len(accepted),
            "escalated": len(escalated),
            "rejected": len(rejected)
        },
        "sources": evaluated,
        "synthesis": {
            "constructs_identified": [],
            "theoretical_connections": [],
            "contradictions": [],
            "gaps": [],
            "next_recommended_action": "Human reviews source decisions before synthesis or repository write."
        },
        "human_decision": None,
        "cycle_completed_at": utc_now()
    }
