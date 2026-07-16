# Real-material CEOS Representation Cards

**Уровень:** Representation Classification. Это ещё не CEOS Family clustering.

Правило выбора записи: минимальный `material_id` среди точных совпадений формулы. Оно зафиксировано до просмотра содержимого.

## FeS — `mp-aaaaadct`

- Source formula: `FeS`
- **composition:** MAP, keys=2, value total=4.0
- **structure:** COMPOSITE, depth=5, leaves=62, object nodes=15, list nodes=18
- **symmetry:** RECORD, slots=8, cross-map=Hexagonal / #194
- **has_props:** RECORD + MAP VIEW, active=12/21
- Active representation capabilities: `bandstructure, charge_density, chemenv, dos, electronic_structure, magnetism, materials, oxi_states, provenance, substrates, thermo, xas`
- **origins:** LIST[RECORD], length=8
- **signature:** `MAP2|COMP(d5,l62,o15,a18)|SYM-19a4e4a89b|CAP12-9e190e9675|ORG8`

## NaCl — `mp-aaaabhux`

- Source formula: `NaCl`
- **composition:** MAP, keys=2, value total=2.0
- **structure:** COMPOSITE, depth=5, leaves=42, object nodes=9, list nodes=12
- **symmetry:** RECORD, slots=8, cross-map=Cubic / #221
- **has_props:** RECORD + MAP VIEW, active=13/21
- Active representation capabilities: `bandstructure, charge_density, chemenv, dos, electronic_structure, magnetism, materials, oxi_states, phonon, provenance, substrates, thermo, xas`
- **origins:** LIST[RECORD], length=8
- **signature:** `MAP2|COMP(d5,l42,o9,a12)|SYM-00a0b42e94|CAP13-347cbd0d54|ORG8`

## SiO2 — `mp-aaaaakgg`

- Source formula: `SiO2`
- **composition:** MAP, keys=2, value total=9.0
- **structure:** COMPOSITE, depth=5, leaves=103, object nodes=30, list nodes=33
- **symmetry:** RECORD, slots=8, cross-map=Hexagonal / #180
- **has_props:** RECORD + MAP VIEW, active=16/21
- Active representation capabilities: `bandstructure, charge_density, chemenv, dielectric, dos, elasticity, electronic_structure, magnetism, materials, oxi_states, phonon, piezoelectric, provenance, substrates, thermo, xas`
- **origins:** LIST[RECORD], length=10
- **signature:** `MAP2|COMP(d5,l103,o30,a33)|SYM-b4d5157fd4|CAP16-17839dfe81|ORG10`

## SrTiO3 — `mp-aaaaagwx`

- Source formula: `SrTiO3`
- **composition:** MAP, keys=3, value total=10.0
- **structure:** COMPOSITE, depth=5, leaves=112, object nodes=33, list nodes=36
- **symmetry:** RECORD, slots=8, cross-map=Tetragonal / #140
- **has_props:** RECORD + MAP VIEW, active=16/21
- Active representation capabilities: `bandstructure, charge_density, chemenv, dielectric, dos, elasticity, electronic_structure, insertion_electrodes, magnetism, materials, oxi_states, phonon, provenance, substrates, thermo, xas`
- **origins:** LIST[RECORD], length=9
- **signature:** `MAP3|COMP(d5,l112,o33,a36)|SYM-7ef5aee35d|CAP16-7be3fd494c|ORG9`

## Что здесь классифицировано

Карточка классифицирует организацию представлений конкретной записи и строит наблюдаемую сигнатуру. Она ещё не утверждает, что материалы образуют разные CEOS Families. Для этого нужны population-level vectorization, scaling, Null Ladder и устойчивое family discovery.

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- representation-object, Builder, organizational-observable, and schema claims under the registered representation protocol.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- physical identity or mechanism inferred from representation shape alone.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
