# GDI site: review shipped, Open Collective and Brevo rebranded (27 Nov 2026)

Paste everything below the line into a new Claude Code session to pick up. It replaces
`2026-11-26-gdi-site-review.md`, which describes the same work before it was published.

---

You are continuing work on the Global Democracy Initiative site, repo
`young-world-federalists/gloki-site`. GitHub Pages publishes `main` to
https://globaldemocracyinitiative.org, so **merging is publishing**: never merge without Eston's yes
in the session. A local clone is at `Gloki Build/gloki-site` on the 2TB Drive. macOS writes `._*`
files into `.git` there; run `find .git -name '._*' -delete` when git complains. The preview config
`gdi-site` in `Gloki Build/.claude/launch.json` serves the clone on port 8788.

## What is live (read back 27 Nov)

All merged, Pages built, each read back on the live site:

| PR | What |
|---|---|
| #5 | Removed the "Open the demo" row: its link had become the real beta sign-up |
| #6 | Eston and Ouri as co-leads; builders page and status board rewritten for ibc-go (MIT, Solidity on the EVM, Cordial Miners, passkeys); Google Cloud line replaced (YWF node in Germany); 16 object icons; shorter copy; status board layout and clipped glyphs fixed; dithered globe and crowd; Join button on the first screen (Turnstile `data-appearance="interaction-only"`); node diagram; closing Join button; Open Collective link; contents row on the builders page; `DESIGN.md` People and Things Rule and Dither Rule |
| #7 | Open Collective cover, PNG of the GDI mark, refreshed `.impeccable/design.json` |
| #8 | Builders page: the node and the app are both MIT |

Eston signed off on Ouri's behalf ("signs off") before #6 was merged. Board date: 27 November 2026.

Decisions Eston left to Claude and that shipped: "When it opens: after the two of us have tested it
on our own node"; the Berners-Lee quote and the US crypto-fraud paragraph are cut; the Open
Collective link stays.

## Outside the site, done 27 Nov

- **App licence:** `young-world-federalists/gloki-engage#35` merged (`c997d74`): MIT, "Copyright
  (c) 2026 Young World Federalists, Inc. and the Gloki contributors" (Eston approved the line).
  GitHub lists the repo as MIT. Nothing deployed.
- **Open Collective (opencollective.com/gloki):** About text updated to match the site (co-leads,
  passkey sign-up, no demo row, "servers store your data without reading it" under Planned). Read
  back from the public GraphQL API. Cover replaced with the figure grid
  (`docs/brand/2026-11-26-dither/oc-cover.png`); Open Collective's curved mask fades the lower-left
  figures. The blue Gloki logo is unchanged on purpose.
- **Brevo (GDI account, Chrome profile with deviceId 06ca759a):** templates #5 "GDI waitlist:
  double opt-in" and #6 "GDI waitlist: welcome" rebranded and saved active: current GDI mark
  (media library `gdi-mark-480`), Jost and Atkinson Hyperlegible, site ink colours, the teal and
  amber dot strip removed, thin border and 6px corners. Wording, subject lines, sender and the
  confirm and unsubscribe links are unchanged. The old `gdi-mark-144` image is still in the library,
  unused by these two.
- **Waitlist:** Eston submitted once on his phone after #6 and reported it "worked fairly well".

## Open

1. **No test email since the Brevo rebrand.** Sign up with a test address and look at both emails
   in a real inbox. Many mail apps ignore web fonts and fall back to a system face.
2. **Turnstile in automated browsers** shows its "Verify you are human" box, which pushes Join below
   the fold there. Real visitors should not see it; unconfirmed beyond Eston's own submit. To undo:
   remove `data-appearance="interaction-only"` in `index.html` and restore
   `.sib-captcha { min-height: 65px; }`.
3. **Brevo's other surfaces** (unsubscribe page, the four default templates) were not looked at.
4. **The globe's coastlines are hand-drawn** in `docs/brand/2026-11-26-dither/make.py`, not map data.
   Natural Earth (public domain) would need a download.
5. **Critique not re-run.** The 26 Nov critique scored 24/36
   (`.impeccable/critique/2026-11-26T13-23-23Z__index-html.md`). Not addressed from it: the
   half-filled "in test" figure reads as a skirt; "a network its members carry" is still in the hero
   and the sign-up chip; the chip "Carry the network" submits "Contribute a node"; the home page is
   still about 1,000 words.
6. **Business case** (discussed in chat only): no investor page. Ideas were grants and donations
   first, then paid support for a hosted verified-human login for civic platforms (Decidim, Consul,
   Loomio), then hosted nodes for organisations. Nothing on the site beyond the Open Collective link.
   The DTF proposal is on hold since 26 Nov: don't raise it unless Eston does.
7. Impeccable v4.11.1 is available (`npx impeccable update`); not run.
