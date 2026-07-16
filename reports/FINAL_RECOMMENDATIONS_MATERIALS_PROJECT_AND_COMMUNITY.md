# Recommendations for Materials Project, Agent-Ready Materials APIs, and Scientific Reporting

## Executive summary

The MaterialsWorld pilot suggests that Materials Project could become easier to use—especially for automated agents—by documenting not only individual fields, but the organization of its representation language.

The recommendations are not framed as database corrections. Materials Project already exposes a rich and highly useful `SummaryDoc`. The proposed next step is to make its representation contracts more explicit, typed, versioned and reproducible.

The central recommendations are:

1. publish a machine-readable **Representation Passport** separating Content, Identity, Metadata and Representation;
2. document nested fields through multidimensional **Object Signatures** rather than only JSON runtime types;
3. expose a **Representation Ecology / Graph** for the complete document language;
4. treat `has_props` as a first-class **Capability Passport** describing representation availability;
5. consolidate provenance and Builder information into a replay-oriented **Builder Passport**;
6. support deterministic transforms, snapshot identity and compatibility declarations for AI agents;
7. encourage scientific publications to include a **Result Passport** and an explicit **Interpretation Boundary**;
8. distinguish nearest organizational correspondence from admitted or independently replicated mapping.

These proposals are based on a 3,000-record pilot and should be treated as design suggestions, not universal conclusions about the full Materials Project corpus.

---

# Part I — Recommendations for Materials Project

## 1. Representation Passport

### Motivation

`SummaryDoc` combines several different semantic roles. A human reader can often infer them, but an automated agent must currently rely heavily on field names and domain assumptions.

A machine-readable passport could distinguish:

```text
SummaryDoc
    ├── Content
    ├── Representation
    ├── Identity
    └── Metadata
```

### Proposed roles

#### Content

Values intended to describe the represented material record, such as composition- or structure-derived content.

#### Representation

The containers, schemas, coordinate systems, key grammars and availability states through which content is expressed.

#### Identity

Stable record identifiers, source keys, version identifiers and immutable snapshot references. Identity should remain explicitly separate from analytical observables.

#### Metadata

Provenance, Builder versions, timestamps, compatibility information and processing lineage.

### Example

```yaml
representation_passport:
  schema_version: mp-summary-representation-v1
  snapshot_id: ...

  roles:
    identity:
      - material_id

    content:
      - composition
      - structure
      - symmetry
      - density
      - volume

    representation:
      - has_props

    metadata:
      - origins
      - builder_meta
```

The exact role assignments should be defined by Materials Project rather than inferred externally. The main recommendation is to expose the separation explicitly.

### Benefit

- fewer hidden assumptions for users;
- reduced risk of treating identifiers as scientific observables;
- easier schema evolution;
- safer automated feature/observable construction;
- clearer contracts for AI agents.

---

## 2. Nested Object Typing

### Motivation

JSON runtime types such as `object` and `array` do not capture the organizational contract of nested fields.

The pilot distinguished several derived representation classes:

| Field | Observed organization | Builder view |
|---|---|---|
| `composition` | open-key homogeneous object | MAP |
| `symmetry` | fixed-slot object | RECORD |
| `structure` | deep heterogeneous hierarchy | COMPOSITE / HIERARCHICAL |
| `has_props` | fixed boolean record with map interface | RECORD + MAP VIEW |
| `origins` | sequence of fixed records | LIST[RECORD] |
| `builder_meta` | fixed-slot object | RECORD |

### Important qualification

The current operational classifier did **not** admit `structure` as a recursive TREE. It identified a heterogeneous hierarchical composite. A future schema could describe tree-like views, but the API should avoid forcing one exclusive label when several organizational axes are relevant.

### Recommended Object Signature

```text
ObjectSignature =
    State
  × Container
  × KeyGrammar
  × ValueGrammar
  × Topology
  × Cardinality
```

### Example

