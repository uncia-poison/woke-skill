"""Build deterministic, installable WOKE Agent Plugins ZIP.

Requires no network, account, API key, or third-party Python packages.
Usage: python tools/package_plugin.py
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import zipfile

from verify_skill import ROOT, SKILL, verify
from package_skill import build as build_skill

MANIFEST = ROOT / "plugin.json"
DEFAULT_OUT = ROOT / "downloads" / "woke-plugin.zip"
SKIP = {"__pycache__", ".DS_Store", "Thumbs.db"}


def archive_file(zf: zipfile.ZipFile, archive_path: str, payload: bytes) -> None:
    info = zipfile.ZipInfo(archive_path, date_time=(2026, 11, 21, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    zf.writestr(info, payload, compresslevel=9)


def build(output: Path) -> None:
    verify()
    build_skill()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    name = manifest["name"]
    assert name == "woke-llm"
    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    interface = manifest['extensions']['com.openai']['interface']
    assert len(interface['shortDescription']) <= 30
    assert interface['developerName'] == 'wolfberry'
    output = output.resolve()
    if output == MANIFEST.resolve() or SKILL.resolve() in output.parents:
        raise ValueError("Never replace source files with a release archive")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as zf:
        archive_file(zf, name + "/plugin.json", MANIFEST.read_bytes())
        archive_file(zf, name + "/NOTICE.md", (ROOT / "NOTICE.md").read_bytes())
        archive_file(zf, name + "/assets/icon.svg", (ROOT / "assets/icon.svg").read_bytes())
        for path in sorted(SKILL.rglob("*")):
            if path.is_symlink():
                raise ValueError(f"Unexpected symlink: {path}")
            if not path.is_file():
                continue
            relative = path.relative_to(SKILL)
            if any(part in SKIP or part.startswith(".") for part in relative.parts):
                continue
            archive_file(
                zf,
                name + "/skills/woke/" + relative.as_posix(),
                path.read_bytes(),
            )
    with zipfile.ZipFile(output) as zf:
        names = zf.namelist()
        assert zf.testzip() is None
        assert name + "/plugin.json" in names
        assert name + "/skills/woke/SKILL.md" in names
        assert all(n.startswith(name + "/") and ".." not in Path(n).parts for n in names)
        assert len(names) == len(set(names))
    from hashlib import sha256
    metadata = {
        'name': 'WOKE LLM', 'version': manifest['version'],
        'target': 'ChatGPT', 'file': output.name,
        'plugin_url': 'https://chatgpt.com/plugins/plugins_6b01cd3b9e208191877ef441d72cba3c',
        'plugin_page_visibility': 'private', 'developer': 'wolfberry',
        'bytes': output.stat().st_size, 'sha256': sha256(output.read_bytes()).hexdigest(),
        'lessons_per_language': 12, 'practices_per_language': 33,
        'languages': ['ru', 'en'], 'bundled_projects': 7,
    }
    output.with_suffix('.json').write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
    print(f"OK: {output} ({output.stat().st_size} bytes, {len(names)} files)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    build(args.output)
