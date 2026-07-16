# CEOS Claim Compiler

## Compiler contract

The CEOS Claim Compiler does not prove scientific truth.

It checks whether a scientific claim package is sufficiently typed, pinned, evidenced, scoped and lifecycle-consistent to be admitted for further scientific discussion.

```text
Compiler success
    ≠ truth

Compiler success
    = claim package is well-formed
      under the registered CEOS governance version
```

## Input package

- typed claim;
- antecedent claim refs;
- EvidenceRefs and ProvenanceRefs;
- identity refs;
- artifact registry;
- lifecycle events;
- qualification history;
- Scientific Null results;
- Interpretation Boundary.

## Compilation phases

### 1. Parse

Validate syntax, schema and controlled enums.

### 2. Resolve

Resolve artifact IDs, identity IDs, claim IDs, versions and content digests.

### 3. Type Check

Reject forbidden coercions and endpoint/direction mismatches.

### 4. Proof Check

Verify actual artifact SHA-256, validators, protocols and independence groups.

### 5. Graph Check

Verify pinned antecedents and reject claim cycles.

### 6. Lifecycle Replay

Derive current state and maturity from events. Authored status cannot override the replay result.

### 7. Semantic Boundary Check

Verify controlled Supports/Prohibits sets are disjoint and mandatory prohibitions are present.

### 8. Null Qualification Check

Verify referenced Scientific and Governance Null requirements for the claim type.

### 9. Emit

Return either a qualified claim package or typed diagnostics.

## Example diagnostics

```text
ERROR GOV-STATE-001
Claim: CL-17
Expected state: ADMITTED
Derived state: NOT_TESTED
Reason: illegal lifecycle transition
```

```text
ERROR GOV-PROV-001
Claim: CL-21
Reason: missing provenance refs
```

```text
ERROR GOV-MAP-001
Claim: CM-04
Reason: evidence inheritance across vocabulary boundary
Forbidden coercion: CrossMapping ↛ IndependentEvidence
```

## Output states

- `QUALIFIED`: registered checks pass, independent Admission pending if required;
- `ADMITTED`: all required independent gates pass;
- `WITHHELD`: claim is well-formed but evidence does not support the stronger assertion;
- `REASSESSMENT_REQUIRED`: previously admitted package is invalidated by new evidence or failed qualification;
- `REJECTED`: package violates a required invariant;
- `RETIRED`: package intentionally removed from active claim space.

## Non-goal

The compiler cannot determine whether a model of nature is ultimately correct. It can reject known classes of malformed reasoning, unsupported transitions and evidence laundering.

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- the protocol, vocabulary, decision history, or document-governance contract explicitly stated here; empirical claims only through separately admitted linked artifacts.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- empirical validation merely because a rule is documented.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
