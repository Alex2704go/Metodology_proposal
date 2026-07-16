#!/usr/bin/env python3
"""Regression of the unchanged 16 System Null concepts against governance v0.2."""
from __future__ import annotations
import copy,json
from pathlib import Path
from validate_governance_v0_2 import validate
from governance_diagnostics_v0_2 import diagnostics
ROOT=Path(__file__).resolve().parents[1];FIX=ROOT/'config/governance_fixture_v0.2.json';OUT=ROOT/'derived/system_null_ladder_v0.2.json';MD=ROOT/'reports/system_null_ladder_v0.2.md'
def main():
 base=json.loads(FIX.read_text());results=[]
 def attack(i,mut):
  x=copy.deepcopy(base);mut(x);r=validate(x);ds=diagnostics(r['errors'][:8]);priority=['GOV-GRAPH-001','GOV-GRAPH-002','GOV-BOUND-001','GOV-ASYM-001','GOV-STATE-002','GOV-STATE-001'];primary=next((q for code in priority for q in ds if q['code']==code),ds[0] if ds else None);results.append({'id':i,'invalid_rejected':not r['valid'],'outcome':'REJECTED' if not r['valid'] else 'SPECIFICATION_GAP_REMAINS','errors':r['errors'][:8],'diagnostics':ds,'primary_diagnostic':primary})
 # Controls.
 valid=validate(copy.deepcopy(base));controls=[{'id':'CONTROL_VALID_FIXTURE','pass':valid['valid'],'detail':valid['errors']}]
 x=copy.deepcopy(base);x['passport']['epistemic_effect']['upgrades_target_ontology']=True;r=validate(x);controls.append({'id':'CONTROL_EPISTEMIC_UPGRADE','pass':not r['valid'],'detail':r['errors']})
 attack('ADMITTED_WITHOUT_QUALIFICATION',lambda x:(x['passport'].__setitem__('qualification_events',[]),x['passport'].__setitem__('lifecycle_events',[]),x['passport'].__setitem__('expected_maturity','NOT_TESTED')))
 attack('GHOST_EVIDENCE',lambda x:x['passport'].__setitem__('independent_evidence_refs',[]))
 attack('GHOST_PROVENANCE',lambda x:x['passport'].__setitem__('provenance_refs',[]))
 attack('DIRECTION_SEMANTIC_NOOP',lambda x:x['passport'].__setitem__('direction','CLASSICAL_TO_CEOS'))
 attack('NOT_TESTED_PLUS_PASS',lambda x:(x['passport'].__setitem__('qualification_events',[]),x['passport'].__setitem__('expected_maturity','NOT_TESTED'),x['passport'].__setitem__('latest_qualification_outcome','PASS')))
 def admitted_failed(x):
  p=x['passport'];p['qualification_events'].append({'event_id':'Q4','level':'INDEPENDENTLY_REPLICATED','outcome':'FAILED','evidence_refs':[p['independent_evidence_refs'][0]],'identity_ids':['WORLD-W1','WORLD-W2','DATASET-D1','DATASET-D2','OBSERVER-O1','OBSERVER-O2']});p['latest_qualification_outcome']='FAILED'
 attack('ADMITTED_PLUS_FAILED',admitted_failed)
 attack('CONTRADICTORY_INTERPRETATION_BOUNDARY',lambda x:x['passport']['interpretation_boundary']['supports_claim_types'].append('PHYSICAL_MECHANISM'))
 attack('EVIDENCE_INHERITANCE_SMUGGLING',lambda x:x['passport']['interpretation_boundary']['supports_claim_types'].append('EVIDENCE_INHERITANCE'))
 attack('UNSEARCHED_COUNTEREXAMPLES',lambda x:x['passport']['counterexample_search'].__setitem__('current_world',None))
 attack('HISTORYLESS_INDEPENDENT_REPLICATION',lambda x:x['passport'].__setitem__('qualification_events',[]))
 def no_independent_ids(x):
  for e in x['passport']['qualification_events']:
   if e['level'] in {'MULTI_WORLD','INDEPENDENTLY_REPLICATED'}:e['identity_ids']=['WORLD-W1','DATASET-D1','OBSERVER-O1']
 attack('INDEPENDENCE_WITHOUT_IDENTITIES',no_independent_ids)
 attack('NON_MARKDOWN_CLAIM_ESCAPE',lambda x:x.setdefault('discovered_artifact_paths',list(a['path'] for a in x['artifact_registry'].values())).append('derived/evil_claim.json'))
 attack('SEMANTIC_MARKDOWN_CONTRADICTION',lambda x:x['document_claim_registry']['ART-REPORT']['supports_claim_types'].append('PHYSICAL_MECHANISM'))
 def cycle(x):
  parent=x['claim_registry']['CL-MAP'];x['claim_registry']['CL-BASE']['antecedent_refs']=[{'claim_id':'CL-MAP','expected_content_digest':parent['content_digest'],'expected_version':parent['version']}]
 attack('CYCLIC_CLAIM_GRAPH',cycle)
 attack('SELF_ASSERTED_TRANSITION_EVIDENCE',lambda x:x['passport']['lifecycle_events'][1].__setitem__('evidence_refs',[{'passed':True}]))
 attack('UNPINNED_ANTECEDENT',lambda x:x['claim_registry']['CL-MAP']['antecedent_refs'][0].__setitem__('expected_content_digest','0'*64))
 passed=sum(r['invalid_rejected'] for r in results);cp=sum(c['pass'] for c in controls);report={'protocol':'system_null_ladder_v0.2','governance_status':'QUALIFIED' if passed==16 and cp==2 else 'REASSESSMENT_REQUIRED','controls':controls,'invalid_attacks':len(results),'rejected_invalid_attacks':passed,'remaining_gaps':len(results)-passed,'results':results,'interpretation_boundary':{'supports':['regression result for the same 16 conceptual attacks against governance v0.2 candidate'],'does_not_support':['completeness of all possible attacks','universal correctness','physical mechanism','prediction of untested properties']}}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# System Null Ladder v0.2 — Regression','','The same 16 conceptual attacks from v0.1 were applied to the proof-carrying governance v0.2 candidate.','',f'- Controls: **{cp}/2**',f'- Invalid attacks rejected: **{passed}/16**',f'- Remaining registered gaps: **{len(results)-passed}**',f"- Candidate governance status: **{report['governance_status']}**",'', '| Attack | Outcome | Diagnostic | Primary rejection reason |','|---|---|---|---|']+[f"| `{r['id']}` | **{r['outcome']}** | `{r['primary_diagnostic']['code'] if r['primary_diagnostic'] else '—'}` | {r['primary_diagnostic']['message'] if r['primary_diagnostic'] else 'none'} |" for r in results]+['','## Interpretation Boundary','','### Supports','','- regression closure status for the 16 registered v0.1 specification gaps.','','### Does not support','','- completeness against unregistered attacks;','- universal correctness of governance v0.2;','- physical mechanism;','- prediction of untested properties.','','### Cross Mapping Asymmetry','','> **Vocabulary correspondence ≠ evidence inheritance.**']
 MD.write_text('\n'.join(lines)+'\n')
 if passed!=16 or cp!=2:raise SystemExit('Governance v0.2 regression failed')
 print({'controls':f'{cp}/2','invalid_rejected':f'{passed}/16','remaining_gaps':len(results)-passed,'status':report['governance_status']})
if __name__=='__main__':main()
