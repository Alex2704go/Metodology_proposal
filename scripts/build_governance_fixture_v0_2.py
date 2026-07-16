#!/usr/bin/env python3
"""Build a content-addressed valid fixture for CEOS governance v0.2."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];DIR=ROOT/'evidence/governance_v0.2';OUT=ROOT/'config/governance_fixture_v0.2.json'
def sha_bytes(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def main():
 DIR.mkdir(parents=True,exist_ok=True)
 payloads={
  'ART-PROV':'Builder and source provenance for synthetic governance fixture.\n',
  'ART-QUAL1':'Single-WORLD qualification passed.\n',
  'ART-QUAL2':'Multi-WORLD qualification passed with distinct roots.\n',
  'ART-EVID1':'Independent evidence package from ROOT-A.\n',
  'ART-EVID2':'Independent evidence package from ROOT-B.\n',
  'ART-COUNTER':'Counterexample search in current and external synthetic WORLDs.\n',
  'ART-ADMIT':'Admission review passed for synthetic fixture.\n',
  'ART-REPORT':'Synthetic claim-bearing report; no real scientific mapping.\n'
 }
 artifacts={}
 identity_map={
  'ART-PROV':['BUILDER-B1'], 'ART-QUAL1':['WORLD-W1','DATASET-D1','OBSERVER-O1'],
  'ART-QUAL2':['WORLD-W1','WORLD-W2','DATASET-D1','DATASET-D2','OBSERVER-O1','OBSERVER-O2'],
  'ART-EVID1':['WORLD-W1','DATASET-D1','OBSERVER-O1'], 'ART-EVID2':['WORLD-W2','DATASET-D2','OBSERVER-O2'],
  'ART-COUNTER':['WORLD-W1','WORLD-W2'], 'ART-ADMIT':['OBSERVER-REVIEW'], 'ART-REPORT':['BUILDER-B1']}
 for aid,text in payloads.items():
  p=DIR/(aid.lower()+('.md' if aid=='ART-REPORT' else '.txt'));p.write_text(text);b=p.read_bytes();artifacts[aid]={'artifact_id':aid,'path':str(p.relative_to(ROOT)),'sha256':sha_bytes(b),'artifact_type':'CLAIM_DOCUMENT' if aid=='ART-REPORT' else 'EVIDENCE','protocol_version':'governance_v0.2','validator_id':'VALIDATOR-GOV-V02','identity_ids':identity_map[aid],'validation_status':'PASS','claim_bearing':aid=='ART-REPORT'}
 identities={
  'WORLD-W1':{'identity_type':'WORLD_ID','independence_group':'GROUP-A','lineage_roots':['ROOT-A']},
  'DATASET-D1':{'identity_type':'DATASET_ID','independence_group':'GROUP-A','lineage_roots':['ROOT-A']},
  'OBSERVER-O1':{'identity_type':'OBSERVER_ID','independence_group':'GROUP-A','lineage_roots':['ROOT-A']},
  'WORLD-W2':{'identity_type':'WORLD_ID','independence_group':'GROUP-B','lineage_roots':['ROOT-B']},
  'DATASET-D2':{'identity_type':'DATASET_ID','independence_group':'GROUP-B','lineage_roots':['ROOT-B']},
  'OBSERVER-O2':{'identity_type':'OBSERVER_ID','independence_group':'GROUP-B','lineage_roots':['ROOT-B']},
  'OBSERVER-REVIEW':{'identity_type':'OBSERVER_ID','independence_group':'GROUP-R','lineage_roots':['ROOT-REVIEW']},
  'BUILDER-B1':{'identity_type':'BUILDER_ID','independence_group':'GROUP-BUILDER','lineage_roots':['ROOT-BUILDER']}}
 def aref(aid,etype):
  a=artifacts[aid];return {'artifact_id':aid,'expected_sha256':a['sha256'],'evidence_type':etype,'protocol_version':a['protocol_version'],'validator_id':a['validator_id']}
 base_payload={'claim_type':'ORGANIZATIONAL_OBJECT','statement':'synthetic base object for validator fixture'}
 base={'claim_id':'CL-BASE','version':'1.0','payload':base_payload,'antecedent_refs':[]};base['content_digest']=sha_bytes(canon({'payload':base_payload,'antecedent_refs':[]}))
 parent={'claim_id':'CL-BASE','expected_content_digest':base['content_digest'],'expected_version':'1.0'}
 map_payload={'claim_type':'CROSS_MAPPING','statement':'synthetic locked vocabulary correspondence'}
 mapping={'claim_id':'CL-MAP','version':'1.0','payload':map_payload,'antecedent_refs':[parent]};mapping['content_digest']=sha_bytes(canon({'payload':map_payload,'antecedent_refs':[parent]}))
 claims={'CL-BASE':base,'CL-MAP':mapping}
 passport={
  'mapping_id':'CM-V02-SYNTHETIC','protocol_version':'governance_v0.2','direction':'CEOS_TO_CLASSICAL','construction_origin':'CEOS',
  'endpoints':{'ceos':{'family_ids':['F-001'],'relation_pattern_ids':['RP-6E1BC31651'],'admission_context_ids':['CTX-SYNTH']},'classical':{'vocabulary':'synthetic','terms':['TERM-X'],'citation_ids':['CIT-SYNTH']}},
  'claim_ref':{'claim_id':'CL-MAP','expected_content_digest':mapping['content_digest'],'expected_version':'1.0'},
  'provenance_refs':[aref('ART-PROV','PROVENANCE')],
  'independent_evidence_refs':[aref('ART-EVID1','INDEPENDENT_EVIDENCE'),aref('ART-EVID2','INDEPENDENT_EVIDENCE')],
  'expected_evidence_strength':'INDEPENDENTLY_REPLICATED','mapping_strength':'MODERATE',
  'qualification_events':[
   {'event_id':'Q1','level':'SINGLE_WORLD','outcome':'PASS','evidence_refs':[aref('ART-QUAL1','QUALIFICATION')],'identity_ids':['WORLD-W1','DATASET-D1','OBSERVER-O1']},
   {'event_id':'Q2','level':'MULTI_WORLD','outcome':'PASS','evidence_refs':[aref('ART-QUAL2','QUALIFICATION')],'identity_ids':['WORLD-W1','WORLD-W2','DATASET-D1','DATASET-D2','OBSERVER-O1','OBSERVER-O2']},
   {'event_id':'Q3','level':'INDEPENDENTLY_REPLICATED','outcome':'PASS','evidence_refs':[aref('ART-EVID1','INDEPENDENT_EVIDENCE'),aref('ART-EVID2','INDEPENDENT_EVIDENCE')],'identity_ids':['WORLD-W1','WORLD-W2','DATASET-D1','DATASET-D2','OBSERVER-O1','OBSERVER-O2']}],
  'lifecycle_events':[
   {'event_id':'L1','transition':'QUALIFY','from_state':'NOT_TESTED','to_state':'QUALIFIED','evidence_refs':[aref('ART-QUAL1','QUALIFICATION')]},
   {'event_id':'L2','transition':'ADMIT','from_state':'QUALIFIED','to_state':'ADMITTED','evidence_refs':[aref('ART-ADMIT','ADMISSION'),aref('ART-COUNTER','COUNTEREXAMPLE_SEARCH')]}],
  'expected_state':'ADMITTED','expected_maturity':'INDEPENDENTLY_REPLICATED','latest_qualification_outcome':'PASS',
  'counterexample_search':{'current_world':aref('ART-COUNTER','COUNTEREXAMPLE_SEARCH'),'external_worlds':aref('ART-COUNTER','COUNTEREXAMPLE_SEARCH')},
  'interpretation_boundary':{'supports_claim_types':['ORGANIZATIONAL_CORRESPONDENCE'],'prohibits_claim_types':['PHYSICAL_MECHANISM','THERMODYNAMIC_PHASE','MICROSCOPIC_HAMILTONIAN','CAUSAL_EXPLANATION','PREDICTION_UNTESTED_PROPERTIES','EVIDENCE_INHERITANCE'],'notes':'Synthetic validation only.'},
  'epistemic_effect':{'mapping_is_descriptive':True,'upgrades_source_ontology':False,'upgrades_target_ontology':False,'independent_admitted_evidence_required_for_upgrade':True}}
 document_claims={'ART-REPORT':{'supports_claim_types':['TECHNICAL_VALIDATION'],'prohibits_claim_types':['PHYSICAL_MECHANISM','THERMODYNAMIC_PHASE','MICROSCOPIC_HAMILTONIAN','CAUSAL_EXPLANATION','PREDICTION_UNTESTED_PROPERTIES','EVIDENCE_INHERITANCE']}}
 fixture={'governance_version':'0.2','identity_registry':identities,'artifact_registry':artifacts,'claim_registry':claims,'document_claim_registry':document_claims,'passport':passport}
 OUT.write_text(json.dumps(fixture,ensure_ascii=False,indent=2)+'\n');print({'identities':len(identities),'artifacts':len(artifacts),'claims':len(claims),'passport':passport['mapping_id']})
if __name__=='__main__':main()
