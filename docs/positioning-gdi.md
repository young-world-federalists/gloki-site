# GDI positioning (locked)

**Status:** v2, 26 Oct 2026. Rewritten after Eston's answers, the Eston–Ouri call (about 13 Oct)
and a read of the node's code (`github.com/ouripoupko/ibc`). Ouri is not being asked yet. Items
marked **[Ouri, before publish]** go to him before the page goes live; they do not block copy.
Sources: `docs/research/2026-10-26-sources.md`.

## 1. The promise

> The Global Democracy Initiative is building an open network for global democracy, where every
> member is a real person, each person counts once, and no company or government is in charge.

Opening line of the page: **"There will be no global democracy without technology."**

Why v1 changed: on the call, Ouri asked what Eston actually wants from decentralization. The
answer was verified humans ("only humans. There's no bots") and open governance, not storage, and
Ouri agreed most people don't care where their data is kept. "Real people" is also the only part
in test today. "Keep your own data" moves to the being-built list.

## 2. The gap

Today's democracy tools decide who counts with a city or national register (Consul, Decidim), a
list the organiser supplies (Vocdoni), no check at all (Polis), or tokens (Democracy Earth). None
of these works across borders without a government, a company or money in the middle.

**Why not BrightID?** BrightID verifies people for other apps. GDI builds the whole foundation a
democracy needs: who counts, where the record lives and, later, how votes are counted, on one
network its members run. We are not selling identity to other apps. The code is open, so anyone
may reuse it, but the plan is a foundation for democracy. The technical differences are all
being built, so the page can't claim them yet: encrypted ballots, nodes run by members, radio
where there is no internet.

## 3. GDI and Gloki

- **GDI builds the network.** It runs on the **Identity Block Chain**, Ouri Poupko's open-source
  node (GPL-3.0), which puts his published research on self-sovereign digital agents into
  practice. Ouri is part of GDI. The page credits him by name and links his papers.
- **Gloki is the first app on the network.**
- Later: the node repo moves to the YWF GitHub organisation. Eston asks Ouri; not needed for launch.

## 4. Who it is for: three doors and a contact line

1. **Build with us.** Engineers and researchers to work on the backend with Ouri and Eston:
   signed writes, encryption, servers that store data without being able to read it, consensus,
   a safer contract language. Ouri's list of hard problems is the content. **[Ouri: the list]**
2. **Carry the network.** Anyone can run the node today for local development. A public node is
   not safe to run yet, so this door records interest.
3. **Join Gloki.** The waitlist for the pilot.

**Funders** get a contact line, not a door.

## 5. Status board: true today vs being built

| What | Status | Basis |
|---|---|---|
| Get in when four people vouch for you | **In test** (app); see note below | Ouri's original `community_contract.py` enforces it: the contract picks four existing members at random, all four must approve, and the newcomer takes their place between them, so everyone keeps exactly four links. The beta's "people who know you" version has no server code yet |
| One shared forum | **In test** | Beta UI |
| A node anyone can run | **Available for developers** | Docker image, GPL-3.0, local only by default |
| Records copied across members' nodes | **Early code** | The node runs a PBFT-style agreement among a contract's partners, but doesn't check signatures yet and has no view change (`consensus/pbft.py`). Never run across separate machines; the live demo is one node |
| Nobody can act as you | **Being built** | The node has no authentication yet (its own API docs say so) |
| Your data on your own server | **Possible, not yet used** | The design allows it. On the live demo everyone's data sits on one project node |
| Encryption; servers that can't read your data | **Being built** (Eston + Ouri) | "I didn't implement it yet" (Ouri, call) |
| Nobody can read your ballot | **Planned** | Blind-server plan |
| Leave with your identity | **Planned** | Sovereignty spec H3 |
| Losing your phone doesn't lose your vote | **Planned** | Sovereignty spec H2 |
| Reaching places without internet (radio) | **Research** | Spec H7, Reticulum as candidate |

