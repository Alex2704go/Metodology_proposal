#!/usr/bin/env python3
"""Build OOD Biography and Boundary Explanation in frozen CEOS spaces."""
from __future__ import annotations
import json
from collections import Counter
from pathlib import Path
import numpy as np
from scipy.optimize import linprog
from sklearn.neighbors import NearestNeighbors
ROOT=Path(__file__).resolve().parents[1];TRAIN=ROOT/'derived/world_vectors_v0.2.npz';POOL=ROOT/'derived/stress_pool_frozen_projection.npz';LAB=ROOT/'derived/family_labels_v0.2.npz';SEL=ROOT/'derived/stress_selection_blind.json';SIX=ROOT/'derived/six_material_stress_results.json';OUT=ROOT/'derived/assignment_explanations_v0.1.json';MD=ROOT/'reports/assignment_explanations.md'
CHANNELS={'representation':['composition_shape','structure_topology','structure_numeric','symmetry_record'],'composition':['composition_shape'],'structure':['structure_topology','structure_numeric'],'symmetry':['symmetry_record'],'observer':['scalar_observers']}
def centroids(X,labels):return np.vstack([X[labels==f].mean(0) for f in sorted(set(labels))])
def distance_profile(X,x,labels):
 c=centroids(X,labels);d=np.linalg.norm(c-x,axis=1);o=np.argsort(d);train_d=np.linalg.norm(X[:,None,:]-c[None,:,:],axis=2).min(1);return {'nearest_family':f'F-{o[0]+1:03d}','second_family':f'F-{o[1]+1:03d}','distances':{f'F-{i+1:03d}':float(v) for i,v in enumerate(d)},'nearest_distance':float(d[o[0]]),'second_distance':float(d[o[1]]),'margin':float((d[o[1]]-d[o[0]])/(d[o[1]]+1e-12)),'training_distance_percentile':float(100*np.mean(train_d<=d[o[0]])),'ood_flag':bool(100*np.mean(train_d<=d[o[0]])>99)}
def knn_profile(X,x,labels,ks=(5,10,25)):
 mx=max(ks);nn=NearestNeighbors(n_neighbors=mx+1,metric='euclidean').fit(X);td,_=nn.kneighbors(X)
 d=np.linalg.norm(X-x,axis=1);order=np.argsort(d,kind='stable');out={}
 for k in ks:
  train_r=td[:,k];r=float(d[order[k-1]]);med=float(np.median(train_r));out[str(k)]={'radius':r,'training_percentile':float(100*np.mean(train_r<=r)),'training_median_radius':med,'radius_over_training_median':float(r/med) if med>0 else None,'relative_density_proxy':float(med/(r+1e-12)) if med>0 else None}
 r25=float(d[order[24]]);tie_complete=order[d[order] <= r25+1e-12];fam=Counter(f'F-{int(labels[i]):03d}' for i in tie_complete);out['neighbor_family_counts_k25']=dict(fam);out['effective_neighbor_count_k25']=len(tie_complete);out['nearest_neighbor_distance']=float(d[order[0]]);return out
def hull_projection(V,x,maxiter=5000,tol=1e-10):
 y=V[np.argmin(np.linalg.norm(V-x,axis=1))].copy();last=np.inf
 for it in range(maxiter):
  g=y-x;j=int(np.argmin(V@g));s=V[j];direction=s-y;den=float(direction@direction)
  if den==0:break
  gamma=float(np.clip(-(g@direction)/den,0,1));y=y+gamma*direction;res=float(np.linalg.norm(y-x))
  if abs(last-res)<tol:break
  last=res
 return {'projection_distance':float(np.linalg.norm(y-x)),'iterations':it+1}
