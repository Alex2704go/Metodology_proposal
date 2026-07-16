#!/usr/bin/env python3
"""Logical consistency audit for Assignment Evidence passports."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/assignment_evidence_passports_v0.2.json';OUT=ROOT/'reports/checkpoint_assignment_admission.md'
def main():
 x=json.loads(SRC.read_text());checks=[]
 for p in x['passports']:
  name=p['formula'];axes=p['evidence_axes'];score=sum(v['score'] for v in axes.values())
  checks += [
   (name,'evidence_sum_exact',score==p['evidence_weight']['score']),
   (name,'admissible_iff_admitted',(p['admissible_family'] is not None)==(p['admission_state']=='ADMITTED')),
   (name,'nearest_always_present',p['nearest_family'] is not None),
   (name,'withheld_reason_required',(p['admission_state']=='ADMITTED') or bool(p['admission_withheld_reason'])),
   (name,'ood_precedence',(not p['assignment_evidence']['ood_flag']) or p['admission_state']=='OOD'),
   (name,'boundary_contract',(p['admission_state']!='BOUNDARY') or (not p['assignment_evidence']['ood_flag'] and p['assignment_evidence']['margin']<.05)),
   (name,'admitted_all_axes',(p['admission_state']!='ADMITTED') or all(v['status']=='PASS' for v in axes.values())),
   (name,'interpretation_support_nonempty',bool(p['interpretation_boundary']['supports'])),
   (name,'interpretation_prohibitions_nonempty',bool(p['interpretation_boundary']['does_not_support'])),
   (name,'physical_mechanism_not_supported','physical mechanism' in p['interpretation_boundary']['does_not_support']),
   (name,'relation_evaluation_contract',(p['knowledge_state']['relation_pattern_evaluation']=='NOT_EVALUATED' and p['knowledge_state']['relation_pattern_id'] is None) or (p['knowledge_state']['relation_pattern_evaluation']=='EVALUATED' and p['knowledge_state']['relation_pattern_id'] is not None)),
  ]
 passed=sum(ok for _,_,ok in checks);lines=['# Checkpoint — Assignment Admission Logic','',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','', '| Object | Check | Result |','|---|---|---|']
 for obj,c,ok in checks:lines.append(f"| {obj} | `{c}` | {'PASS' if ok else '**FAIL**'} |")
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Assignment Admission audit failed')
 print({'checks':len(checks),'passed':passed,'failed':0})
if __name__=='__main__':main()
