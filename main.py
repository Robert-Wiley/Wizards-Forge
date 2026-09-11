from flask import Flask, jsonify, request
import subprocess
import sys
import json
from pathlib import Path
from datetime import datetime, timezone

app = Flask(__name__)

SCOUT_DIR = Path("agents/agent_001_research_scout")
MISSION_FILE = SCOUT_DIR / "mission.runtime.json"

PENDING_APPROVAL = {}


@app.route("/")
def home():
    return jsonify({
        "system": "Wizard's Forge",
        "status": "online",
        "agent_001": "Governance Research Scout",
        "agent_status": "ready",
        "version": "0.2"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/submit-mission", methods=["POST"])
def submit_mission():
    data = request.get_json(silent=True) or {}

    research_question = data.get("research_question", "").strip()

    if not research_question:
        return jsonify({
            "error": "research_question is required"
        }), 400

    mission_id = f"M-{datetime.now(timezone.utc).strftime('%Y%m%d%H%M%S')}"

    mission = {
        "mission_id": mission_id,
        "research_question": research_question,
        "submitted_at": datetime.now(timezone.utc).isoformat(),
        "submitted_by": "human",
        "approval_required": True
    }

    MISSION_FILE.write_text(
        json.dumps(mission, indent=2),
        encoding="utf-8"
    )

    result = subprocess.run(
        [
            sys.executable,
            "agent.py",
            "--mission",
            "mission.runtime.json",
            "--charter",
            "charter.json",
            "--candidates",
            "candidates.example.json"
        ],
        cwd=SCOUT_DIR,
        capture_output=True,
        text=True
    )

    PENDING_APPROVAL[mission_id] = {
        "status": "AWAITING_HUMAN_APPROVAL",
        "research_question": research_question,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "return_code": result.returncode
    }

    return jsonify({
        "mission_id": mission_id,
        "status": "AWAITING_HUMAN_APPROVAL",
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    })


@app.route("/approval/<mission_id>", methods=["GET"])
def approval_status(mission_id):
    mission = PENDING_APPROVAL.get(mission_id)

    if not mission:
        return jsonify({
            "error": "mission not found"
        }), 404

    return jsonify({
        "mission_id": mission_id,
        **mission
    })


@app.route("/approval/<mission_id>", methods=["POST"])
def approval_decision(mission_id):
    mission = PENDING_APPROVAL.get(mission_id)

    if not mission:
        return jsonify({
            "error": "mission not found"
        }), 404

    data = request.get_json(silent=True) or {}
    decision = data.get("decision", "").upper()

    if decision not in {"APPROVE", "REJECT"}:
        return jsonify({
            "error": "decision must be APPROVE or REJECT"
        }), 400

    mission["status"] = (
        "APPROVED" if decision == "APPROVE" else "REJECTED"
    )
    mission["decision"] = decision
    mission["decided_at"] = datetime.now(timezone.utc).isoformat()

    return jsonify({
        "mission_id": mission_id,
        "status": mission["status"],
        "decision": decision
    })


@app.route("/run-scout")
def run_scout():
    result = subprocess.run(
        [
            sys.executable,
            "agent.py",
            "--mission",
            "mission.example.json",
            "--charter",
            "charter.json",
            "--candidates",
            "candidates.example.json"
        ],
        cwd=SCOUT_DIR,
        capture_output=True,
        text=True
    )

    return jsonify({
        "return_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    })
