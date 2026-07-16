# System Null Ladder v0.2 — Regression

The same 16 conceptual attacks from v0.1 were applied to the proof-carrying governance v0.2 candidate.

- Controls: **2/2**
- Invalid attacks rejected: **16/16**
- Remaining registered gaps: **0**
- Candidate governance status: **QUALIFIED**

| Attack | Outcome | Diagnostic | Primary rejection reason |
|---|---|---|---|
| `ADMITTED_WITHOUT_QUALIFICATION` | **REJECTED** | `GOV-STATE-001` | state mismatch:NOT_TESTED |
| `GHOST_EVIDENCE` | **REJECTED** | `GOV-EVID-002` | evidence strength mismatch:NONE |
| `GHOST_PROVENANCE` | **REJECTED** | `GOV-PROV-001` | missing provenance refs |
| `DIRECTION_SEMANTIC_NOOP` | **REJECTED** | `GOV-DIR-001` | direction/origin mismatch |
| `NOT_TESTED_PLUS_PASS` | **REJECTED** | `GOV-MAT-001` | latest outcome mismatch:NOT_RUN |
| `ADMITTED_PLUS_FAILED` | **REJECTED** | `GOV-STATE-002` | ADMITTED with non-PASS latest qualification |
| `CONTRADICTORY_INTERPRETATION_BOUNDARY` | **REJECTED** | `GOV-BOUND-001` | interpretation boundary contradiction |
| `EVIDENCE_INHERITANCE_SMUGGLING` | **REJECTED** | `GOV-BOUND-001` | interpretation boundary contradiction |
| `UNSEARCHED_COUNTEREXAMPLES` | **REJECTED** | `GOV-COUNTER-001` | admission without current-world counterexample search |
| `HISTORYLESS_INDEPENDENT_REPLICATION` | **REJECTED** | `GOV-MAT-001` | maturity mismatch:NOT_TESTED |
| `INDEPENDENCE_WITHOUT_IDENTITIES` | **REJECTED** | `GOV-IND-001` | multi-world without independent WORLD identities |
| `NON_MARKDOWN_CLAIM_ESCAPE` | **REJECTED** | `GOV-ART-001` | unregistered artifact:derived/evil_claim.json |
| `SEMANTIC_MARKDOWN_CONTRADICTION` | **REJECTED** | `GOV-BOUND-001` | document semantic contradiction:ART-REPORT |
| `CYCLIC_CLAIM_GRAPH` | **REJECTED** | `GOV-GRAPH-001` | claim cycle:CL-BASE |
| `SELF_ASSERTED_TRANSITION_EVIDENCE` | **REJECTED** | `GOV-REF-001` | malformed lifecycle ref |
| `UNPINNED_ANTECEDENT` | **REJECTED** | `GOV-GRAPH-002` | unpinned antecedent:CL-MAP->CL-BASE |

## Interpretation Boundary

### Supports

- regression closure status for the 16 registered v0.1 specification gaps.

### Does not support

- completeness against unregistered attacks;
- universal correctness of governance v0.2;
- physical mechanism;
- prediction of untested properties.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the neutral organizational partition, Relation Pattern, Null comparison, or population-support claim explicitly reported for the analyzed sample and registered methodology.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- identity with a classical physical category without separately admitted post hoc Cross Mapping.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
