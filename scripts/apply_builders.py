#!/usr/bin/env python3
"""Apply generic Builder contracts selected by Stage 02A dispatch."""
from __future__ import annotations
import gzip,json,math,statistics
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'derived/objects_blind_stage02_3000.jsonl.gz'
PROFILES=ROOT/'reports/stage02a_representation_profiles.json'
OUT=ROOT/'derived/stage02a_builder_outputs.json'
MD=ROOT/'reports/stage02a_builder_outputs.md'

def typ(v):
 if v is None:return 'NONE'
 if isinstance(v,bool):return 'BOOLEAN'
 if isinstance(v,(int,float)) and not isinstance(v,bool):return 'NUMBER'
 if isinstance(v,str):return 'STRING'
 if isinstance(v,list):return 'LIST'
 if isinstance(v,dict):return 'OBJECT'
 return type(v).__name__.upper()
def q(xs):
 if not xs:return None
 s=sorted(xs);n=len(s)
 return {'min':s[0],'q25':s[round((n-1)*.25)],'median':s[round((n-1)*.5)],'q75':s[round((n-1)*.75)],'max':s[-1]}
def scalar(vs):
 present=[v for v in vs if v is not None];c=Counter(typ(v) for v in present)
 out={'state_counts':{'NONE':len(vs)-len(present),'PRESENT':len(present)},'runtime_types':dict(c),'distinct':len({json.dumps(v,sort_keys=True) for v in present})}
 nums=[float(v) for v in present if typ(v)=='NUMBER' and math.isfinite(float(v))]
 if nums:out['numeric_distribution']=q(nums)
 if present and all(typ(v) in {'STRING','BOOLEAN'} for v in present):out['category_cardinality']=len(set(present))
 return out
def list_builder(vs):
 lists=[v for v in vs if isinstance(v,list)]
 return {'state_counts':{'NONE':sum(v is None for v in vs),'EMPTY_LIST':sum(v==[] for v in vs),'PRESENT_NONEMPTY':sum(isinstance(v,list) and bool(v) for v in vs)},'length_distribution':q([len(v) for v in lists]),'element_runtime_types':dict(Counter(typ(x) for v in lists for x in v))}
def record(vs):
 objs=[v for v in vs if isinstance(v,dict)];keys=sorted(set().union(*(v for v in objs))) if objs else []
 slots={}
 for k in keys:
  vals=[v.get(k) for v in objs]
  slots[k]={'present':sum(k in v for v in objs),'none':sum(x is None for x in vals),'types':dict(Counter(typ(x) for x in vals if x is not None)),'distinct':len({json.dumps(x,sort_keys=True) for x in vals if x is not None})}
 return {'records':len(objs),'slot_count':len(keys),'keyset_variants':len({tuple(sorted(v)) for v in objs}),'slots':slots}
def map_builder(vs):
 objs=[v for v in vs if isinstance(v,dict)];keys=sorted(set().union(*(v for v in objs))) if objs else []
 supports=Counter(k for v in objs for k in v)
 sizes=[len(v) for v in objs]
 vals=[x for v in objs for x in v.values()]
 return {'maps':len(objs),'key_domain_size':len(keys),'map_size_distribution':q(sizes),'value_runtime_types':dict(Counter(typ(x) for x in vals)),'key_support_distribution':q(list(supports.values()))}
def map_view(vs):
 objs=[v for v in vs if isinstance(v,dict)];vals=[x for v in objs for x in v.values()]
 out=map_builder(vs)
 if vals and all(isinstance(x,bool) for x in vals):
  active=[sum(bool(x) for x in v.values()) for v in objs]
  rates={k:sum(v.get(k) is True for v in objs)/len(objs) for k in sorted(set().union(*(v for v in objs)))}
  out['boolean_active_count_distribution']=q(active);out['boolean_key_rate_distribution']=q(list(rates.values()))
  out['boolean_key_rates']=rates
 return out
def record_elements(vs):
 elems=[x for v in vs if isinstance(v,list) for x in v if isinstance(x,dict)]
 return record(elems)
def tree_metrics(v):
 if isinstance(v,dict):
  children=list(v.values());o=1;l=0
 elif isinstance(v,list):children=v;o=0;l=1
 else:return (0,1,0,0)
 zs=[tree_metrics(x) for x in children]
 return (1+max((z[0] for z in zs),default=0),sum(z[1] for z in zs),o+sum(z[2] for z in zs),l+sum(z[3] for z in zs))
def composite(vs):
 ms=[tree_metrics(v) for v in vs if isinstance(v,(dict,list))]
 return {'objects':len(ms),'depth_distribution':q([x[0] for x in ms]),'leaf_distribution':q([x[1] for x in ms]),'object_node_distribution':q([x[2] for x in ms]),'list_node_distribution':q([x[3] for x in ms])}
BUILD={'ScalarBuilder':scalar,'ListBuilder':list_builder,'MapBuilder':map_builder,'RecordBuilder':record,'MapViewBuilder':map_view,'RecordElementBuilder':record_elements,'CompositeBuilder':composite,'TreeBuilder':composite}
def main():
 rows=[]
 with gzip.open(DATA,'rt',encoding='utf-8') as f:
  for line in f:rows.append(json.loads(line))
 profiles=json.loads(PROFILES.read_text())['profiles'];outputs=[]
 for p in profiles:
  vals=[r.get(p['field']) for r in rows];bo={}
  for b in p['builder_dispatch']:bo[b]=BUILD[b](vals)
  outputs.append({'representation_id':p['representation_id'],'field':p['field'],'derived_class':p['derived_class'],'builders':bo})
 report={'stage':'02A','status':'builder outputs; no domain interpretation','records':len(rows),'outputs':outputs}
 OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 lines=['# Stage 02A — Builder Outputs','','Generic Builders применены после field-name-independent dispatch.','','| ID | Поле | Класс | Builder | Основной выход |','|---|---|---|---|---|']
 for x in outputs:
  for b,o in x['builders'].items():
   if b=='ScalarBuilder':s=f"distinct={o['distinct']}"
   elif b=='ListBuilder':s=f"length={o['length_distribution']}"
   elif b in {'RecordBuilder','RecordElementBuilder'}:s=f"slots={o['slot_count']}; keysets={o['keyset_variants']}"
   elif b in {'MapBuilder','MapViewBuilder'}:s=f"key_domain={o['key_domain_size']}; size={o['map_size_distribution']}"
   else:s=f"depth={o['depth_distribution']}; leaves={o['leaf_distribution']}"
   lines.append(f"| {x['representation_id']} | `{x['field']}` | {x['derived_class']} | {b} | `{s}` |")
 lines += ['','## Граница интерпретации','','Выходы описывают организацию представления. Никакие семейства материалов, механизмы или опубликованные классы не назначались. Полные slot-level и key-level результаты находятся в `derived/stage02a_builder_outputs.json`.']
 MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps({'representations':len(outputs),'builder_runs':sum(len(x['builders']) for x in outputs),'output':str(OUT)},indent=2))
if __name__=='__main__':main()
