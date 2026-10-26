# GDI positioning: draft to lock

**Status:** draft for Eston to lock, 26 Oct 2026. Technical words in §4 and §5 need Ouri's sign-off.
No page copy gets written until this is locked. Sources: `docs/research/2026-10-26-sources.md`.

## 1. The promise (pick one)

- **A.** The Global Democracy Initiative is building the foundation global democracy needs: an open
  network where each person counts once, keeps their own data, and no company or government is
  in charge.
- **B.** There will be no global democracy without technology. We are building the part every
  democracy app is missing: a way to know each voice belongs to one real person, across borders.

Recommendation: **A as the promise, B's first sentence as the opening line.** A says what we build.
B says why it has to exist. Both clear the 16-year-old second-language reader.

## 2. The gap we fill

The landscape research checked the identity layer behind today's democracy tools:

| How they decide who counts | Who | Why it fails across borders |
|---|---|---|
| A government or resident register | Consul, Decidim (city census, eID) | No world register exists |
| A voter list the organiser supplies | Vocdoni | Someone has to own the list |
| No check at all | Polis, Talk to the City | Not one person, one vote |
| Tokens or wallets | Democracy Earth (looks inactive) | Money votes |
| Proof-of-human add-ons | World ID, BrightID (vouching), Human Passport | Mostly used by crypto projects; a separate service sits in the middle. Check each before naming it on the page |

**The gap:** nobody offers one person, one vote across borders without a government, a company,
a face scan or money in the middle. GDI's answer: people who know you vouch for you, your data
stays on your own server, and the network is carried by its members.

**Expect "why not BrightID?"** It is the closest neighbour: it also uses vouching by close
contacts and stores no biometrics. We need a one-line answer from Ouri before launch (his
trust-graph research and the per-person server are the likely answer).

## 3. GDI and Gloki, one sentence each

- **GDI builds the network:** identity by vouching, a personal agent that holds each person's data,
  and nodes that people host. Open, so other democracy apps can use it.
- **Gloki is the first app on it:** where real people test the network now.

Same pattern as Matrix (the protocol) and Element (the app). That comparison is for us, not the
page. The network stays unnamed for now: "the network". Note that the 2023 white paper was
"Gloki: Global Digital Voter Identity", so Gloki first meant the identity layer. The page can say
that honestly in the history section: the idea grew into a network and Gloki became its first app.

## 4. Who it is for, in order

1. **Builders and researchers of democracy tech.** They need the gap (§2), the design, the papers
   and a way to help. Today that is "help shape it", not "build on it": there is no public API.
2. **People who will carry the network.** A server now, radio later. The door stays dark until a
   node image exists, and the page says so.
3. **Funders.** A contact line, not a door. The sovereignty spec already names NLnet and OTF as
   funders of open civic infrastructure; check their current calls.
4. **People who want to use Gloki.** The waitlist. In practice this is the warmest traffic (world
   federalists and academics from Eston's network), so the story must still work for them.

Proposed doors: **Build with us / Carry the network / Join Gloki.** This reverses the 15 Oct
order (solve, build, contribute). Eston decides.

## 5. True today vs being built

Rule: the page says "we are building X; here is where it stands." Ouri signs off on every row.

| Property or feature | Status | Basis |
|---|---|---|
| Get in when four people who know you vouch | **In test** (in the app) | Beta UI. Server-side admission rule not yet confirmed (blind-server Q1) |
| One shared forum | **In test** | Beta UI |
| Nobody can act as you (signed writes) | **Being built** | The key works like a password today. No client signing on `ui` |
| Your data on your own server (personal agent) | **Prototype**, Ouri to confirm | Ouri, 11 May 2026: each participant runs "her own personal blockchain instance on her own server". In the beta, data sits on the project's node |
| Nobody can quietly rewrite the record | **Ouri to confirm** | Same email: community contracts "replicated across the servers of all community members". Not verified from our repo |
| Host a node | **Planned** | No runnable image yet |
| Nobody can read your ballot | **Planned** | Blind-server plan. No voting in the beta |
| Leave with your identity | **Planned** | Sovereignty spec H3 |
| Losing your phone doesn't lose your vote | **Planned** | Sovereignty spec H2 |
| Reaching places without internet (radio mesh) | **Research** | Spec H7. Reticulum is a candidate, not a choice |

Never on the page as fact: encrypted, secure, private, decentralized, anonymous. (The 23 Oct email
to Ouri said the test covers "keys and encryption". That is not true yet and stays out of copy.)

## 6. Words

- **Headlines and intro:** network, your own server, people who know you, counts once, carried by
  its members. No "Web5", no "blockchain".
- **A "how it works" section for builders**, in Ouri's own framing: inspired by Tim Berners-Lee's
  Solid (personal data stores) and the Web5 idea; built on Ouri's personal-blockchain design and
  his published research. "Blockchain" appears once, defined. Ouri asked for it in Nov 2025.
- **"Web5" at most as "inspired by", never as a standard we use.** Ouri wrote on 7 Nov 2025: "we
  are not using web5 standards". Press reports say Block wound down its Web5 unit in Nov 2024
  (not yet checked against Block's own letter).
- **"Fighting fire with fire" stays an internal angle.** It is an idiom second-language readers
  miss, and a violent picture for a peace story. The plain version: technology broke this
  promise, and technology has to keep it.

## 7. Story spine (order of the page, not copy)

1. **The promise.** In the 1990s people said the internet would bring the world together. One quote
   at most; Barlow (1996) is the strongest candidate once it is checked on eff.org.
2. **What happened.** It divides us, scams us and worries us. Two numbers at most, checked at the
   source.
3. **The belief.** No global democracy without technology.
4. **The missing piece.** §2, in one paragraph.
5. **What GDI builds.** §3, then the status board (§5).
6. **History.** 2021 coalition, 2023 white paper, how the idea moved on.
7. **Doors.** §4.

## 8. To lock

**Eston:** promise (A, B, or A+B) · GDI = network, Gloki = first app · door order · words (§6)
· story spine · status board on the page.

**Ouri:** (1) Where does the backend code live, and under what licence? "Open" needs a licence;
gloki-engage has no licence file either. (2) Can a second app use the network today? (3) Which
§5 rows are true on the live server: signing, replication, the admission rule? (4) "Blockchain"
once in the builders section: yes or no? "Web5" as inspiration: yes or no? (5) The BrightID answer.
(6) The correct citation for the trust-graph paper (the title he gave could not be found).

**Before any quote or number goes in copy:** open the primary sources in a browser. Every Part A
and Part B item is UNVERIFIED because this session could not reach eff.org, itu.int,
pewresearch.org or ic3.gov. The list of URLs is in the sources file.
