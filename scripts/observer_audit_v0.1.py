#!/usr/bin/env python3
"""Audit dependence and redundancy among preregistered Observer blocks."""
from __future__ import annotations
import json
from itertools import combinations
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1];DATA=ROOT/'derived/world_vectors_v0.1.npz';OUT=ROOT/'reports/checkpoint_observer_audit.json';MD=ROOT/'reports/checkpoint_observer_audit.md';SEED=420042

def rv(a,b):
 a=a-a.mean(0);b=b-b.mean(0);cross=a.T@b;aa=a.T@a;bb=b.T@b
 den=np.sqrt((aa*aa).sum()*(bb*bb).sum());return float((cross*cross).sum()/den) if den else 0.
def main():
 d=np.load(DATA,allow_pickle=False);X=d['X_scaled'];names=d['feature_names'].astype(str);blocks=d['blocks'].astype(str);rng=np.random.default_rng(SEED)
 ub=sorted(set(blocks));pairs=[]
 for a,b in combinations(ub,2):
  A=X[:,blocks==a];B=X[:,blocks==b];obs=rv(A,B);null=np.array([rv(A,B[rng.permutation(len(B))]) for _ in range(30)])
  pairs.append({'block_a':a,'block_b':b,'rv':obs,'null_mean':float(null.mean()),'null_q95':float(np.quantile(null,.95)),'above_null_q95':bool(obs>np.quantile(null,.95)),'excess':float(obs-np.quantile(null,.95))})
 # Top pairwise feature correlations, excluding one-hot complements from same base only after reporting.
 C=np.corrcoef(X,rowvar=False);tops=[]
 for i in range(len(names)):
  for j in range(i+1,len(names)):
   v=float(C[i,j])
   if np.isfinite(v) and abs(v)>=.90:tops.append({'a':names[i],'block_a':blocks[i],'b':names[j],'block_b':blocks[j],'correlation':v})
 tops=sorted(tops,key=lambda z:-abs(z['correlation']))[:100]
 report={'records':len(X),'features':len(names),'block_dependence':sorted(pairs,key=lambda z:-z['rv']),'high_feature_correlations':tops,'rule':'RV coefficient compared with 30 row-permutation nulls; feature flag |r|>=0.90'}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Checkpoint — Observer Audit','',f'- Blocks: **{len(ub)}**',f'- Block pairs: **{len(pairs)}**',f'- Feature pairs with |r| ≥ 0.90 shown: **{len(tops)}**','','## Block dependence','','| Block A | Block B | RV | Null q95 | Above null? |','|---|---|---:|---:|---|']
 for x in sorted(pairs,key=lambda z:-z['rv']):lines.append(f"| `{x['block_a']}` | `{x['block_b']}` | {x['rv']:.4f} | {x['null_q95']:.4f} | {'YES' if x['above_null_q95'] else 'no'} |")
 lines += ['','## Strong feature-level relations','','| Feature A | Feature B | r |','|---|---|---:|']
 for x in tops[:40]:lines.append(f"| `{x['a']}` | `{x['b']}` | {x['correlation']:.5f} |")
 lines += ['','Зависимость выше Null не означает механизм. Она только показывает, что два Observer-блока организационно согласованы сильнее случайного row alignment.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps({'strongest_blocks':report['block_dependence'][:5],'high_corr_count':len(tops)},indent=2))
if __name__=='__main__':main()
