#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python3 -m compileall -q scripts
python3 scripts/validate_governance_v0_2.py
PYTHONPATH=scripts python3 scripts/run_system_null_ladder_v0_2.py
python3 scripts/validate_cross_mapping_passports.py
python3 scripts/check_claim_type_system.py
python3 scripts/audit_assignment_passports.py
python3 scripts/audit_assignment_explanations.py
python3 scripts/audit_conflict_topology.py
python3 scripts/audit_relation_pattern_registry.py
python3 scripts/apply_interpretation_boundaries.py
python3 scripts/lint_ceos_documents.py

python3 - <<'PY'
from pathlib import Path
import json, yaml
root=Path('.')
for path in root.rglob('*.yaml'):
    yaml.safe_load(path.read_text())
for path in root.rglob('*.json'):
    json.load(path.open(encoding='utf-8'))
print({'integrity_gate':'PASS','fail_fast':True,'yaml_json_valid':True})
PY
