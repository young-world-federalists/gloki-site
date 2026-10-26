# Brief: reposition the Global Democracy Initiative (next site session)

Written 2026-10-26 at the end of S44 (gloki-engage) so a cold session can start warm.
Site repo `young-world-federalists/gloki-site`, `main` at the commit that adds this file.
Domain: globaldemocracyinitiative.org (YWF Cloudflare; transfer completing). The page in this repo
today is an interim version: Gloki-first, with GDI as the sender. It is fine to throw its concept away.

## What Eston said (26 Oct 2026, lightly cleaned)

- GDI is being **rebuilt from first principles**. The 2021 coalition, the old Webflow site and the
  2023 white paper are history and context for an "about" or history section, not the plan.
- Gloki has moved far from the white paper. The current work is Ouri's backend: a new internet,
  "Web5", people holding their own data, blind servers, encryption, even **Reticulum** (mesh over
  radio). The democracy features are built on top of that.
- **Position GDI on the backend**: providing the foundation for one person, one vote, safe
  encryption and decentralized infrastructure. Many global democracy apps are being built right
  now; GDI's job is what they all lack. Gloki does provide a democracy platform and we want to
  get there, but right now the focus is the backend.
- **The story**: hope that technology can unite the planet instead of dividing it. In the 1990s
  people believed the internet would bring world peace. It didn't: social media divides us,
  blockchain became a rug-pull scheme, AI is controversial, digital tech as a whole has a bad name,
  and it is being used to enlarge our biggest problems. GDI builds something good, decentralized
  and empowering that unites humanity and helps us solve our greatest challenges: fighting fire
  with fire. Core belief: **there will be no global democracy without technology of some kind.**
- Ouri would want to see the Web5 / new-internet material on the page.
- **Waitlist sign-ups must NOT receive the YWF newsletter.** It is a separate thing.

## Advisor's frame (recommendations, Eston decides)

1. **GDI = the commons, Gloki = the first app on it.** The Matrix/Element pattern. One sentence each.
   Audiences then become: builders of democracy apps (use the backend), people with a server or a
   radio (carry the network), funders and researchers, and only then end users.
2. **Mission plus status, never product claims.** The sovereignty spec (gloki-engage
   `docs/superpowers/specs/2026-10-22-sovereignty-security-track-design.md` §1) lists five
   properties: nobody can act as you, nobody can quietly rewrite the record, nobody can read your
   ballot, you can leave with your identity, losing your phone doesn't lose your vote. **Until each
   holds, public copy must not claim it.** Write "we are building X; here is where it stands" and
   keep a public status board. For an audience burned by crypto, that honesty is part of the pitch.
3. Avoid the words "Web5" and "blockchain" as headline vocabulary unless Eston and Ouri want them:
   both read as crypto to the people the story is trying to win back. Decide this explicitly.

## Workflow for the session

1. **Re-ground** (session-lifecycle rule: the brief is a map, not the territory). Read
   `PRODUCT.md`, this brief, and in gloki-engage on `origin/ui`: `docs/FOR_OURI_blind_servers.md`,
   the sovereignty spec above, MASTER_TODO §7 P12. If Gmail is connected, the 15 Oct 2026
   "Plan for Gloki beta" thread. Ask Eston for any Ouri material on Web5 / Reticulum / the agent.
2. **Research (one agent, web search, return sources and verbatim text only):**
   - 1990s quotes predicting the internet would bring peace or world harmony, each with exact
     wording, speaker, year and a primary-source URL. Candidates to verify, not to trust:
     John Perry Barlow, "A Declaration of the Independence of Cyberspace" (1996); Nicholas
     Negroponte, *Being Digital* (1995). Reject any quote that can't be traced to a primary source.
   - Two or three sourced facts for "technology now divides us" (social media polarisation,
     crypto fraud losses, AI concerns), recent and from reputable sources.
   - The landscape: global or transnational democracy apps being built now, and what they use
     for identity and one-person-one-vote. This is the positioning gap.
3. **Positioning one-pager** before any page copy: who it is for, the one-sentence promise, GDI
   vs Gloki, true-today vs being-built (with Ouri's sign-off on every technical word). Eston locks it.
4. **Copy**: three drafts in parallel from separate agents, each a different angle, e.g.
   (a) "the promise the internet broke", (b) "infrastructure for one person, one vote",
   (c) "fighting fire with fire". Give each the positioning one-pager, PRODUCT.md voice rules
   (plain, concrete, a 16-year-old second-language reader) and the claims rule. Eston picks or merges.
5. **Page concept**: likely new. The current line diagram maps signing up for Gloki; the new
   story is about a network. Run the Impeccable direction step again if installed.
6. **Build, then a claims audit** of every sentence against the five properties and the status board.
7. **Waitlist**: create a separate Buttondown newsletter for GDI (Buttondown supports several
   newsletters per account; check the plan allows it) and point the form at it. Do not reuse the
   YWF list with tags: an existing YWF subscriber who joins the waitlist would get tagged and could
   drop out of YWF sends. Update `privacy.html` with the new list.

## Still open from S44

- Buttondown: the separate GDI newsletter (above), double opt-in, door tags.
- Cloudflare Email Routing for hello@globaldemocracyinitiative.org.
- DNS cutover once the transfer completes (records in README), then custom domain + HTTPS.
- ~~Host copies of the 2021 concept and white paper PDFs~~ Done 26 Oct: `assets/docs/` (from
  Eston's Drive; the white paper is the "2024 White Paper").
- Legal read of `imprint.html` and `privacy.html`.

## Don't

- Don't claim encryption, decentralization, data ownership, ballot secrecy or radio transport as
  working. Mark them Planned or In test with the status board.
- Don't name the 2021 coalition partners as current members.
- Don't use fabricated quotes, numbers, testimonials, partner logos or a launch date.
