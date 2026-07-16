#!/usr/bin/env python3
"""Proof-carrying validator candidate for CEOS governance v0.2."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];FIXTURE=ROOT/'config/governance_fixture_v0.2.json';OUT=ROOT/'reports/checkpoint_governance_v0.2.md';LEVELS=['NOT_TESTED','SINGLE_WORLD','MULTI_WORLD','INDEPENDENTLY_REPLICATED'];PROHIBITED={'PHYSICAL_MECHANISM','THERMODYNAMIC_PHASE','MICROSCOPIC_HAMILTONIAN','CAUSAL_EXPLANATION','PREDICTION_UNTESTED_PROPERTIES','EVIDENCE_INHERITANCE'}
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':')).encode()
def validate(f):
 errors=[];ids=f.get('identity_registry',{});arts=f.get('artifact_registry',{});claims=f.get('claim_registry',{});p=f.get('passport',{})
 # Identity and artifact registry.
 for aid,a in arts.items():
  path=ROOT/a.get('path','')
  if aid!=a.get('artifact_id'):errors.append(f'artifact key mismatch:{aid}')
  if not path.is_file():errors.append(f'artifact missing:{aid}')
  elif sha(path.read_bytes())!=a.get('sha256'):errors.append(f'artifact digest mismatch:{aid}')
  if a.get('validation_status')!='PASS':errors.append(f'artifact not validated:{aid}')
  for i in a.get('identity_ids',[]):
   if i not in ids:errors.append(f'unregistered identity:{i}')
 # Every discovered artifact must be registered by path.
 registered_paths={a.get('path') for a in arts.values()}
 for path in f.get('discovered_artifact_paths',registered_paths):
  if path not in registered_paths:errors.append(f'unregistered artifact:{path}')
 # EvidenceRef verification.
 def ref_ok(r,kind='evidence'):
  required={'artifact_id','expected_sha256','protocol_version','validator_id'}
  if not isinstance(r,dict) or not required<=set(r):errors.append(f'malformed {kind} ref');return False
  a=arts.get(r['artifact_id'])
  if not a:errors.append(f'unknown {kind} artifact:{r["artifact_id"]}');return False
  if r['expected_sha256']!=a.get('sha256'):errors.append(f'unpinned {kind} digest:{r["artifact_id"]}')
  if r['protocol_version']!=a.get('protocol_version') or r['validator_id']!=a.get('validator_id'):errors.append(f'{kind} validator/protocol mismatch:{r["artifact_id"]}')
  return True
 # Claim graph content, pins, acyclicity.
 for cid,c in claims.items():
  if cid!=c.get('claim_id'):errors.append(f'claim key mismatch:{cid}')
  expected=sha(canon({'payload':c.get('payload'),'antecedent_refs':c.get('antecedent_refs',[])}))
  if expected!=c.get('content_digest'):errors.append(f'claim digest mismatch:{cid}')
  for r in c.get('antecedent_refs',[]):
   parent=claims.get(r.get('claim_id'))
   if not parent:errors.append(f'unknown antecedent:{cid}')
   elif r.get('expected_content_digest')!=parent.get('content_digest') or r.get('expected_version')!=parent.get('version'):errors.append(f'unpinned antecedent:{cid}->{r.get("claim_id")}')
 visiting=set();done=set()
 def dfs(cid):
  if cid in visiting:errors.append(f'claim cycle:{cid}');return
  if cid in done or cid not in claims:return
  visiting.add(cid)
  for r in claims[cid].get('antecedent_refs',[]):dfs(r.get('claim_id'))
  visiting.remove(cid);done.add(cid)
 for cid in claims:dfs(cid)
 # Typed mapping endpoints and direction.
 direction=p.get('direction');origin=p.get('construction_origin');required_origin={'CEOS_TO_CLASSICAL':'CEOS','CLASSICAL_TO_CEOS':'CLASSICAL','BIDIRECTIONAL_CANDIDATE':'BOTH'}.get(direction)
 if required_origin is None or origin!=required_origin:errors.append('direction/origin mismatch')
 ep=p.get('endpoints',{});ceos=ep.get('ceos',{});classical=ep.get('classical',{})
 if not (ceos.get('family_ids') or ceos.get('relation_pattern_ids')):errors.append('empty CEOS endpoint')
 if not classical.get('terms') or not classical.get('citation_ids'):errors.append('empty classical endpoint/citations')
 # Pinned mapping claim.
 cr=p.get('claim_ref',{});claim=claims.get(cr.get('claim_id'))
 if not claim or cr.get('expected_content_digest')!=claim.get('content_digest') or cr.get('expected_version')!=claim.get('version'):errors.append('mapping claim unpinned')
 # Provenance and independent evidence.
 prov=p.get('provenance_refs',[])
 if not prov:errors.append('missing provenance refs')
 for r in prov:ref_ok(r,'provenance')
 evid=p.get('independent_evidence_refs',[])
 for r in evid:ref_ok(r,'independent evidence')
 groups=set();roots=set()
 for r in evid:
  a=arts.get(r.get('artifact_id'),{})
  for iid in a.get('identity_ids',[]):
   q=ids.get(iid,{})
   if q.get('identity_type') in {'WORLD_ID','DATASET_ID','OBSERVER_ID'}:groups.add(q.get('independence_group'));roots.update(q.get('lineage_roots',[]))
 derived_evidence='NONE' if not evid else ('INDEPENDENTLY_REPLICATED' if len(groups)>=2 and len(roots)>=2 else 'LIMITED')
 if p.get('expected_evidence_strength')!=derived_evidence:errors.append(f'evidence strength mismatch:{derived_evidence}')
 # Event-sourced maturity.
 maturity='NOT_TESTED';latest='NOT_RUN';seen_levels=[]
 for e in p.get('qualification_events',[]):
  level=e.get('level');outcome=e.get('outcome');refs=e.get('evidence_refs',[])
  if level not in LEVELS[1:]:errors.append('invalid maturity level');continue
  if not refs:errors.append(f'qualification without evidence:{e.get("event_id")}')
  for r in refs:ref_ok(r,'qualification')
  if outcome not in {'PASS','MIXED','FAILED'}:errors.append('invalid qualification outcome')
  latest=outcome
  if outcome=='PASS':
   idx=LEVELS.index(level)
   if idx>LEVELS.index(maturity)+1:errors.append('maturity level skipped')
   maturity=level if idx>=LEVELS.index(maturity) else maturity
   iid=e.get('identity_ids',[])
   unknown=[i for i in iid if i not in ids]
   if unknown:errors.append('qualification uses unknown identities')
   types={t:[ids[i] for i in iid if i in ids and ids[i]['identity_type']==t] for t in ['WORLD_ID','DATASET_ID','OBSERVER_ID']}
   if level in {'MULTI_WORLD','INDEPENDENTLY_REPLICATED'}:
    if len({q['independence_group'] for q in types['WORLD_ID']})<2:errors.append('multi-world without independent WORLD identities')
   if level=='INDEPENDENTLY_REPLICATED':
    for typ in ['WORLD_ID','DATASET_ID','OBSERVER_ID']:
     if len({q['independence_group'] for q in types[typ]})<2 or len(set().union(*(set(q['lineage_roots']) for q in types[typ])))<2:errors.append(f'independence not demonstrated:{typ}')
 if p.get('expected_maturity')!=maturity:errors.append(f'maturity mismatch:{maturity}')
 if p.get('latest_qualification_outcome')!=latest:errors.append(f'latest outcome mismatch:{latest}')
 # Lifecycle state machine.
 state='NOT_TESTED';allowed={'QUALIFY':({'NOT_TESTED','REASSESSMENT_REQUIRED'},'QUALIFIED'),'ADMIT':({'QUALIFIED'},'ADMITTED'),'FAIL':({'NOT_TESTED','QUALIFIED','ADMITTED','REASSESSMENT_REQUIRED'},'REASSESSMENT_REQUIRED'),'RETIRE':({'QUALIFIED','ADMITTED','REASSESSMENT_REQUIRED'},'RETIRED')}
 for e in p.get('lifecycle_events',[]):
  tr=e.get('transition');rule=allowed.get(tr);refs=e.get('evidence_refs',[])
  if not rule:errors.append('unknown lifecycle transition');continue
  if e.get('from_state')!=state or state not in rule[0] or e.get('to_state')!=rule[1]:errors.append(f'illegal lifecycle transition:{tr}')
  if not refs:errors.append(f'lifecycle transition without evidence:{tr}')
  for r in refs:ref_ok(r,'lifecycle')
  state=rule[1]
 if latest in {'FAILED','MIXED'} and state=='ADMITTED':errors.append('ADMITTED with non-PASS latest qualification')
 # Admission guards.
 if state=='ADMITTED':
  if maturity=='NOT_TESTED' or latest!='PASS':errors.append('admission without qualification')
  counter=p.get('counterexample_search',{})
  if not counter.get('current_world'):errors.append('admission without current-world counterexample search')
  else:ref_ok(counter['current_world'],'counterexample search')
  if not p.get('mapping_strength') or p.get('mapping_strength')=='NOT_ASSESSED':errors.append('admission without mapping strength')
 if p.get('expected_state')!=state:errors.append(f'state mismatch:{state}')
 # Controlled Interpretation Boundary.
 ib=p.get('interpretation_boundary',{});supports=set(ib.get('supports_claim_types',[]));prohibits=set(ib.get('prohibits_claim_types',[]))
 if supports&prohibits:errors.append('interpretation boundary contradiction')
 if not PROHIBITED<=prohibits:errors.append('missing mandatory prohibitions')
 if supports&PROHIBITED:errors.append('prohibited claim smuggled into supports')
 ee=p.get('epistemic_effect',{})
 if not (ee.get('mapping_is_descriptive') is True and ee.get('upgrades_source_ontology') is False and ee.get('upgrades_target_ontology') is False and ee.get('independent_admitted_evidence_required_for_upgrade') is True):errors.append('epistemic upgrade/asymmetry violation')
 # Claim-bearing artifact semantic sidecars.
 docclaims=f.get('document_claim_registry',{})
 for aid,a in arts.items():
  if a.get('claim_bearing') and aid not in docclaims:errors.append(f'claim-bearing artifact without claim passport:{aid}')
 for aid,c in docclaims.items():
  if aid not in arts or not arts[aid].get('claim_bearing'):errors.append(f'document claim without registered claim artifact:{aid}')
  s=set(c.get('supports_claim_types',[]));d=set(c.get('prohibits_claim_types',[]))
  if s&d or s&PROHIBITED or not PROHIBITED<=d:errors.append(f'document semantic contradiction:{aid}')
 return {'valid':not errors,'errors':errors,'derived_state':state,'derived_maturity':maturity,'derived_evidence_strength':derived_evidence}
def main():
 f=json.loads(FIXTURE.read_text());r=validate(f);lines=['# Checkpoint — Governance v0.2 Candidate','',f"- Valid fixture: **{r['valid']}**",f"- Derived state: **{r['derived_state']}**",f"- Derived maturity: **{r['derived_maturity']}**",f"- Derived evidence strength: **{r['derived_evidence_strength']}**",f"- Errors: **{len(r['errors'])}**"]+['- '+e for e in r['errors']]
 OUT.write_text('\n'.join(lines)+'\n')
 if not r['valid']:raise SystemExit('Governance v0.2 fixture invalid')
 print(r)
if __name__=='__main__':main()
