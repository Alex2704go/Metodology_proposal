# Assignment Evidence Passports v0.2

`nearest_family` is geometric. `admissible_family` is epistemic and is populated only for `ADMITTED`. Admission State and Relation Pattern are orthogonal.

| Formula | Nearest | Admissible | Knowledge State | Builder | Cross-view | Distribution | Margin | Evidence Weight |
|---|---|---|---|---|---|---|---|---:|
| FeS | F-001 | F-001 | **ADMITTED :: RELATION_PATTERN_NOT_EVALUATED** | ✅ | ✅ | ✅ | ✅ 0.1659 | **4/4** |
| NaCl | F-004 | F-004 | **ADMITTED :: RELATION_PATTERN_NOT_EVALUATED** | ✅ | ✅ | ✅ | ✅ 0.4873 | **4/4** |
| SiO2 | F-001 | F-001 | **ADMITTED :: RELATION_PATTERN_NOT_EVALUATED** | ✅ | ✅ | ✅ | ✅ 0.3371 | **4/4** |
| SrTiO3 | F-002 | F-002 | **ADMITTED :: RELATION_PATTERN_NOT_EVALUATED** | ✅ | ✅ | ✅ | ✅ 0.4451 | **4/4** |
| B10H14C10S(OF2)3 | F-002 | WITHHELD | **OOD :: RP-E5A71975A5** | ✅ | ✅ | ❌ | ⚠️ 0.0581 | **2.5/4** |
| LiMnVF6 | F-001 | WITHHELD | **BOUNDARY :: RELATIONAL_BOUNDARY** | ✅ | ✅ | ✅ | ❌ 0.0133 | **3/4** |

## FeS — ADMITTED

```text
Nearest:   F-001
Admission: F-001
Evidence:  4/4
```

**Interpretation Boundary**

Supports: structural representation family assignment under frozen partition v0.2.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## NaCl — ADMITTED

```text
Nearest:   F-004
Admission: F-004
Evidence:  4/4
```

**Interpretation Boundary**

Supports: structural representation family assignment under frozen partition v0.2.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## SiO2 — ADMITTED

```text
Nearest:   F-001
Admission: F-001
Evidence:  4/4
```

**Interpretation Boundary**

Supports: structural representation family assignment under frozen partition v0.2.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## SrTiO3 — ADMITTED

```text
Nearest:   F-002
Admission: F-002
Evidence:  4/4
```

**Interpretation Boundary**

Supports: structural representation family assignment under frozen partition v0.2.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## B10H14C10S(OF2)3 — OOD

```text
Nearest:   F-002
Admission: WITHHELD
Evidence:  2.5/4
```
Reason: Distance percentile exceeds registered training support

**Interpretation Boundary**

Supports: valid frozen transform, global out-of-distribution diagnosis relative to current WORLD, nearest-family geometry without membership admission, family-label-invariant relation signature RP-E5A71975A5 under conflict_topology_v0.3.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## LiMnVF6 — BOUNDARY

```text
Nearest:   F-001
Admission: WITHHELD
Evidence:  3/4
```
Reason: Nearest and second-nearest families are insufficiently separated

**Interpretation Boundary**

Supports: valid in-support transform, withheld hard assignment due registered low-margin boundary state, family-label-invariant relation signature RP-6E1BC31651 under conflict_topology_v0.3, population-supported organizational pattern RELATIONAL_BOUNDARY within analyzed sample and methodology.
Does not support: physical mechanism, thermodynamic phase, microscopic Hamiltonian, causal explanation, prediction of untested properties, classical material category, universal validity outside current WORLD.
Literature mapping: **LOCKED**.

## State semantics

- **ADMITTED:** all four axes pass.
- **CANDIDATE:** valid but incomplete or warning-level evidence.
- **BOUNDARY:** in-distribution but insufficient family separation.
- **OOD:** valid transform outside registered support.
- **REJECTED:** upstream evidence chain invalid.

Evidence Weight is not a probability and cannot override state precedence.

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
