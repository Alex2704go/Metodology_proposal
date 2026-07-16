# CEOS Architecture — Scientific Claim Control

CEOS is treated here not merely as a data-analysis method, but as a control system for scientific claims.

```text
Raw World
    ↓
Representation Ecology
    ↓
Object Census
    ↓
Object Typing
    ↓
Builder Dispatch
    ↓
Builder Admission
    ↓
Organizational Observables
    ↓
Observer Ecology
    ↓
Targeted Null Ladder
    ↓
Partition Admission
    ↓
Frozen Partition
    ↓
Assignment Evidence
    ↓
Admission State
    ↓
Assignment Explanation
    ↓
Admissible Family / Withheld
    ↓
Interpretation Boundary
    ↓
Cross Mapping
    ↓
Interpretation
```

## Claim Type System

Every entity and claim has an explicit type. Transitions between claim types require registered evidence and Admission; Cross Mapping cannot be coerced into Evidence, and Nearest Assignment cannot be coerced into Admissible Assignment. See `CEOS_TYPE_SYSTEM.md`.

## Meta-governance cycle

```text
Protocol
    ↓
Governance Null Ladder
    ↓
Specification Gap Registry
    ↓
Governance Revision
    ↓
Regression on unchanged attacks
```

Scientific Null Ladder attacks organizational results. Governance Null Ladder attacks claim construction. Their outcomes are non-substitutable. See `SCIENTIFIC_NULL_LADDER.md`, `GOVERNANCE_NULL_LADDER.md` and `CEOS_CLAIM_COMPILER.md`.

## Claim-strength rule

Every transition must satisfy three conditions:

1. the new statement is stronger than the preceding statement;
2. the assumptions required for that increase are explicit;
3. a registered audit can reject the transition.

A later level cannot silently alter an admitted object from an earlier level. If preprocessing, Builder behavior, partitioning, or admission criteria change, the affected downstream objects are invalidated and must be rebuilt under a new version.

## Levels

### Raw World

Immutable source responses, provenance, query specification and checksums.

### Representation Ecology

The population of scalar, list, map, record, hierarchical and composite objects together with explicit NONE/EMPTY/PRESENT states.

### Object Census

Counts, schemas, missingness, ranges, key grammars, cardinalities and repeated forms. No mechanisms or literature classes.

### Object Typing

Data-derived Object Signatures:

```text
State × Container × KeyGrammar × ValueGrammar × Topology × Cardinality
```

### Builder Dispatch

Selection of Builder contracts from Object Signatures rather than source-field names or expected physical meaning.

### Builder Admission

A Builder is admitted only after invariance, replay, leakage, preprocessing and serialization audits. Builder Admission can be revoked independently of family admission.

### Organizational Observables

Builder outputs that measure organization. The preferred term is `organizational observable`, not `feature`.

### Observer Ecology

Dependence, redundancy, coupling, competing views and representation-language effects among Observer blocks.

### Targeted Null Ladder

Each Null attacks a named organizational object while preserving specified lower-level marginals or grammars.

### Partition Admission

The family system passes only if its registered stability, Null and integrity criteria succeed.

### Frozen Partition

Neutral labels and transformation parameters become immutable. Out-of-sample projection must use frozen preprocessing and exact training replay.

### Assignment Evidence

Each projected object receives a versioned Evidence Passport containing nearest family, margin, distance percentile, cross-view agreement, Builder confidence and replay evidence.

### Admission State

Assignment evidence is converted by a registered state machine into `ADMITTED`, `CANDIDATE`, `BOUNDARY`, `OOD`, or `REJECTED`. The state belongs to `Object × Evidence Context`, not to the material intrinsically.

### Assignment Explanation

The state is decomposed into channel distances, block contributions, local density, neighborhood composition, hull evidence and targeted assignment Nulls. Explanation may reveal scale sensitivity, channel conflict or a mismatch between global centroid and local geometry.

`Conflict Topology` is the relational subobject that preserves which channels agree and disagree. It is audited with Conflict Nulls that destroy channel alignment while preserving channel packets. Assignment Explanation does not silently alter the frozen assignment protocol.

### Admissible Family / Withheld

`nearest_family` is geometric and may exist for any valid transform. `admissible_family` is populated only when Assignment Admission reaches `ADMITTED`; otherwise it is explicitly withheld.

### Interpretation Boundary

Every passport declares both positive and negative semantic scope: what the result supports and what it does not support. Missing prohibitions are not interpreted as permission.

### Cross Mapping

Classical terminology is compared post hoc with the frozen organizational ontology. It cannot define or tune the partition.

### Interpretation

Mechanisms and literature-facing language are permitted only after the prior chain remains intact.

## Current admitted claim

```text
Claim
    The current family partition is Structure-dominated.

Support
    Remove structure
        ↓
    ARI 0.0775

    Remove composition
        ↓
    ARI 0.9871

    Remove symmetry
        ↓
    ARI 0.9814
```

Permitted wording:

```text
CEOS Structural Representation Families
```

Not yet permitted:

```text
general materials taxonomy
physical mechanism
classical-family identity
literature-derived material class
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
