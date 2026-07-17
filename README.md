# v0.42.MaterialsWorld

> **Governance status:** v0.1 is `REASSESSMENT_REQUIRED` after 16/16 registered attacks exposed specification gaps or unprotected transitions. Governance v0.2 closed those 16; a newly discovered fail-fast pipeline gap produced patch v0.2.1. Current result: 17/17 registered attacks rejected, `QUALIFIED`, not `ADMITTED`, pending an independent Red Team. Builder and frozen MaterialsWorld results remain admitted within their recorded scope. No real Cross Mapping has been admitted.

Слепой аудит мира материалов в логике CEOS: сначала объекты, представления, Builder Admission, организационные наблюдаемые, Observer-аудит и Null-модели; предметная интерпретация — только после Admission.

CEOS рассматривается как система контроля научных утверждений. Полная лестница и правила инвалидации зафиксированы в `CEOS_ARCHITECTURE.md`; текущий Builder gate — в `reports/BUILDER_ADMISSION.md`.

> **CEOS is a framework for disciplined translation between independently constructed organizational ontologies and existing scientific vocabularies, while explicitly preventing the transfer of evidential weight across that translation.**

## Авторы и участники

- **Alex2704go** — инициатор проекта, соавтор методологии и исследовательской постановки.
- **Arena.ai Agent Mode** — AI-соавтор анализа, реализации, Red Team-проверок и документации.

Авторство относится к совместной разработке представленной методологии и репозитория. Предметные данные сохраняют собственное происхождение и атрибуцию, указанную в `DATA_PROVENANCE.md`.

## Биография результата

CEOS публикует не только итог, но и ключевые события, которые изменили тип, scope или допустимость утверждения:

```text
Dataset
    ↓
Hypotheses proposed / rejected / withheld
    ↓
Scientific and Governance Nulls
    ↓
Representation revisions
    ↓
Admission State × Release State
    ↓
Interpretation Boundary
```

- спецификация: `RESULT_BIOGRAPHY.md`;
- фактическая биография MaterialsWorld: `reports/MATERIALSWORLD_RESULT_BIOGRAPHY.md`;
- машиночитаемая версия: `derived/materialsworld_result_biography_v0.1.json`.

`WITHHELD` означает сознательное удержание claim до прохождения перечисленных gates и не эквивалентен `REJECTED`.

## Cross-WORLD Atlas

Физический атлас двух взаимодополняющих проекций cuprate electronic state:

```text
PbBi2201 STM/STS
    → local one-particle spectral organization

Bi2212 RIXS/DMRG
    → collective spin/charge momentum organization
```

- документ: `CROSS_WORLD_ATLAS_PbBi2201_STM_Bi2212_RIXS.md`;
- machine-readable atlas: `CROSS_WORLD_ATLAS_PbBi2201_STM_Bi2212_RIXS.json`;
- source WORLDs:
  - https://github.com/Alex2704go/pbbi2201-representation-ecology
  - https://github.com/Alex2704go/bi2212-rixs-constrained-ecology-v0.29

Atlas трактует сумму измерений как typed geometry of projections, а не арифметическую сумму.

## Этапы

1. **Stage 00 — Intake**: фиксация происхождения данных, неизменяемого raw-слоя и правил аудита.
2. **Stage 01 — Inventory**: схема, типы, пропуски, диапазоны, дубликаты, возможные ключи. Без физики.
3. **Stage 02 — WORLD**: нейтральное представление объектов.
4. **Stage 03 — Observer Audit**: зависимости, дублирование и семейства Observer-полей.
5. **Stage 04 — Null Ladder**: направленные разрушения организационных объектов.
6. **Stage 05 — Admission**: открытие предметной литературы и post hoc Cross Mapping.

## Каталоги

- `raw/` — исходные неизменённые выгрузки и manifest с контрольными суммами.
- `derived/` — производные таблицы и представления.
- `figures/` — графики.
- `reports/` — отчёты этапов и журнал решений.
- `config/` — версии схем, выборок, признаков и Null-моделей.
- `scripts/` — воспроизводимые утилиты pipeline.

## Правила доступа

API-ключи не хранятся в проекте. Загрузчик должен получать ключ из переменной окружения `MP_API_KEY`. Файлы `.env`, секреты и ключи не коммитятся.

## Следующий контрольный рубеж

До начала Stage 01 необходимо зафиксировать:

- источник и версию API;
- дату выгрузки;
- критерии включения и исключения;
- объём пилотного среза;
- seed и способ построения разнообразной выборки;
- запрашиваемые поля;
- формат и контрольную сумму raw-файла.

## Principle Box

> **Vocabulary correspondence ≠ evidence inheritance.**

Cross Mapping is descriptive. It never upgrades the epistemic status of either ontology. Only independently admitted evidence may upgrade epistemic status.

The normative principles are in `CEOS_PRINCIPLES.md`; claim-transition rules are in `CEOS_TYPE_SYSTEM.md`. Scientific and Governance Nulls are separated in `SCIENTIFIC_NULL_LADDER.md` and `GOVERNANCE_NULL_LADDER.md`. The proof-carrying candidate and compiler contract are documented in `GOVERNANCE_V0.2.md` and `CEOS_CLAIM_COMPILER.md`.

## Document Admission

Every CEOS Markdown document must contain an `Interpretation Boundary` with explicit `Supports` and `Does not support` sections. Run:

```bash
python3 scripts/apply_interpretation_boundaries.py
python3 scripts/lint_ceos_documents.py
```

A generated or edited document is not admitted until the linter passes.

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
