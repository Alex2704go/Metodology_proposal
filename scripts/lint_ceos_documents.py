#!/usr/bin/env python3
"""Fail closed when a CEOS Markdown document lacks an Interpretation Boundary."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];MARK='<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->';OUT=ROOT/'reports/checkpoint_document_contract.md'
def docs():return sorted(list(ROOT.glob('*.md'))+list((ROOT/'reports').glob('*.md')))
def main():
 checks=[]
 for p in docs():
  s=p.read_text(encoding='utf-8');count=s.count(MARK);tail=s.split(MARK,1)[1] if count==1 else ''
  checks += [(str(p.relative_to(ROOT)),'one_boundary_marker',count==1),(str(p.relative_to(ROOT)),'supports_section','### Supports' in tail and len(tail.split('### Supports',1)[1].split('### Does not support',1)[0].strip())>2),(str(p.relative_to(ROOT)),'does_not_support_section','### Does not support' in tail and len(tail.split('### Does not support',1)[1].strip())>2),(str(p.relative_to(ROOT)),'untested_property_prediction_prohibited','prediction of untested properties' in tail),(str(p.relative_to(ROOT)),'cross_mapping_asymmetry','Vocabulary correspondence ≠ evidence inheritance.' in tail)]
 passed=sum(ok for _,_,ok in checks);lines=['# Checkpoint — CEOS Document Contract','', '> **Status:** structural lint only. Semantic enforcement is `REASSESSMENT_REQUIRED` after System Null Ladder v0.1 accepted a contradictory boundary.','',f'- Documents: **{len(docs())}**',f'- Checks: **{len(checks)}**',f'- Passed: **{passed}**',f'- Failed: **{len(checks)-passed}**','', '| Document | Contract | Result |','|---|---|---|']+[f"| `{p}` | `{c}` | {'PASS' if ok else '**FAIL**'} |" for p,c,ok in checks]
 # OUT itself is in scope. Write its boundary directly so the next run is self-consistent.
 boundary='''\n\n<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->\n## Interpretation Boundary — Document Scope\n\n### Supports\n\n- the document-contract lint result for the registered Markdown corpus.\n\n### Does not support\n\n- physical mechanism;\n- thermodynamic phase;\n- microscopic Hamiltonian;\n- causal explanation;\n- prediction of untested properties;\n- transfer of evidence through vocabulary mapping;\n- universal validity outside the registered scope.\n\n### Cross Mapping Asymmetry\n\n> **Vocabulary correspondence ≠ evidence inheritance.**\n'''
 OUT.write_text('\n'.join(lines)+boundary,encoding='utf-8')
 if passed!=len(checks):raise SystemExit('CEOS document contract failed')
 print({'documents':len(docs()),'checks':len(checks),'passed':passed,'failed':0})
if __name__=='__main__':main()
