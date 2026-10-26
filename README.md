# globaldemocracyinitiative.org

The Global Democracy Initiative's site: a home page, a page for builders, an imprint and a privacy
page, one CSS file, self-hosted fonts, no framework and no third-party request. Deploys from `main` with GitHub Pages. The Global Democracy Initiative
is a project of Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the home page. `build.html`: how the network works, for builders.
  `imprint.html`, `privacy.html`: the legal pages.
- `assets/`: the GDI network mark (`gdi-mark.svg`, from the 2022 logo); `docs/` holds the 2021
  concept note and the 2024 white paper; `fonts/` holds Jost and Atkinson Hyperlegible (both OFL,
  licences beside them).
- `PRODUCT.md`: the product facts the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md`: the page's direction contract.

## Before it goes live

- Buttondown: create a separate GDI newsletter (waitlist sign-ups must not get the YWF newsletter),
  point the form's `action` in `index.html` at it, create the three tags (`join-gloki`,
  `build-with-us`, `carry-the-network`) and turn on double opt-in. Put the after-sign-up messages
  from `docs/copy/draft-d-merged.md` in its confirmation page and email. Update `privacy.html` with
  the new list.
- Remove the yellow `[...]` placeholders on the home and builder pages: verify the numbers, add
  Ouri's list of open problems, and open each paper link once in a browser.
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
