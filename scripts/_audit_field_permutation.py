#!/usr/bin/env python3
"""Build block-aware object vectors from generic Builder outputs and run QC."""
from __future__ import annotations
import gzip,hashlib,json,math
from collections import Counter,defaultdict
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'derived/builder_audit_field_permutation.jsonl.gz'
OUT=ROOT/'derived/builder_audit_field_permutation.npz'; MAN=ROOT/'derived/builder_audit_field_permutation_manifest.json'; REPORT=ROOT/'reports/builder_audit_field_permutation.md'
SEED=420042

def walk(v,path,nums,dict_sizes,list_sizes,depth=0):
 if isinstance(v,dict):
  dict_sizes.append(len(v))
  for k,x in v.items():walk(x,f'{path}.{k}',nums,dict_sizes,list_sizes,depth+1)
 elif isinstance(v,list):
  list_sizes.append(len(v))
  for x in v:walk(x,f'{path}[]',nums,dict_sizes,list_sizes,depth+1)
 elif isinstance(v,(int,float)) and not isinstance(v,bool) and math.isfinite(float(v)):nums[path].append(float(v))
def topo(v):
 if isinstance(v,dict):children=list(v.values());o,l=1,0
 elif isinstance(v,list):children=v;o,l=0,1
 else:return 0,1,0,0
 z=[topo(x) for x in children]
 return 1+max((a[0] for a in z),default=0),sum(a[1] for a in z),o+sum(a[2] for a in z),l+sum(a[3] for a in z)
def add_numeric(cols,names,blocks,name,block,vals,missing_block='availability_state'):
 a=np.asarray(vals,dtype=float);bad=~np.isfinite(a)
 if bad.any():
  good=a[~bad];fill=float(np.median(good)) if len(good) else 0.;a[bad]=fill
  cols.append(bad.astype(float));names.append(name+'__MISSING');blocks.append(missing_block)
 cols.append(a);names.append(name);blocks.append(block)
def add_categorical(cols,names,blocks,name,block,vals,maxcat=64):
 vv=['__NONE__' if v is None else str(v) for v in vals];cats=sorted(set(vv))
 if not 2<=len(cats)<=maxcat:return
 for c in (cats[1:] if len(cats)==2 else cats):
  cols.append(np.asarray([x==c for x in vv],float));names.append(f'{name}=={c}');blocks.append(block)
