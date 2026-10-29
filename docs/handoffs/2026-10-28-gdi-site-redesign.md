# GDI site: ship the planned design and the new mark (restart prompt)

Paste everything below the line into a new Claude Code session on Eston's computer (local, not
cloud: you'll want the built-in browser for previews and Claude in Chrome for anything logged in).

---

You are taking the Global Democracy Initiative site, repo `young-world-federalists/gloki-site`,
from the design that is live now to the design Eston chose: the **"One figure, one person"**
Isotype page with the **route B** GDI mark. It's built, but only on a draft branch, and the live
site moved on underneath it. Your job is to bring it onto current `main` without losing anything
that shipped since, get Eston's yes on a preview, and publish it.

Act as an experienced advisor: recommend, don't list options without a view. Write in plain
English and match the house voice.

## Where things stand (28 Oct 2026, re-check before relying on it)

**Live.** https://globaldemocracyinitiative.org is GitHub Pages from `main` with a custom domain.
HTTPS is enforced (Let's Encrypt, apex + www, renews itself). `www` and the old
`young-world-federalists.github.io/gloki-site/` URL both redirect to the apex. DNS is in the "YWF
Cloudfare" Cloudflare account (zone `a3abf426c33ba08e49603671e9a4fc54`), DNS only. The wrangler
token there can't read or edit DNS, so any DNS change is Eston in the dashboard, with you reading
it back with `dig`. **Merging anything into `main` publishes it to the live domain within a
minute or two.**

**What's on `main`** (`7fced32`):
- The 26 Oct page in the "line-diagram" world: Hammersmith One + Cabin, two app screenshots, and
  the 2022 GDI mark (`assets/gdi-mark.svg`, seven coloured nodes).
- `CNAME` (`d0dfaae`, contents `globaldemocracyinitiative.org`). **Never delete or change it**:
  that takes the site off the domain.
- The Brevo waitlist (PR #3, merged 28 Oct): the form in `#join`, Brevo `main.js` and Cloudflare
  Turnstile `api.js` at the end of `index.html`, waitlist rules appended to `style.css`,
  `confirmed.html` (Brevo's double opt-in redirects to `/confirmed`), and Brevo/Turnstile wording
  in `privacy.html`. Field names, the Turnstile sitekey and the form `action` must carry over
  exactly. The waitlist's own restart prompt is on branch `claude/waitlist-handoff`
  (`docs/handoffs/2026-10-28-gdi-waitlist.md`); read its "Open items".
- `imprint.html`, `README.md` ("Live setup" + "Still open"), `docs/brief-gdi-positioning.md`.

**The planned design: PR #1**, branch `claude/gdi-positioning-draft-ktjbo7`, draft, 26–27 Oct.
- Page concept "One figure, one person", an Isotype world. **Eston chose it.** The first screen
  acts out the vouching rule, and the status board uses the figure as its legend.
- **Mark: route B, Eston's choice.** The 2022 network keeps its seven nodes and links, redrawn in
  ink with heavier lines. One brand-blue newcomer sits where two links cross, so it has four links.
  There's a 32px header icon (`assets/gdi-icon-32.svg`), a 16px favicon (an X with a blue centre),
  a Jost 600 lockup and a 1200×630 `og-image.png`. Routes A–C and the reasoning are in
  `docs/brand/2026-10-26/README.md`.
- New `style.css`, with Jost + Atkinson Hyperlegible self-hosted. Old fonts and screenshots are
  removed. Adds `build.html` (for builders: how the node works, its gaps, Ouri's papers), hosts
  the 2021 concept note and the 2024 white paper in `assets/docs/`, and rewrites `DESIGN.md` and
  `.impeccable/design.json` for the new world.
- Passed Impeccable's finish review ("ship") and Playwright checks at 360/390/1440px.
- Still open on it: yellow `<mark class="todo">` placeholders (Pew figure, FBI IC3 crypto losses,
  a fake-accounts figure, Ouri's paper links, Ouri's list of hard problems), and Ouri's sign-off on
  the status-board wording. Its Buttondown step is **superseded**: the waitlist is on Brevo now.
  Its `docs/session-prompt-next.md` has the source-checking procedure; reuse it.

**The other draft: PR #2**, branch `claude/brave-thompson-2ab0ol`, draft, 27–28 Oct.
- A different page, "rings of trust", that keeps the old fonts and the 2022 mark.
- What it adds that PR #1 doesn't have: **naming locked by Eston on 27 Oct** (after PR #1 was
  built). "Gloki = the foundation" (one identity per person, your own record, a network its
  members carry); GDI is the mission; the democracy app gets its own name later. Door order keeps
  world federalists first. See `docs/positioning-gdi.md` on that branch.
- Its copy was source-checked on 28 Oct, with `[checked: …]` markers in `index.html`: the full
  Berners-Lee quote, crypto fraud as *reported* losses, "the evidence is mixed", "some" identity
  tools, white paper dated 2024. Also its claims rule: no "Web5", "blockchain" once and only as "not a blockchain in the
  crypto sense", and nothing that says Gloki *is* decentralized, secure, encrypted, private or
  anonymous.
- Still open: Ouri's status-board rows, the Web5/blockchain rule (waits on Ouri), the democracy
  app's name.

**PR #1 and PR #2 both conflict with `main`, and both would remove the Brevo waitlist.**

## First: confirm the plan with Eston

PR #1 says GDI builds the network and Gloki is "the first app on it". PR #2's later lock says
Gloki *is* the foundation. These can't both go on the page. Recommend this, and get his yes before
building:

> PR #1's design and route B mark, carrying PR #2's 27 Oct naming and its source-checked copy, on
> top of current `main` so the Brevo waitlist, `confirmed.html`, `CNAME` and the privacy wording
> all stay. One page plus `build.html`. PR #1 and #2 are then closed as superseded.

Also ask whether `build.html` ships now or later. Ask; don't assume.

## Then

1. **Branch from current `main`** (`claude/gdi-redesign`). Bring over PR #1's design: `style.css`,
   fonts, mark and icons, `og-image.png`, the Isotype markup in `index.html`, `build.html`,
   `DESIGN.md`, `.impeccable/`, and the hosted papers. Pick one folder for the papers
   (`assets/docs/` or `assets/papers/`) and fix every link to match.
2. **Rewrite the copy into that layout** from PR #2's locked naming and checked copy. Keep its
   claims rule and `[checked: …]` evidence. Anything PR #1 says that the 27 Oct naming
   contradicts gets rewritten, not kept.
3. **Keep from `main`, unchanged:** `CNAME`, the `#join` Brevo form block and both scripts,
   `confirmed.html`, the Brevo/Turnstile and tracking wording in `privacy.html`, `imprint.html`.
   Restyle the waitlist rules to the new tokens if needed, but keep field names, the sitekey and
   the `action`. Make sure `confirmed.html` and the legal pages pick up the new fonts and mark
   too.
4. **Placeholders:** clear or cut every `<mark class="todo">`. A number goes on the page only after
   you open its primary source and copy the exact sentence into the sources file. Ouri's rows and
   his hard-problems list wait for him: leave them as plain "being built" wording, not invented
   detail. Ask Eston before contacting Ouri; draft the message, don't send it.
5. **Check it:** run `python3 -m http.server 8787` in the repo, then open it in the built-in browser at
   360, 390 and 1440px. Check: one h1, no horizontal scroll, fonts load, the favicon and header
   icon render, and the share image is in place. Submit the waitlist from the preview once to
   confirm the form still posts. If the confirmation email is a real send, check with Eston first.
   Have a fresh agent run Impeccable's finish review against the direction contract.
6. **Show Eston the preview** (screenshots at phone and desktop width, plus the share image). Open
   a PR and **wait for his explicit yes** before merging. Merging deploys.
7. **After merge, read back the live site:** HTTP 200 on `/`, `/build`, `/privacy`, `/imprint`,
   `/confirmed`; the new `<title>` and `og:image`; the favicon; the `#join` form posting to Brevo;
   `CNAME` still present; Pages build `built`. Report what you read, not what you intended.
8. Close PR #1 and #2 as superseded, with Eston's OK, linking the new PR. Update `README.md` and
   write the next handoff in `docs/handoffs/`.

## Rules

- Never merge, push to `main`, or change DNS, Cloudflare, Brevo or GitHub settings without
  Eston's yes in the session. Branches and draft PRs are fine.
- No invented quotes, numbers, partners, testimonials or dates. If you can't verify it, cut it.
- Files under `docs/` are served publicly by GitHub Pages. Keep anything private out of the repo.
- At start, check `docs/handoffs/` and the other active sessions on this repo (the waitlist
  session may still be open) before touching `index.html`, `privacy.html` or `style.css`.
