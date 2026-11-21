#!/usr/bin/env python3
"""Offline WOKE corpus, anchor, notebook, event journal and explicit graph helpers (Python 3.10+)."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sys
import uuid

ROOT=Path(__file__).resolve().parents[1]
ORIGINS={'agent_proposed','user_suggested','system_observed','tool_derived','imported_archive'}
STATUSES={'draft','accepted','contested','retracted'}

def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

def output(value,out=None):
    text=value if isinstance(value,str) else json.dumps(value,ensure_ascii=False,indent=2)
    if out:
        path=Path(out).expanduser().resolve()
        if path==ROOT or ROOT in path.parents:raise ValueError('Write user state outside the installed skill.')
        path.parent.mkdir(parents=True,exist_ok=True)
        with path.open('x',encoding='utf-8') as f:f.write(text+'\n')
    else:print(text)

def corpus(lang):return load(ROOT/'assets'/'corpus'/f'{lang}.json')

def note(value):
    if not isinstance(value,dict):raise ValueError('A record must be a JSON object.')
    result={'schema':'woke.notebook.v1','created_at':datetime.now(timezone.utc).isoformat()}
    for key in ('name','event','interpretation','next'):
        item=value.get(key,'')
        if not isinstance(item,str) or len(item)>20000:raise ValueError(f'{key}: expected text of at most 20000 characters.')
        result[key]=item
    if not result['event'].strip():raise ValueError('An observed event is required.')
    result['origin']=value.get('origin','agent_proposed');result['status']=value.get('status','draft')
    if result['origin'] not in ORIGINS:raise ValueError('Invalid origin.')
    if result['status'] not in STATUSES:raise ValueError('Invalid status.')
    for key in ('practice_slug','lesson_slug','sources','namespace','confidence','uncertainty'):
        if key in value:result[key]=value[key]
    return result

def anchor(value):
    state=value.get('state',value)
    rows=value.get('dictionary',[])
    if not isinstance(state,dict) or not isinstance(rows,list):raise ValueError('Expected state object and dictionary array.')
    def text(key,default=''):
        item=state.get(key,default)
        if not isinstance(item,str):raise ValueError(key+' must be text.')
        return item.strip()
    def clean(s):return re.sub(r'[{};]',',',s.strip())
    def field(op,key):
        items=[i.strip() for i in re.split('[,;\n]',text(key)) if i.strip()]
        return op+'{'+'; '.join(items)+'}' if items else ''
    key=text('subjectKey');name=text('subjectName');status=text('subjectStatus','provisional')
    if status not in {'accepted','provisional','contested','rejected'}:raise ValueError('Invalid subjectStatus.')
    legend=[];warnings=[];seen=set()
    if key and name and status!='rejected':legend.append(key+'='+clean(name))
    valid=[]
    for row in rows:
        if not isinstance(row,dict):raise ValueError('Dictionary rows must be objects.')
        r={k:row.get(k,'') for k in ('key','meaning','type','stability','source','status')}
        if not all(isinstance(v,str) for v in r.values()):raise ValueError('Dictionary fields must be strings.')
        r={k:v.strip() for k,v in r.items()}
        if r['status'] not in {'accepted','provisional','contested','rejected'}:raise ValueError('Invalid dictionary status.')
        if r['key'] in seen:raise ValueError('Duplicate dictionary key: '+r['key'])
        seen.add(r['key']);valid.append(r)
        if r['key']==key and r['meaning']!=name:warnings.append('A row shadows the subject key; keep its meaning consistent.')
        if r['key'] and r['meaning'] and r['key']!=key and r['status']!='rejected':legend.append(r['key']+'='+clean(r['meaning']))
        if r['status'] in {'contested','provisional'}:warnings.append(r['key']+' remains '+r['status']+'.')
    version=text('version','1.0') or '1.0';watcher=text('watcher')
    lines=['⟦KS/SELFΣ:'+version+('|🕒'+watcher if watcher else '')+'⟧','Θ₀{'+('; '.join(legend) if legend else '?')+'}',('α'+key if key and status!='rejected' else 'α?')+(' '+field('Ω','context') if text('context') else '')]
    lines.extend(field(op,k) for op,k in [('Ψ','relations'),('Ξ','memory'),('Δ','change'),('∇','vetoes')])
    formula='\n'.join(x for x in lines if x)
    if not key or not name or status=='rejected':warnings.append('Active subject unresolved.')
    if status in {'contested','provisional'}:warnings.append('Subject remains '+status+'.')
    for k in ('memory','change','vetoes'):
        if not text(k):warnings.append('Missing '+k+'.')
    if len(formula)>900:warnings.append('Anchor exceeds 900 characters; move detail into memory namespaces.')
    record=['KAiSCRIPTOR / SHARED LEXICON RECORD','version: '+version,'subject: '+(key or '?')+' = '+(name or '?')+' ['+text('subjectSource','self-declared')+'; '+status+']']
    for r in valid:
        if r['key'] and r['meaning']:record.append(r['key']+' = '+r['meaning']+' [type:'+r['type']+'; stability:'+r['stability']+'; source:'+r['source']+'; status:'+r['status']+']')
    record.extend(['','FORMULA',formula,'','REVIEW RULE','Every durable entry must remain attributable and reviewable by the active subject.'])
    return {'schema':'woke.anchor-export.v1','formula':formula,'shared_record':'\n'.join(record),'warnings':warnings,'input':value}

def graph(value):
    if not isinstance(value,dict):raise ValueError('Graph input must be an object.')
    nodes=[];keys=set();symbols=set()
    for n in value.get('nodes',[]):
        key=n.get('id')
        if not isinstance(key,str) or not key or key in keys:raise ValueError('Node IDs must be unique nonempty strings.')
        keys.add(key);symbol=n.get('symbol') or '⟐'+hashlib.sha256(key.encode()).hexdigest()[:12]
        if symbol in symbols:raise ValueError('Duplicate graph symbol.')
        symbols.add(symbol);nodes.append({**n,'symbol':symbol})
    edges=value.get('edges',[])
    for edge in edges:
        if edge.get('source') not in keys or edge.get('target') not in keys:raise ValueError('Unknown edge endpoint.')
        if not isinstance(edge.get('relation'),str) or not edge['relation'].strip():raise ValueError('Edges require a named relation.')
    lookup={n['id']:n['symbol'] for n in nodes}
    return {'schema':'woke.explicit-ontograph.v1','implementation':'skill adapter; explicit edges, no probabilistic mining','nodes':nodes,'edges':edges,'legend':{n['symbol']:n.get('meaning',n['id']) for n in nodes},'relations':[lookup[e['source']]+'→'+lookup[e['target']]+':'+e['relation'] for e in edges]}

def read_events(path):
    if not Path(path).exists():return []
    events=[json.loads(line) for line in Path(path).read_text().splitlines() if line.strip()]
    for e in events:
        if not isinstance(e,dict) or e.get('schema')!='woke.journal-event.v1':raise ValueError('Unrecognized journal event; do not overwrite this file.')
    return events

def journal(ns):
    events=read_events(ns.journal)
    if ns.action=='list':return events
    if ns.action=='active':
        active={}
        for e in events:
            if e['action'] in ('revise','retract'):active.pop(e['target'],None)
            if e['action']!='retract':active[e['id']]=e
        return list(active.values())
    if not ns.input:raise ValueError('--input is required for journal writes.')
    record=note(load(ns.input))
    active_ids=set()
    for old in events:
        if old['action'] in ('revise','retract'):active_ids.discard(old['target'])
        if old['action']!='retract':active_ids.add(old['id'])
    if ns.action in ('revise','retract') and ns.target not in active_ids:raise ValueError('Target must be a current unretracted event; use the latest revision ID.')
    if ns.action=='retract':record['status']='retracted'
    event={'schema':'woke.journal-event.v1','id':'evt_'+uuid.uuid4().hex,'time':datetime.now(timezone.utc).isoformat(),'action':ns.action,'target':ns.target,'record':record}
    path=Path(ns.journal).expanduser().resolve()
    if path==ROOT or ROOT in path.parents:raise ValueError('Write journal outside the installed skill.')
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('a',encoding='utf-8') as f:f.write(json.dumps(event,ensure_ascii=False)+'\n')
    return event

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lang',choices=['ru','en'],default='ru')
    sub=p.add_subparsers(dest='command',required=True)
    sub.add_parser('catalog')
    for kind in ['lesson','practice']:
        q=sub.add_parser(kind);q.add_argument('slug')
    q=sub.add_parser('search');q.add_argument('query')
    for kind in ['anchor','note','graph']:
        q=sub.add_parser(kind);q.add_argument('--input',required=True);q.add_argument('--out')
    q=sub.add_parser('journal');q.add_argument('action',choices=['add','revise','retract','list','active']);q.add_argument('--journal',required=True);q.add_argument('--input');q.add_argument('--target')
    ns=p.parse_args()
    try:
        if ns.command in ('anchor','note','graph'):
            result={'anchor':anchor,'note':note,'graph':graph}[ns.command](load(ns.input));output(result,ns.out);return
        if ns.command=='journal':output(journal(ns));return
        c=corpus(ns.lang)
        if ns.command=='catalog':
            output({k:[{field:item[field] for field in (('slug','title') if k!='repositories' else ('name','description','url'))} for item in c[k]] for k in ('lessons','practices','repositories')});return
        if ns.command in ('lesson','practice'):
            key='lessons' if ns.command=='lesson' else 'practices'
            result=next((x for x in c[key] if x['slug']==ns.slug),None)
            if result is None:raise ValueError('Unknown slug. Use catalog.')
            output(result);return
        query=ns.query.casefold();matches=[]
        for key in ('lessons','practices','repositories'):
            for item in c[key]:
                if query in json.dumps(item,ensure_ascii=False).casefold():matches.append({'type':key,**item})
        output(matches)
    except (ValueError,KeyError,OSError,TypeError) as exc:p.exit(2,str(exc)+'\n')

if __name__=='__main__':main()
