# Materials Project — One-Page Development Recommendations

## Goal

Make `SummaryDoc` easier to interpret, reproduce and use safely by humans and AI agents without changing its scientific content.

## Recommended additions

### 1. Representation Passport

Separate and document:

```text
Content | Representation | Identity | Metadata
```

Agents should not have to infer these roles from field names.

### 2. Nested Object Signatures

Publish machine-readable signatures for major nested fields:

```text
State × Container × KeyGrammar × ValueGrammar × Topology × Cardinality
```

Pilot examples:

- composition → MAP view;
- symmetry → RECORD;
- structure → HIERARCHICAL COMPOSITE;
- has_props → RECORD + MAP VIEW;
- origins → LIST[RECORD].

### 3. Representation Graph

Document relations among fields, Builders, capabilities and provenance:

```text
BUILT_BY | DERIVED_FROM | AVAILABLE_IF | COMPATIBLE_WITH | SUPERSEDES
```

### 4. Capability Passport

Treat `has_props` as representation availability, not simply a material property. Distinguish:

```text
AVAILABLE | NOT_BUILT | NOT_APPLICABLE | FAILED | DEPRECATED | UNKNOWN
```

### 5. Builder Passport

Expose:

- Builder ID/version;
- code or artifact digest;
- input/output schema versions;
- preprocessing parameters;
- parent artifacts;
- compatibility declarations;
- deterministic replay fixture and tolerance.

### 6. Agent-ready snapshot contracts

Publish immutable snapshot IDs, schema versions, stable pagination/sorting, content manifests and compatibility metadata.

## Scientific reporting recommendation

Publish a compact Result Passport:

```text
Object
Representation
Builder
Organizational Observables
Scientific Null Ladder
Admission State
Mapping Stability
Interpretation Boundary
```

Distinguish:

```text
nearest correspondence
≠
admitted correspondence
```

Mandatory principle:

> **Vocabulary correspondence ≠ evidence inheritance.**

## Suggested implementation order

### Documentation-first

1. field roles;
2. missing/empty/failure semantics;
3. Object Signature annotations;
4. capability semantics;
5. Builder version/compatibility notes.

### Machine-readable

6. Representation Passport;
7. Capability Passport;
8. Builder replay fixture;
9. snapshot manifest;
10. Representation Graph.

## Scope

These are development proposals based on a 3,000-record pilot. They are not claims that Materials Project is defective, nor a physical interpretation of the discovered organizational families.

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
