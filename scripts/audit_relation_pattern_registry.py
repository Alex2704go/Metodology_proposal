#!/usr/bin/env python3
"""Integrity audit for stable Relation Pattern registry."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT/'derived/relation_pattern_registry_v0.1.json';OUT=ROOT/'reports/checkpoint_relation_pattern_registry.md'
def main():
 x=json.loads(SRC.read_text());e=x['entries'];checks=[('registry','population_sum',sum(q['population_count'] for q in e)==3000),('registry','pattern_count',len(e)==x['pattern_count']),('registry','ids_unique',len({q['relation_pattern_id'] for q in e})==len(e)),('registry','signatures_unique',len({q['canonical_signature'] for q in e})==len(e))]
 for q in e:
  expected='RP-'+hashlib.sha256(q['canonical_signature'].encode()).hexdigest()[:10].upper();checks += [(q['relation_pattern_id'],'content_id_exact',q['relation_pattern_id']==expected),(q['relation_pattern_id'],'interpretation_support',bool(q['interpretation_boundary']['supports'])),(q['relation_pattern_id'],'interpretation_prohibitions',bool(q['interpretation_boundary']['does_not_support']))]
 passed=sum(c for _,_,c in checks);lines=['# Checkpoint — Relation Pattern Registry','',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','',f'- Patterns: **{len(e)}**',f"- Population: **{sum(q['population_count'] for q in e)}**",'- Content IDs: SHA256-derived.','- Literature mapping: LOCKED.']
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(checks):raise SystemExit('Registry audit failed')
 print({'checks':len(checks),'passed':passed,'patterns':len(e),'population':3000})
if __name__=='__main__':main()
