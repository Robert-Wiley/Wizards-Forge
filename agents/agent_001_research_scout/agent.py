import argparse
import json
from pathlib import Path

from external_observer import search_crossref
from research_loop import run_research_cycle


def load_json(path):
    return json.loads(
        Path(path).read_text(
            encoding="utf-8"
        )
    )


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--mission",
        required=True
    )

    parser.add_argument(
        "--charter",
        required=True
    )

    parser.add_argument(
        "--candidates",
        required=False
    )

    args = parser.parse_args()

    mission = load_json(args.mission)
    charter = load_json(args.charter)

    research_question = mission.get(
        "research_question"
    )

    if not research_question:
        raise ValueError(
            "Mission does not contain "
            "research_question"
        )

    print(
        f"External observation initiated: "
        f"{research_question}"
    )

    candidates = search_crossref(
        research_question,
        rows=5
    )

    candidate_file = Path(
        "candidates.runtime.json"
    )

    candidate_file.write_text(
        json.dumps(
            candidates,
            indent=2
        ),
        encoding="utf-8"
    )

    print(
        f"Observed {len(candidates)} "
        f"scholarly candidates."
    )

    run_research_cycle(
        mission=mission,
        charter=charter,
        candidates=candidates
    )


if __name__ == "__main__":
    main()
