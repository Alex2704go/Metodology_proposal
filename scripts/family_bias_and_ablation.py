#!/usr/bin/env python3
"""Check sampling-stratum association and leave-one-block-out robustness."""
from __future__ import annotations
import gzip,json
from pathlib import Path
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score,normalized_mutual_info_score
ROOT=Path(__file__).resolve().parents[1];VEC=ROOT/'derived/world_vectors_v0.2.npz';LAB=ROOT/'derived/family_labels_v0.2.npz';DATA=ROOT/'derived/objects_blind_stage02_3000.jsonl.gz';OUT=ROOT/'reports/checkpoint_bias_and_ablation.json';MD=ROOT/'reports/checkpoint_bias_and_ablation.md';SEED=420042
def best_ari(X,ref,k=4):
 vals=[]
 for s in range(10):
  pred=KMeans(n_clusters=k,n_init=20,random_state=SEED+s).fit_predict(X);vals.append(adjusted_rand_score(ref,pred))
 return {'mean':float(np.mean(vals)),'max':float(np.max(vals)),'min':float(np.min(vals))}
def main():
 v=np.load(VEC,allow_pickle=False);l=np.load(LAB,allow_pickle=False);Z=v['X_scaled'];blocks=v['blocks'].astype(str);ref=l['ORGANIZATION']
 rows=[]
 with gzip.open(DATA,'rt',encoding='utf-8') as f:
  for line in f:rows.append(json.loads(line))
 strata=np.array([r['_ceos_stratum'] for r in rows]);ne=np.array([r['nelements'] for r in rows]);sym=np.array([(r.get('symmetry') or {}).get('crystal_system','NONE') for r in rows])
 def contingency(x):
  return {str(a):{f'F-{b:03d}':int(np.sum((x==a)&(ref==b))) for b in sorted(set(ref))} for a in sorted(set(x))}
 assoc={'sampling_stratum':{'nmi':float(normalized_mutual_info_score(strata,ref)),'contingency':contingency(strata)},'nelements':{'nmi':float(normalized_mutual_info_score(ne,ref)),'contingency':contingency(ne)},'symmetry_crystal_system':{'nmi':float(normalized_mutual_info_score(sym,ref)),'contingency':contingency(sym)}}
 org=set(['composition_shape','structure_topology','structure_numeric','symmetry_record']);abl={}
 for name,remove in {'NO_COMPOSITION':['composition_shape'],'NO_STRUCTURE':['structure_topology','structure_numeric'],'NO_SYMMETRY':['symmetry_record']}.items():
  wanted=org-set(remove);X=Z[:,np.isin(blocks,list(wanted))];abl[name]={'features':X.shape[1],**best_ari(X,ref)}
 report={'reference':'ORGANIZATION F labels','association':assoc,'leave_one_block_out':abl}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Checkpoint — Sampling Bias and Block Ablation','','## Association with registered sampling axes','','| Axis | NMI with family |','|---|---:|']+[f"| `{k}` | {x['nmi']:.4f} |" for k,x in assoc.items()]+['','NMI near zero means weak association; NMI near one means that the family partition is largely recoverable from that axis.','','## Leave-one-block-out agreement','','| Ablation | Organizational observables | Mean ARI vs primary | Min | Max |','|---|---:|---:|---:|---:|']
 for k,x in abl.items():lines.append(f"| `{k}` | {x['features']} | {x['mean']:.4f} | {x['min']:.4f} | {x['max']:.4f} |")
 lines += ['','Ablation ARI measures whether the same partition can be recovered without a block. It does not by itself identify a mechanism. Full contingency tables are in the JSON report.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({'nmi':{k:v['nmi'] for k,v in assoc.items()},'ablations':abl},indent=2))
if __name__=='__main__':main()
