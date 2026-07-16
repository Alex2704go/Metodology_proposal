# Six-material CEOS Stress Test

Two additional records were selected from 1,000 unseen API objects without loading formulas or source IDs.

“Most distant” and “most boundary-like” mean **within the preregistered 1,000-object stress pool**, not within the entire Materials Project.

## Audit checks

```text
✓ Builder Admission active
✓ independent API pool
✓ no overlap with training or previous examples
✓ formula absent during selection
✓ source ID absent during selection
✓ frozen preprocessing
✓ training replay raw = 0.0
✓ training replay scaled = 0.0
✓ deterministic blind selection exact
```

## Summary

| Role | Formula | Record | Result | Margin | Training-distance percentile | Cross-view |
|---|---|---|---|---:|---:|---|
| Standard | FeS | `mp-aaaaadct` | **F-001** | 0.1659 | 79.5% | YES |
| Standard | NaCl | `mp-aaaabhux` | **F-004** | 0.4873 | 51.3% | YES |
| Standard | SiO2 | `mp-aaaaakgg` | **F-001** | 0.3371 | 53.8% | YES |
| Standard | SrTiO3 | `mp-aaaaagwx` | **F-002** | 0.4451 | 34.6% | YES |
| DISTANT_OBJECT | B10H14C10S(OF2)3 | `mp-aaacpzld` | **nearest F-002; OOD** | 0.0581 | 99.9% | YES |
| BOUNDARY_OBJECT | LiMnVF6 | `mp-aaacpxpm` | **nearest F-001; BOUNDARY** | 0.0133 | 96.2% | YES |

## DISTANT_OBJECT: B10H14C10S(OF2)3

- Record: `mp-aaacpzld`
- Status: **OOD — nearest family reported, hard admission withheld**
- Nearest structural family: **F-002**
- composition: MAP with 6 keys
- structure: COMPOSITE depth 5, leaves 1782, object nodes 531, list nodes 534
- symmetry cross-map: Monoclinic / #14
- active representation capabilities: 7
- origins length: 4

## BOUNDARY_OBJECT: LiMnVF6

- Record: `mp-aaacpxpm`
- Status: **BOUNDARY — nearest family reported, hard admission ambiguous**
- Nearest structural family: **F-001**
- composition: MAP with 4 keys
- structure: COMPOSITE depth 5, leaves 265, object nodes 84, list nodes 87
- symmetry cross-map: Trigonal / #150
- active representation capabilities: 9
- origins length: 5

## Admission reading

- An OOD object may have a nearest centroid, but nearest is not equivalent to admitted membership.
- A boundary object may have a numerical nearest family while remaining classification-ambiguous.
- The four standard examples remain hard assignments because they are in-distribution and cross-view confirmed.
- Formula names were opened only after the blind selectors had been frozen.

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
