# GDI site review and draft update (26 Nov 2026)

> **Superseded by `2026-11-27-gdi-site-shipped.md`.** Everything below was published on 27 Nov.

Paste everything below the line into a new Claude Code session to pick up.

---

You are continuing work on the Global Democracy Initiative site, repo
`young-world-federalists/gloki-site`. GitHub Pages publishes `main`, so **merging is publishing**.
Never merge without Eston's yes in the session. A local clone is at
`Gloki Build/gloki-site` on the 2TB Drive (macOS writes `._*` files into `.git` there: delete them
with `find .git -name '._*' -delete` when git complains).

## Published today

PR #5 (squash `df398b9`, Eston's yes): removed the "Open the demo" row from the status board. Its
link went to the gloki-engage Pages site, which since 20 Nov is the real beta sign-up with the
founder slot open. Read back: no "Open the demo" and no link to that address on the live page.

## PR #6 (`claude/co-leads-board-polish`): published 27 Nov on Eston's yes

- Who we are: Eston and Ouri as co-leads.
- Accuracy: builders page and status board describe ibc-go (MIT, Solidity on the EVM, Cordial
  Miners, passkeys) instead of the Python node; the Google Cloud line is replaced.
- Sixteen object icons, shorter copy, status-board layout, clipped glyphs fixed.
- Two dithered pictures (globe, crowd) from `docs/brand/2026-11-26-dither/make.py`.
- Join button on the first screen: Turnstile set to `data-appearance="interaction-only"`.
- A node diagram on the builders page.
- `DESIGN.md`: People and Things Rule (replaces One Glyph), Dither Rule.

## Before #6 can publish

1. **Ouri's sign-off** on the status changes and the known-gaps list (the PR body lists the points).
   Contact Ouri only through Eston.
2. **Eston's decisions:** the "When it opens" wording; the MIT line (gloki-engage has no licence
   file); the board date; the cut Berners-Lee quote and crypto-fraud paragraph; the Open Collective
   link (that page still says Eston leads the project and builds the app).
3. **The waitlist form is untested with the Turnstile change.** Turnstile refuses localhost, so the
   invisible mode could not be exercised in the preview. After publishing, submit once on the live
   page with a `+gditest` address and check the success panel, the confirm email and the INTEREST
   values in Brevo. If the submit fails, remove `data-appearance="interaction-only"` from
   `index.html` and restore `.sib-captcha { min-height: 65px; }`.

## Not done

- `.impeccable/design.json` is older than `DESIGN.md` (run `/impeccable document`).
- The globe's coastlines are a rough hand-made outline, not map data.
- The critique snapshot is in `.impeccable/critique/` (24/36 before these changes); not re-run.
- Business case (support contracts for a verified-human login, hosted nodes, grants) was discussed
  only in the session; nothing on the site.