def evaluate_null(X,x,labels):return distance_profile(X,x,labels)
def main():
 t=np.load(TRAIN,allow_pickle=False);p=np.load(POOL,allow_pickle=False);l=np.load(LAB,allow_pickle=False);sel=json.loads(SEL.read_text());six=json.loads(SIX.read_text());names=t['feature_names'].astype(str);blocks=t['blocks'].astype(str);X=t['X_scaled'];P=p['X_scaled'];pids=p['object_ids'].astype(str);labels=l['ORGANIZATION'];formula_by_oid={x['object_id']:x['formula'] for x in six['stress_examples']}
 selected=[]
 for s in sel['selected']:
  pi=int(np.where(pids==s['object_id'])[0][0]);x=P[pi];channels={};knn={}
  for cname,bs in CHANNELS.items():
   mask=np.isin(blocks,bs);channels[cname]=distance_profile(X[:,mask],x[mask],labels);knn[cname]=knn_profile(X[:,mask],x[mask],labels,ks=(5,10,25) if cname=='representation' else (25,))
  fullmask=np.isin(blocks,CHANNELS['representation']);Xf=X[:,fullmask];xf=x[fullmask];cf=centroids(Xf,labels);fd=np.linalg.norm(cf-xf,axis=1);order=np.argsort(fd);contrib={}
  for rank,fi in [('nearest',int(order[0])),('second',int(order[1]))]:
   blockvals={};total=0.
   for bset_name,bset in [('composition',['composition_shape']),('structure',['structure_topology','structure_numeric']),('symmetry',['symmetry_record'])]:
    bm=np.isin(blocks,bset);val=float(np.sum((x[bm]-X[labels==(fi+1)][:,bm].mean(0))**2));blockvals[bset_name]=val;total+=val
   contrib[rank]={'family':f'F-{fi+1:03d}','squared_distance_total':total,'by_block_squared':blockvals,'by_block_fraction':{k:v/total if total else 0 for k,v in blockvals.items()}}
  contrast={k:contrib['second']['by_block_squared'][k]-contrib['nearest']['by_block_squared'][k] for k in contrib['nearest']['by_block_squared']}
  # Positive contrast supports the nearest family; negative contrast supports the runner-up.
  # Exact full-space hull feasibility and approximate projection distance for nearest family.
  fi=int(order[0]);V=Xf[labels==(fi+1)];Aeq=np.vstack([V.T,np.ones(len(V))]);beq=np.r_[xf,1.];lp=linprog(np.zeros(len(V)),A_eq=Aeq,b_eq=beq,bounds=(0,None),method='highs');hull={'family':f'F-{fi+1:03d}','exact_full_space_membership':bool(lp.success),'linprog_status':int(lp.status),'linprog_message':lp.message,**hull_projection(V,xf)}
  # Scale Null 1: remove registered size observables, frozen labels.
  scale_sensitive=np.array([b in {'structure_topology','structure_numeric'} and any(q in n for q in ['leaves','object_nodes','list_nodes','list_size','.count']) for n,b in zip(names,blocks)])
  keep=fullmask & ~scale_sensitive;null_remove=evaluate_null(X[:,keep],x[keep],labels)
  # Scale Null 2: unit-normalize structure channel, preserve other channels and labels.
  struct_local=np.isin(blocks[fullmask],['structure_topology','structure_numeric']);xu=x[fullmask].copy()
  # Row-wise normalization preserves the frozen labels but removes structure-block magnitude.
  Xu=X[:,fullmask].copy()
  for i in range(len(Xu)):
   q=np.linalg.norm(Xu[i,struct_local])
   if q>0:Xu[i,struct_local]/=q
  q=np.linalg.norm(xu[struct_local])
  if q>0:xu[struct_local]/=q
  null_unit=evaluate_null(Xu,xu,labels)
  original=channels['representation'];scale_driven=bool(original['ood_flag'] and not null_remove['ood_flag'] and not null_unit['ood_flag'])
  selected.append({'selector':s['selector'],'object_id':s['object_id'],'formula':formula_by_oid[s['object_id']],'channels':channels,'neighborhoods':knn,'centroid_distance_decomposition':contrib,'block_contrast_second_minus_nearest':contrast,'convex_hull':hull,'scale_nulls':{'removed_observable_count':int(scale_sensitive.sum()),'REMOVE_SCALE_SENSITIVE_STRUCTURE_OBSERVABLES':null_remove,'STRUCTURE_BLOCK_UNIT_NORM':null_unit,'scale_driven_by_registered_rule':scale_driven}})
 report={'protocol':'assignment_explanation_v0.1','probabilities_used':False,'distance_statement':'All block distances are in frozen scaled organizational-observable coordinates.','objects':selected}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Assignment Explanations — OOD Biography and Boundary Anatomy','','No pseudo-probabilities are used. Channel evidence is reported as distances, percentiles and margins.','']
 for o in selected:
  lines += [f"## {o['selector']}: {o['formula']}",'','### Organizational distances','','| Channel | Nearest | Second | Margin | Percentile | OOD |','|---|---|---|---:|---:|---|']
  for c,x in o['channels'].items():lines.append(f"| {c} | {x['nearest_family']} ({x['nearest_distance']:.3f}) | {x['second_family']} ({x['second_distance']:.3f}) | {x['margin']:.3f} | {x['training_distance_percentile']:.1f}% | {'YES' if x['ood_flag'] else 'no'} |")
  lines += ['','### Centroid-distance decomposition','','| Target | Family | Composition d² | Structure d² | Symmetry d² |','|---|---|---:|---:|---:|']
  for k,x in o['centroid_distance_decomposition'].items():lines.append(f"| {k} | {x['family']} | {x['by_block_squared']['composition']:.3f} | {x['by_block_squared']['structure']:.3f} | {x['by_block_squared']['symmetry']:.3f} |")
  c=o['block_contrast_second_minus_nearest'];lines += ['',f"Block contrast `d²(second) − d²(nearest)`: composition {c['composition']:+.3f}, structure {c['structure']:+.3f}, symmetry {c['symmetry']:+.3f}.", 'Positive supports the nearest family; negative supports the runner-up.']
  h=o['convex_hull'];lines += ['','### Neighborhood and hull','',f"- k=25 radius percentile: **{o['neighborhoods']['representation']['25']['training_percentile']:.1f}%**",f"- k=25 radius / training median: **{o['neighborhoods']['representation']['25']['radius_over_training_median']:.2f}**",f"- neighbor-family counts: `{o['neighborhoods']['representation']['neighbor_family_counts_k25']}`",f"- exact full-space convex-hull membership in {h['family']}: **{h['exact_full_space_membership']}**",f"- approximate distance to family convex hull: **{h['projection_distance']:.4f}**",'','### Scale Nulls','','| View | Nearest | Margin | Percentile | OOD |','|---|---|---:|---:|---|']
  orig=o['channels']['representation'];lines.append(f"| Original | {orig['nearest_family']} | {orig['margin']:.3f} | {orig['training_distance_percentile']:.1f}% | {'YES' if orig['ood_flag'] else 'no'} |")
  for key in ['REMOVE_SCALE_SENSITIVE_STRUCTURE_OBSERVABLES','STRUCTURE_BLOCK_UNIT_NORM']:
   x=o['scale_nulls'][key];lines.append(f"| `{key}` | {x['nearest_family']} | {x['margin']:.3f} | {x['training_distance_percentile']:.1f}% | {'YES' if x['ood_flag'] else 'no'} |")
  lines.append(f"\nScale-driven under the registered two-Null rule: **{o['scale_nulls']['scale_driven_by_registered_rule']}**")
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps([{'formula':o['formula'],'channels':{k:{q:x[q] for q in ['nearest_family','second_family','margin','training_distance_percentile','ood_flag']} for k,x in o['channels'].items()},'hull':o['convex_hull'],'scale_nulls':o['scale_nulls']} for o in selected],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
