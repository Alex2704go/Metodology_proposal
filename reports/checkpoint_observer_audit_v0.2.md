# Checkpoint — Observer Audit

- Blocks: **8**
- Block pairs: **28**
- Observable pairs with |r| ≥ 0.90 shown: **13**

## Block dependence

| Block A | Block B | RV | Null q95 | Above null? |
|---|---|---:|---:|---|
| `capability_map` | `provenance_shape` | 0.3553 | 0.0020 | YES |
| `composition_shape` | `structure_topology` | 0.3006 | 0.0020 | YES |
| `capability_map` | `composition_shape` | 0.2661 | 0.0028 | YES |
| `capability_map` | `structure_topology` | 0.2372 | 0.0019 | YES |
| `provenance_shape` | `structure_topology` | 0.2161 | 0.0014 | YES |
| `structure_numeric` | `structure_topology` | 0.1969 | 0.0020 | YES |
| `composition_shape` | `provenance_shape` | 0.1855 | 0.0010 | YES |
| `structure_topology` | `symmetry_record` | 0.1022 | 0.0026 | YES |
| `structure_numeric` | `symmetry_record` | 0.0948 | 0.0035 | YES |
| `scalar_observers` | `structure_topology` | 0.0941 | 0.0016 | YES |
| `composition_shape` | `scalar_observers` | 0.0865 | 0.0015 | YES |
| `composition_shape` | `symmetry_record` | 0.0855 | 0.0034 | YES |
| `capability_map` | `scalar_observers` | 0.0743 | 0.0024 | YES |
| `provenance_shape` | `scalar_observers` | 0.0719 | 0.0014 | YES |
| `capability_map` | `symmetry_record` | 0.0693 | 0.0044 | YES |
| `composition_shape` | `structure_numeric` | 0.0625 | 0.0019 | YES |
| `capability_map` | `structure_numeric` | 0.0606 | 0.0025 | YES |
| `provenance_shape` | `structure_numeric` | 0.0569 | 0.0011 | YES |
| `scalar_observers` | `symmetry_record` | 0.0536 | 0.0040 | YES |
| `provenance_shape` | `symmetry_record` | 0.0507 | 0.0019 | YES |
| `availability_state` | `capability_map` | 0.0297 | 0.0025 | YES |
| `scalar_observers` | `structure_numeric` | 0.0233 | 0.0022 | YES |
| `availability_state` | `structure_topology` | 0.0124 | 0.0029 | YES |
| `availability_state` | `composition_shape` | 0.0070 | 0.0021 | YES |
| `availability_state` | `structure_numeric` | 0.0032 | 0.0015 | YES |
| `availability_state` | `symmetry_record` | 0.0026 | 0.0031 | no |
| `availability_state` | `scalar_observers` | 0.0014 | 0.0030 | no |
| `availability_state` | `provenance_shape` | 0.0009 | 0.0012 | no |

## Strong observable-level relations

| Observable A | Observable B | r |
|---|---|---:|
| `band_gap__MISSING` | `has_props.electronic_structure` | -1.00000 |
| `formation_energy_per_atom__MISSING` | `has_props.thermo` | -1.00000 |
| `structure.leaves` | `structure.sites[].abc[].count` | 0.99926 |
| `structure.lattice.matrix[][].mean` | `structure.sites[].xyz[].mean` | 0.98279 |
| `composition.entropy` | `composition.l2` | -0.98061 |
| `structure.list_size_std` | `structure.sites[].abc[].count` | 0.96680 |
| `composition.max_share` | `composition.l2` | 0.96673 |
| `structure.leaves` | `structure.list_size_std` | 0.96495 |
| `structure.dict_size_std` | `structure.list_size_mean` | -0.94036 |
| `structure.lattice.matrix[][].min` | `structure.sites[].xyz[].min` | 0.91383 |
| `composition.entropy` | `composition.max_share` | -0.90956 |
| `structure.sites[].abc[].mean` | `structure.sites[].abc[].max` | 0.90759 |
| `composition.key_count` | `composition.entropy` | 0.90728 |

Зависимость выше Null не означает механизм. Она только показывает, что два Observer-блока организационно согласованы сильнее случайного row alignment.

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
