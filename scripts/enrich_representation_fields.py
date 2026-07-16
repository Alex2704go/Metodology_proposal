#!/usr/bin/env python3
"""Fetch Stage 02 representation fields for exactly the Stage 00 pilot IDs."""
from __future__ import annotations
import gzip, hashlib, json, os, time, urllib.error, urllib.parse, urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE='https://api.materialsproject.org/materials/summary/'
FIELDS=['material_id','has_props','origins','builder_meta']
BATCH=100

def request(params,key):
    req=urllib.request.Request(BASE+'?'+urllib.parse.urlencode(params),headers={'X-API-KEY':key,'User-Agent':'CEOS-MaterialsWorld/0.42'})
    for n in range(6):
        try:
            with urllib.request.urlopen(req,timeout=90) as r:return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code not in {429,500,502,503,504} or n==5: raise
        except urllib.error.URLError:
            if n==5: raise
        time.sleep(2**n)

def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''):h.update(b)
    return h.hexdigest()

def main():
    key=os.environ.get('MP_API_KEY')
    if not key: raise SystemExit('MP_API_KEY is required and is never persisted')
    mapping=[]
    with gzip.open(ROOT/'raw/object_id_map.jsonl.gz','rt',encoding='utf-8') as f:
        for line in f:mapping.append(json.loads(line))
    ids=[x['material_id'] for x in mapping]
    docs={}; api_version=None
    for i in range(0,len(ids),BATCH):
        batch=ids[i:i+BATCH]
        p=request({'material_ids':','.join(batch),'_limit':BATCH,'_fields':','.join(FIELDS)},key)
        api_version=api_version or p.get('meta',{}).get('api_version')
        docs.update({x['material_id']:x for x in p.get('data',[])})
    missing=sorted(set(ids)-set(docs))
    if missing: raise RuntimeError(f'Missing {len(missing)} requested IDs')

    side=ROOT/'raw/representation_fields_3000.jsonl.gz'
    with gzip.open(side,'wt',encoding='utf-8',newline='\n') as f:
        for mid in ids:f.write(json.dumps(docs[mid],ensure_ascii=False,separators=(',',':'))+'\n')

    source=ROOT/'derived/objects_blind_3000.jsonl.gz'
    output=ROOT/'derived/objects_blind_stage02_3000.jsonl.gz'
    by_object={x['object_id']:x['material_id'] for x in mapping}
    with gzip.open(source,'rt',encoding='utf-8') as inp,gzip.open(output,'wt',encoding='utf-8',newline='\n') as out:
        for line in inp:
            row=json.loads(line); ext=docs[by_object[row['object_id']]]
            for field in FIELDS[1:]: row[field]=ext.get(field)
            out.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')

    manifest=ROOT/'raw/MANIFEST.json'; m=json.loads(manifest.read_text(encoding='utf-8'))
    m.setdefault('stage02_sidecar',{})
    m['stage02_sidecar']={
      'extracted_at':datetime.now(timezone.utc).isoformat(),'api_version':api_version,
      'join_rule':'exact Stage 00 material_id set','requested_fields':FIELDS,
      'credential_persisted':False,
      'files':[
       {'path':str(side.relative_to(ROOT)),'records':len(ids),'sha256':sha(side),'bytes':side.stat().st_size},
       {'path':str(output.relative_to(ROOT)),'records':len(ids),'sha256':sha(output),'bytes':output.stat().st_size}
      ]}
    manifest.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'requested':len(ids),'returned':len(docs),'api_version':api_version,'sidecar':str(side),'blind_stage02':str(output)},indent=2))
if __name__=='__main__':main()
