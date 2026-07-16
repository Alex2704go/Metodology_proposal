# CEOS Admission States

## New epistemic object

```text
Admission State
```

Admission State is not an intrinsic property of a material. It belongs to a versioned relation:

```text
Object × Frozen Partition × Builder Version × Evidence Protocol × Current Checks
```

The same object may change state when evidence accumulates, a Builder is invalidated, the reference WORLD expands, or a new partition version is admitted.

## Partition versus assignment

### Partition Admission

Asks whether the family system itself is reproducible and stronger than its Nulls.

### Assignment Admission

Asks whether the available evidence supports membership of one object in one admitted family.

A globally admitted partition does not guarantee that every transformed object has an admissible assignment.

## Nearest versus admissible

```text
Nearest family
    geometric result of a valid transform

Admissible family
    epistemic result after Assignment Admission
```

An OOD or Boundary object can have a nearest family while its admissible family remains `NONE`.

## States

### ADMITTED

All registered evidence axes pass. `admissible_family = nearest_family`.

### CANDIDATE

The transform is valid, but evidence is incomplete or warning-level. Examples include cross-view disagreement or a warning-level margin.

### BOUNDARY

The object is inside the registered distribution threshold but too close to a family boundary for hard membership.

### OOD

The transform is valid, but the object lies outside registered training support. A nearest centroid may be reported; hard membership is withheld.

### REJECTED

The evidence chain itself is invalid: Builder Admission failed, preprocessing was refit, replay was not exact, leakage was detected, or another integrity gate failed. No assignment claim is permitted.

## Orthogonal Relation Pattern axis

Admission State and Relation Pattern are separate:

```text
BOUNDARY :: RELATIONAL_BOUNDARY
```

The left side records whether a family assignment is admissible. The right side records how independent channels agree or conflict. `RELATIONAL_BOUNDARY` is not a sixth state and does not alter state precedence.

## Evidence Passport

Every assignment stores:

```text
Assignment Evidence

nearest family
admissible family
admission state
margin
distance percentile
OOD flag
cross-view agreement
builder confidence
frozen preprocessing status
exact replay errors
Evidence Weight
withheld reason
partition version
Builder version
protocol version
```

## Evidence Weight v0.1

Four equal axes are reported:

| Axis | PASS | WARN | FAIL |
|---|---:|---:|---:|
| Builder confidence | 1 | — | 0 |
| Cross-view agreement | 1 | — | 0 |
| In-distribution support | 1 | — | 0 |
| Margin | 1 | 0.5 | 0 |

Margin thresholds:

- PASS: `margin ≥ 0.10`;
- WARN: `0.05 ≤ margin < 0.10`;
- FAIL: `margin < 0.05`.

Evidence Weight is displayed as `sum / 4`. It is not a probability and does not override state precedence. For example, an OOD object remains OOD even if its total evidence is 3/4.

## State precedence

```text
REJECTED
    ↓
OOD
    ↓
BOUNDARY
    ↓
CANDIDATE
    ↓
ADMITTED
```

The first applicable state wins. This prevents a high summary score from hiding a decisive failure.

## Knowledge-state transitions

```text
CANDIDATE → ADMITTED
    additional independent support arrives

BOUNDARY → ADMITTED
    partition or representation resolves ambiguity

OOD → CANDIDATE/ADMITTED
    reference WORLD expands and support is re-audited

ADMITTED → REJECTED
    upstream Builder or integrity gate is invalidated

ADMITTED(v1) → CANDIDATE(v2)
    a new partition or evidence protocol requires reassessment
```

Every transition must preserve the old passport and create a new version. States are never silently overwritten.

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
