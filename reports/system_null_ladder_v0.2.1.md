# System Null Ladder v0.2.1 — Fail-Fast Patch

## Newly registered attack

```text
GOV-PIPE-001

A failed integrity stage is followed by a successful command.
The compound shell returns the later success code and masks the failed gate.
```

## Observation

The issue occurred during final integrity execution. Document lint failed because a generated checkpoint had not yet received its Interpretation Boundary, but a following Python command succeeded and the compound shell returned exit code 0.

## Remediation

```bash
set -euo pipefail
```

A single entrypoint now runs all integrity stages:

```text
scripts/run_integrity_gate.sh
```

## Regression

- integrity script declares fail-fast mode: PASS;
- injected failed stage returns non-zero: PASS;
- command after failed stage is not executed: PASS;
- complete normal integrity gate: PASS.

## Aggregate registered result

```text
Inherited invalid attacks rejected: 16/16
New pipeline attack rejected:       1/1
Total registered attacks rejected: 17/17
Remaining registered gaps:          0
```

`Remaining registered gaps` is explicitly scoped to the 17 current attacks. It does not assert absence of unregistered failures.

## Status

```text
Governance v0.2.1: QUALIFIED
Governance v0.2.1: NOT ADMITTED
```

Independent Red Team remains required.

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
