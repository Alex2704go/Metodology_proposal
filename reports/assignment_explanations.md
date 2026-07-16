# Assignment Explanations — OOD Biography and Boundary Anatomy

No pseudo-probabilities are used. Channel evidence is reported as distances, percentiles and margins.

## DISTANT_OBJECT: B10H14C10S(OF2)3

### Organizational distances

| Channel | Nearest | Second | Margin | Percentile | OOD |
|---|---|---|---:|---:|---|
| representation | F-002 (4.737) | F-001 (5.029) | 0.058 | 99.9% | YES |
| composition | F-002 (2.357) | F-003 (2.397) | 0.017 | 99.3% | YES |
| structure | F-002 (4.060) | F-001 (4.361) | 0.069 | 99.7% | YES |
| symmetry | F-003 (0.526) | F-001 (0.588) | 0.104 | 33.3% | no |
| observer | F-003 (1.239) | F-002 (1.244) | 0.004 | 87.8% | no |

### Centroid-distance decomposition

| Target | Family | Composition d² | Structure d² | Symmetry d² |
|---|---|---:|---:|---:|
| nearest | F-002 | 5.554 | 16.486 | 0.403 |
| second | F-001 | 5.928 | 19.022 | 0.345 |

Block contrast `d²(second) − d²(nearest)`: composition +0.374, structure +2.536, symmetry -0.058.
Positive supports the nearest family; negative supports the runner-up.

### Neighborhood and hull

- k=25 radius percentile: **99.5%**
- k=25 radius / training median: **2.40**
- neighbor-family counts: `{'F-002': 13, 'F-001': 12}`
- exact full-space convex-hull membership in F-002: **False**
- approximate distance to family convex hull: **1.4425**

### Scale Nulls

| View | Nearest | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| Original | F-002 | 0.058 | 99.9% | YES |
| `REMOVE_SCALE_SENSITIVE_STRUCTURE_OBSERVABLES` | F-002 | 0.126 | 97.7% | no |
| `STRUCTURE_BLOCK_UNIT_NORM` | F-002 | 0.013 | 99.3% | YES |

Scale-driven under the registered two-Null rule: **False**
## BOUNDARY_OBJECT: LiMnVF6

### Organizational distances

| Channel | Nearest | Second | Margin | Percentile | OOD |
|---|---|---|---:|---:|---|
| representation | F-001 (3.122) | F-003 (3.164) | 0.013 | 96.2% | no |
| composition | F-003 (0.578) | F-002 (0.582) | 0.008 | 76.4% | no |
| structure | F-001 (2.719) | F-003 (2.794) | 0.027 | 94.6% | no |
| symmetry | F-003 (1.368) | F-002 (1.404) | 0.026 | 99.2% | YES |
| observer | F-002 (0.778) | F-003 (0.782) | 0.006 | 74.5% | no |

### Centroid-distance decomposition

| Target | Family | Composition d² | Structure d² | Symmetry d² |
|---|---|---:|---:|---:|
| nearest | F-001 | 0.378 | 7.394 | 1.977 |
| second | F-003 | 0.334 | 7.806 | 1.873 |

Block contrast `d²(second) − d²(nearest)`: composition -0.044, structure +0.412, symmetry -0.104.
Positive supports the nearest family; negative supports the runner-up.

### Neighborhood and hull

- k=25 radius percentile: **96.9%**
- k=25 radius / training median: **1.85**
- neighbor-family counts: `{'F-001': 7, 'F-003': 18}`
- exact full-space convex-hull membership in F-001: **False**
- approximate distance to family convex hull: **1.6620**

### Scale Nulls

| View | Nearest | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| Original | F-001 | 0.013 | 96.2% | no |
| `REMOVE_SCALE_SENSITIVE_STRUCTURE_OBSERVABLES` | F-001 | 0.012 | 98.1% | no |
| `STRUCTURE_BLOCK_UNIT_NORM` | F-003 | 0.024 | 95.1% | no |

Scale-driven under the registered two-Null rule: **False**

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the object-specific nearest-family geometry, evidence passport, Admission State, or Relation Pattern claims explicitly reported under the frozen context.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- membership when admission is withheld, or generalization from one object to a population.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
