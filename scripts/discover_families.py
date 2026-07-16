#!/usr/bin/env python3
"""Discover neutral CEOS families with stability scans and directed Null Ladder."""
from __future__ import annotations
import json,math
from itertools import combinations
from pathlib import Path
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score,silhouette_score
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'derived/world_vectors_v0.2.npz';OUT=ROOT/'derived/family_discovery_v0.2.json';LABELS=ROOT/'derived/family_labels_v0.2.npz';MD=ROOT/'reports/stage04_family_discovery_and_nulls.md'
SEED=420042;KS=range(3,13);NSEEDS=10;NULL_REPS=12
VIEWS={
 'ORGANIZATION':['composition_shape','structure_topology','structure_numeric','symmetry_record'],
 'OBSERVER_AUGMENTED':['composition_shape','structure_topology','structure_numeric','symmetry_record','scalar_observers'],
 'FULL_REPRESENTATION':['composition_shape','structure_topology','structure_numeric','symmetry_record','scalar_observers','capability_map','provenance_shape','availability_state']}
NULL_BLOCKS={'COMPOSITION_BLOCK_PERMUTE':['composition_shape'],'STRUCTURE_BLOCK_PERMUTE':['structure_topology','structure_numeric'],'SYMMETRY_BLOCK_PERMUTE':['symmetry_record'],'SCALAR_BLOCK_PERMUTE':['scalar_observers'],'CAPABILITY_BLOCK_PERMUTE':['capability_map']}
def seed_stability(labelsets):
 vals=[adjusted_rand_score(a,b) for a,b in combinations(labelsets,2)];return float(np.mean(vals)),float(np.min(vals))
def sil(X,l,seed):return float(silhouette_score(X,l,sample_size=min(2000,len(X)),random_state=seed))
def fit(X,k,seed,n_init=20):return KMeans(n_clusters=k,n_init=n_init,random_state=seed,algorithm='lloyd').fit(X)
def bootstrap_stability(X,k,reference):
 rng=np.random.default_rng(SEED+991);aris=[]
 for rep in range(12):
  idx=rng.choice(len(X),size=round(.8*len(X)),replace=True);m=fit(X[idx],k,SEED+3000+rep,n_init=10);pred=m.predict(X);aris.append(adjusted_rand_score(reference,pred))
 return {'mean_ari':float(np.mean(aris)),'min_ari':float(np.min(aris)),'values':aris}
def null_matrix(X,view_blocks,blocks,null_name,rng):
 Y=X.copy()
 if null_name=='ALL_COLUMN_SHUFFLE':
  for j in range(Y.shape[1]):Y[:,j]=Y[rng.permutation(len(Y)),j]
 else:
  targets=set(NULL_BLOCKS[null_name]);idx=np.array([b in targets for b in view_blocks]);perm=rng.permutation(len(Y));Y[:,idx]=Y[perm][:,idx]
 return Y
