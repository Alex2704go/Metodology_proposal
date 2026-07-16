# Builder Admission — v0.2

**Status: ADMITTED**

Builder is audited as an independent CEOS object. Family admission cannot compensate for a failed Builder gate.

## Gate

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

Required numerical tolerance for invariance and replay: **exact 0.0**.

## Results

| Audit | Observable schema | Observer blocks | Raw max error | Scaled max error | Result |
|---|---|---|---:|---:|---|
| Field permutation | equal | equal | 0.0 | 0.0 | PASS |
| Nested object/list permutation | equal | equal | 0.0 | 0.0 | PASS |
| Recursive key-order permutation | equal | equal | 0.0 | 0.0 | PASS |
| Serialization roundtrip | equal | equal | 0.0 | 0.0 | PASS |
| Deterministic rerun | equal | equal | 0.0 | 0.0 | PASS |
| Frozen out-of-sample replay | equal | equal | 0.0 | 0.0 | PASS |

## Audit meanings

### Field permutation

Top-level serialized fields are reordered without changing values. Builder output must not depend on source-field order.

### Nested object permutation

List members are recursively permuted inside nested objects. Current organizational observables are explicitly order-invariant aggregates, so their outputs must remain exact.

This audit does **not** claim that list order is universally meaningless. It tests the declared contract of the current Builder. A future order-sensitive Builder requires a separate admission profile.

### Key-order permutation

Dictionary keys are recursively reordered. MAP and RECORD observables must not depend on serialization insertion order.

### Serialization audit

Every object passes through canonical JSON serialization and parsing. Representation observables must remain exact.

### Deterministic transform

The same source is transformed in two independent runs. Arrays `X_raw`, `X_scaled`, block labels, observable names and object ordering must be exactly equal.

### Frozen preprocessing

Out-of-sample records are transformed using training medians, scales, clipping and block weights. Adding examples cannot refit preprocessing.

### No ID leakage

The organizational-observable manifest contains no material ID, formula, object ID or element-identity observable.

## Failed precursor and remediation

The first Builder Admission attempt was rejected:

- key-order permutation produced raw error `1.7763568394002505e-15`;
- serialization roundtrip produced raw error `8.881784197001252e-16`.

The source was floating-point accumulation order in composition and nested dictionary-size statistics. Values were canonically sorted before aggregation. All downstream vectors, Observer audits, Nulls, partitions and out-of-sample assignments were then recomputed.

The corrected Builder achieves exact zero error for every registered audit.

## Invalidation rule

```text
Builder code change
    ↓
Builder Admission revoked
    ↓
Organizational observables invalidated
    ↓
Observer Audit invalidated
    ↓
Null Ladder invalidated
    ↓
Frozen Partition invalidated
```

No downstream success can waive this chain.

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
