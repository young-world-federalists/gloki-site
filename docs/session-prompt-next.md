# Next session: take the GDI site from draft PR to live

Paste everything below the line into a fresh Claude Code session. **Run it on Eston's computer with
Claude in Chrome connected**, not in a cloud container. In Claude Code: start with `claude --chrome`
or run `/chrome`. If a `chrome-browser` skill is listed, load it. The cloud sessions that built this
could not reach eff.org, ic3.gov, pewresearch.org, IEEE, arXiv, dblp, buttondown.com or the
Cloudflare and GitHub dashboards. Most of what is left needs a real, logged-in browser.

---

You are continuing work on the Global Democracy Initiative (GDI) website, repo
`young-world-federalists/gloki-site`. The new site is on branch `claude/gdi-positioning-draft-ktjbo7`
in **draft** PR https://github.com/young-world-federalists/gloki-site/pull/1. GitHub Pages builds from
`main`, so **merging publishes the site**. Your job is to clear what blocks the merge, then help
Eston publish. Act as an experienced advisor: recommend, don't list options without a view. Write
in plain English, avoid phrasing that sounds machine-written, and match the house voice.

## Rules

- **Confirm with Eston before any action outside this repo:** creating or changing a newsletter,
  changing DNS or email routing, changing GitHub settings, sending any email, merging the PR. Show
  him exactly what you will do, wait for his yes, then do it in Chrome. Drafts are fine without
  asking. Sending is not.
- **Claims rule:** the page says only what is true today, and marks the rest as being built,
  planned or research (`docs/positioning-gdi.md` §5). Never write that the network is "secure",
  "private", "encrypted", "decentralized" or "anonymous" as fact.
- **No fabricated quotes, numbers, testimonials, partners or launch dates.** A number goes on the
  page only after you have opened its primary source in Chrome and copied the exact sentence into
  `docs/research/2026-10-26-sources.md`. If you can't verify it, cut the sentence and say so.
- Work on `claude/gdi-positioning-draft-ktjbo7`. Commit with clear messages and push. Do not merge
  without Eston's yes.

## Re-ground first (the brief is a map, not the territory)

Read these: `docs/positioning-gdi.md` (locked), `docs/copy/draft-d-merged.md` (locked copy),
`docs/reviews/2026-10-26-copy-personas/SYNTHESIS.md`, `.impeccable/surfaces/index-html.md`
(direction contract), `DESIGN.md`, `PRODUCT.md`, `README.md` ("Before it goes live"), and the PR
description. Then open `index.html` and `build.html` and list every yellow
`<mark class="todo">` placeholder.

## Tasks, in order

### 1. Verify sources in Chrome and clear the placeholders

