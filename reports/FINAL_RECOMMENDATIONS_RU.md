# Итоговые рекомендации: Materials Project, AI-агенты и научная отчётность

## Статус документа

Это предложения по развитию, а не перечень недостатков Materials Project. Они основаны на пилотном слепом аудите 3 000 записей и должны проверяться на более широких и независимых выборках.

## Краткий вывод

Materials Project уже предоставляет очень богатый `SummaryDoc`. Следующий возможный шаг — документировать не только значения полей, но и организацию языка представления:

```text
не только данные
но и Representation contracts

не только поля
но и Object Signatures

не только provenance metadata
но и replayable Builder Passports

не только has_props
но и Capability semantics
```

---

# Рекомендации для Materials Project

## 1. Representation Passport

Явно разделить роли полей:

```text
Content
Representation
Identity
Metadata
```

Это позволит пользователям и агентам не определять роль поля по его названию.

Пример:

```yaml
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

Конкретное распределение ролей должен определять сам Materials Project. Рекомендация состоит в том, чтобы сделать его явным и машиночитаемым.

## 2. Nested Object Typing

Одного JSON-типа `object` недостаточно. Для вложенных полей полезно публиковать многомерную сигнатуру:

```text
State
× Container
× KeyGrammar
× ValueGrammar
× Topology
× Cardinality
```

В пилоте были получены следующие рабочие представления:

| Поле | Организационная форма |
|---|---|
| composition | MAP |
| symmetry | RECORD |
| structure | HIERARCHICAL COMPOSITE |
| has_props | RECORD + MAP VIEW |
| origins | LIST[RECORD] |
| builder_meta | RECORD |

Важно: текущий классификатор не подтвердил `structure` как recursive TREE. Поэтому лучше публиковать многомерную Object Signature, а не один исключительный ярлык.

## 3. Representation Ecology / Representation Graph

Документировать не только отдельные поля, но и связи между ними:

```text
SummaryDoc
    ↓
Representation Graph
    ├── Object nodes
    ├── Builder nodes
    ├── Capability nodes
    └── Provenance nodes
```

Возможные связи:

```text
BUILT_BY
DERIVED_FROM
AVAILABLE_IF
HAS_SCHEMA
COMPATIBLE_WITH
SUPERSEDES
PROVENANCE_FROM
```

Это может быть отдельный schema endpoint, JSON-LD-граф или версия документации, генерируемая из общего машиночитаемого источника.

## 4. Capability Passport для has_props

`has_props` следует рассматривать как карту доступности представлений, а не как обычное свойство материала.

Рекомендуемые состояния:

```text
AVAILABLE
NOT_BUILT
NOT_APPLICABLE
FAILED
DEPRECATED
UNKNOWN
```

Булево значение не всегда позволяет отличить отсутствие расчёта от неприменимости или ошибки Builder.

В пилоте capability/provenance образовали отдельный организационный слой и не совпали с primary structural-family space. Это поддерживает их явное отделение от material-family claims.

## 5. Builder Passport и прозрачность построения

`builder_meta` и `origins` уже содержат полезную основу. Её можно развить в единый Builder Passport:

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

Небольшой replay fixture позволил бы пользователю проверить, что одна версия Builder действительно воспроизводит ожидаемый результат.

## 6. Явные состояния Representation

Не объединять автоматически:

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

Для AI-агентов различие между отсутствием содержания, отсутствием расчёта и ошибкой особенно важно.

## 7. Agent-ready API contracts

Полезно публиковать:

- immutable snapshot ID;
- schema/API version в ответе;
- стабильный sorting/pagination contract;
- query manifest;
- content digest snapshot;
- compatibility/deprecation metadata;
- Object Signature endpoint;
- Capability schema;
- Builder Passport endpoint.

Иллюстративные интерфейсы:

```text
/schemas/summary/{version}
/representation-passport/{version}
/builder-passports/{builder_id}/{version}
/capability-schema/{version}
/snapshots/{snapshot_id}/manifest
```

---

# Рекомендации для научного сообщества

## 8. Публиковать паспорт результата

Не только итоговый график или класс, но и lifecycle утверждения:

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
Mapping Stability
    ↓
Interpretation Boundary
```

