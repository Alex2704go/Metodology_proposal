# CEOS Claim Type System

> **Status: REASSESSMENT_REQUIRED.** System Null Ladder v0.1 breached all 16 invalid attacks. This document remains the v0.1 design target, not an admitted proof-carrying implementation.

## Purpose

CEOS assigns explicit types to scientific entities and claims, then constrains legal transitions between them.

```text
Well-typed research does not guarantee truth.
It prevents registered classes of logical error.
```

## Core types

```text
RawObservation
OrganizationalObject
ObserverOutput
FrozenFamily
RelationPattern
AdmissionState
NearestAssignment
AdmissibleAssignment
CrossMapping
IndependentEvidence
InterpretationClaim
InterpretationBoundary
```

## Typing context

A judgment has the form:

```text
Γ ⊢ claim : Type
    [protocol, version, provenance, scope, Admission State]
```

`Γ` contains admitted antecedent claims and evidence artifacts. A claim without provenance, scope and version is incomplete rather than implicitly generic.

## Legal transitions

### Observation → Organizational Object

Requires Object Typing and Builder Admission.

### Organizational Objects → Frozen Family

Requires organizational-observable vectorization, stability, Null Ladder and Partition Admission.

### Channel Assignments → Relation Pattern

Requires canonical channel topology, label invariance, Conflict Null and Pattern Admission.

### CEOS Entity × External Term → Cross Mapping

Requires frozen CEOS identity, Direction, Mapping Provenance, counterexamples, Mapping Stability and Mapping Admission.

### Cross Mapping × Independent Evidence → Interpretation Claim

Requires an independent Evidence Passport and Interpretation Admission. Cross Mapping alone is insufficient.

## Forbidden coercions

```text
ExternalTerm       ↛ OrganizationalObject
CrossMapping       ↛ IndependentEvidence
NearestAssignment  ↛ AdmissibleAssignment
RelationPattern    ↛ AdmissionState
LowMargin          ↛ Boundary when global OOD
FamilyLabel        ↛ PhysicalMechanism
VocabularyName     ↛ PredictionOfUntestedProperties
```

## Non-substitutability

- Relation Pattern and Admission State are orthogonal types.
- Mapping Strength and Evidence Strength are separate types.
- Maturity and Qualification Outcome are separate types.
- Provenance is a required component of a typed claim, not metadata that may be discarded.

## Epistemic upgrade rule

```text
Γ ⊢ mapping : CrossMapping
```

never entails:

```text
Γ ⊢ source_ontology : HigherEpistemicStatus
Γ ⊢ target_ontology : HigherEpistemicStatus
```

An upgrade requires:

```text
Γ + independently_admitted_evidence
```

## Type failure

A failed typing or Admission check produces an explicit state such as:

```text
REJECTED
REASSESSMENT_REQUIRED
WITHHELD
```

It must not be silently coerced into a weaker warning while preserving the stronger claim.

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
