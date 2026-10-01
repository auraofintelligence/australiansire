"""Prepare only the public pages, artwork and licence for GitHub Pages."""
from pathlib import Path
from shutil import copy2, copytree

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / '_site'
DEST.mkdir(exist_ok=True)
for page in ROOT.glob('*.html'):
    copy2(page, DEST / page.name)
copytree(ROOT / 'assets', DEST / 'assets', dirs_exist_ok=True)
copy2(ROOT / 'LICENCE.md', DEST / 'LICENCE.md')
(DEST / '.nojekyll').touch()
print('Prepared the public site in _site/.')
