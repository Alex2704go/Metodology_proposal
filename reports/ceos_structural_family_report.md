# CEOS Structural Representation Families — v0.2

## Status

Stages 00–04 completed for the 3,000-object pilot. The literature/interpretation gate remains locked.

The admitted result is narrower and more precise than a general classification of materials:

```text
CEOS Structural Representation Families
```

The family partition is generated primarily by the generic Structure CompositeBuilder. It is not a classification by material names, formulas, published classes, or element identity.

## Data

- Source: Materials Project summary API.
- API version: `0.87.2.dev4+g6bd8ed856`.
- Pilot size: 3,000 objects.
- Sampling: deterministic stratified cluster-window pilot.
- Strata by `nelements`: 300 / 900 / 900 / 900.
- Seed: `420042`.
- Raw and sidecar files are immutable and checksum-controlled.
- Material names, formulas, source IDs and element identities were excluded from family organizational observables.

## Architecture used

```text
Raw World
    ↓
Representation Ecology
    ↓
Object Census
    ↓
Object Typing
    ↓
Builder Dispatch
    ↓
Builder Admission
    ↓
Organizational Observables
    ↓
Observer Ecology
    ↓
Targeted Null Ladder
    ↓
Admission
    ↓
Frozen Partition
    ↓
Cross Mapping
    ↓
Interpretation
```

The full claim-control contract is recorded in `CEOS_ARCHITECTURE.md`.

### Primary view: ORGANIZATION

Blocks:

- `composition_shape`
- `structure_topology`
- `structure_numeric`
- `symmetry_record`

Retained dimensions: 75.

### Confirmation view: OBSERVER_AUGMENTED

Adds neutral scalar Observer fields. Retained dimensions: 84.

### Control view: FULL_REPRESENTATION

Adds capability, provenance and availability. This view is retained as a map of the representation language, not as the primary material-family decision.

## Scientific vocabulary

The scientific term is **organizational observable** or **representation observable**. The word `feature` is retained only in internal software keys such as `feature_names` for compatibility with existing array formats.

## Builder Admission

Builder is an independently audited CEOS object.

```text
Builder Admission

✓ field permutation
✓ replay exact
✓ no ID leakage
✓ frozen preprocessing
✓ deterministic transform
✓ nested object permutation
✓ key-order permutation
✓ serialization audit
```

Every registered invariance test now has raw and scaled maximum error **0.0**. The first admission attempt failed at approximately `10⁻¹⁵` because floating-point accumulation depended on key order. That run was rejected; aggregation was canonicalized and every downstream stage was recomputed.

Full gate: `reports/BUILDER_ADMISSION.md`.

## Quality-control history

### Vector checkpoint

- Initial automatic organizational observables: 163.
- Final v0.2 retained organizational observables: 105 across all blocks.
- Non-finite values after processing: 0.
- Duplicate complete vectors: 0.
- Material-ID leakage: absent.
- Formula leakage: absent.
- Object-ID leakage: absent.
- Element-identity observables: absent.

The first audit detected duplicated size counters and perfect coupling between scalar missingness and `has_props`. Before clustering, v0.2 separated missingness into `availability_state`, removed within-block correlations at `|r| ≥ 0.995`, dropped binary one-hot complements and excluded `composition.total` as a cross-block size duplicate.

### Observer checkpoint

Strongest organizational relations after revision:

- capability ↔ provenance;
- composition shape ↔ structure topology;
- capability ↔ composition/structure.

These exceed row-permutation Nulls but are not interpreted as mechanisms.

### Family stability

Primary ORGANIZATION result:

- selected families: 4;
- silhouette: 0.2185;
- bootstrap mean ARI: 0.9796;
- all-column-shuffle q95: 0.1430;
- observed minus Null q95: +0.0755;
- minimum family size: 217.

Family sizes:

| Family | Objects |
|---|---:|
| F-001 | 1,520 |
| F-002 | 608 |
| F-003 | 655 |
| F-004 | 217 |

Confirmation OBSERVER_AUGMENTED result:

- selected families: 4;
- bootstrap mean ARI: 0.9701;
- agreement with ORGANIZATION: ARI 0.9945.

FULL_REPRESENTATION agreement with ORGANIZATION is only ARI 0.5198. Capability-block permutation does not reduce its clustering quality below the observed result. This supports keeping the capability/provenance layer separate from the structural-family claim.

## Directed Null Ladder

For ORGANIZATION:

| Null | Attacked object | Null q95 | Observed − q95 |
|---|---|---:|---:|
| ALL_COLUMN_SHUFFLE | all cross-observable organization | 0.1430 | +0.0755 |
| COMPOSITION_BLOCK_PERMUTE | composition alignment | 0.2111 | +0.0074 |
| STRUCTURE_BLOCK_PERMUTE | structure alignment | 0.2039 | +0.0147 |
| SYMMETRY_BLOCK_PERMUTE | symmetry alignment | 0.2135 | +0.0050 |

