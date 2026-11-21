#!/usr/bin/env python3
"""Step the neutral body kernel and export a restorable snapshot outside the skill."""
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'assets/repositories/virtual-body-kai'))
from embodiment_v2 import EmbodimentEngine, SensoryEvent, MotionIntent
from embodiment_v2.bridge import to_agent_context, to_kai_tags
from woke import output

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--events',required=True,help='JSON object with dt_s, events and optional intents')
    p.add_argument('--state-in',help='Previous exported snapshot or export object')
    p.add_argument('--out',help='New output file; existing files are not overwritten')
    ns=p.parse_args()
    try:
        request=json.loads(Path(ns.events).read_text())
        if not isinstance(request,dict):raise ValueError('Input must be an object.')
        if ns.state_in:
            saved=json.loads(Path(ns.state_in).read_text());body=EmbodimentEngine.from_snapshot(saved.get('snapshot',saved))
        else:body=EmbodimentEngine()
        events=[SensoryEvent(**item) for item in request.get('events',[])]
        intents=[MotionIntent(**item) for item in request.get('intents',[])]
        body.step(request.get('dt_s',0.1),events=events,intents=intents)
        output({'schema':'woke.body-export.v1','snapshot':body.snapshot(),'context':to_agent_context(body),'tags':to_kai_tags(body)},ns.out)
    except (ValueError,TypeError,KeyError,OSError) as exc:p.exit(2,str(exc)+'\n')

if __name__=='__main__':main()
