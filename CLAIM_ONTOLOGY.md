# CEOS Claim Ontology

CEOS controls not only entities but transitions between claim types.

```text
Observation
    ↓ Observation Admission
Organizational Object
    ↓ Object/Builder Admission
Family
    ↓ Pattern Admission
Relation Pattern
    ↓ Mapping Admission
Cross Mapping
    ↓ Interpretation Admission
Interpretation
```

The arrows denote increases in claim strength, not automatic inference.

## Claim types

### Observation Claim

States that a value, schema, state or relation was observed under registered provenance.

Admission requires source integrity, immutable raw data, serialization validity and inventory checks.

### Organizational Object Claim

States that an observed representation supports a typed object and admitted Builder contract.

Admission requires Object Signature, Builder dispatch, invariance, no leakage, deterministic transform and exact replay.

### Family Claim

States that a reproducible neutral partition exists in a frozen organizational-observable space.

Admission requires stability, targeted Nulls, minimum support, frozen preprocessing and explicit scope.

### Relation Pattern Claim

States that a family-label-invariant organization of channel agreement/disagreement recurs beyond targeted Conflict Null expectation.

Admission requires canonical topology, population support, label invariance, deterministic neighborhood contract and state-precedence consistency.

### Cross Mapping Claim

States a post hoc correspondence between vocabularies.

Admission requires frozen CEOS entities, citations, counterexamples, Mapping Stability, many-to-many preservation and Cross Mapping Asymmetry.

### Interpretation Claim

States a mechanism, phase semantics, causal account or microscopic model.

It requires independent domain evidence and a dedicated Interpretation Admission protocol. It cannot be admitted by vocabulary correspondence alone.

## Result Biography

Every claim may be accompanied by a Result Biography: an event-sourced DAG of proposed, rejected, withheld, admitted, reassessed and released states. Biography events reference the same content-addressed evidence and antecedent artifacts as the Claim Passport.

A biography is not merely an action log. It records the evolution of claim type, scope and admissibility.

## Non-inheritance rule

Evidence does not automatically propagate through claim transitions.

```text
admitted Relation Pattern
    does not imply
admitted physical interpretation

admitted Cross Mapping
    does not imply
mechanism inheritance
```

Each stronger claim references earlier admitted objects but must add its own evidence.

## Claim Passport

Every claim-bearing object records:

- claim ID and type;
- antecedent claim IDs;
- evidence artifact IDs;
- protocol and version;
- Admission State;
- stability scope;
- counterexamples;
- Interpretation Boundary;
- invalidation dependencies.

## Invalidation

If an antecedent claim is revoked, dependent claims become `REASSESSMENT_REQUIRED`; they are not silently preserved.

## Cross Mapping Asymmetry

```text
Cross Mapping translates vocabularies.
Cross Mapping does not transfer evidence.
```

The rule applies in both directions.

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
