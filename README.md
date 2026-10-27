# globaldemocracyinitiative.org

The Global Democracy Initiative's site, built around its main project, Gloki: one HTML page, an
imprint and a privacy page, one CSS file, self-hosted fonts, inline SVG drawings, no framework,
no script and no third-party request. Deploys from `main` with GitHub Pages. The Global Democracy Initiative
is a project of Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the page. `imprint.html`, `privacy.html`: the legal pages.
- `assets/`: the GDI network mark (`gdi-mark.svg`, from the 2022 logo), the Gloki mark, the two
  screenshots (no longer on the page; kept for the app docs), the fonts (Hammersmith One and Cabin, both OFL; licences beside them).
- `PRODUCT.md`: the product facts the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md`: the page's direction contract.

## Before it goes live

- **Blocker:** the form posts to `REPLACE-WITH-GDI-NEWSLETTER`. Create the separate GDI newsletter
  in Buttondown and put its username in the form's `action` in `index.html`. The privacy line
  under the form promises sign-ups never get the YWF newsletter; `privacy.html` must name the new list.
- Check every quote and number word for word on its source page. They are marked
  `<!-- [check: …] -->` in `index.html`; sources in `docs/research-gdi-positioning.md` (A–D) and,
  for the Berners-Lee quote (Q2), a copy of *Weaving the Web* (1999).
- The status board rows marked in the comment above the table wait on Ouri's answers
  (`docs/positioning-gdi.md` §5). Don't upgrade a status without his sign-off.

- Buttondown (`YoungWorldFederalists`): create the three door tags (`solve-global-issues`,
  `build-digital-democracy`, `contribute-a-node`), turn on double opt-in, and decide whether
  waitlist sign-ups also get the YWF newsletter. The privacy page promises email "about Gloki and
  the Global Democracy Initiative" only.
- Cloudflare Email Routing: forward `hello@globaldemocracyinitiative.org` to a YWF inbox. The page,
  imprint and privacy page all give that address.
- DNS, once the domain transfer completes: GitHub Pages A/AAAA records on the apex and a `www`
  CNAME to `young-world-federalists.github.io`, all **DNS only** (grey cloud). Then set the custom
  domain in the repo's Pages settings, which commits a `CNAME` file, and enforce HTTPS.
- Have someone check the imprint and privacy wording; it was drafted from the YWF bylaws and the
  2026 UNFCCC submission, not by a lawyer.

## Local preview

    python3 -m http.server 8787

then open http://127.0.0.1:8787/.