Минимальные поля:

- scope объекта и выборки;
- версия представления;
- Builder и provenance;
- зарегистрированные Nulls;
- Admission State;
- причины withheld/reassessment;
- Mapping Maturity;
- Qualification Outcome;
- Supports / Does not support.

## 9. Разделять nearest и admitted correspondence

Вместо:

```text
Это SDW.
```

использовать:

```text
В представлении R и по критериям C
объект организационно наиболее близок
к опубликованному описанию SDW.

Mapping Maturity: SINGLE_WORLD
Mechanism evidence transfer: prohibited
```

Рекомендуемые уровни:

```text
nearest correspondence
candidate mapping
admitted mapping
independently replicated mapping
```

## 10. Разделять Mapping Strength и Evidence Strength

```text
Mapping Strength ≠ Evidence Strength
```

Допустимый результат:

```yaml
mapping_strength: STRONG
evidence_strength: NONE
```

Сильное структурное сходство не обязано означать независимое подтверждение общего механизма.

## 11. Публиковать Mapping Provenance и Stability

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

Maturity и outcome должны храниться раздельно. Новая неудачная проверка не переписывает историю, а переводит mapping в reassessment.

## 12. Обязательный Interpretation Boundary

Каждый claim-bearing документ должен отвечать:

```text
Supports
    что именно поддерживает результат?

Does not support
    чего из результата выводить нельзя?
```

Рекомендуемые запреты по умолчанию:

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- universal validity outside scope;
- evidence inheritance through vocabulary mapping.

Главный принцип:

> **Vocabulary correspondence ≠ evidence inheritance.**

## 13. Публиковать отрицательные и withheld states

Научно полезны не только ADMITTED-результаты, но и:

- BOUNDARY;
- OOD;
- CANDIDATE;
- REASSESSMENT_REQUIRED;
- failed Nulls;
- unresolved object types;
- Observer conflicts.

Они показывают, где текущий язык теряет различительную способность.

---

# Приоритет развития

## Быстро и без изменения API-данных

1. Документировать роли Content / Representation / Identity / Metadata.
2. Описать семантику missing/empty/failed/not-applicable.
3. Добавить Object Signature к главным nested fields.
4. Описать has_props как capability layer.
5. Консолидировать Builder version и compatibility documentation.

## Машиночитаемый среднесрочный уровень

6. Representation Passport.
7. Capability Passport.
8. Builder Passport и replay fixture.
9. Immutable snapshot manifest.
10. Representation Graph.

## Экосистемный уровень

11. Result Passport conventions.
12. Mapping Provenance и Mapping Stability standard.
13. Machine-readable Interpretation Boundary.
14. Cross-dataset Builder/schema compatibility tests.
15. Независимые qualification suites для AI-агентов.

---

# Ограничения рекомендаций

Пилот использовал 3 000 записей, выбранных детерминированными стратифицированными cluster windows. Это не равномерная выборка всего Materials Project, поэтому доли семейств не являются population estimates.

Рекомендации не означают:

- что Materials Project содержит ошибочную физику;
- что текущий API необходимо ломающе изменить;
- что CEOS является единственным возможным решением;
- что полученные structural families являются классическими физическими классами;
- что выполнено литературное или механизмное Cross Mapping.

---

# Итог

Для Materials Project наиболее полезное направление — сделать организацию представления столь же явной, как сами значения.

Для научного сообщества — публиковать не только результат, но и его происхождение, Null-проверки, состояние допуска, переносимость и границы интерпретации.

```text
Publish not only the result,
but the lifecycle and boundary of the claim.
```

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
