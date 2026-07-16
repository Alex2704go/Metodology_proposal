#!/usr/bin/env python3
"""Population-level Conflict Topology census and targeted Conflict Nulls."""
from __future__ import annotations
import json
from collections import Counter
from itertools import combinations
from pathlib import Path
import numpy as np
from scipy.stats import fisher_exact
from sklearn.neighbors import NearestNeighbors
ROOT=Path(__file__).resolve().parents[1];TRAIN=ROOT/'derived/world_vectors_v0.2.npz';POOL=ROOT/'derived/stress_pool_frozen_projection.npz';LAB=ROOT/'derived/family_labels_v0.2.npz';SEL=ROOT/'derived/stress_selection_blind.json';SIX=ROOT/'derived/six_material_stress_results.json';OUT=ROOT/'derived/conflict_topology_v0.3.json';MD=ROOT/'reports/conflict_topology_population.md';SEED=420042
CHANNEL_BLOCKS={'composition':['composition_shape'],'structure':['structure_topology','structure_numeric'],'symmetry':['symmetry_record'],'observer':['scalar_observers'],'global':['composition_shape','structure_topology','structure_numeric','symmetry_record']};ORDER=['global','local','composition','structure','symmetry','observer'];SHORT={'global':'G','local':'L','composition':'C','structure':'S','symmetry':'Y','observer':'O'}
def cents(X,labels):return np.vstack([X[labels==f].mean(0) for f in sorted(set(labels))])
def metric(Xtrain,Xquery,labels):
 c=cents(Xtrain,labels);d=np.linalg.norm(Xquery[:,None,:]-c[None,:,:],axis=2);o=np.argsort(d,axis=1);near=d[np.arange(len(d)),o[:,0]];second=d[np.arange(len(d)),o[:,1]];margin=(second-near)/(second+1e-12);base=np.linalg.norm(Xtrain[:,None,:]-c[None,:,:],axis=2).min(1);sb=np.sort(base);pct=100*np.searchsorted(sb,near,side='right')/len(sb)
 return {'vote':o[:,0]+1,'margin':margin,'percentile':pct,'ood':pct>99,'nearest_distance':near}
def local_metric(Xtrain,Xquery,labels,training=False,k=25,baseline_radius=None,tol=1e-12):
 # Canonical tie-complete kNN: include every neighbor at the kth radius.
 from scipy.spatial.distance import cdist
 votes=[];marg=[];radii=[];effective=[]
 indices=np.arange(len(Xtrain))
 for start in range(0,len(Xquery),200):
  D=cdist(Xquery[start:start+200],Xtrain,metric='euclidean')
  for q in range(len(D)):
   absolute=start+q
   if training:D[q,absolute]=np.inf
   order=np.argsort(D[q],kind='stable');kth=float(D[q,order[k-1]])
   row=order[D[q,order] <= kth+tol]
   count=Counter(int(labels[i]) for i in row);maxc=max(count.values());tied={f for f,n in count.items() if n==maxc}
   top=next(int(labels[i]) for i in row if int(labels[i]) in tied)
   second=max([n for f,n in count.items() if f!=top] or [0])
   votes.append(top);marg.append((count[top]-second)/len(row));radii.append(kth);effective.append(len(row))
 radius=np.array(radii)
 base=radius if training else baseline_radius
 if base is None:raise ValueError('baseline_radius required for out-of-sample local metric')
 sb=np.sort(base);pct=100*np.searchsorted(sb,radius,side='right')/len(sb)
 return {'vote':np.array(votes),'margin':np.array(marg,float),'percentile':pct,'ood':pct>99,'nearest_distance':radius,'effective_neighbor_count':np.array(effective),'_baseline_radius':base}
def signature(votes):
 fmap={};groups=[]
 for node in ORDER:
  f=int(votes[node])
  if f not in fmap:fmap[f]=len(groups);groups.append([])
  groups[fmap[f]].append(SHORT[node])
 return '|'.join('{' + ','.join(g) + '}' for g in groups)
def descriptors(votes,oods):
 vals=[int(votes[n]) for n in ORDER];conf=sum(a!=b for a,b in combinations(vals,2))/15;g=int(votes['global']);gld=int(votes['local'])!=g;block_dis=sum(int(votes[n])!=g for n in ['composition','structure','symmetry']);multi=gld and block_dis>=2
 return {'topology_signature':signature(votes),'unique_supported_families':len(set(vals)),'pairwise_conflict_fraction':conf,'global_local_disagreement':gld,'block_disagreement_count':block_dis,'channel_ood_count':sum(bool(oods[n]) for n in ORDER),'multi_axis_conflict':multi}
def make_records(ids,packets):
 out=[]
 for i,oid in enumerate(ids):
  votes={n:int(packets[n]['vote'][i]) for n in ORDER};oods={n:bool(packets[n]['ood'][i]) for n in ORDER};d=descriptors(votes,oods);low=bool(packets['global']['margin'][i]<.05);boundary=bool(low and not oods['global']);out.append({'object_id':str(oid),'low_margin':low,'boundary':boundary,'nodes':{n:{'family':f"F-{votes[n]:03d}",'margin':float(packets[n]['margin'][i]),'support_percentile':float(packets[n]['percentile'][i]),'ood':oods[n]} for n in ORDER},**d})
 return out
