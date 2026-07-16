# Stage 02A — Builder Outputs

Generic Builders применены после field-name-independent dispatch.

| ID | Поле | Класс | Builder | Основной выход |
|---|---|---|---|---|
| R-001 | `_ceos_stratum` | SCALAR | ScalarBuilder | `distinct=4` |
| R-002 | `band_gap` | SCALAR | ScalarBuilder | `distinct=1166` |
| R-003 | `builder_meta` | RECORD | RecordBuilder | `slots=7; keysets=1` |
| R-003 | `builder_meta` | RECORD | MapViewBuilder | `key_domain=7; size={'min': 7, 'q25': 7, 'median': 7, 'q75': 7, 'max': 7}` |
| R-004 | `composition` | MAP | MapBuilder | `key_domain=89; size={'min': 1, 'q25': 2, 'median': 3, 'q75': 4, 'max': 7}` |
| R-005 | `density` | SCALAR | ScalarBuilder | `distinct=3000` |
| R-006 | `elements` | LIST | ListBuilder | `length={'min': 1, 'q25': 2, 'median': 3, 'q75': 4, 'max': 7}` |
| R-007 | `formation_energy_per_atom` | SCALAR | ScalarBuilder | `distinct=2937` |
| R-008 | `has_props` | RECORD | RecordBuilder | `slots=21; keysets=1` |
| R-008 | `has_props` | RECORD | MapViewBuilder | `key_domain=21; size={'min': 21, 'q25': 21, 'median': 21, 'q75': 21, 'max': 21}` |
| R-009 | `is_magnetic` | SCALAR | ScalarBuilder | `distinct=2` |
| R-010 | `nelements` | SCALAR | ScalarBuilder | `distinct=7` |
| R-011 | `object_id` | SCALAR | ScalarBuilder | `distinct=3000` |
| R-012 | `ordering` | SCALAR | ScalarBuilder | `distinct=5` |
| R-013 | `origins` | LIST_OF_OBJECTS | ListBuilder | `length={'min': 3, 'q25': 4, 'median': 5, 'q75': 8, 'max': 11}` |
| R-013 | `origins` | LIST_OF_OBJECTS | RecordElementBuilder | `slots=3; keysets=1` |
| R-014 | `structure` | COMPOSITE | CompositeBuilder | `depth={'min': 5, 'q25': 5, 'median': 5, 'q75': 5, 'max': 5}; leaves={'min': 31, 'q25': 112, 'median': 182, 'q75': 342, 'max': 3022}` |
| R-015 | `symmetry` | RECORD | RecordBuilder | `slots=8; keysets=1` |
| R-016 | `volume` | SCALAR | ScalarBuilder | `distinct=3000` |

## Граница интерпретации

Выходы описывают организацию представления. Никакие семейства материалов, механизмы или опубликованные классы не назначались. Полные slot-level и key-level результаты находятся в `derived/stage02a_builder_outputs.json`.

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
