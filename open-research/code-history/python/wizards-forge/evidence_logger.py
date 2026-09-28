import json
from datetime import datetime, timezone
from pathlib import Path


def utc_now():
    return datetime.now(timezone.utc).isoformat()


def write_log(record: dict, output_dir: str = "output") -> str:
    path = Path(output_dir)
    path.mkdir(parents=True, exist_ok=True)
    mission_id = record.get("mission_id", "mission")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    outfile = path / f"{mission_id}_{stamp}.json"
    outfile.write_text(json.dumps(record, indent=2), encoding="utf-8")
    return str(outfile)
