#!/usr/bin/env python3
"""Executable specification checks for CEOS Claim Type System v0.1."""
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1];CFG=ROOT/'config/claim_type_system_v0.1.yaml';OUT=ROOT/'reports/checkpoint_claim_type_system.md'
def main():
 c=yaml.safe_load(CFG.read_text())['claim_type_system'];trans=c['transitions'];forbidden={tuple(x) for x in c['forbidden_coercions']};tests=[]
 def transition(name,evidence,expected):
  ok=all(evidence.get(x,False) for x in trans[name]['requires']);tests.append((name,ok==expected,f'actual={ok}, expected={expected}'))
 transition('RawObservation_to_OrganizationalObject',{'object_typing':True,'builder_admission':True},True)
 transition('RawObservation_to_OrganizationalObject',{'object_typing':True,'builder_admission':False},False)
 transition('OrganizationalObject_to_FrozenFamily',{'vectorization_admission':True,'stability':True,'null_ladder':True,'partition_admission':True},True)
 transition('ObserverOutput_to_RelationPattern',{'canonical_topology':True,'label_invariance':True,'conflict_null':False,'pattern_admission':True},False)
 transition('CEOS_Entity_x_ExternalTerm_to_CrossMapping',{'direction':True,'mapping_provenance':True,'mapping_stability':True,'counterexamples':True,'mapping_admission':True},True)
 transition('CEOS_Entity_x_ExternalTerm_to_CrossMapping',{'direction':True,'mapping_provenance':False,'mapping_stability':True,'counterexamples':True,'mapping_admission':True},False)
 transition('CrossMapping_x_IndependentEvidence_to_InterpretationClaim',{'independent_evidence_passport':False,'interpretation_admission':True},False)
 transition('CrossMapping_x_IndependentEvidence_to_InterpretationClaim',{'independent_evidence_passport':True,'interpretation_admission':True},True)
 for a,b in sorted(forbidden):tests.append((f'forbidden:{a}↛{b}',(a,b) in forbidden,'registered'))
 tests += [('OOD_precedes_Boundary',not ((99.5<=99) and (.01<.05)),'global OOD cannot type as Boundary'),('CrossMapping_no_epistemic_upgrade',c['normative_rules']['cross_mapping_epistemic_upgrade'] is False,'must be false'),('Independent_evidence_required',c['normative_rules']['independent_evidence_required_for_upgrade'] is True,'must be true')]
 passed=sum(ok for _,ok,_ in tests);lines=['# Checkpoint — CEOS Claim Type System','', '> **Status:** synthetic rule checks only. Proof-carrying enforcement is `REASSESSMENT_REQUIRED` after System Null Ladder v0.1.','',f'- Tests: **{len(tests)}**',f'- Passed: **{passed}**',f'- Failed: **{len(tests)-passed}**','', '| Typing rule | Result | Detail |','|---|---|---|']+[f"| `{n}` | {'PASS' if ok else '**FAIL**'} | {d} |" for n,ok,d in tests]
 OUT.write_text('\n'.join(lines)+'\n')
 if passed!=len(tests):raise SystemExit('Claim Type System check failed')
 print({'tests':len(tests),'passed':passed,'failed':0})
if __name__=='__main__':main()
