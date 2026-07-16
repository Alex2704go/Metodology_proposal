#!/usr/bin/env python3
"""Unblind only preregistered stress selections and report six material records."""
from __future__ import annotations
import gzip,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SEL=ROOT/'derived/stress_selection_blind.json';MAP=ROOT/'raw/stress_pool_map.jsonl.gz';RAW=ROOT/'raw/stress_pool_window_100000.jsonl.gz';OLD=ROOT/'derived/real_examples_family_assignments.json';OUT=ROOT/'derived/six_material_stress_results.json';MD=ROOT/'reports/six_material_stress_test.md'
def topology(v):
 if isinstance(v,dict):children=list(v.values());o,l=1,0
 elif isinstance(v,list):children=v;o,l=0,1
 else:return 0,1,0,0
 z=[topology(x) for x in children]
 return 1+max((x[0] for x in z),default=0),sum(x[1] for x in z),o+sum(x[2] for x in z),l+sum(x[3] for x in z)
def main():
 sel=json.loads(SEL.read_text());selected_ids={x['object_id'] for x in sel['selected']};mapping={}
 with gzip.open(MAP,'rt',encoding='utf-8') as f:
  for line in f:
   x=json.loads(line)
   if x['object_id'] in selected_ids:mapping[x['object_id']]=x
 mids={x['material_id'] for x in mapping.values()};docs={}
 with gzip.open(RAW,'rt',encoding='utf-8') as f:
  for line in f:
   x=json.loads(line)
   if x['material_id'] in mids:docs[x['material_id']]=x
 stress=[]
 for x in sel['selected']:
  mp=mapping[x['object_id']];d=docs[mp['material_id']];r=x['views']['ORGANIZATION'];depth,leaves,on,ln=topology(d['structure']);sym=d.get('symmetry') or {};hp=d.get('has_props') or {}
  if r['ood_flag']:status='OOD — nearest family reported, hard admission withheld'
  elif r['margin']<.05:status='BOUNDARY — nearest family reported, hard admission ambiguous'
  else:status='ADMITTED'
  stress.append({'selector':x['selector'],'formula':mp['formula_pretty'],'material_id':mp['material_id'],'object_id':x['object_id'],'classification_status':status,'nearest_family':r['nearest_family'],'organization_metrics':r,'observer_confirmation':x['views']['OBSERVER_AUGMENTED']['nearest_family']==r['nearest_family'],'representation_card':{'composition_map_keys':len(d.get('composition') or {}),'structure':{'depth':depth,'leaves':leaves,'object_nodes':on,'list_nodes':ln},'symmetry_record':{'crystal_system':sym.get('crystal_system'),'number':sym.get('number')},'capability_active_count':sum(bool(v) for v in hp.values()),'origins_length':len(d.get('origins') or [])}})
 previous=json.loads(OLD.read_text())['results'];report={'protocol':'material_stress_test_v0.1','pool_size':sel['pool_objects'],'selection_was_blind':sel['selection_blind'],'training_replay':sel['replay'],'standard_examples':previous,'stress_examples':stress}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Six-material CEOS Stress Test','','Two additional records were selected from 1,000 unseen API objects without loading formulas or source IDs.','','## Summary','','| Role | Formula | Record | Result | Margin | Training-distance percentile | Cross-view |','|---|---|---|---|---:|---:|---|']
 for p in previous:
  a=p['assignments']['ORGANIZATION'];lines.append(f"| Standard | {p['formula']} | `{p['material_id']}` | **{a['family']}** | {a['margin']:.4f} | {a['training_distance_percentile']:.1f}% | {'YES' if p['confirmed_by_observer_view'] else 'NO'} |")
 for s in stress:
  a=s['organization_metrics'];res=(f"nearest {s['nearest_family']}; OOD" if a['ood_flag'] else f"nearest {s['nearest_family']}; BOUNDARY")
  lines.append(f"| {s['selector']} | {s['formula']} | `{s['material_id']}` | **{res}** | {a['margin']:.4f} | {a['training_distance_percentile']:.1f}% | {'YES' if s['observer_confirmation'] else 'NO'} |")
 for s in stress:
  c=s['representation_card'];lines += ['',f"## {s['selector']}: {s['formula']}",'',f"- Record: `{s['material_id']}`",f"- Status: **{s['classification_status']}**",f"- Nearest structural family: **{s['nearest_family']}**",f"- composition: MAP with {c['composition_map_keys']} keys",f"- structure: COMPOSITE depth {c['structure']['depth']}, leaves {c['structure']['leaves']}, object nodes {c['structure']['object_nodes']}, list nodes {c['structure']['list_nodes']}",f"- symmetry cross-map: {c['symmetry_record']['crystal_system']} / #{c['symmetry_record']['number']}",f"- active representation capabilities: {c['capability_active_count']}",f"- origins length: {c['origins_length']}"]
 lines += ['','## Admission reading','','- An OOD object may have a nearest centroid, but nearest is not equivalent to admitted membership.','- A boundary object may have a numerical nearest family while remaining classification-ambiguous.','- The four standard examples remain hard assignments because they are in-distribution and cross-view confirmed.','- Formula names were opened only after the blind selectors had been frozen.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({'stress_examples':stress},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
