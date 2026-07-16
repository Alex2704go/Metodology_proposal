# CEOS Governance v0.2 — Proof-Carrying Candidate

## Status

```text
QUALIFIED
not ADMITTED
```

Qualification means that the candidate valid fixture passes and the unchanged 16 registered System Null attacks from v0.1 are rejected. Admission requires an independent adversarial review and additional unregistered attacks.

## State Machine

```text
NOT_TESTED
    ↓ QUALIFY
QUALIFIED
    ↓ ADMIT
ADMITTED
    ↓ FAIL
REASSESSMENT_REQUIRED
    ↓ QUALIFY or RETIRE
QUALIFIED / RETIRED
```

Every event contains pinned EvidenceRefs. State is derived by replaying events; it is not an authored passport field.

Impossible transitions are rejected.

## Proof objects

```text
EvidenceRef
    artifact_id
    expected_sha256
    evidence_type
    protocol_version
    validator_id

ProvenanceRef
    artifact_id
    expected_sha256
    provenance_role

AntecedentRef
    claim_id
    expected_content_digest
    expected_version
```

The validator checks registry membership, actual workspace digest, protocol, validator and version.

## Identity Registry

Operational independence uses registered identities:

```text
WORLD_ID
DATASET_ID
OBSERVER_ID
BUILDER_ID
```

Independent replication requires distinct independence groups and distinct lineage roots. This does not prove philosophical independence; it makes the operational assertion explicit and auditable.

## Claim DAG

Claims are content-addressed and antecedents are digest/version pinned.

```text
Claim A → Claim B → Claim C
```

Cycles, unknown parents, digest drift and version drift are rejected.

## Event-sourced Mapping Maturity

Maturity is derived from qualification events:

```text
NOT_TESTED
SINGLE_WORLD
MULTI_WORLD
INDEPENDENTLY_REPLICATED
```

A qualification event contains evidence refs and identity IDs. `FAILED` and `MIXED` are outcomes. If the latest outcome is not PASS, an ADMITTED mapping is invalid and requires reassessment.

## Semantic Interpretation Boundary

Permissions use controlled ClaimType IDs rather than free text:

```text
supports_claim_types
prohibits_claim_types
```

The sets must be disjoint. Mandatory prohibitions include:

- PHYSICAL_MECHANISM;
- THERMODYNAMIC_PHASE;
- MICROSCOPIC_HAMILTONIAN;
- CAUSAL_EXPLANATION;
- PREDICTION_UNTESTED_PROPERTIES;
- EVIDENCE_INHERITANCE.

Free text may explain a claim but cannot grant permission.

## Artifact governance

Claim-bearing artifacts are registered regardless of extension. Markdown, JSON, CSV, images and other outputs cannot escape by format. A claim-bearing artifact requires a controlled claim passport.

## Regression result

```text
v0.1:
    controls 2/2
    specification gaps 16/16

v0.2 candidate:
    controls 2/2
    invalid attacks rejected 16/16
    registered gaps remaining 0
```

## Why only QUALIFIED

The validator and regression suite were designed in the same development loop. Passing them demonstrates closure of known requirements, not completeness or universal soundness.

Admission requires:

1. independent attack design;
2. mutation tests not authored from the remediation list;
3. review of identity-independence semantics;
4. audit of real, not synthetic, claim graphs;
5. fail-closed behavior under corrupted registries and partial files.

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the protocol, vocabulary, decision history, or document-governance contract explicitly stated here; empirical claims only through separately admitted linked artifacts.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- empirical validation merely because a rule is documented.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
