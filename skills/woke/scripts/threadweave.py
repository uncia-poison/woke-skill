#!/usr/bin/env python3
"""Select a supplied ThreadWeave topic offline; print structured task data only."""
import argparse
import json
from pathlib import Path
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT/'assets/repositories/threadweave/src'))
from weave_engine import select_packet


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', required=True, help='explicitly selected UTF-8 JSON input')
    parser.add_argument('--now', type=float, help='epoch seconds, defaults to current time')
    args = parser.parse_args()
    try:
        packet = json.loads(Path(args.input).read_text(encoding='utf-8'))
        result = select_packet(packet, now=time.time() if args.now is None else args.now)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError, TypeError, KeyError) as exc:
        parser.exit(2, str(exc)+'\n')


if __name__ == '__main__':
    main()
