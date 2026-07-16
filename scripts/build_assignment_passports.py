#!/usr/bin/env python3
"""Build versioned Assignment Evidence passports and Admission States."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SIX=ROOT/'derived/six_material_stress_results.json';BUILDER=ROOT/'reports/builder_admission_results.json';DET=ROOT/'reports/deterministic_transform_result.json';REG=ROOT/'derived/relation_pattern_registry_v0.1.json';OUT=ROOT/'derived/assignment_evidence_passports_v0.2.json';MD=ROOT/'reports/assignment_evidence_passports.md'
def margin_evidence(x):
 if x>=.10:return 'PASS',1.0
 if x>=.05:return 'WARN',.5
 return 'FAIL',0.0
def passport(formula,mid,nearest,metric,cross,replay,role):
 builder_checks=json.loads(BUILDER.read_text());det=json.loads(DET.read_text());builder_pass=all(x['pass'] for x in builder_checks.values()) and det['all_exact'] and replay['raw_max_abs_error']==0 and replay['scaled_max_abs_error']==0
 mstatus,mscore=margin_evidence(metric['margin']);ind=not metric['ood_flag'];axes={'builder_confidence':{'status':'PASS' if builder_pass else 'FAIL','score':1.0 if builder_pass else 0.0,'builder_admitted':all(x['pass'] for x in builder_checks.values()),'deterministic_transform':det['all_exact'],'raw_replay_error':replay['raw_max_abs_error'],'scaled_replay_error':replay['scaled_max_abs_error']},'cross_view_agreement':{'status':'PASS' if cross else 'FAIL','score':1.0 if cross else 0.0,'agreement':cross},'in_distribution':{'status':'PASS' if ind else 'FAIL','score':1.0 if ind else 0.0,'distance_percentile':metric['training_distance_percentile'],'threshold_lte':99.0},'margin':{'status':mstatus,'score':mscore,'value':metric['margin'],'pass_gte':.10,'warning_gte':.05}}
 weight=sum(x['score'] for x in axes.values())
 if not builder_pass:state='REJECTED';reason='Builder/integrity/replay evidence failed'
 elif not ind:state='OOD';reason='Distance percentile exceeds registered training support'
 elif metric['margin']<.05:state='BOUNDARY';reason='Nearest and second-nearest families are insufficiently separated'
 elif not cross or metric['margin']<.10:state='CANDIDATE';reason='Evidence is valid but warning-level or cross-view incomplete'
 else:state='ADMITTED';reason=None
 if state=='ADMITTED':supports=['structural representation family assignment under frozen partition v0.2']
 elif state=='OOD':supports=['valid frozen transform','global out-of-distribution diagnosis relative to current WORLD','nearest-family geometry without membership admission']
 elif state=='BOUNDARY':supports=['valid in-support transform','withheld hard assignment due registered low-margin boundary state']
 elif state=='CANDIDATE':supports=['valid provisional assignment evidence requiring additional support']
 else:supports=['rejection of assignment claim under failed evidence chain']
 interpretation={'supports':supports,'does_not_support':['physical mechanism','thermodynamic phase','microscopic Hamiltonian','causal explanation','prediction of untested properties','classical material category','universal validity outside current WORLD'],'scope':'current object under frozen partition, Builder and evidence protocol','literature_mapping_status':'LOCKED'}
 return {'formula':formula,'material_id':mid,'role':role,'context':{'partition':'CEOS_Structural_Representation_Families_v0.2','primary_view':'ORGANIZATION','confirmation_view':'OBSERVER_AUGMENTED','builder_admission':'v0.2','assignment_protocol':'v0.2'},'nearest_family':nearest,'admissible_family':nearest if state=='ADMITTED' else None,'admission_state':state,'admission_withheld_reason':reason,'assignment_evidence':{'margin':metric['margin'],'nearest_distance':metric['nearest_distance'],'second_distance':metric['second_distance'],'distance_percentile':metric['training_distance_percentile'],'ood_flag':metric['ood_flag'],'cross_view_agreement':cross,'builder_confidence':'PASS' if builder_pass else 'FAIL'},'evidence_axes':axes,'evidence_weight':{'score':weight,'maximum':4.0,'display':f'{weight:g}/4'},'interpretation_boundary':interpretation}
def main():
 x=json.loads(SIX.read_text());replay=x['training_replay'];items=[]
 for p in x['standard_examples']:
  m=p['assignments']['ORGANIZATION'];items.append(passport(p['formula'],p['material_id'],m['family'],m,p['confirmed_by_observer_view'],replay,'STANDARD'))
 for p in x['stress_examples']:
  items.append(passport(p['formula'],p['material_id'],p['nearest_family'],p['organization_metrics'],p['observer_confirmation'],replay,p['selector']))
 reg=json.loads(REG.read_text());rp={q['formula']:q for q in reg['selected_examples']}
 for p in items:
  q=rp.get(p['formula'])
  if q:
   p['knowledge_state']={'admission_state':p['admission_state'],'relation_pattern_evaluation':'EVALUATED','relation_pattern_id':q['relation_pattern_id'],'canonical_signature':q['canonical_signature'],'named_relation_pattern':q['named_relation_pattern'],'composite':p['admission_state']+' :: '+(q['named_relation_pattern'] or q['relation_pattern_id'])}
   p['interpretation_boundary']['supports'].append(f"family-label-invariant relation signature {q['relation_pattern_id']} under conflict_topology_v0.3")
   if q['named_relation_pattern']:
    p['interpretation_boundary']['supports'].append(f"population-supported organizational pattern {q['named_relation_pattern']} within analyzed sample and methodology")
  else:
   p['knowledge_state']={'admission_state':p['admission_state'],'relation_pattern_evaluation':'NOT_EVALUATED','relation_pattern_id':None,'canonical_signature':None,'named_relation_pattern':None,'composite':p['admission_state']+' :: RELATION_PATTERN_NOT_EVALUATED'}
 report={'ontology':'Admission State belongs to Object × Evidence Context; Relation Pattern is an orthogonal axis','protocol':'assignment_admission_v0.2','passports':items}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Assignment Evidence Passports v0.2','','`nearest_family` is geometric. `admissible_family` is epistemic and is populated only for `ADMITTED`. Admission State and Relation Pattern are orthogonal.','', '| Formula | Nearest | Admissible | Knowledge State | Builder | Cross-view | Distribution | Margin | Evidence Weight |','|---|---|---|---|---|---|---|---|---:|']
 icon={'PASS':'✅','WARN':'⚠️','FAIL':'❌'}
 for p in items:
  a=p['evidence_axes'];lines.append(f"| {p['formula']} | {p['nearest_family']} | {p['admissible_family'] or 'WITHHELD'} | **{p['knowledge_state']['composite']}** | {icon[a['builder_confidence']['status']]} | {icon[a['cross_view_agreement']['status']]} | {icon[a['in_distribution']['status']]} | {icon[a['margin']['status']]} {a['margin']['value']:.4f} | **{p['evidence_weight']['display']}** |")
 for p in items:
  lines += ['',f"## {p['formula']} — {p['admission_state']}",'', '```text',f"Nearest:   {p['nearest_family']}",f"Admission: {p['admissible_family'] or 'WITHHELD'}",f"Evidence:  {p['evidence_weight']['display']}",'```']
  if p['admission_withheld_reason']:lines.append(f"Reason: {p['admission_withheld_reason']}")
  ib=p['interpretation_boundary'];lines += ['','**Interpretation Boundary**','',f"Supports: {', '.join(ib['supports'])}.",f"Does not support: {', '.join(ib['does_not_support'])}.",f"Literature mapping: **{ib['literature_mapping_status']}**."]
 lines += ['','## State semantics','','- **ADMITTED:** all four axes pass.','- **CANDIDATE:** valid but incomplete or warning-level evidence.','- **BOUNDARY:** in-distribution but insufficient family separation.','- **OOD:** valid transform outside registered support.','- **REJECTED:** upstream evidence chain invalid.','','Evidence Weight is not a probability and cannot override state precedence.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps([{'formula':p['formula'],'nearest':p['nearest_family'],'admissible':p['admissible_family'],'state':p['admission_state'],'evidence':p['evidence_weight']['display']} for p in items],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
