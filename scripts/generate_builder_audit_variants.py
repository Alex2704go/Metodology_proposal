#!/usr/bin/env python3
"""Generate deterministic semantic-preserving variants for Builder Admission audits."""
from __future__ import annotations
import gzip,json,random
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/objects_blind_stage02_3000.jsonl.gz';SEED=420042

def reverse_dict_keys(v):
 if isinstance(v,dict):return {k:reverse_dict_keys(v[k]) for k in sorted(v,reverse=True)}
 if isinstance(v,list):return [reverse_dict_keys(x) for x in v]
 return v

def permute_lists(v,rng):
 if isinstance(v,dict):return {k:permute_lists(x,rng) for k,x in v.items()}
 if isinstance(v,list):
  out=[permute_lists(x,rng) for x in v];rng.shuffle(out);return out
 return v

def write_variant(name,transform):
 out=ROOT/'derived'/f'builder_audit_{name}.jsonl.gz';rng=random.Random(SEED)
 with gzip.open(SRC,'rt',encoding='utf-8') as inp,gzip.open(out,'wt',encoding='utf-8',newline='\n') as dst:
  for line in inp:
   row=json.loads(line);row=transform(row,rng)
   dst.write(json.dumps(row,ensure_ascii=False,separators=(',',':'))+'\n')
 return out

def main():
 paths=[]
 paths.append(write_variant('field_permutation',lambda r,rng:{k:r[k] for k in reversed(list(r))}))
 paths.append(write_variant('key_order_permutation',lambda r,rng:reverse_dict_keys(r)))
 paths.append(write_variant('nested_object_permutation',lambda r,rng:permute_lists(r,rng)))
 paths.append(write_variant('serialization_roundtrip',lambda r,rng:json.loads(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')))))
 print('\n'.join(map(str,paths)))
if __name__=='__main__':main()
