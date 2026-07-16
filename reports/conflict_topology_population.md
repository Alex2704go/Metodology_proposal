# Conflict Topology — Population Test

## Operational definition

```text
RELATIONAL_BOUNDARY =
    Builder valid
    AND exact frozen replay
    AND global representation in-support
    AND global margin < 0.05
    AND Global family ≠ Local family
    AND at least two of {Composition, Structure, Symmetry}
        support a family different from Global
```

Channel-specific OOD remains a recorded node attribute; only global OOD changes the Assignment State from BOUNDARY to OOD.

## Meaning of Population Support PASS

PASS means that this organizational relation pattern is supported in the analyzed sample under the registered methodology and exceeds its targeted Conflict Null criteria. It is not evidence for a physical mechanism, thermodynamic phase boundary, or classical material category.

```text
No physical phase-boundary or mechanism claim is made.
```

## Population result

- Training objects: **3000**
- Global low-margin objects: **52**
- Low-margin objects with global OOD state: **4**
- Admission-State BOUNDARY objects: **48** (1.60%)
- Mean pairwise conflict, Boundary: **0.569**
- Mean pairwise conflict, non-Boundary: **0.470**
- Observed difference: **0.100**
- Packet-Alignment Null q95: **0.039**
- Multi-axis conflict odds ratio: **30.87**
- Fisher exact p: **4.14e-09**
- Relational Boundaries: **8 / 48**
- Population support criterion: **PASS**

## Representation Block Alignment Null

| Statistic | Value |
|---|---:|
| Observed Boundary rate | 0.0160 |
| Conflict Null mean | 0.0155 |
| Conflict Null q05–q95 | 0.0138–0.0177 |

## Selected stress topologies

### LiMnVF6

- Signature: `{G,S}|{L,C,Y}|{O}`
- Boundary: **True**
- Pairwise conflict fraction: **0.733**
- Global/local disagreement: **True**
- Multi-axis conflict: **True**

| Node | Family | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| global | F-001 | 0.013 | 96.2% | no |
| local | F-003 | 0.440 | 96.9% | no |
| composition | F-003 | 0.008 | 76.4% | no |
| structure | F-001 | 0.027 | 94.6% | no |
| symmetry | F-003 | 0.026 | 99.2% | YES |
| observer | F-002 | 0.006 | 74.5% | no |
### B10H14C10S(OF2)3

- Signature: `{G,L,C,S}|{Y,O}`
- Boundary: **False**
- Pairwise conflict fraction: **0.533**
- Global/local disagreement: **False**
- Multi-axis conflict: **False**

| Node | Family | Margin | Percentile | OOD |
|---|---|---:|---:|---|
| global | F-002 | 0.058 | 99.9% | YES |
| local | F-002 | 0.040 | 99.5% | YES |
| composition | F-002 | 0.017 | 99.3% | YES |
| structure | F-002 | 0.069 | 99.7% | YES |
| symmetry | F-003 | 0.104 | 33.3% | no |
| observer | F-003 | 0.004 | 87.8% | no |

## Admission reading

A PASS supports `RELATIONAL_BOUNDARY` as a population-level candidate organizational subtype. It does not convert Boundary into a physical phase category. A FAIL means the LiMnVF₆ motif remains an individual anatomy rather than a supported class.

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