**Note on vouching:** random vouchers are what make Ouri's design resist fake accounts, because
colluders can't choose each other. "People who know you" is easier to use but loses that
guarantee. Until Eston and Ouri pick a rule (or a mix: known people first, random later), the
page says "four people vouch for you", not "four people who know you", and doesn't claim
resistance to fake accounts.

### The protections we planned, in plain words

These are the brainstormed protections (sovereignty spec, blind-server note), so the page can
show the plan without claiming any of it. A line is one sentence on the page; builders get a link
to the spec.

| On the page | Behind it | Status |
|---|---|---|
| Your phone signs everything you do, so nobody can post or vote as you | Keys made on the device, passkey unlock (H1) | Being built |
| Lose your phone, and the people who vouched for you can let you back in | Voucher re-attestation with a waiting period (H2) | Planned |
| Every record is copied to many members' servers, so nobody can change it quietly | Signed append-only logs (H3) | Being built |
| Servers store your data without being able to read it | Encryption, blind servers | Being built |
| You can prove you may vote without saying who you are | Semaphore (H4, step 1) | Planned |
| Votes are counted while still locked; no single server can open one | ElectionGuard threshold keys (H4, step 2) | Planned |
| You can check the app you run is the code we published | Signed releases, CSP/SRI (H5) | Planned |
| Nodes can hide where they are | Tor onion services (H7) | Research |
| Reaching places without internet, by radio | Reticulum over LoRa (H7) | Research |
| Text messages for reminders only, never for votes | SMS/USSD (H7) | Research |
| **No binding vote before an independent security audit** | H8 | A commitment we can make today |

The last row is a policy, not a feature, so the page can state it as true now. **[Eston: commit
to it?]** Engagement mechanics (deliberation, quadratic voting, conviction, delegation) belong to
Gloki, not the network. They go under Gloki as "comes later".

**Pilot rule:** anyone who joins the pilot is told plainly that the project can see their data
until encryption lands, and that moving to the production network may mean a data migration.
Ouri offered to write an automatic migration tool, so nobody has to get verified twice.

## 6. Words

- **Headlines:** network, real people, counts once, carried by its members, no one in charge.
- **"Blockchain":** in the node's name and once in the builder section, in Ouri's own framing.
- **"Web5":** only as context for builders and funders: Tim Berners-Lee's Solid and Jack Dorsey's
  Web5 chased the same idea with far more money, and Web5 has been wound down. It is an honest
  sense of scale. Check Block's own statement first.
- No "fighting fire with fire": it is an idiom second-language readers miss.

## 7. Story spine (page order, not copy)

1. **The promise.** In the 1990s people said the internet would bring the world together. One
   quote at most.
2. **What happened.** Fake accounts and bots, division, scams. Two sourced numbers at most. A bot
   or fake-account figure is still missing from the research.
3. **The belief.** No global democracy without technology.
4. **The missing piece.** §2: knowing each voice is one real person, across borders.
5. **What GDI builds.** §3, then the status board (§5).
6. **History.** The 2021 coalition, the 2023 white paper, how the idea moved on.
7. **Doors.** §4.

## 8. Locked (Eston, 26 Oct 2026)

All five: the promise (§1) · doors in the order Build with us / Carry the network / Join Gloki ·
the credit line "built on Ouri Poupko's open-source node" · the commitment "No binding vote
before an independent security audit" · "four people vouch for you" until a vouching rule is
chosen. Copy drafts A, B and C are written from this version (`docs/copy/`).

Paying for the audit: the commitment costs nothing until a binding vote is planned. Funders of
open civic infrastructure (NLnet's NGI Zero, OTF's Red Team Lab) have offered audits as support
to projects they fund; check their current calls before applying.

**Before publish:**
- **Ouri:** status-board wording, the vouch rule, his problem list, the node repo move (later).
- **Licence for gloki-engage:** AGPL-3.0 recommended. Ouri has to agree, because he co-wrote it.
- **Sources:** quotes and numbers checked in a browser; a sourced bot figure; the trust-graph
  paper citation.
