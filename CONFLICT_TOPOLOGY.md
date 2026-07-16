# Conflict Topology

## Definition

Conflict Topology is an organizational object describing agreement and disagreement among independently constructed assignment channels.

```text
Nodes
    Global geometry
    Local geometry
    Composition
    Structure
    Symmetry
    Observer

Edges
    agreement: same frozen family
    conflict: different frozen families
```

Node attributes include nearest family, margin tier, channel-support percentile and channel-OOD state.

## Topology versus uncertainty

A low margin is a scalar state. Conflict Topology records *who disagrees with whom*.

Two objects may have the same global margin but different topologies:

```text
Object A
    every channel weakly prefers F-001

Object B
    Structure → F-001
    Composition/Symmetry/Local → F-003
    Observer → F-002
```

Only the second contains a multi-axis relational conflict.

## Family-label invariance

The canonical topology signature ignores the names F-001…F-004. It stores only the partition of channel nodes into agreement groups.

Example:

```text
{Global, Structure}
{Composition, Symmetry, Local}
{Observer}
```

Relabeling the families does not change this topology.

## Candidate boundary subtypes

- `CONSENSUS_BOUNDARY`: low global margin but channel votes largely agree.
- `RELATIONAL_BOUNDARY`: low global margin together with disagreement across independent channel groups.
- `LOCAL_GLOBAL_BOUNDARY`: global centroid and local neighborhood support different families.
- `CHANNEL_OOD_BOUNDARY`: at least one channel is outside its registered support while the combined representation remains in-support.

These are candidate organizational classes, not admitted physical categories.

## Conflict Null

Conflict Null preserves each channel packet but destroys object-level alignment:

```text
Composition packets  ─ independently permuted
Structure packets    ─ independently permuted
Symmetry packets     ─ independently permuted
Observer packets     ─ independently permuted
Local packets        ─ independently permuted
```

It attacks channel concordance rather than channel content.

A second form independently permutes complete representation blocks and recomputes frozen-centroid margins. This tests whether Boundary frequency lives in cross-channel alignment.

## Operational definition — v0.3

`RELATIONAL_BOUNDARY` requires:

```text
Builder valid
AND exact frozen replay
AND global representation in-support
AND global margin < 0.05
AND Global family ≠ Local family
AND at least two of {Composition, Structure, Symmetry}
    support a family different from Global
```

Channel-specific OOD remains a node attribute. Global OOD changes the Assignment State to `OOD` and excludes the object from the Boundary population.

## Current population result — v0.3

Among 3,000 training objects, 52 have low global margin. Four are global OOD and are therefore not Boundary under state precedence. Of the remaining 48 Admission-State Boundary objects, eight satisfy the multi-axis relational-conflict rule.

- mean conflict difference, Boundary minus non-Boundary: 0.100;
- Channel-Packet Null q95: 0.039;
- multi-axis conflict odds ratio: 30.87;
- Fisher exact p: 4.14×10⁻⁹.

The representation-block Conflict Null does not materially change the overall Boundary rate. Therefore the admitted organizational reading is:

```text
Boundary as a whole is not established as relational.
RELATIONAL_BOUNDARY is supported as a distinct candidate subtype.
```

LiMnVF₆ has topology:

```text
{Global, Structure}
{Local, Composition, Symmetry}
{Observer}
```

## Interpretation lock

Conflict Topology describes organizational geometry in representation space.

```text
No physical phase-boundary or mechanism claim is made.
```

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
