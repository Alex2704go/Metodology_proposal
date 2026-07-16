# Checkpoint — Observer Audit

- Blocks: **7**
- Block pairs: **21**
- Observable pairs with |r| ≥ 0.90 shown: **32**

## Block dependence

| Block A | Block B | RV | Null q95 | Above null? |
|---|---|---:|---:|---|
| `composition_shape` | `structure_topology` | 0.4599 | 0.0014 | YES |
| `capability_map` | `provenance_shape` | 0.3553 | 0.0015 | YES |
| `capability_map` | `composition_shape` | 0.2736 | 0.0023 | YES |
| `provenance_shape` | `structure_topology` | 0.2260 | 0.0011 | YES |
| `composition_shape` | `provenance_shape` | 0.2242 | 0.0011 | YES |
| `capability_map` | `structure_topology` | 0.2007 | 0.0023 | YES |
| `structure_numeric` | `structure_topology` | 0.1958 | 0.0015 | YES |
| `composition_shape` | `scalar_observers` | 0.1114 | 0.0021 | YES |
| `scalar_observers` | `structure_topology` | 0.1083 | 0.0017 | YES |
| `composition_shape` | `structure_numeric` | 0.0979 | 0.0018 | YES |
| `structure_numeric` | `symmetry_record` | 0.0948 | 0.0030 | YES |
| `composition_shape` | `symmetry_record` | 0.0906 | 0.0034 | YES |
| `structure_topology` | `symmetry_record` | 0.0865 | 0.0025 | YES |
| `capability_map` | `scalar_observers` | 0.0768 | 0.0026 | YES |
| `provenance_shape` | `scalar_observers` | 0.0759 | 0.0017 | YES |
| `capability_map` | `symmetry_record` | 0.0693 | 0.0047 | YES |
| `capability_map` | `structure_numeric` | 0.0606 | 0.0023 | YES |
| `provenance_shape` | `structure_numeric` | 0.0569 | 0.0012 | YES |
| `scalar_observers` | `symmetry_record` | 0.0543 | 0.0040 | YES |
| `provenance_shape` | `symmetry_record` | 0.0507 | 0.0020 | YES |
| `scalar_observers` | `structure_numeric` | 0.0233 | 0.0021 | YES |

## Strong observable-level relations

| Observable A | Observable B | r |
|---|---|---:|
| `composition.total` | `structure.object_nodes` | 1.00000 |
| `composition.total` | `structure.list_nodes` | 1.00000 |
| `structure.object_nodes` | `structure.list_nodes` | 1.00000 |
| `is_magnetic==False` | `is_magnetic==True` | -1.00000 |
| `composition.total` | `structure.sites[].abc[].count` | 1.00000 |
| `structure.object_nodes` | `structure.sites[].abc[].count` | 1.00000 |
| `structure.list_nodes` | `structure.sites[].abc[].count` | 1.00000 |
| `band_gap__MISSING` | `has_props.electronic_structure` | -1.00000 |
| `formation_energy_per_atom__MISSING` | `has_props.thermo` | -1.00000 |
| `structure.object_nodes` | `structure.list_size_max` | 0.99986 |
| `structure.list_nodes` | `structure.list_size_max` | 0.99986 |
| `structure.list_size_max` | `structure.sites[].abc[].count` | 0.99986 |
| `composition.total` | `structure.list_size_max` | 0.99986 |
| `structure.leaves` | `structure.object_nodes` | 0.99926 |
| `structure.leaves` | `structure.list_nodes` | 0.99926 |
| `composition.total` | `structure.leaves` | 0.99926 |
| `structure.leaves` | `structure.sites[].abc[].count` | 0.99926 |
| `structure.leaves` | `structure.list_size_max` | 0.99917 |
| `structure.lattice.matrix[][].mean` | `structure.sites[].xyz[].mean` | 0.98279 |
| `composition.entropy` | `composition.l2` | -0.98061 |
| `structure.object_nodes` | `structure.list_size_std` | 0.96680 |
| `structure.list_nodes` | `structure.list_size_std` | 0.96680 |
| `composition.total` | `structure.list_size_std` | 0.96680 |
| `structure.list_size_std` | `structure.sites[].abc[].count` | 0.96680 |
| `composition.max_share` | `composition.l2` | 0.96673 |
| `structure.list_size_std` | `structure.list_size_max` | 0.96524 |
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
