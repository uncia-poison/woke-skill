"""Build the standalone WOKE skill and matching public checksum metadata."""
from pathlib import Path
import hashlib
import json
import zipfile
from verify_skill import verify, ROOT, SKILL


def build():
    verify()
    output = ROOT / 'dist/woke-skill.zip'
    output.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as z:
        for p in sorted(SKILL.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts:
                info = zipfile.ZipInfo('woke/' + str(p.relative_to(SKILL)), date_time=(2026, 11, 21, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.external_attr = 0o100644 << 16
                z.writestr(info, p.read_bytes())
    public = ROOT / 'downloads/woke-skill.zip'
    public.parent.mkdir(exist_ok=True)
    public.write_bytes(output.read_bytes())
    version = json.loads((ROOT / 'plugin.json').read_text())['version']
    meta = {
        'name': 'WOKE', 'version': version, 'target': 'Agent Skills',
        'tested_host': 'ChatGPT', 'other_platforms': 'not tested; host setup and compatibility check required',
        'file': public.name, 'bytes': public.stat().st_size,
        'sha256': hashlib.sha256(public.read_bytes()).hexdigest(),
        'lessons_per_language': 12, 'practices_per_language': 33,
        'languages': ['ru', 'en'], 'bundled_projects': 7,
    }
    public.with_suffix('.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    print(output)
    return public


if __name__ == '__main__':
    build()