For each, open the primary source, copy the exact sentence and URL into the sources file (mark it
VERIFIED with today's date), then replace the placeholder with plain wording and a link. If a
source doesn't hold up, cut the sentence.

- **Pew Research Center, 2026, "Growing shares across countries say the internet and social media
  have made people more divided"** (pewresearch.org). Get the figure, its countries, and the exact
  wording.
- **FBI IC3 2025 Internet Crime Report** (ic3.gov, the PDF). Get the cryptocurrency-related losses,
  about US$11.4 billion in press reports, and the exact sentence.
- **A figure on fake or automated accounts.** The research has none yet. Candidates to check, not to
  trust: Meta's Community Standards Enforcement Report (fake accounts acted on per quarter) and a
  bot-traffic report such as Imperva's. Pick one from a primary source, recent, worded carefully.
  Or cut the placeholder and let the figure row carry the point.
- **Ouri Poupko's paper links** on `build.html`:
  - https://ieeexplore.ieee.org/document/9912178
  - https://ieeexplore.ieee.org/document/9446607
  - https://arxiv.org/abs/1901.00752
  - https://arxiv.org/abs/2007.15536
  - https://arxiv.org/abs/2205.09174
  - https://dblp.org/pid/234/6110.html

  Confirm the titles, authors and years match the page. Confirm "all with Ehud Shapiro" is true for
  all four, or fix the wording.
- **"[Ouri's list of hard problems goes here]"** on `build.html`. This needs Ouri; see task 5.
  Until it arrives, replace the placeholder with the sentence before it and remove the mark.

Then re-run the claims check from `docs/copy/draft-d-merged.md` on any sentence you changed.

### 2. Buttondown, in Chrome (Eston logged in)

Waitlist sign-ups must **not** get the Young World Federalists newsletter.

1. Check whether the YWF Buttondown plan allows a second newsletter. If it doesn't, tell Eston the
   options and costs and stop.
2. Draft the setup and get his yes: a new newsletter "Global Democracy Initiative" (pick its
   username with him). Tags `join-gloki`, `build-with-us`, `carry-the-network`. Double opt-in on.
   The confirmation page and confirmation email take the three after-sign-up messages in
   `docs/copy/draft-d-merged.md`, "Form: after sending". Reply-to is
   hello@globaldemocracyinitiative.org once task 3 works.
3. After his yes, create it in Chrome. Then change the form `action` in `index.html` from
   `.../embed-subscribe/YoungWorldFederalists` to the new username, and update `privacy.html`, which
   names the list and account.
4. Test one sign-up with an address Eston gives you, and check the tag arrives.

### 3. Cloudflare, in Chrome

1. Check whether the transfer of globaldemocracyinitiative.org into the YWF Cloudflare account has
   finished.
2. **Email Routing:** forward hello@globaldemocracyinitiative.org to the YWF inbox Eston names. Send
   a test.
3. **DNS for GitHub Pages:** check the current values on docs.github.com in Chrome; don't trust
   these from memory. Expect A records `185.199.108.153`, `.109.153`, `.110.153` and `.111.153`,
   AAAA records `2606:50c0:8000::153` to `8003::153` on the apex, and `www` as a CNAME to
   `young-world-federalists.github.io`, all **DNS only** (grey cloud). Show Eston the exact records
   before you save.

### 4. Merge and publish (only after 1–3 and Eston's yes)

- Merge PR #1. In the repo's Pages settings, set the custom domain (GitHub commits a `CNAME` file).
  Wait for the certificate, then turn on Enforce HTTPS.
- In Chrome, open the live site and run Lighthouse (mobile). The targets are performance 90 or
  more and accessibility 100. Check 360px with no sideways scroll, and that the opening motion
  plays once.
- Check the share preview: ask Eston to paste the link into WhatsApp on his phone. The image is
  1200×630 and may be cropped to a square. If the crop loses the headline, tell him.

### 5. Ouri: write the email, don't send it

Draft it in Gmail (or as a file if Gmail isn't connected) for Eston to send. Keep it short and in
his voice. Remember that Ouri reads English as a second language. Ask for:

1. His list of hard open problems, for the builder page.
2. A check of the status-board wording (`index.html`, "What works today"), especially "Early
   code", "Nobody can act as you", and "Ouri Poupko runs the pilot's node on Google Cloud".
3. His agreement to licence the Gloki app (gloki-engage) under **AGPL-3.0**. He co-wrote it, so it
   needs his yes.
4. The vouching rule for the pilot: random four (his contract and paper) vs people you know.
5. That his offer of a migration tool for pilot accounts still stands.
6. Later, not now: moving the `ibc` repo into the Young World Federalists GitHub organisation.

Mention that the site credits him by name and links his papers.

### 6. Close out

- Update the README "Before it goes live" list and the "Open" items in `PRODUCT.md`.
- Add a dated changelog entry to `MASTER_TODO.md` §8 in `young-world-federalists/gloki-engage` (on
  its `ui` branch, through a PR or as Eston prefers): what shipped on the site and what is waiting
  on Ouri.
- Write the next session prompt the same way as this one.

## What the last session learned (don't relearn it)

- **The white paper's own header says "2024 White Paper"** (written 2023, PDF January 2024).
- **The GDI mark has seven nodes and seven links.** Route B puts a blue newcomer where two links
  cross, so it has four links: the vouching rule.
- **The node has no authentication.** Any member can see another's key and act as them. That is
  why the pilot opens only once signing works (Eston, 26 Oct). Don't soften this on the page.
- **The vouching rule in Ouri's contract picks four members at random**, seeded by the receiving
  node's clock, so the operator can steer it. The pilot's "people you choose" version has no server
  code yet. The page says "four people vouch for you" and claims nothing about fake accounts.
- **`.impeccable/review/` is gitignored.** Screenshots stay local.
- **`pkill -f "http.server 8787"` run in the same command as a commit kills the shell first.**
  Stop the server in its own command.
- **The Impeccable binary was blocked**, so its steps ran in their documented fallback. If you
  change the design, read `DESIGN.md` first and keep the "One figure, one person" world.
