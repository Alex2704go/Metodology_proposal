# OOD Biography and Boundary Anatomy

## 1. B₁₀H₁₄C₁₀S(OF₂)₃ — OOD Biography

```text
Nearest:   F-002
Admission: WITHHELD
State:     OOD
```

### Channel passport

| Organizational channel | Nearest | Margin | Training percentile | State |
|---|---|---:|---:|---|
| Representation | F-002 | 0.058 | 99.9% | OOD |
| Composition | F-002 | 0.017 | 99.3% | OOD |
| Structure | F-002 | 0.069 | 99.7% | OOD |
| Symmetry | F-003 | 0.104 | 33.3% | in-support |
| Scalar Observer | F-003 | 0.004 | 87.8% | in-support / ambiguous |

The object is therefore not OOD in every channel. Its unusual position is concentrated in composition and structure; symmetry lies well inside training support.

### Local geometry

- k=25 radius percentile: 99.5%;
- k=25 radius is 2.40 times the training median;
- nearest-neighbor families: F-002 = 13, F-001 = 12;
- exact full-space membership in the F-002 convex hull: false;
- approximate distance to the F-002 convex hull: 1.4425.

The centroid result is supported by low local density and by being outside the exact family hull. Convex-hull exclusion is a stringent high-dimensional test and is not, by itself, evidence for a new family.

### Why F-002 is nearest

Squared-distance comparison against runner-up F-001:

```text
Block contrast = d²(F-001) − d²(F-002)

composition  +0.374  → supports F-002
structure    +2.536  → strongly supports F-002
symmetry     -0.058  → weakly supports F-001
```

Within the selected representation, the structure block gives the largest contribution to the distinction between the two nearest organizational families, while composition independently lies outside training support.

### Scale audit

| Representation | Nearest | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| Original | F-002 | 0.058 | 99.9% | yes |
| Remove four registered scale-sensitive structure observables | F-002 | 0.126 | 97.7% | no |
| Unit-normalize the complete structure block | F-002 | 0.013 | 99.3% | yes |

Registered conclusion:

```text
Scale contributes materially.
Scale alone does not explain the OOD state.
```

The two registered scale Nulls disagree about OOD removal, and composition remains OOD. Therefore the stronger claim “OOD is scale-driven” is not admitted.

### Current organizational reading

This record is better described as a low-density, multi-channel edge object than as merely a large structure. Whether it represents a new organizational family cannot be decided from one record and remains a candidate question.

---

## 2. LiMnVF₆ — Boundary Anatomy

```text
Nearest:   F-001
Admission: WITHHELD
State:     BOUNDARY
Runner-up: F-003
```

### Channel passport

| Organizational channel | Nearest | Margin | Training percentile | State |
|---|---|---:|---:|---|
| Representation | F-001 | 0.013 | 96.2% | boundary |
| Composition | F-003 | 0.008 | 76.4% | ambiguous |
| Structure | F-001 | 0.027 | 94.6% | ambiguous |
| Symmetry | F-003 | 0.026 | 99.2% | channel-OOD |
| Scalar Observer | F-002 | 0.006 | 74.5% | ambiguous |

No channel gives a high-margin decision. Different channels select three different nearest families.

### Exact block dispute

Squared-distance comparison between nearest F-001 and runner-up F-003:

```text
Block contrast = d²(F-003) − d²(F-001)

composition  -0.044  → supports F-003
structure    +0.412  → supports F-001
symmetry     -0.104  → supports F-003
-----------------------------------
net          +0.264  → F-001 wins narrowly
```

The global F-001 assignment is produced by the structure block overcoming opposing composition and symmetry contributions.

### Local geometry

- k=25 radius percentile: 96.9%;
- k=25 radius is 1.85 times the training median;
- nearest-neighbor families: F-003 = 18, F-001 = 7;
- global centroid nearest family: F-001;
- local-neighborhood majority: F-003;
- exact full-space membership in the F-001 convex hull: false;
- approximate distance to the F-001 convex hull: 1.6620.

This is not only an object-level observable conflict. It is also a conflict between global centroid geometry and local family geometry.

### Scale audit

| Representation | Nearest | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| Original | F-001 | 0.013 | 96.2% | no |
| Remove scale-sensitive structure observables | F-001 | 0.012 | 98.1% | no |
| Unit-normalize structure block | F-003 | 0.024 | 95.1% | no |

Boundary ambiguity survives both Nulls. Unit normalization flips the nearest family but does not resolve the boundary. Therefore scale affects direction but does not cause the low discriminability.

### Missing-language hypotheses

The current evidence does not identify one missing material observable. It supports at least two competing methodological hypotheses:

1. **Local-geometry hypothesis:** one centroid per family is insufficient; F-001 and F-003 may contain multiple organizational subregions.
2. **Channel-resolution hypothesis:** structure, composition and symmetry need an explicit conflict-aware assignment layer rather than immediate aggregation into one distance.

These hypotheses can be tested without literature by comparing frozen centroid assignment with local density, family-specific covariance and multi-prototype representations. Until then, LiMnVF₆ remains `BOUNDARY`.

## Admitted claims

```text
B₁₀H₁₄C₁₀S(OF₂)₃:
    multi-channel low-density OOD
    scale-sensitive but not admitted as scale-driven

LiMnVF₆:
    in-support boundary
    structure favors F-001
    composition and symmetry favor F-003
    local neighbors favor F-003
    centroid geometry and local geometry disagree
```

No physical phase-boundary or mechanism claim is made.

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
