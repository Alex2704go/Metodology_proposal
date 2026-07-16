# CEOS Cross Mapping Contract

**Status: LOCKED / REASSESSMENT_REQUIRED.** System Null Ladder v0.1 found critical schema and lifecycle breaches. No real mapping may be admitted until a remediated version passes the unchanged adversarial regression suite.

## Normative Rule

```text
Cross Mapping is descriptive.
It never upgrades the epistemic status of either ontology.
Only independently admitted evidence may upgrade epistemic status.
```

This rule has precedence over mapping strength, maturity, direction and vocabulary familiarity. No Cross Mapping record may waive it.

## Principle Box

> **Vocabulary correspondence ≠ evidence inheritance.**

## Mapping unit

Cross Mapping is many-to-many and does not assume that a classical term corresponds to one CEOS Family.

```text
Classical Term
    ↕
Frozen Family × Relation Pattern × Admission Context
```

Possible mappings:

```text
Classical term: X
    observed with
    Family F-003
    Relation Patterns RP-A, RP-B, RP-C
```

or:

```text
Relation Pattern RP-X
    observed in literature using
    classical terms A, B, C
```

## Required fields

Every Cross Mapping record must include:

- classical term and source citation;
- frozen CEOS family version, if relevant;
- stable Relation Pattern ID;
- canonical family-label-invariant signature;
- object population and inclusion criteria;
- explicit Direction enum;
- Mapping Provenance checklist and source artifact IDs;
- mapping strength and counterexamples;
- Mapping Stability maturity and Qualification Outcome;
- Admission State distribution;
- Interpretation Boundary;
- explicit statement that mapping was post hoc.

## Direction

Every mapping declares exactly one direction:

```text
CEOS_TO_CLASSICAL
CLASSICAL_TO_CEOS
BIDIRECTIONAL_CANDIDATE
```

`BIDIRECTIONAL_CANDIDATE` means that both directional correspondences are being tested. It does not waive Cross Mapping Asymmetry and does not imply evidential equivalence.

## Mapping Provenance

Every mapping records what it was constructed from:

```text
Mapping Provenance

Constructed from:
    □ Family only
    □ Relation Pattern
    □ Admission Context
    □ Population statistics
    □ Independent Observer agreement

Source artifact IDs:
    ...
```

Unchecked provenance dimensions are explicit absences of support, not neutral formatting omissions.

## Mapping Stability

Every mapping carries an independent stability passport:

```text
Mapping Stability

Observed across:
    □ one WORLD
    □ multiple WORLDs
    □ independent datasets
    □ independent Observers

Counterexamples searched:
    □ within current WORLD
    □ outside current WORLD

Mapping Maturity:
    NOT_TESTED
        ↓
    SINGLE_WORLD
        ↓
    MULTI_WORLD
        ↓
    INDEPENDENTLY_REPLICATED

Qualification Outcome:
    NOT_RUN | PASS | MIXED | FAILED
```

Maturity is monotonic. `FAILED` is a qualification outcome, not a maturity level. A failed new test does not rewrite history; it records a contradiction or failed qualification against the last admitted maturity and triggers reassessment.

A mapping observed in one WORLD cannot be described as transferable. Independent Observer agreement is distinct from independent-dataset replication and must be reported separately.

## Cross Mapping Asymmetry

> **Cross Mapping translates between vocabularies. It does not transfer evidence.**

Mapping a CEOS entity to a classical term does not import the term’s mechanisms, causal models, phase semantics, Hamiltonians, or accumulated evidential strength into CEOS.

Conversely, CEOS Population Support does not validate every physical interpretation historically associated with the classical term.

```text
Vocabulary correspondence
    ≠ evidence inheritance
```

Any transferred-looking claim requires a new independent Evidence Passport and its own Admission. Mapping strength and evidence strength are separate fields.

## Forbidden behavior

- Classical terminology cannot define or tune a frozen Family.
- A literature term cannot rename a CEOS entity without preserving the neutral ID.
- One matching example cannot establish an equivalence.
- Many-to-many structure cannot be collapsed for narrative convenience.
- Cross Mapping cannot be used as evidence of mechanism unless a separate mechanism protocol is admitted.

## Interpretation Boundary template

```text
Interpretation Boundary

Supports:
    post hoc association between a classical vocabulary item
    and one or more frozen organizational entities

Does not support:
    identity of ontologies
    physical mechanism
    thermodynamic phase equivalence
    microscopic Hamiltonian
    causal explanation
    prediction of untested properties
```

## Current status

```text
Families:
    frozen

Relation Pattern registry:
    available

Literature mapping:
    LOCKED

Physical interpretation:
    LOCKED
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
