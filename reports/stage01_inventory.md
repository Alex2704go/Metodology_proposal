# Stage 01 — Inventory

**Режим:** слепой описательный аудит; без предметной интерпретации.

- Объектов: **3 000**
- Полей верхнего уровня: **13**
- Возможные ключи слепого представления: **density, object_id, structure, volume**

## Поля верхнего уровня

| Поле | Типы | Пропуски | Null | Уникальных | Диапазон / категории |
|---|---|---:|---:|---:|---|
| `_ceos_stratum` | string:3000 | 0 | 0 | 4 | "N3":900; "N2":900; "N4P":900; "N1":300 |
| `band_gap` | number:2998 | 0 | 2 | 1166 | [0, 17.8914] |
| `composition` | object:3000 | 0 | 0 | 2752 | — |
| `density` | number:3000 | 0 | 0 | 3000 | [0.023670128, 26.581336] |
| `elements` | array:3000 | 0 | 0 | 2282 | — |
| `formation_energy_per_atom` | number:2997 | 0 | 3 | 2937 | [-4.4127165, 4.6882049] |
| `is_magnetic` | boolean:3000 | 0 | 0 | 2 | false:2137; true:863 |
| `nelements` | integer:3000 | 0 | 0 | 7 | [1, 7] |
| `object_id` | string:3000 | 0 | 0 | 3000 | "Object 0001":1; "Object 0002":1; "Object 0003":1; "Object 0004":1; "Object 0005":1; "Object 0006":1; "Object 0007":1; "Object 0008":1; … |
| `ordering` | string:3000 | 0 | 0 | 5 | "NM":1241; "Unknown":896; "FM":653; "FiM":177; "AFM":33 |
| `structure` | object:3000 | 0 | 0 | 3000 | — |
| `symmetry` | object:3000 | 0 | 0 | 192 | — |
| `volume` | number:3000 | 0 | 0 | 3000 | [6.9261478, 10887.909] |

## Повторы

- Полностью совпадающие строки: **0**.
- Совпадения содержимого без `object_id` и служебной страты: **0**.
- Различных кодировок `composition`: **2752**.
- Строк сверх первой с повторяющейся кодировкой `composition`: **248**.

## Возможные ключи

Кандидат определяется только технически: нет пропусков/Null и значение уникально во всех строках.

- `density`
- `object_id`
- `structure`
- `volume`

## Ограничения отчёта

- Диапазоны — только min/max конечных числовых значений, не проверка допустимости.
- `composition.*` обозначает динамические ключи словаря; сами метки не раскрываются в схеме.
- Для массивов статистика вложенной схемы относится к элементам массива, а не к числу объектов.
- Цель, предметные классы, механизмы и литературные соответствия не назначались.

Полная машинно-читаемая вложенная схема находится в `stage01_inventory.json`.

<!-- CEOS-INTERPRETATION-BOUNDARY v0.1 -->
## Interpretation Boundary — Document Scope

### Supports

- descriptive schema, type, missingness, range, duplication, and provenance claims for the registered dataset.

### Does not support

- physical mechanism;
- thermodynamic phase;
- microscopic Hamiltonian;
- causal explanation;
- prediction of untested properties;
- transfer of evidence through vocabulary or Cross Mapping;
- universal validity outside the registered WORLD, sample, protocol, and version;
- material-family membership or mechanism inferred from inventory statistics.

### Cross Mapping Asymmetry

> **Vocabulary correspondence ≠ evidence inheritance.**