All registered ORGANIZATION Nulls reduce the observed silhouette. Structure permutation produces the largest block-specific reduction.

## Tested claim: Structure dominance

```text
Claim
    The current family partition is Structure-dominated.

Support
    Remove structure
        ↓
    ARI 0.0775

    Remove composition
        ↓
    ARI 0.9871

    Remove symmetry
        ↓
    ARI 0.9814
```

| Test | ARI against primary partition |
|---|---:|
| Remove composition | 0.9871 |
| Remove symmetry | 0.9814 |
| Remove structure | 0.0775 |

The claim is admitted at the level supported by this ablation:

```text
These are structural representation families.
```

They are not recoverable without the Structure Builder. Composition and symmetry refine the partition but do not define it.

Sampling-axis checks:

- NMI with registered sampling stratum: 0.1183;
- NMI with `nelements`: 0.1146;
- NMI with source crystal-system value: 0.1803.

The partition is not simply a restatement of the pilot quotas or one existing categorical field.

## Real-material out-of-sample classification

Exact-formula matches can contain multiple records. To avoid selecting an expected known phase, the record was chosen before content inspection by the deterministic rule:

```text
minimum material_id among exact-formula matches
```

| Formula | Selected record | Structural family | Margin | Training-distance percentile | Observer-view confirmation |
|---|---|---|---:|---:|---|
| FeS | `mp-aaaaadct` | **F-001** | 0.166 | 79.5% | yes |
| NaCl | `mp-aaaabhux` | **F-004** | 0.487 | 51.3% | yes |
| SiO₂ | `mp-aaaaakgg` | **F-001** | 0.337 | 53.8% | yes |
| SrTiO₃ | `mp-aaaaagwx` | **F-002** | 0.445 | 34.6% | yes |

No example is flagged out of distribution. All four assignments agree between ORGANIZATION and OBSERVER_AUGMENTED.

The margin compares the two nearest centroids and is not a probability. The percentile compares each example’s nearest-centroid distance with training-object distances.

### Important polymorph warning

The classification applies to a specific Materials Project record, not to a formula in the abstract. FeS, NaCl, SiO₂ and SrTiO₃ each have multiple records or structures. A different record with the same formula may belong to another CEOS structural family.

## Independent 1,000-object stress pool

Two additional records were selected blindly from an unseen API window:

- maximum distance to every frozen centroid;
- minimum margin between the two nearest centroids.

| Selector | Formula revealed after selection | Result |
|---|---|---|
| DISTANT_OBJECT | B₁₀H₁₄C₁₀S(OF₂)₃ | OOD 99.9%; nearest F-002, hard admission withheld |
| BOUNDARY_OBJECT | LiMnVF₆ | margin 0.0133; nearest F-001, hard assignment ambiguous |

This validates a necessary distinction:

```text
nearest centroid ≠ admitted family membership
```

“Most” refers only to the preregistered 1,000-object pool, not the full Materials Project.

## Assignment Evidence and Admission State

Every object now receives a versioned evidence passport rather than a single nearest-centroid label.

| Formula | Nearest family | Admissible family | Admission State | Evidence Weight |
|---|---|---|---|---:|
| FeS | F-001 | F-001 | ADMITTED | 4/4 |
| NaCl | F-004 | F-004 | ADMITTED | 4/4 |
| SiO₂ | F-001 | F-001 | ADMITTED | 4/4 |
| SrTiO₃ | F-002 | F-002 | ADMITTED | 4/4 |
| B₁₀H₁₄C₁₀S(OF₂)₃ | F-002 | WITHHELD | OOD | 2.5/4 |
| LiMnVF₆ | F-001 | WITHHELD | BOUNDARY | 3/4 |

Evidence axes are Builder confidence, cross-view agreement, in-distribution support and margin. Evidence Weight is a transparent summary, not a probability and not a substitute for state precedence.

Admission State belongs to:

```text
Object × Frozen Partition × Builder Version × Evidence Protocol × Current Checks
```

It may change as evidence or the reference WORLD changes. Previous passports are preserved rather than overwritten.

## Assignment Explanation

The two withheld assignments were decomposed by channel, local density and targeted scale Nulls.

### B₁₀H₁₄C₁₀S(OF₂)₃

- composition percentile: 99.3%;
- structure percentile: 99.7%;
- symmetry percentile: 33.3%;
- k=25 radius percentile: 99.5%;
- one scale-observable-removal Null removes OOD;
- structure unit normalization does not remove OOD.

Admitted wording: **scale-sensitive multi-channel OOD**, not scale-driven.

### LiMnVF₆

- structure favors F-001;
- composition and symmetry favor F-003;
- global centroid favors F-001;
- 18 of 25 local neighbors belong to F-003;
- unit-normalizing structure flips nearest family to F-003 but leaves the object Boundary.

The evidence supports a conflict between organizational channels and between global-centroid and local-density geometry. It does not yet prove that one specific material observable is missing.

## Conflict Topology population test

Conflict Topology was evaluated across all 3,000 training objects with six nodes: Global, Local, Composition, Structure, Symmetry and Observer.