def conflict_array(vote_arrays):
 A=np.column_stack([vote_arrays[n] for n in ORDER]);return np.array([sum(row[i]!=row[j] for i,j in combinations(range(6),2))/15 for row in A])
def multi_array(v):
 g=v['global'];return (v['local']!=g)&(((v['composition']!=g).astype(int)+(v['structure']!=g)+(v['symmetry']!=g))>=2)
def main():
 t=np.load(TRAIN,allow_pickle=False);p=np.load(POOL,allow_pickle=False);l=np.load(LAB,allow_pickle=False);X=t['X_scaled'];P=p['X_scaled'];names=t['feature_names'].astype(str);blocks=t['blocks'].astype(str);labels=l['ORGANIZATION'];rng=np.random.default_rng(SEED)
 train_packets={};pool_packets={}
 for ch,bs in CHANNEL_BLOCKS.items():
  mask=np.isin(blocks,bs);train_packets[ch]=metric(X[:,mask],X[:,mask],labels);pool_packets[ch]=metric(X[:,mask],P[:,mask],labels)
 train_packets['global']['vote']=labels.copy() # frozen partition labels
 local_mask=np.isin(blocks,CHANNEL_BLOCKS['global'])
 train_packets['local']=local_metric(X[:,local_mask],X[:,local_mask],labels,training=True)
 pool_packets['local']=local_metric(X[:,local_mask],P[:,local_mask],labels,training=False,baseline_radius=train_packets['local']['_baseline_radius'])
 train_records=make_records(t['object_ids'].astype(str),train_packets);pool_records=make_records(p['object_ids'].astype(str),pool_packets)
 low_margin=np.array([r['low_margin'] for r in train_records]);boundary=np.array([r['boundary'] for r in train_records]);conf=np.array([r['pairwise_conflict_fraction'] for r in train_records]);multi=np.array([r['multi_axis_conflict'] for r in train_records]);gld=np.array([r['global_local_disagreement'] for r in train_records])
 obs_diff=float(conf[boundary].mean()-conf[~boundary].mean());table=np.array([[np.sum(boundary&multi),np.sum(boundary&~multi)],[np.sum(~boundary&multi),np.sum(~boundary&~multi)]]);odds,pval=fisher_exact(table)
 # Packet Alignment Null: preserve each channel packet marginal, destroy object alignment.
 packet_diffs=[];packet_multi_odds=[]
 basevotes={n:train_packets[n]['vote'].copy() for n in ORDER}
 for rep in range(100):
  v={'global':basevotes['global']}
  for n in ORDER[1:]:v[n]=basevotes[n][rng.permutation(len(labels))]
  q=conflict_array(v);mm=multi_array(v);packet_diffs.append(float(q[boundary].mean()-q[~boundary].mean()));tt=np.array([[np.sum(boundary&mm),np.sum(boundary&~mm)],[np.sum(~boundary&mm),np.sum(~boundary&~mm)]]);packet_multi_odds.append(float(fisher_exact(tt)[0]))
 # Representation Block Alignment Null: preserve blocks, destroy their joint alignment and recompute global margins.
 orgmask=np.isin(blocks,CHANNEL_BLOCKS['global']);Xo=X[:,orgmask];bo=blocks[orgmask];co=cents(Xo,labels);base_near=np.linalg.norm(Xo[:,None,:]-co[None,:,:],axis=2).min(1);sorted_base=np.sort(base_near);null_rates=[]
 for rep in range(30):
  Y=Xo.copy()
  for bs in [['composition_shape'],['structure_topology','structure_numeric'],['symmetry_record']]:
   m=np.isin(bo,bs);perm=rng.permutation(len(Y));Y[:,m]=Y[perm][:,m]
  d=np.linalg.norm(Y[:,None,:]-co[None,:,:],axis=2);o=np.sort(d,axis=1);margin=(o[:,1]-o[:,0])/(o[:,1]+1e-12);near=o[:,0];pct=100*np.searchsorted(sorted_base,near,side='right')/len(sorted_base);null_rates.append(float(np.mean((margin<.05)&(pct<=99))))
 sig_b=Counter(r['topology_signature'] for r in train_records if r['boundary']);sig_n=Counter(r['topology_signature'] for r in train_records if not r['boundary'])
 criteria={'conflict_difference_above_packet_null_q95':bool(obs_diff>np.quantile(packet_diffs,.95)),'multi_axis_odds_ratio_gt_2':bool(odds>2),'fisher_p_lt_0.01':bool(pval<.01)};candidate=all(criteria.values())
 selected_ids={x['object_id'] for x in json.loads(SEL.read_text())['selected']};selected=[r for r in pool_records if r['object_id'] in selected_ids];form={x['object_id']:x['formula'] for x in json.loads(SIX.read_text())['stress_examples']}
 for r in selected:r['formula']=form[r['object_id']]
 summary={'training_objects':len(train_records),'low_margin_count':int(low_margin.sum()),'low_margin_global_ood_count':int(np.sum(low_margin & np.array([r['nodes']['global']['ood'] for r in train_records]))),'boundary_count':int(boundary.sum()),'boundary_rate':float(boundary.mean()),'mean_conflict_boundary':float(conf[boundary].mean()),'mean_conflict_nonboundary':float(conf[~boundary].mean()),'observed_conflict_difference':obs_diff,'packet_null_conflict_difference_q95':float(np.quantile(packet_diffs,.95)),'multi_axis_table':table.tolist(),'multi_axis_odds_ratio':float(odds),'multi_axis_fisher_p':float(pval),'relational_boundary_count':int(np.sum(boundary&multi)),'relational_boundary_fraction_of_boundaries':float(np.mean(multi[boundary])),'global_local_disagreement_boundary_rate':float(np.mean(gld[boundary])),'global_local_disagreement_nonboundary_rate':float(np.mean(gld[~boundary])),'representation_block_null_boundary_rate':{'observed':float(boundary.mean()),'null_mean':float(np.mean(null_rates)),'null_q05':float(np.quantile(null_rates,.05)),'null_q95':float(np.quantile(null_rates,.95))},'candidate_admission_criteria':criteria,'relational_boundary_population_supported':candidate,'top_boundary_signatures':sig_b.most_common(10),'top_nonboundary_signatures':sig_n.most_common(10)}
 report={'protocol':'conflict_topology_v0.3','summary':summary,'selected_stress_topologies':selected,'training_records':train_records,'pool_records':pool_records}
 OUT.write_text(json.dumps(report,ensure_ascii=False,separators=(',',':'))+'\n')
 lines=['# Conflict Topology — Population Test','','## Operational definition','','```text','RELATIONAL_BOUNDARY =','    Builder valid','    AND exact frozen replay','    AND global representation in-support','    AND global margin < 0.05','    AND Global family ≠ Local family','    AND at least two of {Composition, Structure, Symmetry}','        support a family different from Global','```','','Channel-specific OOD remains a recorded node attribute; only global OOD changes the Assignment State from BOUNDARY to OOD.','','## Meaning of Population Support PASS','','PASS means that this organizational relation pattern is supported in the analyzed sample under the registered methodology and exceeds its targeted Conflict Null criteria. It is not evidence for a physical mechanism, thermodynamic phase boundary, or classical material category.','','```text','No physical phase-boundary or mechanism claim is made.','```','','## Population result','',f"- Training objects: **{len(train_records)}**",f"- Global low-margin objects: **{low_margin.sum()}**",f"- Low-margin objects with global OOD state: **{np.sum(low_margin & np.array([r['nodes']['global']['ood'] for r in train_records]))}**",f"- Admission-State BOUNDARY objects: **{boundary.sum()}** ({boundary.mean()*100:.2f}%)",f"- Mean pairwise conflict, Boundary: **{conf[boundary].mean():.3f}**",f"- Mean pairwise conflict, non-Boundary: **{conf[~boundary].mean():.3f}**",f"- Observed difference: **{obs_diff:.3f}**",f"- Packet-Alignment Null q95: **{np.quantile(packet_diffs,.95):.3f}**",f"- Multi-axis conflict odds ratio: **{odds:.2f}**",f"- Fisher exact p: **{pval:.3g}**",f"- Relational Boundaries: **{np.sum(boundary&multi)} / {boundary.sum()}**",f"- Population support criterion: **{'PASS' if candidate else 'FAIL'}**",'','## Representation Block Alignment Null','', '| Statistic | Value |','|---|---:|',f"| Observed Boundary rate | {boundary.mean():.4f} |",f"| Conflict Null mean | {np.mean(null_rates):.4f} |",f"| Conflict Null q05–q95 | {np.quantile(null_rates,.05):.4f}–{np.quantile(null_rates,.95):.4f} |",'','## Selected stress topologies','']
 for r in selected:
  lines += [f"### {r['formula']}",'',f"- Signature: `{r['topology_signature']}`",f"- Boundary: **{r['boundary']}**",f"- Pairwise conflict fraction: **{r['pairwise_conflict_fraction']:.3f}**",f"- Global/local disagreement: **{r['global_local_disagreement']}**",f"- Multi-axis conflict: **{r['multi_axis_conflict']}**",'', '| Node | Family | Margin | Percentile | OOD |','|---|---|---:|---:|---|']
  for n in ORDER:
   q=r['nodes'][n];lines.append(f"| {n} | {q['family']} | {q['margin']:.3f} | {q['support_percentile']:.1f}% | {'YES' if q['ood'] else 'no'} |")
 lines += ['','## Admission reading','','A PASS supports `RELATIONAL_BOUNDARY` as a population-level candidate organizational subtype. It does not convert Boundary into a physical phase category. A FAIL means the LiMnVF₆ motif remains an individual anatomy rather than a supported class.']
 MD.write_text('\n'.join(lines)+'\n')
 print(json.dumps(summary,indent=2))
if __name__=='__main__':main()
