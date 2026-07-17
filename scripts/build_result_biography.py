#!/usr/bin/env python3
"""Build the machine-readable MaterialsWorld Result Biography v0.1."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'derived/materialsworld_result_biography_v0.1.json'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 raw=[
 ('BIO-001','REPRESENTATION_CREATED','PRE_RESULT','NONE','BLIND_PROTOCOL_ACTIVE','blind protocol registered',['FORBIDDEN.md']),
 ('BIO-002','DATASET_REGISTERED','PRE_RESULT','NO_WORLD','PILOT_WORLD_REGISTERED','3,000-record pilot registered',['raw/MANIFEST.json']),
 ('BIO-003','REPRESENTATION_CREATED','POST_RESULT','RAW_SCHEMA','OBJECT_SIGNATURES','MAP/RECORD/COMPOSITE ontology derived',['reports/representation_ontology_v0.1.md']),
 ('BIO-004','REPRESENTATION_REVISED','PRE_RESULT','VECTOR_V0.1','VECTOR_V0.2','Observer audit found duplicate size and availability leakage',['reports/checkpoint_observer_audit_v0.2.md']),
 ('BIO-005','CLAIM_ADMITTED','POST_RESULT','PARTITION_CANDIDATE','PARTITION_ADMITTED_WITH_SCOPE','four structural representation families passed registered Nulls',['reports/stage04_family_discovery_and_nulls.md']),
 ('BIO-006','NULL_PASSED','POST_RESULT','STRUCTURE_DOMINANCE_CANDIDATE','STRUCTURE_DOMINANCE_ADMITTED_WITH_SCOPE','structure ablation destroyed partition recovery',['reports/checkpoint_bias_and_ablation.md']),
 ('BIO-007','CLAIM_REJECTED','POST_RESULT','EXAMPLE_ASSIGNMENT_CANDIDATE','PROJECTION_REJECTED','out-of-sample preprocessing refit caused replay mismatch',['scripts/project_real_examples.py']),
 ('BIO-008','CLAIM_ADMITTED','POST_RESULT','PROJECTION_REJECTED','EXAMPLE_ASSIGNMENTS_ADMITTED','frozen preprocessing restored exact replay',['reports/real_examples_ceos_families.md']),
 ('BIO-009','BUILDER_REVOKED','POST_RESULT','BUILDER_CANDIDATE','BUILDER_REASSESSMENT','key-order and serialization error near 1e-15',['reports/BUILDER_ADMISSION.md']),
 ('BIO-010','BUILDER_ADMITTED','POST_RESULT','BUILDER_REASSESSMENT','BUILDER_ADMITTED','canonical aggregation produced exact zero replay',['reports/BUILDER_ADMISSION.md']),
 ('BIO-011','HYPOTHESIS_WITHHELD','POST_RESULT','SCALE_DRIVEN_CANDIDATE','SCALE_SENSITIVE_WITHHELD','registered Scale Nulls disagreed',['reports/ood_boundary_biographies.md']),
 ('BIO-012','CLAIM_REJECTED','POST_RESULT','CONFLICT_V0.1','CONFLICT_SCOPE_REJECTED','Local node used wrong representation scope',['reports/DECISION_LOG.md']),
 ('BIO-013','CLAIM_QUALIFIED','POST_RESULT','CONFLICT_SCOPE_REJECTED','RELATIONAL_BOUNDARY_QUALIFIED','v0.3 population test passed registered criteria',['reports/conflict_topology_population.md']),
 ('BIO-014','CLAIM_REASSESSMENT','POST_RESULT','GOVERNANCE_V0.1_CANDIDATE','GOVERNANCE_V0.1_REASSESSMENT','16 specification gaps or unprotected transitions exposed',['reports/system_null_ladder_v0.1_reframed.md']),
 ('BIO-015','CLAIM_QUALIFIED','POST_RESULT','GOVERNANCE_V0.1_REASSESSMENT','GOVERNANCE_V0.2_QUALIFIED','same 16 attacks rejected by proof-carrying candidate',['reports/system_null_ladder_v0.2.md']),
 ('BIO-016','CLAIM_REASSESSMENT','POST_RESULT','GOVERNANCE_V0.2_QUALIFIED','PIPELINE_GAP_FOUND','failed gate masked by later shell success',['reports/system_null_ladder_v0.2.1.md']),
 ('BIO-017','CLAIM_QUALIFIED','POST_RESULT','PIPELINE_GAP_FOUND','GOVERNANCE_V0.2.1_QUALIFIED','fail-fast gate passed and 17 registered attacks rejected',['reports/system_null_ladder_v0.2.1.md']),
 ('BIO-018','CLAIM_RELEASED','POST_RESULT','RECOMMENDATIONS_DRAFT','RECOMMENDATIONS_RELEASED','final scoped recommendations prepared',['reports/FINAL_RECOMMENDATIONS_RU.md'])]
 events=[]
 for i,(eid,etype,timing,pre,post,reason,arts) in enumerate(raw):
  e={'event_id':eid,'timestamp':'2026-07-15' if i<13 else '2026-07-16','event_type':etype,'actor_id':'COLLAB-ALEX2704GO-ARENA-AGENT','claim_ids':['MATERIALSWORLD-PILOT'],'parent_event_ids':[raw[i-1][0]] if i else [],'input_artifact_refs':arts,'output_artifact_refs':arts,'pre_state':pre,'post_state':post,'decision_timing':timing,'reason_code':reason.upper().replace(' ','_'),'evidence_refs':arts}
  e['content_digest']=digest(e);events.append(e)
 withheld=[
  {'claim_id':'LITERATURE_CROSS_MAPPING','release_state':'WITHHELD','reason':'literature mapping not independently qualified','pending_gates':['Mapping Provenance','Mapping Stability','counterexample search','Cross Mapping Asymmetry audit'],'available_evidence_refs':['derived/relation_pattern_registry_v0.1.json'],'reconsideration_condition':'post hoc mapping protocol admitted','responsible_actor_id':'COLLAB-ALEX2704GO-ARENA-AGENT','next_review_trigger':'independent literature mapping study','interpretation_boundary':'CROSS_MAPPING_CONTRACT.md'},
  {'claim_id':'PHYSICAL_MECHANISM','release_state':'WITHHELD','reason':'organizational geometry does not transfer mechanism evidence','pending_gates':['independent physical evidence','mechanism-specific Nulls','Interpretation Admission'],'available_evidence_refs':['reports/ceos_structural_family_report.md'],'reconsideration_condition':'mechanism protocol and independent evidence admitted','responsible_actor_id':'COLLAB-ALEX2704GO-ARENA-AGENT','next_review_trigger':'mechanism-specific study','interpretation_boundary':'reports/ceos_structural_family_report.md'},
  {'claim_id':'GOVERNANCE_ADMISSION','release_state':'WITHHELD','reason':'v0.2.1 is qualified by self-authored regression only','pending_gates':['independent Red Team','unregistered mutation attacks','real claim graph audit'],'available_evidence_refs':['reports/system_null_ladder_v0.2.1.md'],'reconsideration_condition':'independent governance review passes','responsible_actor_id':'COLLAB-ALEX2704GO-ARENA-AGENT','next_review_trigger':'independent Red Team','interpretation_boundary':'GOVERNANCE_V0.2.md'}]
 out={'biography_id':'RB-MATERIALSWORLD-V0.1','version':'0.1','authors':[{'id':'Alex2704go','role':'initiator and methodology co-author'},{'id':'Arena.ai Agent Mode','role':'AI co-author of analysis, implementation, Red Team and documentation'}],'object_scope':'v0.42.MaterialsWorld pilot','dataset_refs':['raw/MANIFEST.json','raw/STRESS_POOL_MANIFEST.json'],'events':events,'withheld_register':withheld,'interpretation_boundary':{'supports':['documented claim lifecycle and critical turning points'],'does_not_support':['complete record of every exploratory action','physical mechanism','thermodynamic phase','prediction of untested properties']}}
 OUT.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print({'events':len(events),'withheld':len(withheld),'output':str(OUT)})
if __name__=='__main__':main()
