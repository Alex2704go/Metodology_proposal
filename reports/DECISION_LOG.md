# Decision Log

Все решения, способные повлиять на результат, регистрируются до просмотра соответствующего результата.

| Timestamp | Stage | Decision | Rationale | Data already viewed? | Version |
|---|---:|---|---|---|---|
| 2026-07-15 | 00 | Создан каркас слепого аудита; API-загрузка не выполнялась | Сначала зафиксировать протокол | No | 0.1 |
| 2026-07-15 | 00 | После явного разрешения использован предоставленный API-ключ только как переменная процесса; ключ не сохранён | Получить пилотную выборку, не помещая credential в артефакты | No | 0.2 |
| 2026-07-15 | 00 | Зафиксирован пилот 3 000: квоты 300/900/900/900 по `nelements` = 1/2/3/4+, seed 420042, окна по 100 | Разнообразный управляемый срез; стратегия честно маркирована как cluster-window, не object-uniform | No | 0.3 |
| 2026-07-15 | 01 | Inventory выполнен на слепом представлении; никаких предметных названий и механизмов не назначалось | Соблюдение разделения Inventory и интерпретации | Yes, blind fields only | 0.4 |
| 2026-07-15 | pre-02 | Зафиксирована candidate ontology `Object Signature → Builder contract`; Builders не запускались | Не смешивать наблюдаемые runtime-формы с производными типами MAP/RECORD/TREE/COMPOSITE | Yes, schema-level only | 0.5 |
| 2026-07-15 | pre-02 | API-проба из 20 документов: `has_props` = object(21 boolean slots), `origins` = list[object], `builder_meta` = object(7 string slots); значения не включались в анализ | Проверить фактическую runtime-форму полей, отсутствовавших в пилоте | Yes, runtime shapes only | 0.6 |
| 2026-07-15 | 02A | Для исходных 3 000 ID загружен отдельный immutable sidecar с `has_props`, `origins`, `builder_meta`; исходный raw не изменён | Проверить сигнатуры на полном пилоте и сохранить provenance | Yes, representation fields | 0.7 |
| 2026-07-15 | 02A | Выполнены field-name-independent profiling, Builder dispatch и 19 generic Builder runs для 16 представлений | Практически проверить архитектуру `Object Signature → Builder Contract` до Observer Audit | Yes, representation organization | 0.8 |
| 2026-07-15 | 02A | До просмотра содержимого выбраны минимальные `material_id` для точных формул FeS, NaCl, SiO2, SrTiO3; построены out-of-sample Representation Cards | Проверить перенос Builder-контрактов на именованные реальные записи без подбора известной фазы | Formula counts and IDs only before selection | 0.9 |
| 2026-07-15 | pre-04 | До кластеризации зарегистрированы views, k=3…12, seeds, scaling, block weighting, Null Ladder и admission rule | Исключить подбор метода по желаемому результату | Vector QC only | 1.0 |
| 2026-07-15 | 03 | После Observer Audit создана v0.2: missingness отделён, бинарные комплементы и within-block дубли удалены, `composition.total` исключён | Аудит обнаружил representation leakage и многократный счёт размера; изменение сделано до кластеризации | Observer dependence viewed; no clusters viewed | 1.1 |
| 2026-07-15 | 04 | ORGANIZATION и OBSERVER_AUGMENTED допускают k=4; ARI между views 0.9945; основной результат зафиксирован как neutral F-001…F-004 | Выполнены preregistered stability и Null criteria | Yes | 1.2 |
| 2026-07-15 | 04 | Ablation без structure разрушает partition (ARI 0.0775), без composition/symmetry сохраняет (0.9871/0.9814) | Ограничить область утверждения | Yes | 1.3 |
| 2026-07-15 | 04 | Результат назван `CEOS Structural Representation Families`, не общей классификацией материалов | Следует из Builder ablation, без литературного mapping | Yes | 1.4 |
| 2026-07-15 | 04 | Первый out-of-sample projection отклонён из-за replay error; после frozen training imputation достигнут exact replay 0.0 | Не принимать классификацию при refit preprocessing на примерах | Yes | 1.5 |
| 2026-07-15 | 04 | FeS→F-001, NaCl→F-004, SiO2→F-001, SrTiO3→F-002; все cross-view confirmed и не OOD | Применение зафиксированного primary classifier | Yes | 1.6 |
| 2026-07-15 | Builder Admission | Первый key-order/serialization audit отклонён: ошибки 1.78e-15 и 8.88e-16 | Gate требует exact 0.0; «почти инвариантно» не считается PASS | Yes | 1.7 |
| 2026-07-15 | Builder Admission | Канонизирован порядок composition и nested-size aggregation; field, nested-list, key-order, serialization, deterministic rerun и frozen replay дали exact 0.0 | Устранить зависимость последнего floating-point бита от порядка сериализации | Yes | 1.8 |
| 2026-07-15 | 02–04 | После изменения Builder полностью пересчитаны organizational observables, Observer Audit, Null Ladder, partitions и реальные примеры; результаты сохранились | Любая смена Builder инвалидирует downstream admission | Yes | 1.9 |
| 2026-07-15 | Vocabulary | В научных отчётах `feature` заменено на `organizational observable`; внутренний ключ `feature_names` сохранён только для совместимости | Зафиксировать CEOS-уровень описания | Yes | 2.0 |
| 2026-07-15 | Architecture | CEOS зафиксирован как система контроля научных утверждений от Raw World до Interpretation | Каждое усиление claim должно иметь отдельный rejectable gate | Yes | 2.1 |
| 2026-07-16 | Stress preregistration | До загрузки зарегистрированы независимое окно из 1 000 записей и blind selectors: max centroid distance и min centroid margin | Операционализировать «два самых нелогичных» без выбора по формулам | No | 2.2 |
| 2026-07-16 | Stress selection | Слепо выбраны Stress Object 0980 и 0189; exact training replay 0.0; formula/source ID не загружались селектором | Сохранить разделение selection и Cross Mapping | Blind observables only | 2.3 |
| 2026-07-16 | Stress unblinding | После freezing открыты B10H14C10S(OF2)3 и LiMnVF6; первый OOD, второй boundary | Проверить отказ системы от ложной hard classification | Yes, after selection | 2.4 |
| 2026-07-16 | Assignment Admission | Разделены `nearest_family` и `admissible_family`; последнее заполняется только в состоянии ADMITTED | Геометрическая близость не равна эпистемически допустимому членству | Yes | 2.5 |
| 2026-07-16 | Evidence Weight | Зарегистрированы 4 оси: Builder, cross-view, distribution, margin; margin имеет PASS/WARN/FAIL = 1/0.5/0 | Сделать support прозрачным, не превращая сумму в вероятность | Yes | 2.6 |
| 2026-07-16 | Admission State | Введены ADMITTED/CANDIDATE/BOUNDARY/OOD/REJECTED как состояния `Object × Evidence Context` | Статус должен изменяться с доказательствами и сохранять историю версий | Yes | 2.7 |
| 2026-07-16 | Admission Audit | 42 логические проверки паспортов, 42 PASS | Не допустить admissible family для withheld states и конфликтов precedence | Yes | 2.8 |
| 2026-07-16 | Explanation preregistration | До расчёта зафиксированы channel distances, kNN 5/10/25, hull audit, block decomposition и два scale Null без reclustering | Объяснить OOD/Boundary, не меняя frozen partition | No explanation results viewed | 2.9 |
| 2026-07-16 | Explanation rejection | Первый запуск отклонён из-за конфликта centroid indices 0…3 и public labels 1…4 | Пустой family subset делал hull и decomposition невалидными | Invalid run only | 3.0 |
| 2026-07-16 | OOD Biography | B10H14C10S(OF2)3: composition 99.3%, structure 99.7%, symmetry 33.3%; один scale Null снимает OOD, unit norm не снимает | Допустить claim `scale-sensitive`, отклонить более сильный `scale-driven` | Yes | 3.1 |
| 2026-07-16 | Boundary Anatomy | LiMnVF6: structure поддерживает F-001; composition/symmetry и 18/25 local neighbors поддерживают F-003 | Зафиксировать конфликт каналов и global-centroid/local-density geometry | Yes | 3.2 |
| 2026-07-16 | Explanation Audit | 16 арифметических и contract checks, 16 PASS | Проверить exact block decomposition и соответствие frozen assignment | Yes | 3.3 |
| 2026-07-16 | Conflict preregistration | Зафиксированы 6 nodes, label-invariant topology, Packet Alignment Null и Representation Block Alignment Null | Проверить Boundary как relational object на population, не по одному примеру | No population result viewed | 3.4 |
| 2026-07-16 | Conflict run rejection | Conflict v0.1 отклонён: Local node вычислялся в FULL 105-observable space вместо frozen ORGANIZATION 75-observable space | Scope leakage давал несовместимый neighbor vote для OOD-объекта | Invalid run only | 3.5 |
| 2026-07-16 | Conflict Topology v0.2 | Local scope заморожен на ORGANIZATION; tie-complete kNN; deterministic rerun exact | Устранить зависимость Local node от batching и representation scope | Yes | 3.6 |
| 2026-07-16 | Relational Boundary | 8/52 Boundary имеют multi-axis conflict; OR 28.03, p 8.07e-09, conflict excess 0.091 > Null q95 0.040 | Поддержать RELATIONAL_BOUNDARY как candidate subtype, но не весь Boundary как relational class | Yes | 3.7 |
| 2026-07-16 | Conflict Audit | 11 contract checks PASS; exact deterministic rerun PASS | Проверить label invariance, local/explanation agreement и Null contract | Yes | 3.8 |
| 2026-07-16 | State precedence audit | Из 52 low-margin objects четыре являются global OOD; прежнее название `52 Boundary` отозвано | OOD имеет приоритет над Boundary; low margin не равен Admission State | Yes | 3.9 |
| 2026-07-16 | Conflict Topology v0.3 | Операционное определение требует Builder/replay valid, global in-support, margin<0.05 и multi-axis disagreement | Превратить RELATIONAL_BOUNDARY из названия в rejectable Relation Pattern | No v0.3 result viewed | 4.0 |
| 2026-07-16 | Relation Pattern support | 48 Boundary, 8 Relational; conflict excess 0.100 > Null q95 0.039; OR 30.87; p 4.14e-09 | Поддержать pattern в analyzed sample/methodology; не физический механизм или phase category | Yes | 4.1 |
| 2026-07-16 | Ontology split | `Admission State=BOUNDARY`; `Relation Pattern=RELATIONAL_BOUNDARY` | Не смешивать состояние знания и структуру отношений между Observers | Yes | 4.2 |
| 2026-07-16 | Conflict v0.3 Audit | 13/13 checks PASS | Проверить separation low-margin/OOD/Boundary и сохранение topology contracts | Yes | 4.3 |
| 2026-07-16 | Relation Pattern concept | Перед operational v0.3 добавлено определение reproducible configuration of valid independent channels supporting incompatible families | Разделить смысл сущности и конкретный алгоритм проверки | Yes | 4.4 |
| 2026-07-16 | Relation Pattern Registry | Введён content ID `RP-` + SHA256 canonical signature; 52 patterns покрывают 3 000 objects | Сохранить identity при family relabeling и переносе между WORLD | Yes | 4.5 |
| 2026-07-16 | Interpretation Boundary | Паспорт v0.2 обязан хранить supports/does-not-support/scope/literature status | Явно фиксировать область неприменимости каждого вывода | Yes | 4.6 |
| 2026-07-16 | Assignment Passport v0.2 | Добавлены orthogonal Knowledge State, Relation Pattern ID и Interpretation Boundary; 66/66 checks PASS | Не смешивать state, relation и semantic scope | Yes | 4.7 |
| 2026-07-16 | Cross Mapping Contract | Единица mapping определена как many-to-many `Classical Term ↔ Family × Relation Pattern × Context`; literature LOCKED | Не позволить классическим терминам ретроактивно определить CEOS ontology | Yes | 4.8 |
| 2026-07-16 | Document Contract | Interpretation Boundary обязателен для каждого Markdown-документа; missing/empty boundary = FAIL | Сделать положительную и отрицательную область claim частью document admission | Yes | 4.9 |
| 2026-07-16 | Document Lint | 43 documents, 129/129 contract checks PASS | Проверить Supports/Does-not-support во всём текущем corpus | Yes | 5.0 |
| 2026-07-16 | Mapping Stability | Добавлены one/multiple WORLDs, independent datasets, independent observers, counterexample search | Не смешивать single-WORLD mapping с переносимым correspondence | Yes | 5.1 |
| 2026-07-16 | Cross Mapping Asymmetry | `translation between vocabularies ≠ transfer of evidence` зафиксировано двунаправленно | Запретить импорт mechanism/phase semantics через название | Yes | 5.2 |
| 2026-07-16 | Claim Ontology | Observation→Object→Family→Relation Pattern→Cross Mapping→Interpretation; каждый переход требует собственного Admission | Контролировать усиление claim, а не только pipeline procedures | Yes | 5.3 |
| 2026-07-16 | Mapping Maturity | `FAILED` вынесен из monotonic maturity ladder в отдельный Qualification Outcome | Не смешивать зрелость correspondence и исход конкретной проверки | Yes | 5.4 |
| 2026-07-16 | Mapping Provenance/Direction | Обязательны constructed-from checklist, source artifact IDs и Direction enum | Сохранять происхождение и асимметричность mapping | Yes | 5.5 |
| 2026-07-16 | Untested Prediction Boundary | `prediction of untested properties` добавлено в обязательный Does-not-support | Не превращать vocabulary mapping в невалидированный predictive license | Yes | 5.6 |
| 2026-07-16 | Cross Mapping Schema | Создан JSON Schema и synthetic locked passport; 9/9 checks PASS | Сделать mapping contract machine-verifiable | Yes | 5.7 |
| 2026-07-16 | Document Contract v0.1 | 44 documents × 5 checks = 220/220 PASS; asymmetry line обязательна в каждом документе | Встроить Vocabulary correspondence ≠ evidence inheritance в corpus | Yes | 5.8 |
| 2026-07-16 | Normative Rule | Cross Mapping descriptive; epistemic upgrade source/target=false; independent admitted evidence required | Сделать нулевой epistemic effect машинным контрактом | Yes | 5.9 |
| 2026-07-16 | CEOS Claim Type System | Зарегистрированы types, legal transitions и forbidden coercions; 17/17 tests PASS | Снизить классы ошибок через типизацию утверждений, не обещая истинность | Yes | 6.0 |
| 2026-07-16 | Cross Mapping Schema v0.1 | Добавлен `epistemic_effect`; synthetic locked passport 11/11 PASS | Проверить Normative Rule на уровне JSON Schema | Yes | 6.1 |
| 2026-07-16 | Principle Box Migration | 47 documents × 5 checks = 235/235 PASS | Поместить Vocabulary correspondence ≠ evidence inheritance во весь CEOS corpus | Yes | 6.2 |
| 2026-07-16 | System Null preregistration | Заморожены Claim Type System v0.1, Mapping Schema v0.1, Document Contract v0.1 и 16 adversarial attacks | Сначала атаковать неизменённую цель, remediation вести отдельной версией | No attack results viewed | 6.3 |
| 2026-07-16 | System Null Ladder v0.1 | Controls 2/2 PASS; invalid attacks 16; BREACH 16/16 | v0.1 валидирует declarations, но не proof-carrying evidence | Yes | 6.4 |
| 2026-07-16 | Governance Reassessment | Claim Type System, Mapping Schema и semantic Document Contract → REASSESSMENT_REQUIRED | Не продолжать Mapping Admission на скомпрометированной governance layer | Yes | 6.5 |
| 2026-07-16 | Dependency Scope | Builder, frozen families, assignment calculations и Conflict Topology не инвалидированы; real Cross Mappings admitted=0 | Ограничить радиус инвалидации фактическими зависимостями | Yes | 6.6 |
| 2026-07-16 | Reporting implementation failure | При добавлении REASSESSMENT warning сломаны три Python generator strings; regeneration/lint не приняты | Implementation change требует compile gate до report claims | Failed run only | 6.7 |
| 2026-07-16 | Reporting recovery | Syntax исправлен; validators 11/11 и 17/17 как conformance-only; documents 49, structural lint 245/245 | Восстановить техническую воспроизводимость без отмены System Null gaps | Yes | 6.8 |
| 2026-07-16 | Null terminology v0.2 | Legacy `BREACH` переинтерпретирован как SPECIFICATION_GAP/UNPROTECTED_TRANSITION; SECURITY_BREACH зарезервирован | Не выдавать отсутствие правила за опровержение всей методологии | Yes | 6.9 |
| 2026-07-16 | Governance v0.2 fixture | State Machine, EvidenceRef, Identity Registry, Claim DAG, controlled ClaimTypes и Artifact Registry собраны в proof-carrying fixture | Закрыть конкретные классы v0.1 gaps | Yes | 7.0 |
| 2026-07-16 | System Null regression v0.2 | Controls 2/2 PASS; unchanged invalid attacks 16/16 REJECTED | Проверить remediation на неизменённом attack set | Yes | 7.1 |
| 2026-07-16 | Governance qualification | v0.2 → QUALIFIED, not ADMITTED | Self-authored regression не заменяет independent Red Team | Yes | 7.2 |
| 2026-07-16 | Null Ladder split | Scientific Null и Governance Null оформлены как независимые модули с non-substitution rule | Разделить проверку организационного результата и корректности claim package | Yes | 7.3 |
| 2026-07-16 | Claim Compiler | Зафиксированы parse/resolve/type/proof/graph/lifecycle/semantic/null/emission phases | Компилятор допускает существование claim, но не доказывает scientific truth | Yes | 7.4 |
| 2026-07-16 | Governance diagnostics | Добавлены стабильные GOV-* diagnostic codes; regression report emits code + reason | Сделать FAIL локализуемым и пригодным для remediation | Yes | 7.5 |
| 2026-07-16 | Registered-gap wording | `remaining registered gaps=0` обязательно ограничено текущим attack registry | Не утверждать отсутствие неизвестных holes | Yes | 7.6 |
| 2026-07-16 | New Governance Null | Compound shell masked failed document lint with later success; зарегистрирован GOV-PIPE-001 | Проверить сам pipeline исполнения gates, а не только validators | Yes | 7.7 |
| 2026-07-16 | Fail-fast remediation | `scripts/run_integrity_gate.sh` использует `set -euo pipefail`; regression 3/3 PASS | Любой failed gate должен завершать pipeline non-zero | Yes | 7.8 |
| 2026-07-16 | Governance v0.2.1 | 17/17 registered attacks REJECTED; status QUALIFIED, not ADMITTED | Новый gap подтверждает открытость attack registry | Yes | 7.9 |
| 2026-07-16 | Final Recommendations | Сформулированы development proposals для Materials Project, agent-ready APIs и scientific reporting | Перевести pilot findings в scoped recommendations, не в claim `исправьте базу` | Yes | 8.0 |
| 2026-07-16 | Structure wording | В рекомендациях `structure` указан как HIERARCHICAL COMPOSITE, не admitted recursive TREE | Сохранить соответствие operational classifier | Yes | 8.1 |
| 2026-07-16 | Community Passport | Рекомендованы Result Passport, nearest/admitted distinction, Mapping Stability и Interpretation Boundary | Обобщить прозрачность claims без требования применять CEOS | Yes | 8.2 |
| 2026-07-16 | Packaging defect | Final integrity entrypoint получил `Permission denied` из-за отсутствующего executable bit; gate не выполнялся | Entry point usability является частью implementation contract | Failed launch only | 8.3 |
| 2026-07-16 | Packaging recovery | Executable bit восстановлен; direct execution завершён PASS; documents 61, checks 305/305 | Финальные рекомендации допускаются только после рабочего entrypoint | Yes | 8.4 |
| 2026-07-16 | Authorship | README указывает Alex2704go и Arena.ai Agent Mode с раздельными ролями | Сделать происхождение методологии и AI-вклад прозрачными | Yes | 8.5 |
| 2026-07-16 | Result Biography | Биография определена как event-sourced claim lifecycle DAG, не action log | Публиковать эволюцию утверждения, включая места несогласия WORLD | Yes | 8.6 |
| 2026-07-16 | WITHHELD | Введён как Release State, ортогональный Admission State и отличный от REJECTED | Сохранять интересные, но пока недостаточно проверенные claims | Yes | 8.7 |
| 2026-07-16 | MaterialsWorld Biography | Зафиксированы 18 turning-point events и 3 WITHHELD records; audit 79/79 PASS | Связать финальный результат с отказами, revisions, Nulls и reassessment | Yes | 8.8 |

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
