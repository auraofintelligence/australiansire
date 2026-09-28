"""Check every local page, destination, image and required navigation control."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(); self.ids=set(); self.links=[]; self.images=[]; self.artwork=[]; self.h1=0; self.previous=0; self.next=0; self.top=0; self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='a':
            self.links.append(a.get('href',''))
            self.previous+=a.get('rel')=='prev';self.next+=a.get('rel')=='next';self.top+=a.get('aria-label')=='Back to top'
        if tag in ('img','script','link'):
            src=a.get('src',a.get('href',''))
            if src:self.images.append(src)
        if tag=='img':
            assert a.get('alt'), 'Missing image description'
            self.artwork.append(a.get('src',''))
pages={p.name:Page(p.read_text(encoding='utf-8')) for p in ROOT.glob('*.html')}
errors=[]
seen_artwork={}
for name,p in pages.items():
    for src in p.artwork:
        asset=ROOT/src
        if asset.is_file():
            digest=sha256(asset.read_bytes()).hexdigest()
            if digest in seen_artwork:errors.append(f'{name}: repeated artwork {src}, already used in {seen_artwork[digest]}')
            seen_artwork[digest]=name
    if (p.h1,p.previous,p.next,p.top)!=(1,1,1,1):errors.append(f'{name}: missing heading or navigation')
    for href in p.links+p.images:
        u=urlsplit(href)
        if u.scheme or u.netloc:continue
        path=unquote(u.path) or name
        if not (ROOT/path).is_file():errors.append(f'{name}: missing {path}')
        if u.fragment and path in pages and u.fragment not in pages[path].ids:errors.append(f'{name}: missing anchor {href}')
assert len(pages)==9, f'Expected nine pages, found {len(pages)}'
assert not errors, '\n'.join(errors)
print(f'PASS: {len(pages)} pages; {len(seen_artwork)} unique artwork placements; all local links, anchors, images, headings and chapter controls present.')
