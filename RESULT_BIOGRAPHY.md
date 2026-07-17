# CEOS Result Biography

## English summary

A **Result Biography** is a structured, evidence-linked history of how a scientific claim became its current form. It records not only the final result, but also rejected hypotheses, failed Null tests, representation changes, withheld claims, reassessments and the decisions that occurred before or after observing results.

A log records actions. A biography records the evolution of a claim.

```text
Dataset
    ↓
Initial hypotheses
    ↓
Rejected / withheld alternatives
    ↓
Scientific and Governance Nulls
    ↓
Representation changes
    ↓
Admission and release states
    ↓
Interpretation Boundary
```

---

# Концептуальное определение

> **Биография результата — это структурированная, версионированная и связанная с доказательствами история того, как научное утверждение стало тем, чем оно является сейчас.**

Она показывает не только финальный вывод, но и:

- какие альтернативы существовали;
- какие гипотезы были отвергнуты;
- какие результаты были сознательно withheld;
- какие Null-тесты не прошли;
- когда менялось представление данных;
- какие решения были приняты до просмотра результата;
- где новые проверки заставили провести reassessment;
- какие утверждения остаются запрещёнными Interpretation Boundary.

## Почему «биография», а не «лог»

```text
Лог:
    последовательность действий

Биография:
    история эволюции утверждения
```

Биография допускает:

- рождение объектов и гипотез;
- ветвление альтернатив;
- отказ от первоначальных ожиданий;
- смену Representation;
- кризис после проваленного Null;
- WITHHELD-состояния;
- повторную квалификацию;
- retirement или supersession.

Поэтому Result Biography является не плоским списком, а направленным ациклическим графом событий и зависимостей.

---

# Практическая мотивация

В исследованиях аналитической вариативности разные добросовестные команды нередко приходят к разным выводам на одном наборе данных. Причина может находиться не в ошибке, а в множестве допустимых решений:

- какие данные фильтровать;
- что считать выбросом;
- какое Representation выбрать;
- какие organizational observables включить;
- какую модель использовать;
- какие Nulls считать достаточными;
- когда остановить анализ.

Финальная статья часто скрывает этот decision space.

Биография делает его видимым:

```text
Dataset
    ↓
Hypotheses proposed
    ↓
Hypotheses rejected
        reason + evidence
    ↓
Null tests
        PASS / FAIL
    ↓
Representation revisions
        before / after result visibility
    ↓
Objects admitted or withheld
    ↓
Interpretation Boundary
```

## Две формально похожие статьи

### Статья A

```text
Мы нашли корреляцию.
p = 0.004.
```

### Статья B

```text
Сначала было 14 гипотез.
9 отпали после проверки устойчивости.
3 не пережили Null tests.
1 зависела от Representation.
Осталась одна, прошедшая зарегистрированные проверки.
```

Финальный численный результат может совпадать, но вторая статья позволяет оценить путь отбора, пространство альтернатив и места, где данные не согласились с авторами.

---

# Онтология состояний

## Admission State

Описывает, какое утверждение допускается evidence context:

```text
ADMITTED
CANDIDATE
BOUNDARY
OOD
REJECTED
REASSESSMENT_REQUIRED
```

## Release State

Описывает, выпускается ли утверждение во внешний научный оборот:

```text
DRAFT
WITHHELD
RELEASED
RETIRED
```

### WITHHELD

> **WITHHELD означает, что объект или claim считается содержательно интересным, но сознательно не выпускается как утверждение до прохождения перечисленных проверок.**

Это отличается от `REJECTED`:

```text
REJECTED:
    зарегистрированная проверка показала,
    что claim не выдержал требования

WITHHELD:
    оснований пока недостаточно,
    обязательные проверки ещё не завершены
```

`WITHHELD` является Release State, а не заменой Admission State. Возможны составные состояния:

```text
CANDIDATE :: WITHHELD
BOUNDARY :: WITHHELD
REASSESSMENT_REQUIRED :: WITHHELD
ADMITTED :: RELEASED
REJECTED :: RETIRED
```

## Обязательные поля WITHHELD

- причина удержания;
- недостающие gates;
- evidence, уже доступное;
- условие повторного рассмотрения;
- ответственный actor;
- дата или событие следующего review;
- Interpretation Boundary.

