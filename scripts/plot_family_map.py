#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
ROOT=Path(__file__).resolve().parents[1]
v=np.load(ROOT/'derived/world_vectors_v0.2.npz',allow_pickle=False);l=np.load(ROOT/'derived/family_labels_v0.2.npz',allow_pickle=False);e=np.load(ROOT/'derived/real_examples_projected_vectors.npz',allow_pickle=False)
mask=l['ORGANIZATION_feature_mask'];X=v['X_scaled'][:,mask];E=e['X_scaled'][:,mask];labels=l['ORGANIZATION'];forms=e['formulas'].astype(str)
pca=PCA(n_components=2,random_state=420042).fit(X);Y=pca.transform(X);EY=pca.transform(E)
colors=['#4169e1','#e67e22','#2ca25f','#9b59b6']
fig,ax=plt.subplots(figsize=(10,7),dpi=170)
for fam in sorted(set(labels)):
 idx=labels==fam;ax.scatter(Y[idx,0],Y[idx,1],s=10,alpha=.25,color=colors[fam-1],label=f'F-{fam:03d} (n={idx.sum()})',rasterized=True)
for (x,y),name in zip(EY,forms):
 ax.scatter(x,y,s=150,marker='*',c='black',edgecolors='white',linewidths=1.3,zorder=10)
 ax.annotate(name,(x,y),xytext=(7,7),textcoords='offset points',fontsize=10,fontweight='bold',zorder=11)
ax.set_title('CEOS Structural Representation Families — PCA audit view')
ax.set_xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)')
ax.set_ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)')
ax.grid(alpha=.15);ax.legend(frameon=False,ncol=2,fontsize=9)
fig.text(.01,.01,'PCA is a visualization only; assignments use full 75-dimensional ORGANIZATION space.',fontsize=8,color='#555')
fig.tight_layout(rect=(0,.03,1,1));fig.savefig(ROOT/'figures/structural_families_pca.png',bbox_inches='tight')
print({'explained_variance_2d':float(pca.explained_variance_ratio_.sum())})
