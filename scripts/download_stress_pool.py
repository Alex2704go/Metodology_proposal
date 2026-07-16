#!/usr/bin/env python3
"""Download a preregistered out-of-sample stress pool without persisting credentials."""
from __future__ import annotations
import gzip,hashlib,json,os,time,urllib.error,urllib.parse,urllib.request
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];BASE='https://api.materialsproject.org/materials/summary/'
FIELDS=['material_id','formula_pretty','nelements','elements','composition','structure','symmetry','band_gap','formation_energy_per_atom','is_magnetic','ordering','density','volume','has_props','origins','builder_meta']
def req(params,key):
 r=urllib.request.Request(BASE+'?'+urllib.parse.urlencode(params),headers={'X-API-KEY':key,'User-Agent':'CEOS-MaterialsWorld/0.42'})
 for n in range(6):
  try:
   with urllib.request.urlopen(r,timeout=120) as x:return json.load(x)
  except urllib.error.HTTPError as e:
   if e.code not in {429,500,502,503,504} or n==5:raise
  time.sleep(2**n)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
 key=os.environ.get('MP_API_KEY')
 if not key:raise SystemExit('MP_API_KEY required and never persisted')
 excluded=set()
 with gzip.open(ROOT/'raw/object_id_map.jsonl.gz','rt') as f:
  for line in f:excluded.add(json.loads(line)['material_id'])
 prev=json.loads((ROOT/'derived/real_examples_representation_cards.json').read_text())['cards'];excluded.update(x['material_id'] for x in prev)
 p=req({'_skip':100000,'_limit':1000,'_sort_fields':'material_id','_fields':','.join(FIELDS)},key)
 rawdocs=p.get('data',[]);docs=[x for x in rawdocs if x['material_id'] not in excluded]
 raw=ROOT/'raw/stress_pool_window_100000.jsonl.gz';blind=ROOT/'derived/stress_pool_blind.jsonl.gz';mapping=ROOT/'raw/stress_pool_map.jsonl.gz'
 with gzip.open(raw,'wt',encoding='utf-8',newline='\n') as a,gzip.open(blind,'wt',encoding='utf-8',newline='\n') as b,gzip.open(mapping,'wt',encoding='utf-8',newline='\n') as c:
  for i,d in enumerate(docs,1):
   a.write(json.dumps(d,ensure_ascii=False,separators=(',',':'))+'\n');oid=f'Stress Object {i:04d}'
   c.write(json.dumps({'object_id':oid,'material_id':d['material_id'],'formula_pretty':d.get('formula_pretty')},ensure_ascii=False,separators=(',',':'))+'\n')
   clean={k:v for k,v in d.items() if k not in {'material_id','formula_pretty'}};clean={'object_id':oid,**clean,'_ceos_stratum':'STRESS_POOL'}
   b.write(json.dumps(clean,ensure_ascii=False,separators=(',',':'))+'\n')
 man={'created_at':datetime.now(timezone.utc).isoformat(),'api_version':p.get('meta',{}).get('api_version'),'query':{'skip':100000,'limit':1000,'sort':'material_id'},'returned_before_exclusion':len(rawdocs),'retained_after_exclusion':len(docs),'excluded_known_ids':len(rawdocs)-len(docs),'credential_persisted':False,'files':[{'path':str(x.relative_to(ROOT)),'sha256':sha(x),'bytes':x.stat().st_size} for x in [raw,blind,mapping]]}
 (ROOT/'raw/STRESS_POOL_MANIFEST.json').write_text(json.dumps(man,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(man,indent=2))
if __name__=='__main__':main()
