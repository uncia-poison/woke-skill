"""Build an uploadable WOKE archive from the reviewed public skill files."""
from pathlib import Path
import zipfile
from verify_skill import verify,ROOT,SKILL
verify()
output=ROOT/'dist/woke-skill.zip';output.parent.mkdir(exist_ok=True)
with zipfile.ZipFile(output,'w',compression=zipfile.ZIP_DEFLATED) as z:
    for p in sorted(SKILL.rglob('*')):
        if p.is_file():
            info=zipfile.ZipInfo('woke/'+str(p.relative_to(SKILL)),date_time=(2026,11,21,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644 << 16
            z.writestr(info,p.read_bytes())
print(output)
