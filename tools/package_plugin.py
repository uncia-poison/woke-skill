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
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["name"] == "woke"
    assert manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
    output = output.resolve()
    if output == MANIFEST.resolve() or SKILL.resolve() in output.parents:
        raise ValueError("Never replace source files with a release archive")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as zf:
        archive_file(zf, "woke/plugin.json", MANIFEST.read_bytes())
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
                "woke/skills/woke/" + relative.as_posix(),
                path.read_bytes(),
            )
    with zipfile.ZipFile(output) as zf:
        names = zf.namelist()
        assert zf.testzip() is None
        assert "woke/plugin.json" in names
        assert "woke/skills/woke/SKILL.md" in names
        assert all(n.startswith("woke/") and ".." not in Path(n).parts for n in names)
        assert len(names) == len(set(names))
    print(f"OK: {output} ({output.stat().st_size} bytes, {len(names)} files)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    build(args.output)
