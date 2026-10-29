# GDI waitlist: closed out (29 October 2026)

The waitlist review from `2026-10-28-gdi-waitlist.md` is done. This note records what was checked,
what changed and what is still open. No new waitlist work is planned. Re-check anything here before
relying on it.

## What is live

- The `#join` form on globaldemocracyinitiative.org posts to Brevo (GDI account, list "GDI waitlist"
  #3, attribute `INTEREST`, double opt-in), as merged in PR #3 (`7fced32`).
- The page loads only three hosts: the site itself, `sibforms.com` (Brevo) and
  `challenges.cloudflare.com` (Turnstile). It sets no cookies. This matches the privacy page.
- At 360px there is no horizontal scroll, Turnstile switches to compact, and the page has one h1.
  Error text is 5.0:1 and the fine print 7.6:1.
- DMARC is still `p=none; rua=mailto:rua@dmarc.brevo.com`.

## What changed on 29 October

- **Welcome email (#6).** The first paragraph now reads: "Thanks for confirming. We're building
  Gloki, a network its members carry. You get in because people who know you vouch for you." It
  replaces the "one real person gets one vote" clause, which describes a goal rather than what the
  test version does today. Eston approved the wording. It was saved, read back after a reload, and
  a test send arrived from hello@globaldemocracyinitiative.org.
- **Double opt-in email (#5)** passed the claims check unchanged.
- **Brevo test list** now has a second test address of Eston's alongside
  hello@globaldemocracyinitiative.org.
- **Open and click tracking** stays on (Eston's decision). The privacy page sentence that discloses
  it stays too.

## Handed to the site redesign

Three waitlist fixes went into the redesign branch `claude/gdi-redesign` (GDI Site Restart
session), not into a separate PR, because that branch replaces `index.html` and `style.css`. The
redesign shipped on 29 October as PR #4 (`e822e48`). Checked on the branch at `e3c4a05` and again
on `main` after the merge:

- Focus moves to the success or error panel when Brevo shows it. Before, `AUTOHIDE` hid the form
  while focus was still on the button.
- The third door's visible name is "Carry the network" everywhere. Its value stays
  "Contribute a node", which is the Brevo option.
- Handoff item 9 (body `overflow-x: hidden`, hover contrast) is gone with the new `style.css`.

The form action, sitekey, field names, `AUTOHIDE` and both scripts are unchanged from PR #3. Draft
PRs #1 and #2 are closed, so the open item about them undoing the waitlist is gone.

## Still open

- **A real submit on the redesigned page.** Not done yet (item 1 in
  `2026-10-29-gdi-redesign-shipped.md`). Eston, or a session with his OK, submits once on the live
  page with a fresh test address, then checks the success panel takes focus and the `INTEREST`
  choices arrive in Brevo. Turnstile doesn't allow localhost, so it can't be tested on a local
  preview. The same note flags that on phones the Turnstile check pushes the Join button down.
- **Test contacts.** List #3 still holds Eston's two test contacts from 28 October and no real
  sign-ups. Eston deletes them.
- **Turnstile hostname.** Eston is removing `gdi-site.webflow.io` from the "GDI waitlist form"
  widget in the YWF Cloudflare account. Read back the widget's hostnames afterwards.
- **DMARC to `p=quarantine`.** Look at the reports from mid-November 2026 (around 17 November). If
  they are clean, Eston changes the record in Cloudflare and you read it back with `dig`.
- **Branded tracking subdomain** in Brevo: later, optional.
- **Inbox placement:** worth one look once the welcome wording settles; an earlier confirmation
  landed in Gmail's Promotions tab.
- **Legal wording** of the imprint and privacy page is still unreviewed (README, "Still open").

## Ground rules

Unchanged from the 28 October prompt: Brevo stays on the free plan; send email only to Eston's
test addresses; never handle passwords, API keys or the Turnstile secret; keep GDI mail separate
from YWF; Eston deletes contacts; `docs/` is public, so keep personal details out of it.
