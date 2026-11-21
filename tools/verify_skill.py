"""Check public distribution integrity without invoking any model or remote service."""
from pathlib import Path
import hashlib,json,re
ROOT=Path(__file__).resolve().parents[1]
SKILL=ROOT/'skills/woke'
def verify():
    manifest=json.loads((SKILL/'assets/manifest.json').read_text())
    for rel,digest in manifest['sha256'].items():
        assert hashlib.sha256((SKILL/rel).read_bytes()).hexdigest()==digest,rel
    for lang in ('ru','en'):
        c=json.loads((SKILL/f'assets/corpus/{lang}.json').read_text())
        assert (len(c['lessons']),len(c['practices']),len(c['repositories']))==(12,33,14)
    assert len(manifest['bundled_projects'])==7
    for target in re.findall(r'\]\((references/[^)#]+)(?:#[^)]*)?\)',(SKILL/'SKILL.md').read_text()):
        assert (SKILL/target).is_file(),target
    for p in SKILL.rglob('*'):
        if p.is_file():
            assert not p.is_symlink()
            assert not any(part.startswith('.') or part=='__pycache__' for part in p.relative_to(SKILL).parts)
            text=p.read_text(encoding='utf-8')
            assert not re.search(r'github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{30,}|-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----',text),p
    print('OK: provenance hashes, RU/EN curriculum, seven components and portable references.')
if __name__=='__main__':verify()