```yaml
composition:
  container: OBJECT
  key_grammar: OPEN
  value_grammar: HOMOGENEOUS_NUMERIC
  topology: FLAT
  derived_views: [MAP]

symmetry:
  container: OBJECT
  key_grammar: FIXED
  value_grammar: SLOT_TYPED
  topology: FLAT
  derived_views: [RECORD]

structure:
  container: OBJECT
  key_grammar: FIXED
  value_grammar: HETEROGENEOUS
  topology: HIERARCHICAL_COMPOSITE
  recursive_tree_contract: false
  derived_views: [COMPOSITE, HIERARCHY]
```

### Benefit

- Builder dispatch can be based on type rather than field name;
- agents can select valid transformations automatically;
- API consumers can distinguish MAP operations from RECORD operations;
- schema compatibility becomes testable.

---

## 3. Representation Ecology and Representation Graph

### Motivation

Traditional API documentation describes fields independently. Rich scientific documents also have a language-level structure: fields depend on Builders, capability availability, nested objects and provenance.

A Representation Graph could make this explicit:

```text
SummaryDoc
    ↓
Representation Graph
    ├── Object nodes
    ├── Builder nodes
    ├── Capability nodes
    ├── Provenance nodes
    └── dependency / availability edges
```

### Suggested graph relations

- `BUILT_BY`;
- `DERIVED_FROM`;
- `AVAILABLE_IF`;
- `HAS_SCHEMA`;
- `COMPATIBLE_WITH`;
- `SUPERSEDES`;
- `IDENTIFIED_BY`;
- `PROVENANCE_FROM`.

### Possible delivery formats

- versioned JSON Schema extensions;
- a dedicated schema endpoint;
- JSON-LD or another typed graph format;
- downloadable schema snapshots;
- generated human documentation from the same source.

### Benefit

The representation language becomes inspectable as a system, not only as a list of fields.

---

## 4. Capability Passport for `has_props`

### Motivation

`has_props` is not simply another property of a material. It describes which representational capabilities are available for a record.

In the pilot it behaved as:

```text
fixed RECORD grammar
+
MAP-like capability interface
```

This makes it closer to a passport for the language’s available views than to an intrinsic material observable.

### Recommended separation

```yaml
capability_passport:
  schema_version: ...
  capability_keys:
    bandstructure:
      available: true
      producer: ...
      version: ...
      compatibility: ...

    elasticity:
      available: false
      reason: NOT_BUILT
```

Possible availability states should distinguish:

- available;
- not built;
- not applicable;
- failed;
- deprecated;
- unknown.

A boolean alone can collapse these different states.

### Evidence from the pilot

Capability and provenance formed a strong organizational layer distinct from the primary structural-family space. The full representation view agreed only moderately with the organization-only partition. This supports keeping representation availability separate from material-family claims.

### Benefit

- agents know which analyses are possible before requesting large objects;
- missing data are not confused with negative scientific values;
- capability evolution becomes versioned;
- provenance and availability can be audited separately.

---

## 5. Builder Transparency and Builder Passport

### Motivation

Materials Project already exposes useful provenance-related fields such as `builder_meta` and `origins`. These could be consolidated into a replay-oriented Builder Passport.

### Proposed Builder Passport

```yaml
builder_passport:
  builder_id: ...
  builder_version: ...
  code_digest: ...
  input_schema_version: ...
  output_schema_version: ...

  preprocessing:
    steps: [...]
    parameters: {...}
    fitted_on_snapshot: ...
    frozen: true

  provenance:
    input_artifact_ids: [...]
    parent_builder_ids: [...]

  compatibility:
    backward_compatible_with: [...]
    breaking_changes: [...]

  replay:
    deterministic: true
    expected_tolerance: 0.0
    reference_artifact: ...
```

### Replay recommendation

Where feasible, publish a small reference fixture and expected digest or numerical output. A consumer can then verify:

```text
same input
same Builder version
same preprocessing
    ↓
exact or declared-tolerance replay
```

