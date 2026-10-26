# globaldemocracyinitiative.org

The Global Democracy Initiative's site, built around its main project, Gloki: one HTML page, an
imprint and a privacy page, one CSS file, self-hosted fonts, two real app screenshots, no framework
and no third-party request. Deploys from `main` with GitHub Pages. The Global Democracy Initiative
is a project of Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the page. `imprint.html`, `privacy.html`: the legal pages.
- `assets/`: the GDI network mark (`gdi-mark.svg`, from the 2022 logo), the Gloki mark, the two
  screenshots, the fonts (Hammersmith One and Cabin, both OFL; licences beside them).
- `PRODUCT.md`: the product facts the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md`: the page's direction contract.

## Before it goes live

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
