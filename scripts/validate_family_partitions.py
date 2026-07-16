#!/usr/bin/env python3
"""Cross-view consistency, family profiles, and assignment diagnostics."""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path
import numpy as np
from sklearn.metrics import adjusted_rand_score
ROOT=Path(__file__).resolve().parents[1];VEC=ROOT/'derived/world_vectors_v0.2.npz';LAB=ROOT/'derived/family_labels_v0.2.npz';OUT=ROOT/'reports/checkpoint_family_validation.json';MD=ROOT/'reports/checkpoint_family_validation.md'
VIEWS=['ORGANIZATION','OBSERVER_AUGMENTED','FULL_REPRESENTATION']
def main():
 v=np.load(VEC,allow_pickle=False);z=v['X_scaled'];names=v['feature_names'].astype(str);blocks=v['blocks'].astype(str)
 l=np.load(LAB,allow_pickle=False);report={'cross_view':[],'views':{}}
 for a,b in combinations(VIEWS,2):
  la=l[a];lb=l[b];cont={}
  for x,y in zip(la,lb):cont[f'F-{x:03d}|F-{y:03d}']=cont.get(f'F-{x:03d}|F-{y:03d}',0)+1
  report['cross_view'].append({'a':a,'b':b,'ari':float(adjusted_rand_score(la,lb)),'contingency':cont})
 for view in VIEWS:
  labels=l[view];mask=l[view+'_feature_mask'];X=z[:,mask];fn=names[mask];fb=blocks[mask];cent=l[view+'_centroids'];profiles=[]
  d=np.linalg.norm(X[:,None,:]-cent[None,:,:],axis=2);order=np.sort(d,axis=1);margin=(order[:,1]-order[:,0])/(order[:,1]+1e-12)
  for fam in sorted(set(labels)):
   idx=labels==fam;mu=X[idx].mean(0);top=np.argsort(-np.abs(mu))[:12]
   profiles.append({'family':f'F-{fam:03d}','size':int(idx.sum()),'median_assignment_margin':float(np.median(margin[idx])),'q10_assignment_margin':float(np.quantile(margin[idx],.1)),'top_standardized_features':[{'feature':fn[j],'block':fb[j],'mean':float(mu[j])} for j in top]})
  report['views'][view]={'families':profiles,'overall_margin':{'median':float(np.median(margin)),'q10':float(np.quantile(margin,.1))},'low_margin_below_0.05':int((margin<.05).sum())}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Checkpoint — Family Validation','','## Cross-view agreement','','| View A | View B | ARI |','|---|---|---:|']
 for x in report['cross_view']:lines.append(f"| `{x['a']}` | `{x['b']}` | {x['ari']:.4f} |")
 for view,x in report['views'].items():
  lines += ['',f'## {view}','',f"- Median assignment margin: **{x['overall_margin']['median']:.4f}**",f"- q10 margin: **{x['overall_margin']['q10']:.4f}**",f"- Objects with margin < 0.05: **{x['low_margin_below_0.05']}**",'','| Family | Size | Median margin | q10 margin | Leading neutral coordinates |','|---|---:|---:|---:|---|']
  for f in x['families']:
   top='; '.join(f"{q['feature']} ({q['mean']:+.2f})" for q in f['top_standardized_features'][:5]);lines.append(f"| {f['family']} | {f['size']} | {f['median_assignment_margin']:.3f} | {f['q10_assignment_margin']:.3f} | {top} |")
 lines += ['','Margins measure geometric confidence relative to the two nearest centroids. They are not probabilities.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({'cross_view_ari':[{x['a']+' vs '+x['b']:x['ari']} for x in report['cross_view']], 'low_margin':{k:v['low_margin_below_0.05'] for k,v in report['views'].items()}},indent=2))
if __name__=='__main__':main()
