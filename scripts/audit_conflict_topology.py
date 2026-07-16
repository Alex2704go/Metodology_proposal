#!/usr/bin/env python3
"""Contract audit for Conflict Topology v0.2."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/conflict_topology_v0.3.json';EX=ROOT/'derived/assignment_explanations_v0.1.json';OUT=ROOT/'reports/checkpoint_conflict_topology.md'
def canonical(votes,order):
 short={'global':'G','local':'L','composition':'C','structure':'S','symmetry':'Y','observer':'O'};fmap={};groups=[]
 for n in order:
  f=votes[n]
  if f not in fmap:fmap[f]=len(groups);groups.append([])
  groups[fmap[f]].append(short[n])
 return '|'.join('{'+','.join(g)+'}' for g in groups)
def main():
 x=json.loads(SRC.read_text());e=json.loads(EX.read_text());checks=[];order=['global','local','composition','structure','symmetry','observer'];em={q['object_id']:q for q in e['objects']}
 for r in x['selected_stress_topologies']:
  votes={n:r['nodes'][n]['family'] for n in order};permuted={n:{'F-001':'Q4','F-002':'Q1','F-003':'Q3','F-004':'Q2'}[f] for n,f in votes.items()}
  checks += [(r['formula'],'signature_recomputed',canonical(votes,order)==r['topology_signature']),(r['formula'],'family_relabel_invariant',canonical(permuted,order)==r['topology_signature']),(r['formula'],'local_family_matches_explanation',r['nodes']['local']['family']==max(em[r['object_id']]['neighborhoods']['representation']['neighbor_family_counts_k25'],key=em[r['object_id']]['neighborhoods']['representation']['neighbor_family_counts_k25'].get)),(r['formula'],'global_family_matches_explanation',r['nodes']['global']['family']==em[r['object_id']]['channels']['representation']['nearest_family'])]
 s=x['summary'];checks += [('population','low_margin_count_exact',s['low_margin_count']==52),('population','low_margin_ood_separated',s['low_margin_global_ood_count']==4),('population','boundary_state_count_exact',s['boundary_count']==48),('population','criteria_conjunction',s['relational_boundary_population_supported']==all(s['candidate_admission_criteria'].values())),('population','null_interval_order',s['representation_block_null_boundary_rate']['null_q05']<=s['representation_block_null_boundary_rate']['null_mean']<=s['representation_block_null_boundary_rate']['null_q95'])]
 passed=sum(c for _,_,c in checks);lines=['# Checkpoint — Conflict Topology Integrity','',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','', '| Object | Check | Result |','|---|---|---|']+[f"| {a} | `{b}` | {'PASS' if c else '**FAIL**'} |" for a,b,c in checks]
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Conflict Topology audit failed')
 print({'checks':len(checks),'passed':passed,'failed':0})
if __name__=='__main__':main()
