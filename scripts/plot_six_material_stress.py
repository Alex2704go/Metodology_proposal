#!/usr/bin/env python3
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
ROOT=Path(__file__).resolve().parents[1]
v=np.load(ROOT/'derived/world_vectors_v0.2.npz',allow_pickle=False);l=np.load(ROOT/'derived/family_labels_v0.2.npz',allow_pickle=False);e=np.load(ROOT/'derived/real_examples_projected_vectors.npz',allow_pickle=False);s=np.load(ROOT/'derived/stress_pool_frozen_projection.npz',allow_pickle=False);sel=json.loads((ROOT/'derived/stress_selection_blind.json').read_text());rep=json.loads((ROOT/'derived/six_material_stress_results.json').read_text())
mask=l['ORGANIZATION_feature_mask'];X=v['X_scaled'][:,mask];labels=l['ORGANIZATION'];E=e['X_scaled'][:,mask];forms=list(e['formulas'].astype(str));pool_ids=s['object_ids'].astype(str);P=s['X_scaled'][:,mask]
idx=[int(np.where(pool_ids==x['object_id'])[0][0]) for x in sel['selected']];S=P[idx];sn=[x['formula'] for x in rep['stress_examples']]
pca=PCA(n_components=2,random_state=420042).fit(X);Y=pca.transform(X);EY=pca.transform(E);SY=pca.transform(S)
colors=['#4169e1','#e67e22','#2ca25f','#9b59b6'];fig,ax=plt.subplots(figsize=(11,7.5),dpi=170)
for fam in sorted(set(labels)):
 q=labels==fam;ax.scatter(Y[q,0],Y[q,1],s=9,alpha=.2,color=colors[fam-1],label=f'F-{fam:03d}',rasterized=True)
for (x,y),name in zip(EY,forms):ax.scatter(x,y,s=140,marker='*',c='black',edgecolors='white',zorder=8);ax.annotate(name,(x,y),xytext=(6,6),textcoords='offset points',fontweight='bold')
markers=['X','D'];sc=['#d62728','#00a6a6']
for (x,y),name,m,c in zip(SY,sn,markers,sc):ax.scatter(x,y,s=150,marker=m,c=c,edgecolors='white',linewidths=1,zorder=9,label=name);ax.annotate(name,(x,y),xytext=(8,-14),textcoords='offset points',fontweight='bold',color=c)
ax.set_title('Six-material CEOS stress test — PCA audit view');ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)');ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)');ax.grid(alpha=.15);ax.legend(frameon=False,ncol=2,fontsize=8)
fig.text(.01,.01,'Assignments and OOD decisions use the frozen 75-observable space, not this 2D projection.',fontsize=8,color='#555');fig.tight_layout(rect=(0,.03,1,1));fig.savefig(ROOT/'figures/six_material_stress_pca.png',bbox_inches='tight')
