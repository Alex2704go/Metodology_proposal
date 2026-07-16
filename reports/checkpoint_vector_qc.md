# Checkpoint — WORLD Vector QC

- Objects: **3000**
- Candidate organizational observables: **163**
- Retained organizational observables: **110**
- Non-finite values after processing: **0**
- Duplicate vector rows beyond first: **0**

## Blocks

- `capability_map`: 18
- `composition_shape`: 12
- `provenance_shape`: 1
- `scalar_observers`: 12
- `structure_numeric`: 20
- `structure_topology`: 8
- `symmetry_record`: 39

## Leakage checks

- `material_id_present`: **False**
- `formula_present`: **False**
- `object_id_present`: **False**
- `element_identity_features`: **False**

## Removed exact duplicates

- `composition.sorted_share_1` = `composition.max_share`
- `structure.lattice.a.min` = `structure.lattice.a.mean`
- `structure.lattice.a.max` = `structure.lattice.a.mean`
- `structure.lattice.alpha.min` = `structure.lattice.alpha.mean`
- `structure.lattice.alpha.max` = `structure.lattice.alpha.mean`
- `structure.lattice.b.min` = `structure.lattice.b.mean`
- `structure.lattice.b.max` = `structure.lattice.b.mean`
- `structure.lattice.beta.min` = `structure.lattice.beta.mean`
- `structure.lattice.beta.max` = `structure.lattice.beta.mean`
- `structure.lattice.c.min` = `structure.lattice.c.mean`
- `structure.lattice.c.max` = `structure.lattice.c.mean`
- `structure.lattice.gamma.min` = `structure.lattice.gamma.mean`
- `structure.lattice.gamma.max` = `structure.lattice.gamma.mean`
- `structure.lattice.volume.min` = `structure.lattice.volume.mean`
- `structure.lattice.volume.max` = `structure.lattice.volume.mean`
- `structure.sites[].species[].occu.count` = `composition.total`
- `structure.sites[].xyz[].count` = `structure.sites[].abc[].count`
- `volume` = `structure.lattice.volume.mean`
- `nelements` = `composition.key_count`

## Removed constants

- `structure.depth`
- `structure.charge.count`
- `structure.charge.mean`
- `structure.charge.std`
- `structure.charge.min`
- `structure.charge.max`
- `structure.lattice.a.count`
- `structure.lattice.a.std`
- `structure.lattice.alpha.count`
- `structure.lattice.alpha.std`
- `structure.lattice.b.count`
- `structure.lattice.b.std`
- `structure.lattice.beta.count`
- `structure.lattice.beta.std`
- `structure.lattice.c.count`
- `structure.lattice.c.std`
- `structure.lattice.gamma.count`
- `structure.lattice.gamma.std`
- `structure.lattice.matrix[][].count`
- `structure.lattice.volume.count`
- `structure.lattice.volume.std`
- `structure.sites[].species[].occu.mean`
- `structure.sites[].species[].occu.std`
- `structure.sites[].species[].occu.min`
- `structure.sites[].species[].occu.max`
- `symmetry.angle_tolerance`
- `symmetry.symprec`
- `has_props.chemenv`
- `has_props.magnetism`
- `has_props.materials`
- `has_props.oxi_states`
- `origins.keyset_variants`
- `builder_meta.slot_count`
- `builder_meta.populated`

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
