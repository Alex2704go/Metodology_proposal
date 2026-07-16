#!/usr/bin/env python3
"""Project four out-of-sample records into admitted CEOS family spaces with OOD checks."""
from __future__ import annotations
import json,math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
TRAIN=ROOT/'derived/world_vectors_v0.2.npz';MERGED=ROOT/'derived/world_vectors_examples_3004.npz';MAN=ROOT/'derived/world_vectors_v0.2_manifest.json';LAB=ROOT/'derived/family_labels_v0.2.npz';CARDS=ROOT/'derived/real_examples_representation_cards.json';OUT=ROOT/'derived/real_examples_family_assignments.json';MD=ROOT/'reports/real_examples_ceos_families.md'
VIEWS=['ORGANIZATION','OBSERVER_AUGMENTED','FULL_REPRESENTATION']
def main():
 t=np.load(TRAIN,allow_pickle=False);m=np.load(MERGED,allow_pickle=False);l=np.load(LAB,allow_pickle=False);manifest=json.loads(MAN.read_text());cards=json.loads(CARDS.read_text())['cards']
 tn=t['feature_names'].astype(str);mn=m['feature_names'].astype(str);lookup={x:i for i,x in enumerate(mn)}
 missing=[x for x in tn if x not in lookup]
 if missing:raise RuntimeError(f'Merged extraction lacks {missing}')
 raw=m['X_raw'][:,[lookup[x] for x in tn]]
 # Replace refitted imputation values with frozen training medians wherever a saved
 # missingness indicator is active. This is mandatory for true out-of-sample replay.
 name_to_index={x:i for i,x in enumerate(tn)}
 for j,name in enumerate(tn):
  miss=name+'__MISSING'
  if miss in name_to_index:
   indicator=raw[:,name_to_index[miss]]>0.5
   raw[indicator,j]=manifest['scaling'][j]['median']
 # Exact replay check on the 3,000 training rows before applying saved scaling.
 raw_diff=float(np.max(np.abs(raw[:3000]-t['X_raw'])))
 Z=np.empty_like(raw,float);counts={k:int(v) for k,v in manifest['block_counts'].items()};blocks=t['blocks'].astype(str)
 for j,s in enumerate(manifest['scaling']):Z[:,j]=np.clip((raw[:,j]-s['median'])/s['scale'],-8,8)/math.sqrt(counts[blocks[j]])
 scaled_diff=float(np.max(np.abs(Z[:3000]-t['X_scaled'])))
 if raw_diff>1e-12 or scaled_diff>1e-12:raise RuntimeError(f'Replay mismatch raw={raw_diff} scaled={scaled_diff}')
 results=[]
 for ei,card in enumerate(cards):
  row=3000+ei;assign={}
  for view in VIEWS:
   mask=l[view+'_feature_mask'];cent=l[view+'_centroids'];Xtr=t['X_scaled'][:,mask];x=Z[row,mask]
   td=np.linalg.norm(Xtr[:,None,:]-cent[None,:,:],axis=2);train_near=td.min(1)
   d=np.linalg.norm(cent-x,axis=1);order=np.argsort(d);fam=int(order[0]+1);margin=float((d[order[1]]-d[order[0]])/(d[order[1]]+1e-12));pct=float(100*np.mean(train_near<=d[order[0]]))
   assign[view]={'family':f'F-{fam:03d}','nearest_distance':float(d[order[0]]),'second_distance':float(d[order[1]]),'margin':margin,'training_distance_percentile':pct,'ood_flag':bool(pct>99)}
  results.append({'formula':card['requested_formula'],'material_id':card['material_id'],'assignments':assign,'primary_family':assign['ORGANIZATION']['family'],'confirmed_by_observer_view':assign['ORGANIZATION']['family']==assign['OBSERVER_AUGMENTED']['family']})
 report={'classification':'out-of-sample nearest admitted centroid','primary_view':'ORGANIZATION','family_scope':'CEOS Structural Representation Family','replay_checks':{'raw_max_abs_difference':raw_diff,'scaled_max_abs_difference':scaled_diff},'results':results}
 np.savez_compressed(ROOT/'derived/real_examples_projected_vectors.npz', feature_names=tn, blocks=blocks, example_ids=np.array([c['material_id'] for c in cards]), formulas=np.array([c['requested_formula'] for c in cards]), X_scaled=Z[3000:])
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 lines=['# Real Materials → CEOS Families','','Primary view: **ORGANIZATION**. `OBSERVER_AUGMENTED` is an independent confirmation view; `FULL_REPRESENTATION` is a language/control view.','',f'- Training replay raw max error: **{raw_diff:.1e}**',f'- Training replay scaled max error: **{scaled_diff:.1e}**','', '| Formula | ORGANIZATION | Margin | OOD percentile | Observer confirmation | FULL language family |','|---|---|---:|---:|---|---|']
 for x in results:
  a=x['assignments'];lines.append(f"| {x['formula']} | **{a['ORGANIZATION']['family']}** | {a['ORGANIZATION']['margin']:.3f} | {a['ORGANIZATION']['training_distance_percentile']:.1f}% | {'YES' if x['confirmed_by_observer_view'] else 'NO: '+a['OBSERVER_AUGMENTED']['family']} | {a['FULL_REPRESENTATION']['family']} |")
 lines += ['','## Reading the checks','','- Margin compares the nearest and second-nearest centroids; it is not a probability.','- OOD percentile compares the example distance with training-object distances to their nearest centroid. Above 99% is flagged.','- A family is considered cross-view confirmed only when ORGANIZATION and OBSERVER_AUGMENTED agree.','- FULL_REPRESENTATION is not used as the material-family decision because capability/provenance form a distinct representation-language layer.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