def main():
 rows=[]
 with gzip.open(DATA,'rt',encoding='utf-8') as f:
  for line in f:rows.append(json.loads(line))
 n=len(rows);cols=[];names=[];blocks=[]
 # Composition shape: keys are deliberately ignored; only distribution shape is retained.
 comps=[r.get('composition') or {} for r in rows]
 add_numeric(cols,names,blocks,'composition.key_count','composition_shape',[len(x) for x in comps])
 # composition.total excluded after Observer Audit: exact cross-block size duplicate
 for stat in ['entropy','max_share','min_share','l2']:
  vals=[]
  for x in comps:
   a=np.asarray(sorted(x.values()),float);p=a/a.sum() if len(a) and a.sum()!=0 else np.zeros(len(a))
   if stat=='entropy':v=float(-(p[p>0]*np.log(p[p>0])).sum()) if len(p) else 0.
   elif stat=='max_share':v=float(p.max()) if len(p) else 0.
   elif stat=='min_share':v=float(p.min()) if len(p) else 0.
   else:v=float(np.sqrt((p*p).sum()))
   vals.append(v)
  add_numeric(cols,names,blocks,'composition.'+stat,'composition_shape',vals)
 maxk=max(map(len,comps))
 for j in range(maxk):
  vals=[]
  for x in comps:
   a=np.asarray(sorted(x.values()),float);p=sorted((a/a.sum()).tolist(),reverse=True) if len(a) and a.sum()!=0 else []
   vals.append(p[j] if j<len(p) else 0.)
  add_numeric(cols,names,blocks,f'composition.sorted_share_{j+1}','composition_shape',vals)
 # Generic structure topology and numeric leaf-path aggregations.
 path_rows=[]
 for r in rows:
  s=r.get('structure');d,leaf,on,ln=topo(s);nums=defaultdict(list);ds=[];ls=[];walk(s,'structure',nums,ds,ls)
  path_rows.append(nums)
  for name,val in [('depth',d),('leaves',leaf),('object_nodes',on),('list_nodes',ln),('dict_size_mean',np.mean(ds)),('dict_size_std',np.std(ds)),('list_size_mean',np.mean(ls)),('list_size_std',np.std(ls)),('list_size_max',max(ls))]:
   pass
 topo_names=['depth','leaves','object_nodes','list_nodes','dict_size_mean','dict_size_std','list_size_mean','list_size_std','list_size_max']
 topo_values={k:[] for k in topo_names}
 for r in rows:
  s=r.get('structure');d,leaf,on,ln=topo(s);nums=defaultdict(list);ds=[];ls=[];walk(s,'structure',nums,ds,ls)
  ds=sorted(ds);ls=sorted(ls)
  vv=[d,leaf,on,ln,float(np.mean(ds)),float(np.std(ds)),float(np.mean(ls)),float(np.std(ls)),max(ls)]
  for k,v in zip(topo_names,vv):topo_values[k].append(v)
 for k,v in topo_values.items():add_numeric(cols,names,blocks,'structure.'+k,'structure_topology',v)
 paths=sorted(set().union(*(x.keys() for x in path_rows)))
 for path in paths:
  present=sum(path in x for x in path_rows)
  if present/n<.95:continue
  for stat in ['count','mean','std','min','max']:
   vals=[]
   for x in path_rows:
    a=np.asarray(sorted(x.get(path,[])),float)
    if stat=='count':v=len(a)
    elif not len(a):v=np.nan
    elif stat=='mean':v=float(a.mean())
    elif stat=='std':v=float(a.std())
    elif stat=='min':v=float(a.min())
    else:v=float(a.max())
    vals.append(v)
   add_numeric(cols,names,blocks,f'{path}.{stat}','structure_numeric',vals)
 # Fixed-record symmetry: generic scalar slot encoding.
 syms=[r.get('symmetry') or {} for r in rows];symkeys=sorted(set().union(*(x for x in syms)))
 for k in symkeys:
  vals=[x.get(k) for x in syms];non=[v for v in vals if v is not None]
  if non and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in non):add_numeric(cols,names,blocks,'symmetry.'+k,'symmetry_record',[np.nan if v is None else v for v in vals])
  else:add_categorical(cols,names,blocks,'symmetry.'+k,'symmetry_record',vals)
 # Scalar top-level observers; source IDs and service fields are excluded.
 scalar_fields=['band_gap','formation_energy_per_atom','density','volume','nelements','is_magnetic','ordering']
 for k in scalar_fields:
  vals=[r.get(k) for r in rows];non=[v for v in vals if v is not None]
  if non and all(isinstance(v,(int,float)) and not isinstance(v,bool) for v in non):add_numeric(cols,names,blocks,k,'scalar_observers',[np.nan if v is None else v for v in vals])
  else:add_categorical(cols,names,blocks,k,'scalar_observers',vals)
 # Capability MAP/RECORD boolean slots.
 caps=[r.get('has_props') or {} for r in rows];capkeys=sorted(set().union(*(x for x in caps)))
 for k in capkeys:add_numeric(cols,names,blocks,'has_props.'+k,'capability_map',[float(bool(x.get(k))) for x in caps])
 add_numeric(cols,names,blocks,'has_props.active_count','capability_map',[sum(bool(v) for v in x.values()) for x in caps])
 # Provenance organizational shape only; content strings are not used.
 origins=[r.get('origins') or [] for r in rows];bmeta=[r.get('builder_meta') or {} for r in rows]
 add_numeric(cols,names,blocks,'origins.length','provenance_shape',[len(x) for x in origins])
 add_numeric(cols,names,blocks,'origins.keyset_variants','provenance_shape',[len({tuple(sorted(y)) for y in x if isinstance(y,dict)}) for x in origins])
 add_numeric(cols,names,blocks,'builder_meta.slot_count','provenance_shape',[len(x) for x in bmeta])
 add_numeric(cols,names,blocks,'builder_meta.populated','provenance_shape',[sum(v is not None for v in x.values()) for x in bmeta])
 X=np.column_stack(cols);raw_count=X.shape[1]
 # Remove constants, then exact duplicate columns (including complements are retained).
 keep=[];removed_constants=[]
 for j in range(X.shape[1]):
  if np.nanmax(X[:,j])-np.nanmin(X[:,j])==0:removed_constants.append(names[j])
  else:keep.append(j)
 X=X[:,keep];names=[names[j] for j in keep];blocks=[blocks[j] for j in keep]
 seen={};keep=[];dups=[]
 for j in range(X.shape[1]):
  h=hashlib.sha256(np.ascontiguousarray(X[:,j]).tobytes()).hexdigest()
  if h in seen and np.array_equal(X[:,j],X[:,seen[h]]):dups.append({'removed':names[j],'kept':names[seen[h]]})
  else:seen[h]=j;keep.append(j)
 X=X[:,keep];names=[names[j] for j in keep];blocks=[blocks[j] for j in keep]
 # Observer-audit revision: remove near-duplicate columns within the same block only.
 corr_removed=[];keep=[]
 for j in range(X.shape[1]):
  duplicate_of=None
  for i in keep:
   if blocks[i]==blocks[j]:
    c=np.corrcoef(X[:,i],X[:,j])[0,1]
    if np.isfinite(c) and abs(c)>=0.995:
     duplicate_of=i;break
  if duplicate_of is None:keep.append(j)
  else:corr_removed.append({'removed':names[j],'kept':names[duplicate_of]})
 X=X[:,keep];names=[names[j] for j in keep];blocks=[blocks[j] for j in keep]
 # Robust scaling and equal block weighting.
 Z=np.zeros_like(X,dtype=float);scale_info=[]
 for j in range(X.shape[1]):
  med=float(np.median(X[:,j]));q1,q3=np.quantile(X[:,j],[.25,.75]);sc=float(q3-q1)
  if sc==0:sc=float(np.std(X[:,j]))
  if sc==0:sc=1.
  Z[:,j]=np.clip((X[:,j]-med)/sc,-8,8);scale_info.append({'median':med,'scale':sc})
 counts=Counter(blocks)
 for j,b in enumerate(blocks):Z[:,j]/=math.sqrt(counts[b])
 row_hash=Counter(hashlib.sha256(np.ascontiguousarray(Z[i]).tobytes()).hexdigest() for i in range(n))
 np.savez_compressed(OUT,X_raw=X,X_scaled=Z,object_ids=np.array([r['object_id'] for r in rows]),feature_names=np.array(names),blocks=np.array(blocks))
 manifest={'records':n,'raw_candidate_features':raw_count,'retained_features':len(names),'block_counts':dict(Counter(blocks)),'removed_constants':removed_constants,'removed_exact_duplicates':dups,'removed_within_block_correlations':corr_removed,'nonfinite_after_processing':int((~np.isfinite(Z)).sum()),'duplicate_vector_rows_beyond_first':sum(v-1 for v in row_hash.values() if v>1),'feature_names':names,'blocks':blocks,'scaling':scale_info,'forbidden_feature_checks':{'material_id_present':any('material_id' in x for x in names),'formula_present':any('formula' in x for x in names),'object_id_present':any('object_id' in x for x in names),'element_identity_features':False}}
 MAN.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 lines=['# Checkpoint — WORLD Vector QC','',f'- Objects: **{n}**',f'- Candidate features: **{raw_count}**',f'- Retained features: **{len(names)}**',f"- Non-finite values after processing: **{manifest['nonfinite_after_processing']}**",f"- Duplicate vector rows beyond first: **{manifest['duplicate_vector_rows_beyond_first']}**",'', '## Blocks','']+[f'- `{k}`: {v}' for k,v in sorted(manifest['block_counts'].items())]+['','## Leakage checks','']+[f"- `{k}`: **{v}**" for k,v in manifest['forbidden_feature_checks'].items()]+['','## Removed exact duplicates','']+[f"- `{x['removed']}` = `{x['kept']}`" for x in dups]+['','## Removed within-block |r| >= 0.995','']+[f"- `{x['removed']}` ≈ `{x['kept']}`" for x in corr_removed]+['','## Removed constants','']+[f'- `{x}`' for x in removed_constants]
 REPORT.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps({k:manifest[k] for k in ['records','raw_candidate_features','retained_features','block_counts','nonfinite_after_processing','duplicate_vector_rows_beyond_first','forbidden_feature_checks']},indent=2))
if __name__=='__main__':main()
