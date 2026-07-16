#!/usr/bin/env python3
"""Arithmetic and contract audit for Assignment Explanations."""
import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/assignment_explanations_v0.1.json';SEL=ROOT/'derived/stress_selection_blind.json';OUT=ROOT/'reports/checkpoint_assignment_explanation.md'
def main():
 x=json.loads(SRC.read_text());s=json.loads(SEL.read_text());blind={q['object_id']:q for q in s['selected']};checks=[]
 for o in x['objects']:
  name=o['formula'];b=blind[o['object_id']]['views']['ORGANIZATION'];r=o['channels']['representation'];checks += [(name,'frozen_nearest_match',r['nearest_family']==b['nearest_family']),(name,'frozen_distance_match',abs(r['nearest_distance']-b['nearest_distance'])<1e-12),(name,'frozen_margin_match',abs(r['margin']-b['margin'])<1e-12)]
  for rank in ['nearest','second']:
   q=o['centroid_distance_decomposition'][rank];summed=sum(q['by_block_squared'].values());target=(r['nearest_distance'] if rank=='nearest' else r['second_distance'])**2;checks.append((name,f'{rank}_block_sum_exact',abs(summed-target)<1e-10))
  n=o['scale_nulls'];rule=r['ood_flag'] and not n['REMOVE_SCALE_SENSITIVE_STRUCTURE_OBSERVABLES']['ood_flag'] and not n['STRUCTURE_BLOCK_UNIT_NORM']['ood_flag'];checks.append((name,'scale_rule_exact',rule==n['scale_driven_by_registered_rule']));checks.append((name,'no_probabilities',x['probabilities_used'] is False));checks.append((name,'hull_family_matches_nearest',o['convex_hull']['family']==r['nearest_family']))
 passed=sum(ok for _,_,ok in checks);lines=['# Checkpoint — Assignment Explanation Integrity','',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','', '| Object | Check | Result |','|---|---|---|']+[f"| {a} | `{b}` | {'PASS' if c else '**FAIL**'} |" for a,b,c in checks]
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Explanation audit failed')
 print({'checks':len(checks),'passed':passed,'failed':0})
if __name__=='__main__':main()
