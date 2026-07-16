#!/usr/bin/env python3
"""Download the preregistered MaterialsWorld pilot without persisting credentials."""
from __future__ import annotations

import gzip
import hashlib
import json
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw"
DERIVED = ROOT / "derived"
BASE_URL = "https://api.materialsproject.org/materials/summary/"
SEED = 420042
WINDOW = 100
STRATA = [
    {"id": "N1", "min": 1, "max": 1, "population": 833, "quota": 300},
    {"id": "N2", "min": 2, "max": 2, "population": 21130, "quota": 900},
    {"id": "N3", "min": 3, "max": 3, "population": 91413, "quota": 900},
    {"id": "N4P", "min": 4, "max": 20, "population": 157949, "quota": 900},
]
FIELDS = [
    "material_id", "nelements", "elements", "composition", "structure",
    "symmetry", "band_gap", "formation_energy_per_atom", "is_magnetic",
    "ordering", "density", "volume",
]


def request_json(params: dict, api_key: str, attempts: int = 6) -> dict:
    url = BASE_URL + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(
        url,
        headers={"X-API-KEY": api_key, "User-Agent": "CEOS-MaterialsWorld/0.42"},
    )
    for attempt in range(attempts):
        try:
            with urllib.request.urlopen(req, timeout=90) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == attempts - 1:
                raise
        except (TimeoutError, urllib.error.URLError):
            if attempt == attempts - 1:
                raise
        time.sleep(2 ** attempt)
    raise RuntimeError("unreachable")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    api_key = os.environ.get("MP_API_KEY")
    if not api_key:
        raise SystemExit("Set MP_API_KEY in the process environment; it will not be saved.")

    rng = random.Random(SEED)
    records: list[dict] = []
    sampling_log: list[dict] = []
    api_version = None

    for stratum in STRATA:
        selected: dict[str, dict] = {}
        windows: list[dict] = []
        max_start = max(0, stratum["population"] - WINDOW)
        attempts = 0
        while len(selected) < stratum["quota"]:
            attempts += 1
            if attempts > 200:
                raise RuntimeError(f"Could not fill {stratum['id']} quota")
            start = rng.randint(0, max_start)
            params = {
                "_limit": WINDOW,
                "_skip": start,
                "_sort_fields": "material_id",
                "_fields": ",".join(FIELDS),
                "nelements_min": stratum["min"],
                "nelements_max": stratum["max"],
            }
            payload = request_json(params, api_key)
            api_version = api_version or payload.get("meta", {}).get("api_version")
            before = len(selected)
            for document in payload.get("data", []):
                selected[document["material_id"]] = document
            windows.append({"skip": start, "returned": len(payload.get("data", [])),
                            "new_unique": len(selected) - before})

        chosen = list(selected.values())[: stratum["quota"]]
        for document in chosen:
            document["_ceos_stratum"] = stratum["id"]
        records.extend(chosen)
        sampling_log.append({**stratum, "windows": windows, "selected": len(chosen)})

    # Stable object numbering is independent of download completion order.
    records.sort(key=lambda item: item["material_id"])
    raw_path = RAW / "materials_pilot_3000.jsonl.gz"
    with gzip.open(raw_path, "wt", encoding="utf-8", newline="\n") as stream:
        for item in records:
            stream.write(json.dumps(item, ensure_ascii=False, separators=(",", ":")) + "\n")

    # Blind view: source IDs are replaced; no names/formula labels were requested.
    blind_path = DERIVED / "objects_blind_3000.jsonl.gz"
    map_path = RAW / "object_id_map.jsonl.gz"
    with gzip.open(blind_path, "wt", encoding="utf-8", newline="\n") as blind, \
         gzip.open(map_path, "wt", encoding="utf-8", newline="\n") as mapping:
        for index, item in enumerate(records, start=1):
            object_id = f"Object {index:04d}"
            mapping.write(json.dumps({"object_id": object_id, "material_id": item["material_id"]},
                                     separators=(",", ":")) + "\n")
            clean = {key: value for key, value in item.items() if key != "material_id"}
            clean = {"object_id": object_id, **clean}
            blind.write(json.dumps(clean, ensure_ascii=False, separators=(",", ":")) + "\n")

    extracted_at = datetime.now(timezone.utc).isoformat()
    manifest = {
        "source": "Materials Project summary API",
        "endpoint": BASE_URL,
        "api_version": api_version,
        "extracted_at": extracted_at,
        "requested_fields": FIELDS,
        "sampling": {
            "strategy": "stratified deterministic random contiguous windows",
            "warning": "Cluster-window pilot; not a uniform object-level random sample.",
            "stratification_variable": "nelements",
            "window_size": WINDOW,
            "seed": SEED,
            "population_size_reported": sum(x["population"] for x in STRATA),
            "sample_size": len(records),
            "strata": sampling_log,
        },
        "files": [],
        "credential_persisted": False,
    }
    for path, role in [(raw_path, "immutable raw response records"),
                       (map_path, "restricted source-to-blind ID map"),
                       (blind_path, "blind analysis view")]:
        manifest["files"].append({
            "path": str(path.relative_to(ROOT)), "role": role,
            "records": len(records), "sha256": sha256(path), "bytes": path.stat().st_size,
        })
    manifest_path = RAW / "MANIFEST.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"records": len(records), "api_version": api_version,
                      "raw": str(raw_path), "manifest": str(manifest_path)}, indent=2))


if __name__ == "__main__":
    main()
