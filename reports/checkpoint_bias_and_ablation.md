# Checkpoint — Sampling Bias and Block Ablation

## Association with registered sampling axes

| Axis | NMI with family |
|---|---:|
| `sampling_stratum` | 0.1183 |
| `nelements` | 0.1146 |
| `symmetry_crystal_system` | 0.1803 |

NMI near zero means weak association; NMI near one means that the family partition is largely recoverable from that axis.

## Leave-one-block-out agreement

| Ablation | Organizational observables | Mean ARI vs primary | Min | Max |
|---|---:|---:|---:|---:|
| `NO_COMPOSITION` | 64 | 0.9871 | 0.9871 | 0.9871 |
| `NO_STRUCTURE` | 50 | 0.0775 | 0.0759 | 0.0799 |
| `NO_SYMMETRY` | 36 | 0.9814 | 0.9814 | 0.9814 |

Ablation ARI measures whether the same partition can be recovered without a block. It does not by itself identify a mechanism. Full contingency tables are in the JSON report.

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
