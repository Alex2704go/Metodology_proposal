# CEOS Representation Ontology v0.1

**Статус:** candidate ontology / preregistration.  
**Не является результатом Stage 02. Builders ещё не запускались.**

## 1. Наблюдаемый архитектурный переход

```text
SummaryDoc
    ↓
Representation Objects
    ↓
Object Signatures
    ↓
Builder dispatch
    ↓
WORLD
```

Builder выбирается не по имени поля и не по предметной трактовке, а по наблюдаемой сигнатуре объекта.

## 2. Почему плоской метки типа недостаточно

Вложенный JSON технически всегда образует дерево разбора. Поэтому утверждение `structure → TREE` ничего не различает без дополнительного операционного определения TREE.

Аналогично, объект с именованными ключами может одновременно выглядеть как:

- `MAP`, если ключи рассматриваются как элементы переменного домена;
- `RECORD`, если набор ключей стабилен и каждый ключ является фиксированным слотом;
- `COMPOSITE`, если он объединяет несколько различных контейнерных грамматик.

Следовательно, тип нельзя честно назначать только по runtime-классу `dict` или `list`.

## 3. Object Signature

Предлагается многомерная сигнатура:

```text
ObjectSignature =
    State
  × Container
  × KeyGrammar
  × ValueGrammar
  × Topology
  × Cardinality
```

### 3.1 State

- `PRESENT`
- `NONE`
- `EMPTY_LIST`
- `EMPTY_MAP`

`NONE`, `EMPTY_LIST` и `EMPTY_MAP` — состояния представления, а не содержательные типы. Их нельзя молча объединять: они несут различные сведения о доступности и построении объекта.

### 3.2 Container

- `SCALAR`
- `LIST`
- `OBJECT`

Это непосредственно наблюдаемый runtime-уровень.

### 3.3 KeyGrammar

Применяется к `OBJECT`:

- `FIXED` — набор ключей устойчив между объектами;
- `OPEN` — ключи принадлежат переменному домену;
- `MIXED` — существует устойчивое ядро и переменная периферия;
- `NA` — ключевой грамматики нет.

Устойчивость должна оцениваться по распределению наборов ключей, а не по одному примеру.

### 3.4 ValueGrammar

- `HOMOGENEOUS` — значения следуют одному контракту;
- `HETEROGENEOUS` — именованные слоты имеют разные контракты;
- `RECURSIVE` — значение воспроизводит грамматику родительского объекта;
- `MIXED`;
- `UNRESOLVED`.

### 3.5 Topology

- `ATOMIC`
- `FLAT`
- `SEQUENCE`
- `HIERARCHICAL`
- `RECURSIVE_TREE`
- `COMPOSITE`

`RECURSIVE_TREE` требует повторяющейся node/children-грамматики. Просто большая глубина вложенности недостаточна. `HIERARCHICAL` допускает древовидный JSON без рекурсивного типа узла. `COMPOSITE` означает сочетание нескольких самостоятельных контейнерных грамматик.

### 3.6 Cardinality

Регистрируются как распределения, а не словесные классы:

- длина списка;
- число ключей;
- глубина;
- число листьев;
- branching profile;
- доля отсутствующих и пустых состояний.

## 4. Производные CEOS-классы

Плоские классы допускаются только как производные проекции сигнатуры.

### MAP

```text
Container = OBJECT
KeyGrammar = OPEN или MIXED
ValueGrammar = HOMOGENEOUS
```

### RECORD

```text
Container = OBJECT
KeyGrammar = FIXED
ValueGrammar = HETEROGENEOUS либо slot-addressed
```

### TREE

```text
Topology = RECURSIVE_TREE
```

TREE нельзя назначать только потому, что объект вложенный.

### COMPOSITE

```text
Topology = COMPOSITE
```

Объект содержит несколько различимых подграмматик и требует координации нескольких Builder-контрактов.

## 5. Текущие гипотезы, не окончательные назначения

| Поле | Наблюдаемая форма | Кандидат | Что необходимо проверить |
|---|---|---|---|
| `composition` | object; переменные ключи; числовые значения | MAP | устойчивость открытой key grammar на всём пилоте |
| `symmetry` | object; именованные слоты | RECORD | стабильность ключей, типов и missingness |
| `structure` | глубокий object с несколькими подграмматиками | HIERARCHICAL или COMPOSITE; TREE пока гипотеза | наличие повторяющейся node/children grammar; глубина и branch profile |
| `has_props` | object; 21 boolean slot в API-пробе | RECORD по грамматике / MAP по интерфейсу | стабильны ли 21 ключ; допускаются ли новые capability keys |
| `builder_meta` | object; 7 строковых слотов в API-пробе | RECORD | полная стабильность key/type grammar |
| `origins` | list of objects в API-пробе | LIST[RECORD] или COMPOSITE | вариативность внутренних схем и длины |

`has_props` является решающим тестом: Builder dispatch должен учитывать сигнатуру, а не заставлять объект иметь одну метафизическую метку.

## 6. Builder contracts

Builder не должен знать имя исходного поля. Он получает сигнатуру и объект.

```text
ScalarBuilder
  input:  SCALAR signature
  output: value observer + state observer

ListBuilder
  input:  LIST signature
  output: length, element signatures, order-sensitive/insensitive views

MapBuilder
  input:  OBJECT + OPEN/MIXED key grammar
  output: key-domain, value-domain, sparsity and map observers

RecordBuilder
  input:  OBJECT + FIXED key grammar
  output: slot schema, slot missingness, cross-slot observers

HierarchyBuilder
  input:  HIERARCHICAL signature
  output: depth, branching, path grammar, subtree signatures

TreeBuilder
  input:  RECURSIVE_TREE signature
  output: node/edge representation and recursive observers

CompositeBuilder
  input:  COMPOSITE signature
  output: subobject decomposition + coordination graph
```

## 7. Builder selection protocol

1. Наблюдать runtime-форму без имени поля.
2. Оценить состояния `NONE/EMPTY/PRESENT`.
3. Вывести key/value grammar на всей выборке.
4. Измерить topology и cardinality profile.
5. Сформировать Object Signature.
6. Выбрать Builder по preregistered dispatch rules.
7. Проверить альтернативные Builders как competing representations.
8. Не использовать качество предметной цели для выбора Builder до Admission.

## 8. Nulls нового уровня

Теперь Null должен атаковать не только данные, но и организационную грамматику:

- `Key Null`: перестановка ключей между MAP-объектами с сохранением размеров и маргиналов;
- `Slot Null`: перестановка значений внутри RECORD-слотов между объектами;
- `Topology Null`: rewiring с сохранением depth/degree profile;
- `Cardinality Null`: перестановка размеров контейнеров между объектами;
- `State Null`: перестановка `NONE/EMPTY/PRESENT` с сохранением частот;
- `Builder Null`: применение конкурирующего Builder того же уровня сложности.

## 9. Критерий перехода к Builders

Переход разрешается только после того, как:

- правила типов формализованы до просмотра Builder-результатов;
- определены случаи пересечения типов;
- зафиксирован приоритет или multi-dispatch;
- измерена устойчивость сигнатур на пилоте;
- API-пробы `has_props`, `origins`, `builder_meta` включены в воспроизводимую выгрузку либо явно исключены;
- отрицательные и неоднозначные назначения сохраняются как `UNRESOLVED`.

## 10. Текущий вывод

Главный объект следующего уровня — не `structure` и не `has_props` сами по себе.

Главный объект:

```text
Object Signature
    ↓
Builder contract
```

Это превращает Representation из списка полей в архитектуру построения WORLD.

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
