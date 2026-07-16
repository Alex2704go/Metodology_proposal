# Checkpoint — Family Validation

## Cross-view agreement

| View A | View B | ARI |
|---|---|---:|
| `ORGANIZATION` | `OBSERVER_AUGMENTED` | 0.9945 |
| `ORGANIZATION` | `FULL_REPRESENTATION` | 0.5198 |
| `OBSERVER_AUGMENTED` | `FULL_REPRESENTATION` | 0.5239 |

## ORGANIZATION

- Median assignment margin: **0.3529**
- q10 margin: **0.1493**
- Objects with margin < 0.05: **52**

| Family | Size | Median margin | q10 margin | Leading neutral coordinates |
|---|---:|---:|---:|---|
| F-001 | 1520 | 0.359 | 0.137 | structure.sites[].abc[].min (+0.27); structure.leaves (+0.20); composition.sorted_share_4 (+0.15); symmetry.crystal_system==Orthorhombic (+0.14); structure.list_size_std (+0.14) |
| F-002 | 608 | 0.342 | 0.190 | structure.lattice.beta.mean (+1.78); structure.lattice.alpha.mean (+0.73); structure.sites[].abc[].min (+0.23); structure.sites[].xyz[].min (-0.22); structure.leaves (+0.20) |
| F-003 | 655 | 0.326 | 0.165 | structure.lattice.beta.mean (-1.78); structure.lattice.alpha.mean (-0.83); structure.sites[].abc[].min (+0.32); structure.lattice.gamma.mean (-0.27); structure.sites[].xyz[].std (+0.21) |
| F-004 | 217 | 0.452 | 0.087 | structure.dict_size_mean (+2.25); structure.list_size_mean (-1.91); structure.sites[].abc[].max (-1.16); structure.sites[].abc[].std (-1.15); structure.dict_size_std (+1.05) |

## OBSERVER_AUGMENTED

- Median assignment margin: **0.3144**
- q10 margin: **0.1319**
- Objects with margin < 0.05: **52**

| Family | Size | Median margin | q10 margin | Leading neutral coordinates |
|---|---:|---:|---:|---|
| F-001 | 1517 | 0.321 | 0.128 | band_gap (+0.27); structure.sites[].abc[].min (+0.27); structure.leaves (+0.21); ordering==FM (+0.16); ordering==NM (+0.16) |
| F-002 | 609 | 0.305 | 0.158 | structure.lattice.beta.mean (+1.78); structure.lattice.alpha.mean (+0.73); band_gap (+0.28); structure.sites[].abc[].min (+0.23); structure.sites[].xyz[].min (-0.22) |
| F-003 | 649 | 0.294 | 0.151 | structure.lattice.beta.mean (-1.78); structure.lattice.alpha.mean (-0.82); structure.sites[].abc[].min (+0.32); band_gap (+0.29); structure.lattice.gamma.mean (-0.27) |
| F-004 | 225 | 0.429 | 0.097 | structure.dict_size_mean (+2.21); structure.list_size_mean (-1.89); structure.sites[].abc[].max (-1.13); structure.sites[].abc[].std (-1.11); structure.dict_size_std (+1.05) |

## FULL_REPRESENTATION

- Median assignment margin: **0.3221**
- q10 margin: **0.1326**
- Objects with margin < 0.05: **86**

| Family | Size | Median margin | q10 margin | Leading neutral coordinates |
|---|---:|---:|---:|---|
| F-001 | 1993 | 0.313 | 0.153 | structure.lattice.beta.mean (+0.54); band_gap (+0.27); structure.sites[].abc[].min (+0.26); structure.lattice.alpha.mean (+0.24); structure.leaves (+0.21) |
| F-002 | 693 | 0.342 | 0.106 | structure.lattice.beta.mean (-1.66); structure.lattice.alpha.mean (-0.87); band_gap (+0.32); structure.sites[].abc[].min (+0.31); structure.lattice.gamma.mean (-0.25) |
| F-003 | 314 | 0.333 | 0.088 | structure.dict_size_mean (+1.80); structure.list_size_mean (-1.64); structure.sites[].abc[].max (-0.94); structure.dict_size_std (+0.93); structure.sites[].abc[].std (-0.82) |

Margins measure geometric confidence relative to the two nearest centroids. They are not probabilities.

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the explicit execution, replay, invariance, integrity, or contract checks reported in this document under the registered software and data versions.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- a substantive material family, organizational mechanism, or scientific interpretation merely because a technical check passes.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
