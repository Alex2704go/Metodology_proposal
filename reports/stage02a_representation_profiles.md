# Stage 02A — Representation Profiles

**Режим:** имя поля не участвует в правилах классификации; предметная интерпретация отсутствует.

- Объектов: **3000**
- Представлений верхнего уровня: **16**

| ID | Поле | State | Container | Key grammar | Value grammar | Topology | Class | Builder dispatch |
|---|---|---|---|---|---|---|---|---|
| R-001 | `_ceos_stratum` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-002 | `band_gap` | PRESENT:2998, NONE:2 | SCALAR:2998 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-003 | `builder_meta` | PRESENT:3000 | OBJECT:3000 | FIXED | HOMOGENEOUS | FLAT | **RECORD** | RecordBuilder + MapViewBuilder |
| R-004 | `composition` | PRESENT:3000 | OBJECT:3000 | OPEN | HOMOGENEOUS | FLAT | **MAP** | MapBuilder |
| R-005 | `density` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-006 | `elements` | PRESENT:3000 | LIST:3000 | NA | HOMOGENEOUS | SEQUENCE | **LIST** | ListBuilder |
| R-007 | `formation_energy_per_atom` | PRESENT:2997, NONE:3 | SCALAR:2997 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-008 | `has_props` | PRESENT:3000 | OBJECT:3000 | FIXED | HOMOGENEOUS | FLAT | **RECORD** | RecordBuilder + MapViewBuilder |
| R-009 | `is_magnetic` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-010 | `nelements` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-011 | `object_id` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-012 | `ordering` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |
| R-013 | `origins` | PRESENT:3000 | LIST:3000 | NA | HOMOGENEOUS | HIERARCHICAL | **LIST_OF_OBJECTS** | ListBuilder + RecordElementBuilder |
| R-014 | `structure` | PRESENT:3000 | OBJECT:3000 | FIXED | HETEROGENEOUS | COMPOSITE | **COMPOSITE** | CompositeBuilder |
| R-015 | `symmetry` | PRESENT:3000 | OBJECT:3000 | FIXED | HETEROGENEOUS | FLAT | **RECORD** | RecordBuilder |
| R-016 | `volume` | PRESENT:3000 | SCALAR:3000 | NA | ATOMIC | ATOMIC | **SCALAR** | ScalarBuilder |

## Ограничения

- Классы являются проекциями многомерных сигнатур, а не исходными типами API.
- Рекурсия определяется консервативно по повторению одной key-signature на разных глубинах.
- `MapViewBuilder` — конкурирующее представление фиксированной однородной записи, а не замена `RecordBuilder`.
- Builder outputs ещё не вычислялись; здесь выполнен только dispatch.

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
