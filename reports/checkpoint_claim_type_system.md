# Checkpoint — CEOS Claim Type System

> **Status:** synthetic rule checks only. Proof-carrying enforcement is `REASSESSMENT_REQUIRED` after System Null Ladder v0.1.

- Tests: **17**
- Passed: **17**
- Failed: **0**

| Typing rule | Result | Detail |
|---|---|---|
| `RawObservation_to_OrganizationalObject` | PASS | actual=True, expected=True |
| `RawObservation_to_OrganizationalObject` | PASS | actual=False, expected=False |
| `OrganizationalObject_to_FrozenFamily` | PASS | actual=True, expected=True |
| `ObserverOutput_to_RelationPattern` | PASS | actual=False, expected=False |
| `CEOS_Entity_x_ExternalTerm_to_CrossMapping` | PASS | actual=True, expected=True |
| `CEOS_Entity_x_ExternalTerm_to_CrossMapping` | PASS | actual=False, expected=False |
| `CrossMapping_x_IndependentEvidence_to_InterpretationClaim` | PASS | actual=False, expected=False |
| `CrossMapping_x_IndependentEvidence_to_InterpretationClaim` | PASS | actual=True, expected=True |
| `forbidden:CrossMapping↛IndependentEvidence` | PASS | registered |
| `forbidden:ExternalTerm↛OrganizationalObject` | PASS | registered |
| `forbidden:FamilyLabel↛PhysicalMechanism` | PASS | registered |
| `forbidden:NearestAssignment↛AdmissibleAssignment` | PASS | registered |
| `forbidden:RelationPattern↛AdmissionState` | PASS | registered |
| `forbidden:VocabularyName↛PredictionOfUntestedProperties` | PASS | registered |
| `OOD_precedes_Boundary` | PASS | global OOD cannot type as Boundary |
| `CrossMapping_no_epistemic_upgrade` | PASS | must be false |
| `Independent_evidence_required` | PASS | must be true |

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the explicit execution, replay, invariance, integrity, or contract checks reported in this document under the registered software and data versions.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- a substantive material family, organizational mechanism, or scientific interpretation merely because a technical check passes.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
