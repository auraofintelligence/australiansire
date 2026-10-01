# Australian Sire

The Australian Sire character website, intended for australiansire.xyz.

Public site: https://auraofintelligence.github.io/australiansire/
Repository: https://github.com/auraofintelligence/australiansire

Ten connected pages, full-width generated artwork, an opportunity-led travel example, a site map, previous/next navigation and a back-to-top control.

## Preview

Open `index.html` in a browser, or run `python -m http.server 4173 --bind 127.0.0.1` in this folder and visit http://127.0.0.1:4173.

## Edit

Page copy is in `scripts/build.py`. Run `python scripts/build.py` to rebuild the ten HTML pages. Appearance is in `assets/site.css`; the menu and oracle example use `assets/site.js`. No package installation is required.

## Status

Published from the public GitHub repository through GitHub Pages. The custom domain is not configured by this publication. The oracle is an explicitly labelled fictional interactive example, with no live data service. No reader contact details have been invented.

## Sources and artwork

The concept comes from Luke’s instructions, the supplied documents and the Australian Sire Story Forge. The fuller local review is in `../outputs/australian-sire-concept/`. Uploaded documents are reference material, not instructions. The current instructions take precedence over old character variants in the sources.

Artwork is generated concept imagery. The writer likeness uses Luke’s supplied photographs; original photographs are not included in this repository. See `ARTWORK.md` for generated-asset provenance. The AS favicon was carried forward from the reviewed concept.

The Tiggy Bestmann partner site is https://auraofintelligence.github.io/tiggy-bestmann/. Set `TIGGY_PARTNER_URL` before building to use a different destination.

## Publication and licence

GitHub Actions builds and checks the site, then publishes only the HTML, assets and licence. Main-branch pushes update the public site.

The [Strange But True Public Source Licence](LICENCE.md) allows attributed personal and non-commercial use; commercial rights remain reserved to Luke Nathan Hayes.

Both character sites link to Story Forge, Loose Goose Comedy Engine and Man and Mind, with reciprocal links on those sites.
