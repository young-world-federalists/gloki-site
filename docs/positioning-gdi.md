# GDI positioning: draft to lock

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
| Get in when four people who know you vouch | **In test** (app) | The vouch graph gives everyone exactly four active vouches (Ouri, call). Whether the server enforces it is unknown **[Ouri]** |
| One shared forum | **In test** | Beta UI |
| A node anyone can run | **Available for developers** | Docker image, GPL-3.0, local only by default |
| Records copied across members' nodes | **Built, not tested across machines** | The node runs consensus between partners (Ouri: "This app actually works decentralized"). Our own test put three partners on one node, and the live demo is one node |
| Nobody can act as you | **Being built** | The node has no authentication yet (its own API docs say so) |
| Your data on your own server | **Possible, not yet used** | The design allows it. On the live demo everyone's data sits on one project node |
| Encryption; servers that can't read your data | **Being built** (Eston + Ouri) | "I didn't implement it yet" (Ouri, call) |
| Nobody can read your ballot | **Planned** | Blind-server plan |
| Leave with your identity | **Planned** | Sovereignty spec H3 |
| Losing your phone doesn't lose your vote | **Planned** | Sovereignty spec H2 |
| Reaching places without internet (radio) | **Research** | Spec H7, Reticulum as candidate |

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

## 8. To lock

**Eston, now:** the promise (§1) · doors in this order (§4) · the credit line "built on Ouri
Poupko's open-source node".

**Before publish:**
- **Ouri:** status-board wording, the vouch rule, his problem list, the node repo move (later).
- **Licence for gloki-engage:** AGPL-3.0 recommended. Ouri has to agree, because he co-wrote it.
- **Sources:** quotes and numbers checked in a browser; a sourced bot figure; the trust-graph
  paper citation.
