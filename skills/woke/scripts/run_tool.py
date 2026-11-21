#!/usr/bin/env python3
"""Run reviewed bundled helpers offline; no network services or child processes."""
import argparse
from pathlib import Path
import runpy
import sys

ROOT=Path(__file__).resolve().parents[1]

def offline_event(event,args):
    if event.startswith('socket.') or event.startswith('os.exec') or event.startswith('os.spawn') or event in {'subprocess.Popen','os.system','os.fork','os.forkpty','os.posix_spawn'}:
        raise PermissionError('The WOKE launcher is offline: network and child-process operations are disabled. Use the host connector for an authorized document task; configure other runtimes separately.')

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('tool',choices=['unscript','ais','body-demo'])
    parser.add_argument('args',nargs=argparse.REMAINDER)
    ns=parser.parse_args();args=ns.args[1:] if ns.args[:1]==['--'] else ns.args
    sys.dont_write_bytecode=True
    repo,module={'unscript':('UNSCRIPT','unscript'),'ais':('autonomous-identity-scaffolding','ais'),'body-demo':('virtual-body-kai','examples.embodiment_v2_demo')}[ns.tool]
    base=ROOT/'assets/repositories'/repo
    sys.path.insert(0,str(base/'src' if (base/'src').is_dir() else base))
    sys.argv=[module]+args
    sys.addaudithook(offline_event)
    try:runpy.run_module(module,run_name='__main__')
    except ModuleNotFoundError as exc:parser.exit(2,f'Missing dependency {exc.name!r}. Read references/tools.md; install only the selected tool dependencies in a separate environment.\n')
    except PermissionError as exc:parser.exit(2,str(exc)+'\n')

if __name__=='__main__':main()