def main():
 d=np.load(DATA,allow_pickle=False);Z=d['X_scaled'];names=d['feature_names'].astype(str);blocks=d['blocks'].astype(str);oids=d['object_ids'].astype(str);rng=np.random.default_rng(SEED)
 reports={};label_arrays={};centroid_arrays={}
 for vname,wanted in VIEWS.items():
  mask=np.isin(blocks,wanted);X=Z[:,mask];vb=blocks[mask];scan=[];models={}
  for k in KS:
   ls=[];sils=[];mins=[]
   for s in range(NSEEDS):
    m=fit(X,k,SEED+s);ls.append(m.labels_);sils.append(sil(X,m.labels_,SEED+s));mins.append(int(np.bincount(m.labels_).min()))
   meanari,minari=seed_stability(ls);scan.append({'k':k,'seed_stability_mean_ari':meanari,'seed_stability_min_ari':minari,'silhouette_mean':float(np.mean(sils)),'silhouette_std':float(np.std(sils)),'minimum_family_size':min(mins)})
   models[k]=(ls[0],fit(X,k,SEED))
  eligible=[x for x in scan if x['minimum_family_size']>=30]
  selected=max(eligible,key=lambda x:(x['seed_stability_mean_ari'],x['silhouette_mean']))
  k=selected['k'];reference,model=models[k];boot=bootstrap_stability(X,k,reference)
  obs_sil=sil(X,reference,SEED);nulls={}
  applicable=['ALL_COLUMN_SHUFFLE']+[x for x,bs in NULL_BLOCKS.items() if any(b in wanted for b in bs)]
  for null_name in applicable:
   vals=[];mins_null=[]
   for rep in range(NULL_REPS):
    Y=null_matrix(X,vb,blocks,null_name,rng);m=fit(Y,k,SEED+5000+rep,n_init=10);vals.append(sil(Y,m.labels_,SEED+rep));mins_null.append(int(np.bincount(m.labels_).min()))
   nulls[null_name]={'silhouettes':vals,'mean':float(np.mean(vals)),'q95':float(np.quantile(vals,.95)),'observed_minus_q95':float(obs_sil-np.quantile(vals,.95)),'minimum_family_size_min':min(mins_null)}
  admit=bool(obs_sil>nulls['ALL_COLUMN_SHUFFLE']['q95'] and boot['mean_ari']>=.75 and np.bincount(reference).min()>=30)
  # Stable neutral labels ordered by centroid norm then original cluster index.
  order=sorted(range(k),key=lambda c:(float(np.linalg.norm(model.cluster_centers_[c])),c));mapping={old:i+1 for i,old in enumerate(order)};neutral=np.array([mapping[x] for x in reference])
  reports[vname]={'features':int(mask.sum()),'blocks':wanted,'scan':scan,'selected_k':k,'observed_silhouette':obs_sil,'bootstrap':boot,'family_sizes':{f'F-{i:03d}':int((neutral==i).sum()) for i in range(1,k+1)},'nulls':nulls,'admitted':admit}
  label_arrays[vname]=neutral;centroid_arrays[vname]=model.cluster_centers_[order];label_arrays[vname+'_feature_mask']=mask
 report={'protocol':'family_discovery_v0.2','records':len(Z),'views':reports}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 np.savez_compressed(LABELS,object_ids=oids,feature_names=names,blocks=blocks,**label_arrays,**{k+'_centroids':v for k,v in centroid_arrays.items()})
 lines=['# Stage 04 — Family Discovery and Null Ladder','','Нейтральные семейства; литературные отображения заблокированы.','']
 for v,r in reports.items():
  lines += [f'## {v}','',f"- Organizational observables: **{r['features']}**",f"- Selected k: **{r['selected_k']}**",f"- Silhouette: **{r['observed_silhouette']:.4f}**",f"- Bootstrap mean ARI: **{r['bootstrap']['mean_ari']:.4f}**",f"- Admission: **{'PASS' if r['admitted'] else 'FAIL'}**",'', 'Family sizes: '+', '.join(f'{k}={n}' for k,n in r['family_sizes'].items()),'', '| Null | Mean silhouette | q95 | Observed − q95 |','|---|---:|---:|---:|']
  for n,x in r['nulls'].items():lines.append(f"| `{n}` | {x['mean']:.4f} | {x['q95']:.4f} | {x['observed_minus_q95']:.4f} |")
  lines += ['','### k scan','','| k | Seed ARI | Silhouette | Min family |','|---:|---:|---:|---:|']
  for x in r['scan']:lines.append(f"| {x['k']} | {x['seed_stability_mean_ari']:.4f} | {x['silhouette_mean']:.4f} | {x['minimum_family_size']} |")
  lines.append('')
 lines += ['## Interpretation lock','','`F-###` labels describe reproducible partitions of the chosen Representation view. They are not yet physical, chemical, or literature families.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({v:{'k':r['selected_k'],'silhouette':r['observed_silhouette'],'bootstrap_ari':r['bootstrap']['mean_ari'],'admitted':r['admitted'],'sizes':r['family_sizes']} for v,r in reports.items()},indent=2))
if __name__=='__main__':main()
