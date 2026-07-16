#!/usr/bin/env python3
"""Stage 01 inventory. Descriptive data audit only; no domain interpretation."""
from __future__ import annotations

import gzip
import hashlib
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "derived" / "objects_blind_3000.jsonl.gz"
OUT_JSON = ROOT / "reports" / "stage01_inventory.json"
OUT_MD = ROOT / "reports" / "stage01_inventory.md"


def canonical(value) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def digest_value(value) -> str:
    return hashlib.sha256(canonical(value).encode("utf-8")).hexdigest()


def type_name(value) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, int):
        return "integer"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, list):
        return "array"
    if isinstance(value, dict):
        return "object"
    return type(value).__name__


def recursive_schema(value, path: str, acc: dict[str, Counter], dynamic_map=False) -> None:
    acc[path][type_name(value)] += 1
    if isinstance(value, dict):
        if path == "composition":
            for child in value.values():
                recursive_schema(child, "composition.*", acc)
        else:
            for key, child in value.items():
                recursive_schema(child, f"{path}.{key}", acc)
    elif isinstance(value, list):
        for child in value:
            recursive_schema(child, f"{path}[]", acc)


def main() -> None:
    rows = []
    with gzip.open(INPUT, "rt", encoding="utf-8") as stream:
        for line in stream:
            rows.append(json.loads(line))
    n = len(rows)
    fields = sorted(set().union(*(row.keys() for row in rows)))
    schema: dict[str, Counter] = defaultdict(Counter)
    field_report = []

    for row in rows:
        for key, value in row.items():
            recursive_schema(value, key, schema)

    for field in fields:
        values = [row.get(field) for row in rows]
        present = sum(field in row for row in rows)
        nulls = sum(value is None for value in values)
        types = Counter(type_name(value) for value in values if value is not None)
        hashes = Counter(digest_value(value) for value in values if value is not None)
        entry = {
            "field": field,
            "present": present,
            "missing": n - present,
            "null": nulls,
            "types": dict(types),
            "distinct_non_null": len(hashes),
            "duplicate_rows_non_null": sum(count - 1 for count in hashes.values() if count > 1),
        }
        numeric = [float(v) for v in values if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(float(v))]
        if numeric:
            ordered = sorted(numeric)
            entry["range"] = {"min": ordered[0], "max": ordered[-1]}
        if all((v is None or isinstance(v, (str, bool))) for v in values):
            counts = Counter(canonical(v) for v in values if v is not None)
            entry["category_counts"] = dict(counts.most_common(25))
            entry["category_counts_truncated"] = len(counts) > 25
        field_report.append(entry)

    exact_counter = Counter()
    content_counter = Counter()
    composition_counter = Counter()
    for row in rows:
        exact_counter[digest_value(row)] += 1
        content = {k: v for k, v in row.items() if k not in {"object_id", "_ceos_stratum"}}
        content_counter[digest_value(content)] += 1
        composition_counter[digest_value(row.get("composition"))] += 1

    candidate_keys = []
    for item in field_report:
        if item["missing"] == 0 and item["null"] == 0 and item["distinct_non_null"] == n:
            candidate_keys.append(item["field"])

    report = {
        "stage": "01_inventory",
        "mode": "blind; descriptive only",
        "input": str(INPUT.relative_to(ROOT)),
        "records": n,
        "top_level_field_count": len(fields),
        "top_level_fields": field_report,
        "nested_schema": {path: dict(types) for path, types in sorted(schema.items())},
        "duplicates": {
            "exact_duplicate_rows": sum(c - 1 for c in exact_counter.values() if c > 1),
            "duplicate_content_rows_excluding_object_id_and_stratum": sum(c - 1 for c in content_counter.values() if c > 1),
            "rows_beyond_first_with_same_composition_encoding": sum(c - 1 for c in composition_counter.values() if c > 1),
            "distinct_composition_encodings": len(composition_counter),
        },
        "candidate_keys_in_blind_view": candidate_keys,
        "notes": [
            "Ranges are finite-value minima and maxima; they are not domain-validity judgments.",
            "composition.* denotes dynamic dictionary keys; labels were not expanded into schema field names.",
            "Array-path occurrence counts are element occurrences, not record-level presence counts.",
            "No target designation, class naming, mechanism, filtering, or literature mapping was performed.",
        ],
    }
    OUT_JSON.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "# Stage 01 — Inventory", "",
        "**Режим:** слепой описательный аудит; без предметной интерпретации.", "",
        f"- Объектов: **{n:,}**".replace(",", " "),
        f"- Полей верхнего уровня: **{len(fields)}**",
        f"- Возможные ключи слепого представления: **{', '.join(candidate_keys) or 'не обнаружены'}**",
        "", "## Поля верхнего уровня", "",
        "| Поле | Типы | Пропуски | Null | Уникальных | Диапазон / категории |",
        "|---|---|---:|---:|---:|---|",
    ]
    for item in field_report:
        types = ", ".join(f"{k}:{v}" for k, v in item["types"].items()) or "—"
        if "range" in item:
            detail = f"[{item['range']['min']:.8g}, {item['range']['max']:.8g}]"
        elif "category_counts" in item:
            cats = list(item["category_counts"].items())[:8]
            detail = "; ".join(f"{k}:{v}" for k, v in cats)
            if item.get("category_counts_truncated") or len(item["category_counts"]) > 8:
                detail += "; …"
        else:
            detail = "—"
        lines.append(f"| `{item['field']}` | {types} | {item['missing']} | {item['null']} | {item['distinct_non_null']} | {detail} |")

    dup = report["duplicates"]
    lines += [
        "", "## Повторы", "",
        f"- Полностью совпадающие строки: **{dup['exact_duplicate_rows']}**.",
        f"- Совпадения содержимого без `object_id` и служебной страты: **{dup['duplicate_content_rows_excluding_object_id_and_stratum']}**.",
        f"- Различных кодировок `composition`: **{dup['distinct_composition_encodings']}**.",
        f"- Строк сверх первой с повторяющейся кодировкой `composition`: **{dup['rows_beyond_first_with_same_composition_encoding']}**.",
        "", "## Возможные ключи", "",
        "Кандидат определяется только технически: нет пропусков/Null и значение уникально во всех строках.", "",
    ]
    lines += [f"- `{key}`" for key in candidate_keys] or ["- Не обнаружены."]
    lines += [
        "", "## Ограничения отчёта", "",
        "- Диапазоны — только min/max конечных числовых значений, не проверка допустимости.",
        "- `composition.*` обозначает динамические ключи словаря; сами метки не раскрываются в схеме.",
        "- Для массивов статистика вложенной схемы относится к элементам массива, а не к числу объектов.",
        "- Цель, предметные классы, механизмы и литературные соответствия не назначались.",
        "", "Полная машинно-читаемая вложенная схема находится в `stage01_inventory.json`.",
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps({"records": n, "fields": len(fields), "candidate_keys": candidate_keys,
                      "duplicates": report["duplicates"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
