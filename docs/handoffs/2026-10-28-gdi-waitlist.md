# GDI waitlist: review and close out (restart prompt)

> **Status: closed on 29 October 2026.** This prompt has been run. What happened and what is still
> open is in `2026-10-29-gdi-waitlist-closeout.md`. Don't run it again.

Paste everything below the line into a new Claude Code session.

---

You are picking up the GDI waitlist after it went live on 2026-10-28. The job now: review what
shipped, settle the open decisions with Eston, apply only what he approves, and close this part of
the project. No new features.

## Where things stand (as of 2026-10-28, re-check before relying on it)

- **Live:** the form in `#join` on globaldemocracyinitiative.org posts to Brevo, GDI account
  (login hello@globaldemocracyinitiative.org, in Chrome "Browser 2"). List "GDI waitlist" (#3),
  multiple-choice attribute `INTEREST` (Solve global issues, Build digital democracy, Contribute a
  node), double opt-in. Merged in young-world-federalists/gloki-site PR #3 as `7fced32`.
- **Emails:** template #5 (double opt-in, `{{ doubleoptin }}`) and #6 (welcome,
  `{{ unsubscribe }}`), styled to the site's `DESIGN.md`. The confirm link redirects to
  `/confirmed`.
- **Spam check:** Cloudflare Turnstile widget "GDI waitlist form" (Managed) in the YWF Cloudflare
  account. Allowed hostnames: globaldemocracyinitiative.org, sibforms.com, gdi-site.webflow.io.
  On screens 400px wide or less the page switches it to compact.
- **Hosted Brevo form:** restyled to match, captcha above the button.
- **Site pages:** `confirmed.html` added. `privacy.html` names Brevo SAS (France) and Turnstile,
  dated 28 October 2026. README has a "Waitlist" section.
- **Tested live end to end:** captcha, on-page success, confirmation email (SPF, DKIM, DMARC
  pass), redirect to `/confirmed`, welcome email, contact in list #3 only with the right
  `INTEREST`, no overflow at 360px.
- **DMARC:** `p=none; rua=mailto:rua@dmarc.brevo.com`.

## Open items

1. **The two open draft PRs would undo the waitlist.** gloki-site PR #1
   (`claude/gdi-positioning-draft-ktjbo7`) and PR #2 (`claude/brave-thompson-2ab0ol`) both branch
   from before `7fced32` and still have the Buttondown form in `index.html`. PR #1 also rewrites
   `privacy.html`. Whichever lands must keep the Brevo form block, the scripts at the end of
   `index.html`, the waitlist CSS in `style.css`, and the Brevo/Turnstile wording in
   `privacy.html`. Check who owns those PRs (other sessions) and tell them, or note it on the PR
   with Eston's OK. Don't merge or rebase them yourself.
2. **Test contacts.** Two `+gditest` contacts (`+gditest` and `+gditest2`) are in list #3. Eston
   deletes them; you only check whether they're gone.
3. **"One real person gets one vote"** in the welcome email (#6) needs Eston's approval or new
   wording.
4. **Open and click tracking** is on in Brevo and disclosed on the privacy page. Eston decides
   whether to keep it. If it goes off, take the sentence off the privacy page in the same change.
5. **Turnstile hostnames:** `gdi-site.webflow.io` is no longer used. Removing it is Eston's call,
   done in the Cloudflare dashboard.
6. **DMARC to `p=quarantine`** once a few weeks of reports at rua@dmarc.brevo.com come back clean.
   Not before mid-November 2026. Suggest a date, don't change DNS.
7. **Branded tracking subdomain** in Brevo: later, optional.
8. **Inbox placement:** the second confirmation email landed in Gmail's Promotions tab, the first
   in Updates. Worth one more look after the template wording is final. No fix needed now.
9. **Style issues the design checker flagged** in existing `style.css` rules (not the waitlist
   rules): a hover state with low contrast and body overflow clipping. Review, then fix only with
   Eston's OK.
10. **Legal wording** of the imprint and privacy page is still unreviewed (README "Still open").
    Not for this session to solve; just keep it listed.

## Do this

1. **Check first.** Read `docs/handoffs/` in gloki-site and look for other active sessions on GDI
   or the site. Read back the live state: the pages (`/`, `/confirmed`, `/privacy`), the form
   markup, the DMARC record, the open PRs, and in Brevo the list count and the two test contacts.
   Report what changed since this note.
2. **Review.** Review what PR #3 shipped (`git show 7fced32`), the live page at desktop and 360px,
   and templates #5 and #6. Cover: correctness against Brevo's `main.js` (field names, `sib-` and
   `entry__` classes, `data-value`, error and success panels, `AUTOHIDE`), keyboard and screen
   reader use of the form, contrast, the privacy page against what the form actually loads, and
   copy against the writing rules below. Ask Eston before running the local review panel (it sends
   the diff to cloud models). Rank findings by severity and show them before fixing anything.
3. **Decide.** Put items 3, 4, 5 and 9, plus any review findings, to Eston in one
   AskUserQuestion. Don't draft new claims or promises without asking.
4. **Apply.** Site changes go on a branch with a PR. Merging to `main` publishes live, so merge
   only with Eston's explicit OK in that session. Template or form changes in Brevo: save, send a
   test to a fresh `+gditest` address only, and read back what was saved.
5. **Close out.** Update the gloki-site README and this file's status, update the
   `gdi-waitlist-brevo` memory, write the closing handoff to `docs/handoffs/` and commit it to
   `main` (with Eston's OK, since `main` is live). Then tell Eston what is finished and what is
   still his.

## Ground rules (unchanged)

- Brevo stays on the free plan. Don't pay for or change any plan.
- Send email only to Eston's `+gditest` addresses. Don't import contacts.
- Never type, paste, print or store a password, API key or the Turnstile secret key. If a step
  needs one, stop and ask Eston to do it.
- GDI stays separate from YWF mail. Don't touch the YWF newsletter, the YWF Buttondown account or
  the World Passport Studio Brevo account. The Brevo MCP connector is linked to World Passport
  Studio, so don't use it here; use the Brevo web app in Chrome.
- Eston deletes contacts; you don't delete data.
- Branding follows gloki-site `DESIGN.md`. The old Webflow look (cream, coral, DM Sans) is out.
- Anything visitors read: plain, warm, short. No em or en dashes. Avoid phrasing that reads as
  AI-written.
- `docs/` on this repo is served publicly by GitHub Pages. Keep secrets and personal details out
  of anything committed here.
- After any deploy or settings change, read back the live state and report the read-back.