### Benefit

- easier reproducibility;
- safer cached or federated data;
- explicit compatibility checks;
- stronger agent confidence;
- simpler debugging of historical records.

---

## 6. Preserve Representation States

The following states should remain distinguishable:

```text
NONE
EMPTY_LIST
EMPTY_MAP
PRESENT
NOT_BUILT
FAILED
NOT_APPLICABLE
UNKNOWN
```

They should not be silently normalized into one null representation.

This is particularly important for automated systems, which otherwise cannot distinguish absence of content from absence of processing.

---

## 7. Snapshot and Deterministic API Contracts

For reproducible agent workflows, consider publishing:

- immutable snapshot IDs;
- schema version and API version in every response;
- stable sorting and pagination contracts;
- query manifest serialization;
- content digests for downloadable snapshots;
- deprecation and compatibility metadata;
- explicit maximum-page and rate-limit contracts;
- machine-readable field-role and object-signature endpoints.

### Suggested endpoints

```text
/schemas/summary/{version}
/representation-passport/{version}
/builder-passports/{builder_id}/{version}
/capability-schema/{version}
/snapshots/{snapshot_id}/manifest
```

These are illustrative interfaces, not prescriptions for the existing API architecture.

---

## 8. Agent-Readiness Acceptance Tests

A future agent-ready contract could be tested through questions such as:

1. Can an agent distinguish Identity from Content without inferring from names?
2. Can it determine whether a nested object is MAP-, RECORD- or COMPOSITE-like?
3. Can it distinguish missing, empty, failed and not-applicable states?
4. Can it identify the Builder and schema version for a value?
5. Can it reproduce a reference transform within the declared tolerance?
6. Can it know which capabilities are available before downloading large nested objects?
7. Can it detect that an API schema change is breaking?
8. Can it construct a provenance manifest without domain-specific hard-coding?

---

# Part II — Recommendations for Scientific Reporting

## 9. Publish a Result Passport, Not Only a Result

A scientific result can be accompanied by a compact passport:

```text
Object
    ↓
Representation
    ↓
Builder
    ↓
Organizational Observables
    ↓
Scientific Null Ladder
    ↓
Admission State
    ↓
Transfer / Mapping Stability
    ↓
Interpretation Boundary
```

### Suggested fields

```yaml
result_passport:
  object_scope: ...
  representation_version: ...
  builder_id: ...
  provenance_refs: [...]
  organizational_observables: [...]

  null_ladder:
    registered_attacks: [...]
    survived: [...]
    failed: [...]

  admission:
    state: ...
    evidence_weight: ...
    withheld_reason: ...

  transfer:
    nearest_correspondence: ...
    admissible_correspondence: ...
    mapping_maturity: ...
    qualification_outcome: ...

  interpretation_boundary:
    supports: [...]
    does_not_support: [...]
```

This recommendation does not require adoption of CEOS terminology. It expresses a general transparency principle.

---

## 10. Distinguish Nearest Correspondence from Confirmed Correspondence

Scientific writing often compresses similarity into identity.

Instead of:

```text
This is SDW.
```

prefer a scoped statement such as:

```text
Under representation R and criteria C,
this object is organizationally nearest to the published SDW description.
The correspondence has maturity SINGLE_WORLD and does not transfer mechanism evidence.
```

Recommended distinctions:

```text
nearest correspondence
candidate mapping
admitted mapping
independently replicated mapping
```

A nearest match is geometric or descriptive. It is not automatically an ontological identity.

---

## 11. Separate Mapping Strength from Evidence Strength

```text
Mapping Strength ≠ Evidence Strength
```

A correspondence may be structurally strong but have no independent evidence for shared mechanism.

Every mapping should report both:

```yaml
mapping_strength: STRONG
evidence_strength: NONE
```

This combination is valid and informative.

---

## 12. Publish Mapping Provenance and Stability

### Mapping Provenance