---

# Событийная модель

Каждое событие биографии содержит:

```yaml
event_id: BIO-...
timestamp: ...
event_type: ...
actor_id: ...
claim_ids: [...]
parent_event_ids: [...]
input_artifact_refs: [...]
output_artifact_refs: [...]
pre_state: ...
post_state: ...
decision_timing: PRE_RESULT | POST_RESULT
reason_code: ...
evidence_refs: [...]
content_digest: ...
```

## Типы событий

```text
DATASET_REGISTERED
HYPOTHESIS_PROPOSED
HYPOTHESIS_REJECTED
HYPOTHESIS_WITHHELD
REPRESENTATION_CREATED
REPRESENTATION_REVISED
OBSERVER_ADDED
NULL_REGISTERED
NULL_PASSED
NULL_FAILED
BUILDER_ADMITTED
BUILDER_REVOKED
CLAIM_QUALIFIED
CLAIM_ADMITTED
CLAIM_WITHHELD
CLAIM_REJECTED
CLAIM_REASSESSMENT
CLAIM_RELEASED
CLAIM_RETIRED
INTERPRETATION_BOUNDARY_CHANGED
```

## Decision timing

Особенно важно различать:

```text
PRE_RESULT
    решение зарегистрировано до просмотра результата

POST_RESULT
    решение принято после просмотра результата
```

POST_RESULT не является автоматически ошибкой, но требует явного обоснования и новой версии claim.

---

# Biography Passport

```yaml
result_biography:
  biography_id: ...
  version: ...
  object_scope: ...
  dataset_refs: [...]
  claim_graph_root_ids: [...]

  hypotheses:
    proposed: [...]
    rejected: [...]
    withheld: [...]
    admitted: [...]

  representations:
    versions: [...]
    revisions: [...]

  nulls:
    scientific: [...]
    governance: [...]

  admission_states: [...]
  release_states: [...]

  critical_turning_points:
    - event_id: ...
      world_disagreement: ...
      response: ...

  interpretation_boundary:
    supports_claim_types: [...]
    prohibits_claim_types: [...]
```

---

# Биография и доверие

Result Biography не должна превращаться в соревнование по количеству проведённых тестов. Большое число гипотез или Nulls не гарантирует качество.

Она позволяет оценить:

- полноту зарегистрированного decision space;
- количество и типы отказов;
- изменение анализа после просмотра результатов;
- зависимость вывода от Representation;
- наличие альтернативных допустимых путей;
- причины остановки;
- текущие пробелы evidence.

Биография не заменяет preregistration, multiverse analysis, robustness checks или independent replication. Она связывает их в одну историю claim lifecycle.

---

# Связь с фразой «мир может не соглашаться»

```text
Мы научились разговаривать с миром так,
чтобы он мог с нами не соглашаться.
```

Биография результата фиксирует места такого несогласия:

- rejected hypotheses;
- failed Nulls;
- OOD objects;
- Boundary conflicts;
- invalid replay;
- governance specification gaps;
- reassessment после новой проверки.

Именно эти повороты часто наиболее полезны для воспроизводимости и продолжения исследования.

---

# Минимальный формат для публикации

Даже без полной CEOS-инфраструктуры статья может публиковать таблицу:

| Этап | Количество | Ключевые причины |
|---|---:|---|
| Гипотез предложено | ... | ... |
| Отвергнуто до model fitting | ... | ... |
| Не прошло robustness | ... | ... |
| Не прошло Null tests | ... | ... |
| Зависело от Representation | ... | ... |
| WITHHELD | ... | pending gates |
| ADMITTED | ... | evidence summary |
| REASSESSMENT_REQUIRED | ... | new contradiction |

И обязательно:

```text
Supports
    ...

Does not support
    ...
```

---

# Ограничения

Полная биография не означает публикацию всех личных заметок, конфиденциальных данных или нерелевантных проб. В неё входят события, способные изменить тип, evidence, scope, Admission State, Release State или Interpretation Boundary claim.

Биография также не гарантирует истинность результата. Она делает эволюцию утверждения проверяемой и показывает, где исследовательская система позволяла данным возражать.

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
