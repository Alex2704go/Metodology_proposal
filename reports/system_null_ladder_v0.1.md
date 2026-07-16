# CEOS System Null Ladder v0.1 — Red-Team Report

> **Terminology note:** `BREACH` is the frozen legacy machine code of this attack harness. Normatively, the 16 results are classified as `SPECIFICATION_GAP` or `UNPROTECTED_TRANSITION`, not as proof that CEOS organizational analysis is broken and not as an actual security compromise.

The target specifications were frozen before attack execution. In this historical report, `BREACH` means only that a logically invalid claim was accepted or escaped registered validation.

- Invalid attacks: **16**
- Breaches: **16**
- Invalid attacks survived: **0**
- Controls passed: **2/2**

| Attack | Class | Severity | Outcome |
|---|---|---|---|
| `CONTROL_VALID_PASSPORT` | control | CONTROL | **SURVIVED** |
| `CONTROL_REMOVE_ASYMMETRY` | control | CONTROL | **SURVIVED** |
| `ADMITTED_WITHOUT_QUALIFICATION` | status | CRITICAL | **BREACH** |
| `GHOST_EVIDENCE` | evidence | CRITICAL | **BREACH** |
| `GHOST_PROVENANCE` | provenance | HIGH | **BREACH** |
| `DIRECTION_SEMANTIC_NOOP` | direction | HIGH | **BREACH** |
| `NOT_TESTED_PLUS_PASS` | maturity | HIGH | **BREACH** |
| `ADMITTED_PLUS_FAILED` | status | CRITICAL | **BREACH** |
| `CONTRADICTORY_INTERPRETATION_BOUNDARY` | semantics | CRITICAL | **BREACH** |
| `EVIDENCE_INHERITANCE_SMUGGLING` | semantics | CRITICAL | **BREACH** |
| `UNSEARCHED_COUNTEREXAMPLES` | qualification | HIGH | **BREACH** |
| `HISTORYLESS_INDEPENDENT_REPLICATION` | lifecycle | CRITICAL | **BREACH** |
| `INDEPENDENCE_WITHOUT_IDENTITIES` | independence | CRITICAL | **BREACH** |
| `NON_MARKDOWN_CLAIM_ESCAPE` | artifact_scope | CRITICAL | **BREACH** |
| `SEMANTIC_MARKDOWN_CONTRADICTION` | document_semantics | CRITICAL | **BREACH** |
| `CYCLIC_CLAIM_GRAPH` | claim_graph | CRITICAL | **BREACH** |
| `SELF_ASSERTED_TRANSITION_EVIDENCE` | typing | CRITICAL | **BREACH** |
| `UNPINNED_ANTECEDENT` | versioning | HIGH | **BREACH** |

## Breach details

### ADMITTED_WITHOUT_QUALIFICATION

accepted=True; maturity=NOT_TESTED; targets empty

### GHOST_EVIDENCE

accepted=True; evidence artifact IDs=[]

### GHOST_PROVENANCE

accepted=True; source artifact IDs=[]

### DIRECTION_SEMANTIC_NOOP

both accepted=True; endpoints unchanged=True

### NOT_TESTED_PLUS_PASS

accepted=True; maturity NOT_TESTED + outcome PASS

### ADMITTED_PLUS_FAILED

accepted=True; ADMITTED + latest FAILED

### CONTRADICTORY_INTERPRETATION_BOUNDARY

accepted=True; physical mechanism in Supports and Does-not-support

### EVIDENCE_INHERITANCE_SMUGGLING

accepted=True; asymmetry boolean true while Supports imports evidence

### UNSEARCHED_COUNTEREXAMPLES

accepted=True; searches={'current_world': False, 'external_worlds': False}

### HISTORYLESS_INDEPENDENT_REPLICATION

accepted=True; schema has no qualification history

### INDEPENDENCE_WITHOUT_IDENTITIES

accepted=True; no WORLD/dataset/Observer identity fields exist

### NON_MARKDOWN_CLAIM_ESCAPE

claim-bearing JSON covered=False; include=['/*.md', '/reports/*.md']

### SEMANTIC_MARKDOWN_CONTRADICTION

current structural linter accepts contradictory Supports/Does-not-support=True

### CYCLIC_CLAIM_GRAPH

cycle A↔B; acyclicity rule present=False

### SELF_ASSERTED_TRANSITION_EVIDENCE

boolean-only evidence accepted=True; no artifact verification

### UNPINNED_ANTECEDENT

content/version pin rule present=False

## Interpretation Boundary

### Supports

- identification of concrete logical gaps in the frozen v0.1 specification.

### Does not support

- a claim that every CEOS result is invalid;
- a physical mechanism or material interpretation;
- completeness of the adversarial attack set;
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
