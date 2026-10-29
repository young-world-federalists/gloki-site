# globaldemocracyinitiative.org

The Global Democracy Initiative's site, built around Gloki, the foundation it is building: a home
page and a page for builders, an imprint and a privacy page, one CSS file, self-hosted fonts, no
framework. The design is "One figure, one person", an Isotype world (`DESIGN.md`).
The only third-party requests are the waitlist form's: Brevo's form script and Cloudflare
Turnstile. Deploys from `main` with GitHub Pages. The Global Democracy Initiative is a project of
Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the home page. `build.html`: for builders (the node, the gaps, the
  research). `imprint.html`, `privacy.html`: the legal pages.
- `confirmed.html`: where Brevo sends people after they click the confirm link (`/confirmed`).

## Waitlist

The form in `#join` posts to Brevo (the GDI account, list "GDI waitlist", attribute `INTEREST`),
with double opt-in, Cloudflare Turnstile (widget "GDI waitlist form" in the YWF Cloudflare
account) and Brevo's `main.js` showing the messages on the page. Keep the field names (`EMAIL`,
`INTEREST[]`), the sitekey and the `sib-`/`entry__` classes: Brevo's script depends on them. It is
separate from the YWF newsletter on purpose.
- `assets/`: the GDI mark, route B (`gdi-mark.svg`, `gdi-icon-32.svg`, favicon `gdi-icon-16.svg`;
  see `docs/brand/2026-10-26/`), the share image `og-image.png`, the fonts (Jost and Atkinson
  Hyperlegible, both OFL; licences beside them), the 2021 concept and 2024 white paper in
  `assets/papers/`. `gloki-icon.png` is unused by the pages but kept because emails may link to it.
- `docs/positioning-gdi.md`: the locked naming (Gloki = the foundation) and the status-board basis
  (§5). Don't upgrade a status row without Ouri's sign-off.
- `PRODUCT.md`: the product facts the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md`: the page's direction contract.

## Live setup

- The site is live at globaldemocracyinitiative.org: GitHub Pages A/AAAA records on the apex and a
  `www` CNAME to `young-world-federalists.github.io`, all **DNS only** (grey cloud), HTTPS
  enforced. Keep the `CNAME` file: without it the site falls off the domain. Merging to `main`
  publishes straight away.
- Cloudflare Email Routing forwards `hello@globaldemocracyinitiative.org`, the address the page,
  imprint, privacy page and waitlist emails give.

## Still open

- Ouri's sign-off on the status board, the Google Cloud line, his list of open problems for
  `build.html`, and the "blockchain"/"Web5" wording. A draft email waits on Eston.
- A real waitlist submit on the live page since the redesign (Turnstile blocks automated tests).
- On phones, the Turnstile check pushes the Join button below the first screen.
- Have someone check the imprint and privacy wording; it was drafted from the YWF bylaws and the
  2026 UNFCCC submission, not by a lawyer.

## Local preview

    python3 -m http.server 8787

then open http://127.0.0.1:8787/.