- low-margin objects: 52;
- low-margin global-OOD objects excluded by state precedence: 4;
- Admission-State Boundary objects: 48;
- relational multi-axis Boundary objects: 8;
- mean conflict excess over non-Boundary: 0.100;
- Packet-Alignment Null q95: 0.039;
- multi-axis conflict odds ratio: 30.87;
- Fisher exact p: 4.14×10⁻⁹.

The global Boundary rate remains inside the representation-block Conflict Null interval. Therefore Boundary as a whole is not admitted as a relational class. `RELATIONAL_BOUNDARY` is supported as a separate candidate organizational subtype.

Population Support PASS means that this Relation Pattern is supported in the analyzed sample under the registered methodology. It is not evidence of a physical mechanism, phase boundary or classical material category.

LiMnVF₆ has the family-label-invariant topology:

```text
{Global, Structure}
{Local, Composition, Symmetry}
{Observer}
```

No physical phase-boundary or mechanism claim is made.

## Relation Pattern Registry and Interpretation Boundary

Canonical family-label-invariant signatures are now assigned stable content-derived IDs. The current registry contains 52 patterns covering all 3,000 training objects.

- LiMnVF₆: `RP-6E1BC31651` = `{G,S}|{L,C,Y}|{O}`;
- B₁₀H₁₄C₁₀S(OF₂)₃: `RP-E5A71975A5` = `{G,L,C,S}|{Y,O}`.

Assignment Passport v0.2 stores two orthogonal axes:

```text
Admission State × Relation Pattern
```

and a mandatory Interpretation Boundary:

```text
Supports:
    registered organizational claim within current WORLD

Does not support:
    physical mechanism
    thermodynamic phase
    microscopic Hamiltonian
    causal explanation
    universal validity outside current WORLD
```

Literature Cross Mapping remains LOCKED. Its contract is many-to-many: `Classical Term ↔ Frozen Family × Relation Pattern × Admission Context`.

Mapping Stability is tracked separately across one WORLD, multiple WORLDs, independent datasets and independent Observers. Maturity is monotonic (`NOT_TESTED → SINGLE_WORLD → MULTI_WORLD → INDEPENDENTLY_REPLICATED`); `FAILED` is a Qualification Outcome, not a maturity level. No mapping currently inherits evidence from either vocabulary.

Every mapping must also declare Direction and Mapping Provenance. Mapping Strength and Evidence Strength remain independent fields.

```text
Cross Mapping translates between vocabularies.
It does not transfer evidence.

Vocabulary correspondence ≠ evidence inheritance.
```

Every claim-bearing CEOS document now requires a machine-linted Interpretation Boundary, including an explicit prohibition on prediction of untested properties and the Principle Box `Vocabulary correspondence ≠ evidence inheritance`. Current document corpus: 66 documents, 330/330 structural contract checks PASS. Scientific Null Ladder and Governance Null Ladder are separate non-substitutable modules. Governance v0.2 acts as a qualified claim-compiler candidate: it checks whether a claim package may exist under CEOS, not whether the scientific conclusion is true. Semantic enforcement remains `REASSESSMENT_REQUIRED` after the contradictory-boundary System Null breach.

The initial executable Claim Type System suite passed 17/17 synthetic transition tests, and the Cross Mapping Passport schema passed 11/11 conformance checks. A subsequent adversarial System Null Ladder showed that these were syntactic/self-consistency checks rather than proof-carrying enforcement: all 16 registered invalid attacks exposed specification gaps or unprotected transitions in v0.1 while both controls passed. Governance v0.1 is therefore `REASSESSMENT_REQUIRED`. A proof-carrying v0.2 candidate with derived lifecycle state, content-addressed evidence, identity registries and claim DAG rejected all 16 unchanged attacks with controls 2/2. A later compound-shell failure exposed a new fail-fast Governance Null; v0.2.1 adds a single `set -euo pipefail` integrity entrypoint and rejects 17/17 currently registered attacks. Its status remains only `QUALIFIED`, not `ADMITTED`, pending independent Red Team review. No real Cross Mapping had been admitted.

## Projection replay check

The out-of-sample transformer was required to reproduce all 3,000 training vectors before accepting any example assignment.

- Raw-vector maximum absolute replay error: 0.0.
- Scaled-vector maximum absolute replay error: 0.0.

An initial projection attempt failed this test because imputation medians were accidentally refitted after adding four objects. The run was rejected. The transformer was corrected to use frozen training medians, after which exact replay passed.

## Integrity checkpoint

- All Python scripts compile.
- All JSON artifacts parse.
- All numeric NPZ arrays are finite.
- All registered raw checksums pass.
- Persisted API-key occurrences: 0.

## Interpretation lock

No literature family names have been assigned. The neutral labels remain:

```text
F-001
F-002
F-003
F-004
```

The next permissible step is Stage 05 Cross Mapping, where these families may be compared post hoc with classical structural categories. The CEOS partition must remain fixed during that comparison.

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
