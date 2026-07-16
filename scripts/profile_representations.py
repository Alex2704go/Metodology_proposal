#!/usr/bin/env python3
"""Infer Stage 02A Object Signatures and dispatch Builders without field-specific rules."""
from __future__ import annotations
import gzip,json,math,statistics
from collections import Counter,defaultdict
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INPUT=ROOT/'derived/objects_blind_stage02_3000.jsonl.gz'
OUT=ROOT/'reports/stage02a_representation_profiles.json'
MD=ROOT/'reports/stage02a_representation_profiles.md'
SERVICE={'object_id','_ceos_stratum'}

def atom_type(v):
    if v is None:return 'NONE'
    if isinstance(v,bool):return 'BOOLEAN'
    if isinstance(v,(int,float)) and not isinstance(v,bool):return 'NUMBER'
    if isinstance(v,str):return 'STRING'
    if isinstance(v,list):return 'LIST'
    if isinstance(v,dict):return 'OBJECT'
    return type(v).__name__.upper()

def state(v):
    if v is None:return 'NONE'
    if isinstance(v,list) and not v:return 'EMPTY_LIST'
    if isinstance(v,dict) and not v:return 'EMPTY_MAP'
    return 'PRESENT'

def metrics(v,depth=0,dict_sets=None):
    if dict_sets is None:dict_sets=defaultdict(Counter)
    kind=atom_type(v)
    out={'max_depth':depth,'leaves':0,'objects':0,'lists':0}
    if isinstance(v,dict):
        out['objects']=1;dict_sets[depth][tuple(sorted(v))]+=1
        for x in v.values():
            z=metrics(x,depth+1,dict_sets)
            for k in out:out[k]=max(out[k],z[k]) if k=='max_depth' else out[k]+z[k]
    elif isinstance(v,list):
        out['lists']=1
        for x in v:
            z=metrics(x,depth+1,dict_sets)
            for k in out:out[k]=max(out[k],z[k]) if k=='max_depth' else out[k]+z[k]
    else:out['leaves']=1
    return out

def quantiles(xs):
    if not xs:return None
    ys=sorted(xs);n=len(ys)
    def q(p):return ys[round((n-1)*p)]
    return {'min':ys[0],'q25':q(.25),'median':q(.5),'q75':q(.75),'max':ys[-1]}

