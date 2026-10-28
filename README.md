# globaldemocracyinitiative.org

The Global Democracy Initiative's site, built around its main project, Gloki: one HTML page, an
imprint and a privacy page, one CSS file, self-hosted fonts, inline SVG drawings, no framework,
no script and no third-party request. Deploys from `main` with GitHub Pages. The Global Democracy Initiative
is a project of Young World Federalists, Inc., which publishes the site.

- `index.html`, `style.css`: the page. `imprint.html`, `privacy.html`: the legal pages.
- `assets/papers/`: the 2021 GDI concept and the 2024 white paper, hosted here instead of on Webflow.
- `assets/`: the GDI network mark (`gdi-mark.svg`, from the 2022 logo), the Gloki mark, the two
  screenshots (no longer on the page; kept for the app docs), the fonts (Hammersmith One and Cabin, both OFL; licences beside them).
- `PRODUCT.md`: the product facts the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md`: the page's direction contract.

## Before it goes live

- **Blocker: the waitlist.** The form posts to `REPLACE-WITH-GDI-NEWSLETTER`. Decided 28 Oct: a
  separate free Buttondown account for GDI (not the YWF account; a second newsletter there costs
  $29/month). Create it with double opt-in and the tags `solve-global-issues`,
  `build-digital-democracy`, `contribute-a-node`, then put its username in the form `action` in
  `index.html` and name it in `privacy.html`.
- Quotes and numbers: checked 28 Oct against their sources (marked `[checked: …]` in `index.html`).
- The status board waits on Ouri's answers (`docs/positioning-gdi.md` §5). Don't upgrade a status
  without his sign-off.
- Email: done 28 Oct. Cloudflare Email Routing forwards `hello@globaldemocracyinitiative.org` to
  Eston (MX, SPF and DKIM records added).
- DNS cutover, once the registrar transfer (Tucows to Cloudflare, started 28 Oct) completes. Today a
  Cloudflare redirect rule sends the domain to gdi-site.webflow.io, and the apex and `www` A records
  point at the placeholder 192.0.2.1, proxied. To cut over: delete the redirect rule and the two
  placeholder A records; add GitHub Pages' four A records on the apex and a `www` CNAME to
  `young-world-federalists.github.io`, all **DNS only** (grey cloud); keep the MX and TXT records.
  Then set the custom domain in the repo's Pages settings (it commits a `CNAME` file) and enforce HTTPS.
- Have someone check the imprint and privacy wording; it was drafted from the YWF bylaws and the
  2026 UNFCCC submission, not by a lawyer.

## Local preview

    python3 -m http.server 8787

then open http://127.0.0.1:8787/.
