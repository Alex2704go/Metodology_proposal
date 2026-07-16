# System Null Ladder v0.1 — Failure Analysis

## Verdict

```text
Controls passed: 2/2
Invalid attacks: 16
Breaches: 16/16
```

The frozen CEOS Claim Type System v0.1, Cross Mapping Passport schema v0.1 and Document Contract v0.1 do not yet form a proof-carrying type system.

## Root cause

> **The current system validates declarations more strongly than it validates the evidence behind those declarations.**

Booleans and status strings can attest that provenance, independence, qualification or asymmetry exists without supplying typed, content-pinned proof objects.

## Failure families

### 1. Status is not derived from qualification

Breaches:

- `ADMITTED_WITHOUT_QUALIFICATION`;
- `NOT_TESTED_PLUS_PASS`;
- `ADMITTED_PLUS_FAILED`;
- `UNSEARCHED_COUNTEREXAMPLES`.

An attacker can set `status = ADMITTED` while targets are empty, maturity is `NOT_TESTED`, qualification is `FAILED`, or counterexample searches were never run.

Required improvement:

```text
status must be derived
not user-authored
```

### 2. Evidence and provenance are attestations, not proof objects

Breaches:

- `GHOST_EVIDENCE`;
- `GHOST_PROVENANCE`;
- `SELF_ASSERTED_TRANSITION_EVIDENCE`;
- `UNPINNED_ANTECEDENT`.

The schema accepts `INDEPENDENTLY_REPLICATED` evidence with no evidence artifact IDs and asserted provenance with no source artifacts. Transition requirements are booleans rather than verified references.

Required improvement:

```text
EvidenceRef =
    artifact_id
    content_digest
    evidence_type
    protocol_version
    validator_id
    independence_group
```

### 3. Direction is a label, not a typed endpoint relation

Breach:

- `DIRECTION_SEMANTIC_NOOP`.

Changing `CEOS_TO_CLASSICAL` to `CLASSICAL_TO_CEOS` leaves endpoint structure untouched and both records validate.

Required improvement:

```text
Mapping endpoints must be typed neutrally.
Direction must determine source/target roles.
```

### 4. Maturity is a snapshot without lifecycle proof

Breaches:

- `HISTORYLESS_INDEPENDENT_REPLICATION`;
- `INDEPENDENCE_WITHOUT_IDENTITIES`.

A mapping can claim independent replication without qualification events, WORLD IDs, dataset IDs or Observer IDs.

Required improvement:

```text
Mapping Maturity must be event-sourced.
Independence must be demonstrated through distinct typed identities.
```

### 5. Structural validation does not prevent semantic contradiction

Breaches:

- `CONTRADICTORY_INTERPRETATION_BOUNDARY`;
- `EVIDENCE_INHERITANCE_SMUGGLING`;
- `SEMANTIC_MARKDOWN_CONTRADICTION`.

A document can support and prohibit `physical mechanism` simultaneously. A passport can acknowledge Asymmetry while its Supports text claims evidence inheritance. The Markdown linter checks section presence, not semantic disjointness.

Required improvement:

```text
Supports and Does-not-support require controlled ClaimType IDs.
Their sets must be disjoint.
Free text may explain but cannot define permission.
```

### 6. Claim-bearing artifacts can escape document governance

Breach:

- `NON_MARKDOWN_CLAIM_ESCAPE`.

The Document Contract scans Markdown, while claim-bearing JSON, CSV, figures and machine artifacts can exist without an Interpretation Boundary.

Required improvement:

```text
Artifact Registry
    ↓
claim-bearing flag
    ↓
required sidecar Claim Passport
```

### 7. The claim graph is not represented or checked

Breach:

- `CYCLIC_CLAIM_GRAPH`.

The current transition list cannot detect cyclic antecedents such as `A → B → A`.

Required improvement:

```text
Claims form a content-addressed DAG.
Cycles are rejected.
Antecedent versions and digests are mandatory.
```

## What survived

Two controls passed:

1. the valid synthetic locked passport is accepted;
2. disabling Cross Mapping Asymmetry is rejected.

Therefore the schema performs syntactic and selected constant-value validation. The breach is the gap between syntactic conformance and evidential validity.

## Dependency impact

### Reassessment required

- CEOS Claim Type System v0.1;
- Cross Mapping Passport schema v0.1;
- semantic claims made about Document Contract v0.1;
- any future Mapping Admission based solely on these specifications.

### Not invalidated by this Null Ladder

- immutable Materials Project raw data;
- Builder Admission and exact replay;
- organizational-observable vectors;
- frozen structural families;
- Assignment State calculations;
- Conflict Topology population statistics.

No real Cross Mapping had been admitted; the literature gate remains locked.

## Remediation order

### P0 — Fail closed

1. Derived status rather than authored status.
2. Typed, content-hashed EvidenceRef and ProvenanceRef.
3. Controlled ClaimType sets for Interpretation Boundary.
4. Claim DAG with cycle and digest validation.
5. Claim-bearing Artifact Registry covering non-Markdown outputs.

### P1 — Qualification lifecycle

6. Event-sourced Mapping Maturity.
7. Typed WORLD, dataset and Observer identities for independence.
8. Direction-bound typed endpoints.
9. Counterexample-search artifacts.

### P2 — Reattack

The same 16 attacks must be rerun unchanged against v0.2. Remediation is admitted only when:

```text
controls pass
AND all 16 invalid attacks are rejected
AND no new critical breach is introduced
```

## Interpretation Boundary

### Supports

- the conclusion that the frozen v0.1 claim-governance specifications contain the documented logical and validation gaps;
- prioritization of remediation and unchanged adversarial regression tests.

### Does not support

- the claim that all CEOS organizational results are invalid;
- completeness of the attack set;
- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
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