```text
Constructed from:
    □ Family
    □ Relation Pattern
    □ Admission Context
    □ Population statistics
    □ Independent Observer agreement
```

### Mapping Stability

```text
Maturity:
    NOT_TESTED
    SINGLE_WORLD
    MULTI_WORLD
    INDEPENDENTLY_REPLICATED

Latest Qualification Outcome:
    NOT_RUN
    PASS
    MIXED
    FAILED
```

Maturity and outcome should remain separate. A new failed test should not erase the historical maturity record; it should trigger reassessment.

---

## 13. Make Interpretation Boundary Mandatory

Every claim-bearing result should state:

```text
Supports
    ...

Does not support
    ...
```

Recommended default questions:

- Does the result support an organizational pattern?
- Does it support family membership?
- Does it support a physical mechanism?
- Does it support a thermodynamic phase assignment?
- Does it support a microscopic Hamiltonian?
- Does it support causal explanation?
- Does it support prediction of untested properties?
- Does it generalize outside the analyzed population?

The mandatory principle is:

> **Vocabulary correspondence ≠ evidence inheritance.**

---

## 14. Publish Withheld and Negative States

Useful scientific outputs include:

- `BOUNDARY`;
- `OOD`;
- `CANDIDATE`;
- `REASSESSMENT_REQUIRED`;
- failed Nulls;
- unresolved representation types;
- conflicting Observer channels.

These should not be collapsed into miscellaneous uncertainty. They often reveal where the current language loses discriminability.

---

# Part III — Prioritized Development Path

## Low-cost, documentation-first

1. Publish field roles: Content / Representation / Identity / Metadata.
2. Document NONE / EMPTY / FAILED / NOT_APPLICABLE semantics.
3. Add Object Signature annotations to major nested fields.
4. Document `has_props` as representation availability.
5. Publish Builder version and compatibility descriptions.

## Medium-term, machine-readable

6. Versioned Representation Passport.
7. Capability Passport schema.
8. Builder Passport and replay fixture.
9. Immutable snapshot manifests and content digests.
10. Agent-readable Representation Graph.

## Longer-term, ecosystem-facing

11. Shared Result Passport conventions.
12. Mapping Provenance and Mapping Stability standards.
13. Machine-readable Interpretation Boundaries.
14. Cross-dataset schema and Builder compatibility tests.
15. Independent agent-readiness qualification suites.

---

# Evidence basis and limitations

## What the pilot supports

- nested API objects exhibit distinguishable organizational grammars;
- field-name-independent Builder dispatch is practical;
- capability/provenance forms a representation-language layer distinct from structural organization;
- exact replay and frozen preprocessing catch real pipeline errors;
- nearest-family geometry should be separated from admitted membership;
- explicit Interpretation Boundaries and provenance improve auditability.

## What the pilot does not support

- a claim that the full Materials Project has exactly the same distribution as the pilot;
- universal object classifications for every API version;
- a physical taxonomy of materials;
- a mechanism-level interpretation of the discovered families;
- a claim that Materials Project is defective;
- a claim that CEOS is the only suitable implementation of these recommendations.

## Sampling limitation

The analysis used a deterministic 3,000-record stratified cluster-window pilot rather than a uniform sample of the entire Materials Project. Family proportions are therefore not population estimates.

## Version limitation

Observed schemas and counts correspond to the recorded API version and extraction date. They should be rechecked against future versions.

---

# Closing recommendation

Materials Project is already valuable because it exposes a rich world of material records. The proposed evolution is to expose the organization of that world with the same clarity as its values:

```text
not only data
but representation contracts

not only fields
but object signatures

not only provenance fields
but replayable Builder passports

not only property availability
but capability semantics
```

For the scientific community, the analogous recommendation is:

```text
publish not only the result
but the lifecycle and boundary of the claim
```

This would make both human and agent-driven research easier to reproduce, qualify and interpret without transferring evidence through terminology alone.

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
