#!/usr/bin/env python3
"""Validate Cross Mapping Passports against schema and monotonic maturity contracts."""
import json
from pathlib import Path
from jsonschema import Draft202012Validator
ROOT=Path(__file__).resolve().parents[1];SCHEMA=ROOT/'schemas/cross_mapping_passport.schema.json';OUT=ROOT/'reports/checkpoint_cross_mapping_passports.md'
def logical_checks(x):
 s=x['mapping_stability'];m=s['maturity'];o=s['observed_across'];checks=[]
 checks.append(('mapping_strength_separate_from_evidence_strength',x['mapping_strength'] is not x['evidence_strength']))
 checks.append(('not_tested_consistency',m!='NOT_TESTED' or not any(o.values())))
 checks.append(('single_world_consistency',m not in {'SINGLE_WORLD','MULTI_WORLD','INDEPENDENTLY_REPLICATED'} or o['one_world']))
 checks.append(('multi_world_consistency',m not in {'MULTI_WORLD','INDEPENDENTLY_REPLICATED'} or o['multiple_worlds']))
 checks.append(('independent_replication_consistency',m!='INDEPENDENTLY_REPLICATED' or (o['independent_datasets'] and o['independent_observers'])))
 checks.append(('failed_is_outcome_not_maturity',m!='FAILED' and s['qualification_outcome'] in {'NOT_RUN','PASS','MIXED','FAILED'}))
 checks.append(('asymmetry_acknowledged',x['cross_mapping_asymmetry_acknowledged'] is True))
 e=x['epistemic_effect'];checks.append(('mapping_descriptive_only',e['mapping_is_descriptive'] is True and e['upgrades_source_ontology'] is False and e['upgrades_target_ontology'] is False))
 checks.append(('independent_evidence_required_for_upgrade',e['independent_admitted_evidence_required_for_upgrade'] is True))
 checks.append(('untested_prediction_prohibited','prediction of untested properties' in x['interpretation_boundary']['does_not_support']))
 return checks
def main():
 schema=json.loads(SCHEMA.read_text());validator=Draft202012Validator(schema);files=sorted((ROOT/'config').glob('cross_mapping_passport*.json'));rows=[]
 for p in files:
  x=json.loads(p.read_text());errors=sorted(validator.iter_errors(x),key=lambda e:list(e.path));rows.append((p.name,'json_schema',not errors,'; '.join(e.message for e in errors)))
  for name,ok in logical_checks(x):rows.append((p.name,name,ok,''))
 passed=sum(r[2] for r in rows);lines=['# Checkpoint — Cross Mapping Passport Specification','', '> **Status:** schema-conformance check only. Mapping Admission remains `REASSESSMENT_REQUIRED` after System Null Ladder v0.1.','',f'- Passports: **{len(files)}**',f'- Checks: **{len(rows)}**',f'- Passed: **{passed}**',f'- Failed: **{len(rows)-passed}**','', '| Passport | Check | Result | Detail |','|---|---|---|---|']+[f"| `{a}` | `{b}` | {'PASS' if c else '**FAIL**'} | {d} |" for a,b,c,d in rows]
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(rows):raise SystemExit('Cross Mapping Passport validation failed')
 print({'passports':len(files),'checks':len(rows),'passed':passed,'failed':0})
if __name__=='__main__':main()
