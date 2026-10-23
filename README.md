# gloki.app

The landing page for Gloki's beta: one HTML file, one CSS file, self-hosted fonts, two real app
screenshots, no framework and no third-party request. Deploys as a static site (GitHub Pages).

- `index.html`, `style.css` — the page.
- `assets/` — the Gloki mark, the two screenshots, the fonts (Hammersmith One and Cabin, both OFL;
  licences beside them).
- `PRODUCT.md` — product truth the page is written from (Impeccable `init`).
- `.impeccable/surfaces/index-html.md` — the page's direction contract.

## Before it goes live

- Replace `BUTTONDOWN_USERNAME` in `index.html` with the YWF newsletter's Buttondown username.
- Point gloki.app at the Pages site (CNAME) and enforce HTTPS.
- Decide one Buttondown list with a `tag` per door (as built) or one list per door.

## Local preview

    python3 -m http.server 8787

then open http://127.0.0.1:8787/.