def profile(values):
    states=Counter(state(v) for v in values)
    present=[v for v in values if state(v)=='PRESENT']
    containers=Counter('SCALAR' if atom_type(v) not in {'LIST','OBJECT'} else atom_type(v) for v in present)
    dominant=containers.most_common(1)[0][0] if containers else 'UNRESOLVED'
    result={'states':dict(states),'containers':dict(containers),'dominant_container':dominant}
    sizes=[];depths=[];leaves=[];obj_counts=[];list_counts=[];all_dict_depths=defaultdict(Counter)
    for v in present:
        if isinstance(v,(dict,list)):sizes.append(len(v))
        z=metrics(v,dict_sets=all_dict_depths);depths.append(z['max_depth']);leaves.append(z['leaves']);obj_counts.append(z['objects']);list_counts.append(z['lists'])
    result['cardinality']={'size':quantiles(sizes),'depth':quantiles(depths),'leaves':quantiles(leaves),'object_nodes':quantiles(obj_counts),'list_nodes':quantiles(list_counts)}
    result['key_grammar']='NA';result['value_grammar']='UNRESOLVED';result['topology']='UNRESOLVED';result['recursive_signature_detected']=False

    # Conservative recursion test: the same non-empty object key signature occurs at different depths.
    signature_depths=defaultdict(set)
    for d,c in all_dict_depths.items():
        for sig,count in c.items():
            if sig and count:signature_depths[sig].add(d)
    recursive=any(len(ds)>1 for ds in signature_depths.values())
    result['recursive_signature_detected']=recursive

    if dominant=='SCALAR':
        result['value_grammar']='ATOMIC';result['topology']='ATOMIC';derived='SCALAR';builders=['ScalarBuilder']
    elif dominant=='LIST':
        lists=[v for v in present if isinstance(v,list)]
        elem_types=Counter(atom_type(x) for v in lists for x in v)
        result['element_types']=dict(elem_types)
        result['value_grammar']='HOMOGENEOUS' if len(elem_types)<=1 else 'HETEROGENEOUS'
        nested=any(isinstance(x,(dict,list)) for v in lists for x in v)
        if recursive:
            result['topology']='RECURSIVE_TREE';derived='TREE';builders=['TreeBuilder']
        elif nested:
            result['topology']='HIERARCHICAL';derived='LIST_OF_OBJECTS';builders=['ListBuilder','RecordElementBuilder'] if set(elem_types)=={'OBJECT'} else ['CompositeBuilder']
        else:
            result['topology']='SEQUENCE';derived='LIST';builders=['ListBuilder']
    elif dominant=='OBJECT':
        objs=[v for v in present if isinstance(v,dict)]
        keysets=[set(v) for v in objs]
        union=set().union(*keysets) if keysets else set(); inter=set.intersection(*keysets) if keysets else set()
        variants=len({tuple(sorted(x)) for x in keysets})
        if variants<=1:kg='FIXED'
        elif union and len(inter)/len(union)>=.5:kg='MIXED'
        else:kg='OPEN'
        result['key_grammar']=kg
        result['keys']={'union_count':len(union),'intersection_count':len(inter),'keyset_variants':variants,'intersection_over_union':len(inter)/len(union) if union else None}
        value_types=Counter(atom_type(x) for v in objs for x in v.values())
        result['object_value_types']=dict(value_types)
        vg='HOMOGENEOUS' if len(value_types)<=1 else 'HETEROGENEOUS';result['value_grammar']=vg
        nested=any(isinstance(x,(dict,list)) for v in objs for x in v.values())
        if recursive:
            result['topology']='RECURSIVE_TREE';derived='TREE';builders=['TreeBuilder']
        elif nested:
            result['topology']='COMPOSITE';derived='COMPOSITE';builders=['CompositeBuilder']
        else:
            result['topology']='FLAT'
            if kg in {'OPEN','MIXED'} and vg=='HOMOGENEOUS':derived='MAP';builders=['MapBuilder']
            elif kg=='FIXED':
                derived='RECORD';builders=['RecordBuilder']
                if vg=='HOMOGENEOUS':builders.append('MapViewBuilder')
            else:derived='OBJECT_UNRESOLVED';builders=['CompetingMapRecordBuilders']
    else:derived='UNRESOLVED';builders=[]
    result['derived_class']=derived;result['builder_dispatch']=builders
    return result

def main():
    rows=[]
    with gzip.open(INPUT,'rt',encoding='utf-8') as f:
        for line in f:rows.append(json.loads(line))
    fields=sorted(set().union(*(r for r in rows)))
    profiles=[]
    for i,field in enumerate(fields,1):
        p=profile([r.get(field) for r in rows]);p={'representation_id':f'R-{i:03d}','field':field,'service':field in SERVICE,**p};profiles.append(p)
    report={'stage':'02A','status':'representation profiling; no domain interpretation','records':len(rows),'input':str(INPUT.relative_to(ROOT)),'classifier_rule':'field-name-independent','profiles':profiles}
    OUT.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# Stage 02A — Representation Profiles','','**Режим:** имя поля не участвует в правилах классификации; предметная интерпретация отсутствует.','',f'- Объектов: **{len(rows)}**',f'- Представлений верхнего уровня: **{len(profiles)}**','','| ID | Поле | State | Container | Key grammar | Value grammar | Topology | Class | Builder dispatch |','|---|---|---|---|---|---|---|---|---|']
    for p in profiles:
        st=', '.join(f'{k}:{v}' for k,v in p['states'].items())
        co=', '.join(f'{k}:{v}' for k,v in p['containers'].items())
        lines.append(f"| {p['representation_id']} | `{p['field']}` | {st} | {co} | {p['key_grammar']} | {p['value_grammar']} | {p['topology']} | **{p['derived_class']}** | {' + '.join(p['builder_dispatch'])} |")
    lines += ['','## Ограничения','','- Классы являются проекциями многомерных сигнатур, а не исходными типами API.','- Рекурсия определяется консервативно по повторению одной key-signature на разных глубинах.','- `MapViewBuilder` — конкурирующее представление фиксированной однородной записи, а не замена `RecordBuilder`.','- Builder outputs ещё не вычислялись; здесь выполнен только dispatch.']
    MD.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    for p in profiles:print(p['representation_id'],p['field'],p['derived_class'],'+'.join(p['builder_dispatch']))
if __name__=='__main__':main()
