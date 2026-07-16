#!/usr/bin/env python3
"""Build stable family-label-invariant Relation Pattern registry."""
import hashlib,json
from collections import Counter,defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/conflict_topology_v0.3.json';OUT=ROOT/'derived/relation_pattern_registry_v0.1.json';MD=ROOT/'reports/relation_pattern_registry.md'
def rid(sig):return 'RP-'+hashlib.sha256(sig.encode()).hexdigest()[:10].upper()
def main():
 x=json.loads(SRC.read_text());agg=defaultdict(lambda:{'population_count':0,'boundary_count':0,'relational_boundary_count':0})
 for r in x['training_records']:
  a=agg[r['topology_signature']];a['population_count']+=1;a['boundary_count']+=int(r['boundary']);a['relational_boundary_count']+=int(r['boundary'] and r['multi_axis_conflict'])
 entries=[];seen={}
 for sig,a in sorted(agg.items()):
  i=rid(sig)
  if i in seen and seen[i]!=sig:raise RuntimeError(f'Relation Pattern ID collision: {i}')
  seen[i]=sig;entries.append({'relation_pattern_id':i,'canonical_signature':sig,**a,'interpretation_boundary':{'supports':['family-label-invariant organizational agreement/disagreement pattern in conflict_topology_v0.3'],'does_not_support':['physical mechanism','thermodynamic phase','microscopic Hamiltonian','causal explanation','prediction of untested properties','universal validity outside current WORLD'],'scope':'3,000-object pilot under registered CEOS methodology','literature_mapping_status':'LOCKED'}})
 bysig={e['canonical_signature']:e['relation_pattern_id'] for e in entries};selected=[]
 for r in x['selected_stress_topologies']:
  selected.append({'formula':r['formula'],'relation_pattern_id':bysig.get(r['topology_signature'],rid(r['topology_signature'])),'registered_in_training_population':r['topology_signature'] in bysig,'canonical_signature':r['topology_signature'],'admission_state':'BOUNDARY' if r['boundary'] else ('OOD' if r['nodes']['global']['ood'] else 'OTHER'),'named_relation_pattern':'RELATIONAL_BOUNDARY' if r['boundary'] and r['multi_axis_conflict'] else None})
 report={'registry_version':'0.1','identity_rule':'RP- + first 10 uppercase hex of SHA256(canonical signature)','family_label_invariant':True,'literature_mapping_status':'LOCKED','pattern_count':len(entries),'population_count':sum(e['population_count'] for e in entries),'entries':entries,'selected_examples':selected}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 top=sorted(entries,key=lambda e:-e['population_count']);lines=['# Relation Pattern Registry v0.1','',f'- Registered patterns: **{len(entries)}**',f"- Population accounted for: **{report['population_count']}**",'- IDs are content-derived and stable under family relabeling.','- Literature mapping: **LOCKED**.','','| ID | Canonical signature | Population | Boundary | Relational Boundary |','|---|---|---:|---:|---:|']
 for e in top[:30]:lines.append(f"| `{e['relation_pattern_id']}` | `{e['canonical_signature']}` | {e['population_count']} | {e['boundary_count']} | {e['relational_boundary_count']} |")
 lines += ['','## Selected examples','', '| Formula | Relation Pattern ID | Signature | Named pattern |','|---|---|---|---|']
 for s in selected:lines.append(f"| {s['formula']} | `{s['relation_pattern_id']}` | `{s['canonical_signature']}` | {s['named_relation_pattern'] or '—'} |")
 lines += ['','## Interpretation Boundary','','Supports: family-label-invariant organizational relation patterns within the analyzed sample and methodology.','','Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, or universal validity outside the current WORLD.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({'patterns':len(entries),'population':report['population_count'],'selected':selected},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
