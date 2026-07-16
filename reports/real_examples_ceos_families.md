# Real Materials → CEOS Families

Primary view: **ORGANIZATION**. `OBSERVER_AUGMENTED` is an independent confirmation view; `FULL_REPRESENTATION` is a language/control view.

- Training replay raw max error: **0.0e+00**
- Training replay scaled max error: **0.0e+00**

| Formula | ORGANIZATION | Margin | OOD percentile | Observer confirmation | FULL language family |
|---|---|---:|---:|---|---|
| FeS | **F-001** | 0.166 | 79.5% | YES | F-003 |
| NaCl | **F-004** | 0.487 | 51.3% | YES | F-003 |
| SiO2 | **F-001** | 0.337 | 53.8% | YES | F-001 |
| SrTiO3 | **F-002** | 0.445 | 34.6% | YES | F-001 |

## Reading the checks

- Margin compares the nearest and second-nearest centroids; it is not a probability.
- OOD percentile compares the example distance with training-object distances to their nearest centroid. Above 99% is flagged.
- A family is considered cross-view confirmed only when ORGANIZATION and OBSERVER_AUGMENTED agree.
- FULL_REPRESENTATION is not used as the material-family decision because capability/provenance form a distinct representation-language layer.

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
