#!/usr/bin/env python3
"""Build out-of-sample CEOS Representation Cards for deterministically selected formulas."""
from __future__ import annotations
import gzip,hashlib,json,os,time,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BASE='https://api.materialsproject.org/materials/summary/'
SELECTION=[('FeS','mp-aaaaadct'),('NaCl','mp-aaaabhux'),('SiO2','mp-aaaaakgg'),('SrTiO3','mp-aaaaagwx')]
FIELDS=['material_id','formula_pretty','nelements','elements','composition','structure','symmetry','band_gap','formation_energy_per_atom','is_magnetic','ordering','density','volume','has_props','origins','builder_meta']

def request(params,key):
 req=urllib.request.Request(BASE+'?'+urllib.parse.urlencode(params),headers={'X-API-KEY':key,'User-Agent':'CEOS-MaterialsWorld/0.42'})
 for n in range(6):
  try:
   with urllib.request.urlopen(req,timeout=90) as r:return json.load(r)
  except urllib.error.HTTPError as e:
   if e.code not in {429,500,502,503,504} or n==5:raise
  time.sleep(2**n)
def topology(v):
 if isinstance(v,dict):children=list(v.values());o=1;l=0
 elif isinstance(v,list):children=v;o=0;l=1
 else:return (0,1,0,0)
 z=[topology(x) for x in children]
 return (1+max((x[0] for x in z),default=0),sum(x[1] for x in z),o+sum(x[2] for x in z),l+sum(x[3] for x in z))
def short_hash(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()[:10]
def main():
 key=os.environ.get('MP_API_KEY')
 if not key:raise SystemExit('MP_API_KEY required; never persisted')
 ids=[x[1] for x in SELECTION]
 p=request({'material_ids':','.join(ids),'_limit':10,'_fields':','.join(FIELDS)},key)
 docs={x['material_id']:x for x in p['data']}
 if set(ids)!=set(docs):raise RuntimeError('Selected ID set not returned exactly')
 raw=ROOT/'raw/real_examples_4.jsonl.gz'
 with gzip.open(raw,'wt',encoding='utf-8',newline='\n') as f:
  for formula,mid in SELECTION:f.write(json.dumps(docs[mid],ensure_ascii=False,separators=(',',':'))+'\n')
 cards=[]
 for requested,mid in SELECTION:
  d=docs[mid];depth,leaves,onodes,lnodes=topology(d['structure'])
  hp=d.get('has_props') or {}; active=sorted(k for k,v in hp.items() if v)
  sym=d.get('symmetry') or {};orig=d.get('origins') or [];bm=d.get('builder_meta') or {}
  card={
   'requested_formula':requested,'source_formula':d.get('formula_pretty'),'material_id':mid,
   'selection_rule':'lexicographically minimum material_id among exact-formula matches',
   'representations':{
    'composition':{'class':'MAP','builder':'MapBuilder','key_count':len(d.get('composition') or {}),'value_total':sum((d.get('composition') or {}).values())},
    'structure':{'class':'COMPOSITE','builder':'CompositeBuilder','depth':depth,'leaves':leaves,'object_nodes':onodes,'list_nodes':lnodes},
    'symmetry':{'class':'RECORD','builder':'RecordBuilder','slot_count':len(sym),'populated_slots':sum(v is not None for v in sym.values()),'record_fingerprint':short_hash(sym),'cross_mapping':{'crystal_system':sym.get('crystal_system'),'number':sym.get('number')}},
    'has_props':{'class':'RECORD+MAP_VIEW','builders':['RecordBuilder','MapViewBuilder'],'slot_count':len(hp),'active_count':len(active),'active_keys':active,'pattern_fingerprint':short_hash(hp)},
    'origins':{'class':'LIST_OF_OBJECTS','builders':['ListBuilder','RecordElementBuilder'],'length':len(orig),'element_keyset_variants':len({tuple(sorted(x)) for x in orig if isinstance(x,dict)})},
    'builder_meta':{'class':'RECORD+MAP_VIEW','slot_count':len(bm),'populated_slots':sum(v is not None for v in bm.values())}
   }
  }
  r=card['representations'];card['representation_signature']=f"MAP{r['composition']['key_count']}|COMP(d{depth},l{leaves},o{onodes},a{lnodes})|SYM-{r['symmetry']['record_fingerprint']}|CAP{r['has_props']['active_count']}-{r['has_props']['pattern_fingerprint']}|ORG{r['origins']['length']}"
  cards.append(card)
 out=ROOT/'derived/real_examples_representation_cards.json';out.write_text(json.dumps({'created_at':datetime.now(timezone.utc).isoformat(),'api_version':p.get('meta',{}).get('api_version'),'classification_level':'Representation Classification; CEOS Family not assigned','cards':cards},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 md=ROOT/'reports/real_examples_representation_cards.md'
 lines=['# Real-material CEOS Representation Cards','','**Уровень:** Representation Classification. Это ещё не CEOS Family clustering.','',f"Правило выбора записи: минимальный `material_id` среди точных совпадений формулы. Оно зафиксировано до просмотра содержимого.",'']
 for c in cards:
  r=c['representations'];lines += [f"## {c['requested_formula']} — `{c['material_id']}`",'',f"- Source formula: `{c['source_formula']}`",f"- **composition:** MAP, keys={r['composition']['key_count']}, value total={r['composition']['value_total']}",f"- **structure:** COMPOSITE, depth={r['structure']['depth']}, leaves={r['structure']['leaves']}, object nodes={r['structure']['object_nodes']}, list nodes={r['structure']['list_nodes']}",f"- **symmetry:** RECORD, slots={r['symmetry']['slot_count']}, cross-map={r['symmetry']['cross_mapping']['crystal_system']} / #{r['symmetry']['cross_mapping']['number']}",f"- **has_props:** RECORD + MAP VIEW, active={r['has_props']['active_count']}/{r['has_props']['slot_count']}",f"- Active representation capabilities: `{', '.join(r['has_props']['active_keys'])}`",f"- **origins:** LIST[RECORD], length={r['origins']['length']}",f"- **signature:** `{c['representation_signature']}`",'']
 lines += ['## Что здесь классифицировано','','Карточка классифицирует организацию представлений конкретной записи и строит наблюдаемую сигнатуру. Она ещё не утверждает, что материалы образуют разные CEOS Families. Для этого нужны population-level vectorization, scaling, Null Ladder и устойчивое family discovery.']
 md.write_text('\n'.join(lines)+'\n',encoding='utf-8')
 print(json.dumps([{'formula':c['requested_formula'],'id':c['material_id'],'signature':c['representation_signature']} for c in cards],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
