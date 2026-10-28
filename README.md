# globaldemocracyinitiative.org

The Global Democracy Initiative's site, built around its main project, Gloki: one HTML page, an
imprint and a privacy page, one CSS file, self-hosted fonts, two real app screenshots, no framework.
The only third-party requests are the waitlist form's: Brevo's form script and Cloudflare
Turnstile. Deploys from `main` with GitHub Pages. The Global Democracy Initiative is a project of
Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the page. `imprint.html`, `privacy.html`: the legal pages.
- `confirmed.html`: where Brevo sends people after they click the confirm link (`/confirmed`).

## Waitlist

The form in `#join` posts to Brevo (the GDI account, list "GDI waitlist", attribute `INTEREST`),
with double opt-in, Cloudflare Turnstile (widget "GDI waitlist form" in the YWF Cloudflare
account) and Brevo's `main.js` showing the messages on the page. Keep the field names (`EMAIL`,
`INTEREST[]`), the sitekey and the `sib-`/`entry__` classes: Brevo's script depends on them. It is
separate from the YWF newsletter on purpose.
- `assets/`: the GDI network mark (`gdi-mark.svg`, from the 2022 logo), the Gloki mark, the two
  screenshots, the fonts (Hammersmith One and Cabin, both OFL; licences beside them).
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

- Have someone check the imprint and privacy wording; it was drafted from the YWF bylaws and the
  2026 UNFCCC submission, not by a lawyer.

## Local preview

    python3 -m http.server 8787

then open http://127.0.0.1:8787/.
