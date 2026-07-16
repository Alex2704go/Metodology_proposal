#!/usr/bin/env python3
"""Select stress objects in frozen CEOS space without loading formulas or source IDs."""
from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1];TRAIN=ROOT/'derived/world_vectors_v0.2.npz';POOL=ROOT/'derived/world_vectors_stress_4004.npz';MAN=ROOT/'derived/world_vectors_v0.2_manifest.json';LAB=ROOT/'derived/family_labels_v0.2.npz';OUT=ROOT/'derived/stress_selection_blind.json';VECOUT=ROOT/'derived/stress_pool_frozen_projection.npz'
VIEWS=['ORGANIZATION','OBSERVER_AUGMENTED','FULL_REPRESENTATION']
def main():
 t=np.load(TRAIN,allow_pickle=False);p=np.load(POOL,allow_pickle=False);l=np.load(LAB,allow_pickle=False);m=json.loads(MAN.read_text())
 tn=t['feature_names'].astype(str);pn=p['feature_names'].astype(str);lookup={x:i for i,x in enumerate(pn)};missing=[x for x in tn if x not in lookup]
 if missing:raise RuntimeError(f'Frozen observable schema missing: {missing}')
 raw=p['X_raw'][:,[lookup[x] for x in tn]];idx={x:i for i,x in enumerate(tn)}
 for j,name in enumerate(tn):
  mi=name+'__MISSING'
  if mi in idx:raw[raw[:,idx[mi]]>.5,j]=m['scaling'][j]['median']
 blocks=t['blocks'].astype(str);counts={k:int(v) for k,v in m['block_counts'].items()};Z=np.empty_like(raw,float)
 for j,s in enumerate(m['scaling']):Z[:,j]=np.clip((raw[:,j]-s['median'])/s['scale'],-8,8)/math.sqrt(counts[blocks[j]])
 rawerr=float(np.max(np.abs(raw[:3000]-t['X_raw'])));scalederr=float(np.max(np.abs(Z[:3000]-t['X_scaled'])))
 if rawerr!=0 or scalederr!=0:raise RuntimeError(f'Exact replay failed raw={rawerr} scaled={scalederr}')
 pool_start=3004;pool_ids=p['object_ids'].astype(str)[pool_start:];P=Z[pool_start:];view_metrics={}
 for view in VIEWS:
  mask=l[view+'_feature_mask'];cent=l[view+'_centroids'];train=t['X_scaled'][:,mask];dtrain=np.linalg.norm(train[:,None,:]-cent[None,:,:],axis=2).min(1);d=np.linalg.norm(P[:,None,mask]-cent[None,:,:],axis=2);order=np.argsort(d,axis=1);near=d[np.arange(len(P)),order[:,0]];second=d[np.arange(len(P)),order[:,1]];margin=(second-near)/(second+1e-12);pct=np.array([100*np.mean(dtrain<=x) for x in near]);view_metrics[view]={'family':order[:,0]+1,'distance':near,'second_distance':second,'margin':margin,'percentile':pct}
 org=view_metrics['ORGANIZATION'];distant=int(np.argmax(org['distance']));margin_copy=org['margin'].copy();margin_copy[distant]=np.inf;boundary=int(np.argmin(margin_copy));chosen=[('DISTANT_OBJECT',distant),('BOUNDARY_OBJECT',boundary)]
 selected=[]
 for role,i in chosen:
  views={}
  for view in VIEWS:
   x=view_metrics[view];views[view]={'nearest_family':f"F-{int(x['family'][i]):03d}",'nearest_distance':float(x['distance'][i]),'second_distance':float(x['second_distance'][i]),'margin':float(x['margin'][i]),'training_distance_percentile':float(x['percentile'][i]),'ood_flag':bool(x['percentile'][i]>99)}
  selected.append({'selector':role,'pool_index':i,'object_id':pool_ids[i],'views':views})
 report={'selection_blind':True,'formula_loaded':False,'source_id_loaded':False,'pool_objects':len(P),'replay':{'raw_max_abs_error':rawerr,'scaled_max_abs_error':scalederr},'selected':selected}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');np.savez_compressed(VECOUT,object_ids=pool_ids,X_scaled=P,feature_names=tn,blocks=blocks)
 print(json.dumps(report,indent=2))
if __name__=='__main__':main()
