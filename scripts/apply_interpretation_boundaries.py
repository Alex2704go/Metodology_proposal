#!/usr/bin/env python3
"""Idempotently attach the mandatory CEOS Interpretation Boundary to Markdown documents."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MARK='<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->'
def docs():return sorted(list(ROOT.glob('*.md'))+list((ROOT/'reports').glob('*.md')))
def category(p):
 n=p.name.lower()
 if p.parent==ROOT or n in {'decision_log.md'}:return 'governance'
 if n.startswith('checkpoint_') or n.startswith('builder_audit_') or n=='builder_admission.md':return 'technical'
 if 'inventory' in n:return 'inventory'
 if 'representation' in n or 'stage02' in n:return 'representation'
 if any(x in n for x in ['assignment','real_examples','six_material']):return 'assignment'
 if any(x in n for x in ['family','conflict','relation_pattern','biograph','stage04']):return 'organizational'
 return 'organizational'
def support(c):
 return {
  'governance':'the protocol, vocabulary, decision history, or document-governance contract explicitly stated here; empirical claims only through separately admitted linked artifacts',
  'technical':'the explicit execution, replay, invariance, integrity, or contract checks reported in this document under the registered software and data versions',
  'inventory':'descriptive schema, type, missingness, range, duplication, and provenance claims for the registered dataset',
  'representation':'representation-object, Builder, organizational-observable, and schema claims under the registered representation protocol',
  'assignment':'the object-specific nearest-family geometry, evidence passport, Admission State, or Relation Pattern claims explicitly reported under the frozen context',
  'organizational':'the neutral organizational partition, Relation Pattern, Null comparison, or population-support claim explicitly reported for the analyzed sample and registered methodology',
 }[c]
def block(c):
 extra={
  'governance':'empirical validation merely because a rule is documented',
  'technical':'a substantive material family, organizational mechanism, or scientific interpretation merely because a technical check passes',
  'inventory':'material-family membership or mechanism inferred from inventory statistics',
  'representation':'physical identity or mechanism inferred from representation shape alone',
  'assignment':'membership when admission is withheld, or generalization from one object to a population',
  'organizational':'identity with a classical physical category without separately admitted post hoc Cross Mapping',
 }[c]
 return f'''\n\n{MARK}\n## Interpretation Boundary — Document Scope\n\n### Supports\n\n- {support(c)}.\n\n### Does not support\n\n- physical mechanism;\n- thermodynamic phase;\n- microscopic Hamiltonian;\n- causal explanation;\n- prediction of untested properties;\n- transfer of evidence through vocabulary or Cross Mapping;\n- universal validity outside the registered WORLD, sample, protocol, and version;\n- {extra}.\n\n### Cross Mapping Asymmetry\n\n> **Vocabulary correspondence ≠ evidence inheritance.**\n'''
def main():
 changed=0
 for p in docs():
  s=p.read_text(encoding='utf-8')
  prefix=s.split(MARK,1)[0].rstrip() if MARK in s else s.rstrip()
  updated=prefix+block(category(p))
  if updated!=s:
   p.write_text(updated,encoding='utf-8');changed+=1
 print({'documents':len(docs()),'boundaries_added':changed})
if __name__=='__main__':main()
