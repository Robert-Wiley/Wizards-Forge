import argparse
import json
from pathlib import Path

from evidence_logger import write_log
from research_loop import run_research_cycle


def load_json(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def main():
    parser = argparse.ArgumentParser(description="Governance Research Scout v0.1")
    parser.add_argument("--mission", default="mission.example.json")
    parser.add_argument("--charter", default="charter.json")
    parser.add_argument("--candidates", default=None,
                        help="Optional JSON file containing a list of candidate sources")
    args = parser.parse_args()

    charter = load_json(args.charter)
    mission = load_json(args.mission)
    candidates = load_json(args.candidates) if args.candidates else []

    record = run_research_cycle(mission, charter, candidates)
    outfile = write_log(record)
    print(f"Research cycle complete. Evidence log: {outfile}")
    print(json.dumps(record["counts"], indent=2))


if __name__ == "__main__":
    main()
