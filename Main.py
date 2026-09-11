from flask import Flask, jsonify
import subprocess
import sys
from pathlib import Path

app = Flask(__name__)

SCOUT_DIR = Path("agents/agent_001_research_scout")


@app.route("/")
def home():
    return jsonify({
        "system": "Wizard's Forge",
        "status": "online",
        "agent_001": "Governance Research Scout",
        "agent_status": "ready"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
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
