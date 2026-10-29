# GDI redesign shipped (29 Oct 2026)

Paste everything below the line into a new Claude Code session on Eston's computer to pick up.

---

You are continuing work on the Global Democracy Initiative site, repo
`young-world-federalists/gloki-site`. GitHub Pages publishes `main` to
https://globaldemocracyinitiative.org, so **merging is publishing**. Never merge without Eston's
yes in the session. Start by reading `README.md`, `docs/positioning-gdi.md` and this file, and
check for other active sessions on the site, the waitlist or Gloki.

## What shipped

PR #4 (squash `e822e48`, merged 29 Oct with Eston's yes). It is the "One figure, one person"
Isotype page and the route B mark, carrying the 27 Oct naming (GDI = the mission, **Gloki = the
foundation**, world federalists first) and PR #2's source-checked copy (`[checked: …]` comments in
`index.html`), on top of the Brevo waitlist. `build.html` shipped too. It supersedes PRs #1 and #2,
which are still open as drafts: close them as superseded with Eston's OK, linking #4.

The status board follows `docs/positioning-gdi.md` §5, plus:
- A developer-node row, from Ouri's `ibc` README.
- Ouri's 29 Oct answers: in the test version you are verified by asking someone who is already
  verified; joining a community works; signing, signed logs and blind servers are planned, not
  being built; the node checks no signatures.

Internal security details from the Gloki Build session (who can repoint the verified list, open
contract deploy) are deliberately **not** on the public pages. Keep them off.

## Read back after merge (29 Oct, about 11:10 UTC)

| Check | Expected | Actual |
|---|---|---|
| Pages build | `built` for e822e48 | built e822e48 |
| `/`, `/build`, `/privacy`, `/imprint`, `/confirmed` | 200 | 200 each |
| Papers, og-image, icons, `gloki-icon.png` | 200 | 200 each |
| `<title>` | "Global Democracy Initiative: one real person, one vote" | same |
| `og:image` | `/assets/og-image.png` | same |
| Favicon | `assets/gdi-icon-16.svg` | same, header icon renders |
| Form `action`, sitekey | unchanged from #3 | same Brevo URL, `0x4AAAAAAFqCnrqcYK-xXckD` |
| `CNAME` | `globaldemocracyinitiative.org` | same |
| http and www | 301 to https apex | 301 to https apex |
| Fonts, console | Jost + Atkinson load, no errors | loaded, no console errors |
| Real waitlist submit | Brevo success panel, confirm email | **not tested**: Turnstile showed an interactive "Verify you are human" check in the automated browser |

## Open

1. **A real waitlist submit since the redesign.** Eston (or the waitlist session, with his OK and a
   `+gditest` address he then deletes) submits once on the live page. Check the success panel
   appears and takes focus, and that the INTEREST choices arrive in Brevo.
2. **Two wording decisions for Eston**, both in `index.html`:
   - The beta section says it opens "once your phone can sign what you do". That was Eston's 26 Oct
     rule, but Ouri now says signing isn't coming soon.
   - The hero caption "You get in when four people who know you vouch for you." reads as present
     fact while vouching is in test. Recommended: "You'll get in when…".
3. **Ouri.** A draft email (status rows and the Google Cloud line, open problems, the
   blockchain/Web5 wording, the paper list) was shown to Eston in the 29 Oct session; nothing was
   sent. Contact Ouri only through Eston.
4. **Phone first screen.** The Turnstile check (compact, 148px) pushes the Join button about 180px
   below the fold at 360–390px. Moving the button above the check would break focus order. If it
   matters, agree a fix with whoever owns the waitlist form.
5. Legal review of the imprint and privacy wording (README "Still open").
