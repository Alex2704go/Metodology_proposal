#!/usr/bin/env python3
"""Audit Result Biography event DAG, digests and WITHHELD contracts."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/materialsworld_result_biography_v0.1.json';OUT=ROOT/'reports/checkpoint_result_biography.md'
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
 x=json.loads(SRC.read_text());events=x['events'];ids={e['event_id'] for e in events};checks=[]
 required={'event_id','timestamp','event_type','actor_id','claim_ids','parent_event_ids','input_artifact_refs','output_artifact_refs','pre_state','post_state','decision_timing','reason_code','evidence_refs','content_digest'}
 graph={e['event_id']:e['parent_event_ids'] for e in events}
 for e in events:
  q=dict(e);claimed=q.pop('content_digest');checks += [(e['event_id'],'required_fields',required<=set(e)),(e['event_id'],'digest_exact',claimed==digest(q)),(e['event_id'],'parents_exist',all(p in ids for p in e['parent_event_ids'])),(e['event_id'],'decision_timing',e['decision_timing'] in {'PRE_RESULT','POST_RESULT'})]
 visiting=set();done=set();cycle=[False]
 def dfs(n):
  if n in visiting:cycle[0]=True;return
  if n in done:return
  visiting.add(n)
  for p in graph.get(n,[]):dfs(p)
  visiting.remove(n);done.add(n)
 for n in graph:dfs(n)
 checks.append(('BIOGRAPHY','acyclic',not cycle[0]))
 wr={'claim_id','release_state','reason','pending_gates','available_evidence_refs','reconsideration_condition','responsible_actor_id','next_review_trigger','interpretation_boundary'}
 for w in x['withheld_register']:checks += [(w['claim_id'],'withheld_state',w['release_state']=='WITHHELD'),(w['claim_id'],'withheld_contract',wr<=set(w) and bool(w['pending_gates']))]
 passed=sum(c for _,_,c in checks);lines=['# Checkpoint — Result Biography','',f'- Events: **{len(events)}**',f"- WITHHELD records: **{len(x['withheld_register'])}**",f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**']
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Result Biography audit failed')
 print({'events':len(events),'withheld':len(x['withheld_register']),'checks':len(checks),'passed':passed})
if __name__=='__main__':main()
