# CEOS Entity Ontology

## Distinct entity types

```text
WORLD
Object
Observer
Family
Relation Pattern
Admission State
Release State
Result Biography
Interpretation Boundary
```

These are not progressively detailed descriptions of one entity. They have different identity conditions and audit contracts.

## Typed relations

```text
WORLD contains Object
Observer describes Object
Builder produces Organizational Observable
Family organizes Object representations
Relation Pattern organizes relations among assignment channels
Admission State qualifies a claim about Object × Evidence Context
Interpretation Boundary limits the semantic scope of a claim
```

## Identity conditions

### WORLD

Identified by source population, extraction protocol, representation ecology and version.

### Object

Identified by an anonymized object key within a WORLD. Source IDs are provenance, not organizational observables.

### Observer

Identified by its measurement contract, input signature and output semantics.

### Family

Identified by a frozen partition protocol, organizational-observable space, Null admission and version.

### Relation Pattern

Identified by a canonical structure of agreement/disagreement among typed channels. Family names may be relabeled without changing the pattern.

### Admission State

Identified by `Object × Frozen Partition × Builder Version × Evidence Protocol × Current Checks`. It can change when evidence changes.

### Release State

Identified by the publication lifecycle of a claim: `DRAFT`, `WITHHELD`, `RELEASED`, or `RETIRED`. It is orthogonal to Admission State.

### Result Biography

Identified by a versioned, content-addressed event DAG that records critical changes to hypotheses, representations, Null results, Admission States, Release States and Interpretation Boundaries.

### Interpretation Boundary

Identified by explicit supported and unsupported claim types attached to a result passport.

## Two orthogonal questions

```text
Relation Pattern:
    How are independent channels organized relative to one another?

Admission State:
    What claim is currently permitted about this object?
```

Example:

```text
Object:
    LiMnVF6 record

Admission State:
    BOUNDARY

Relation Pattern:
    RELATIONAL_BOUNDARY

Interpretation Boundary:
    supports organizational conflict pattern
    does not support physical mechanism or phase boundary
```

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
