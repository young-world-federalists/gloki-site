# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML and one CSS file, no framework runtime, no third-party script. Deploys from GitHub Pages
on `young-world-federalists/gloki-site` (created 26 Oct 2026). The domain is
**globaldemocracyinitiative.org**, held in the YWF Cloudflare account (Eston, 26 Oct 2026; the
transfer from the old Webflow setup was still completing that day). gloki.app is dropped for now. Page budget under
200 KB including images. Build path: code-first (Eston, 2026-10-23).

## Users

Three audiences, one per door, in this order (Eston to Ouri, 15 Oct 2026):

1. **Solve global issues** — first invitees are academics and world federalists: people who already
   deliberate about transnational problems and want a place where a global "we" can decide something.
2. **Build digital democracy** — civic-tech people, organisers and researchers who want to help shape
   the mechanism (one person one vote, vouching instead of ID, deliberation before any vote).
3. **Contribute to a new internet** — people with a server who would host a node and help carry the
   network.

Behind them, the pilot's eventual participants: young people in Kenya, Nigeria, Malawi and DR Congo on
cheap Android phones, intermittent data, English often a third language. They are not the page's
first readers, but the page must clear their reading level.

The reader arrives from a link in an email, a WhatsApp group or a talk, on a phone as often as a
laptop, and decides in under a minute whether to leave an email address.

## Publisher (Eston, 26 Oct 2026)

The page is published by the **Global Democracy Initiative (GDI)**, with Gloki as its main project.
GDI began in 2021 as a coalition of seven organisations (concept note, 24 May 2021; values doc;
2023 Digital Democracy Lab abstract by Eston McKeague, David Gallup, Ouri Poupko, Lars Luenenburger
and Gery Colombo, all in the YWF shared drive under "Global Democracy Initiative"). It is no longer
an active coalition and has no legal existence of its own: it is a **project of Young World
Federalists, Inc.**, which is its fiscal and legal host and the publisher named in the imprint and
privacy pages. Say exactly that; never present GDI as a separate organisation or the 2021 partners
as current members (their names stay off the page).

Sources added 26 Oct 2026: the old GDI homepage (gdi-site.webflow.io: motto "Assume global
responsibility", values Global Democracy / Global Citizenship / Open Source Innovation) and the 2024
white paper (its own header says "2024 White Paper"; PDF dated Jan 2024) "Gloki: Global Digital Voter Identity" (Poupko, McKeague, Gallup, Colombo,
Lünenburger; Drive doc "Gloki White Paper"). The page links both PDFs as history. Where the paper
and the beta differ, the beta wins and the page says so: the paper has strangers chosen at random
vouch, unique profile photos checked by software, blockchains and "decentralized" records; the beta
has people who know you vouch, and none of those claims may appear as fact on the page.

## Product Purpose

Gloki is a global direct-democracy platform: communities anywhere turn shared problems into
collective mandates through deliberation, then a vote. The beta that this page sells is "the network,
not the pipeline": you get in because people who know you vouch for you, you get your own agent that
holds your data, you can host a node, and everyone who is in shares one forum. The democracy pipeline
(problem → discussion → solutions → vote → mandate) returns later, on a network that by then has real
verified people in it.

Success for the page: a reader understands what Gloki is, which door is theirs, and joins the waitlist.
Success for the product: ≥70% of participants complete the journey unaided, and someone in Nairobi and
someone in Lilongwe feel they are building something together.

## Positioning

Three things a neighbouring product cannot truthfully copy together:

- **You get in because people who know you vouch for you.** Four people vouching makes you verified;
  no ID papers, no face scans, nothing you pay or upload.
- **One person, one vote, never plutocratic.** No token weighting, no pay-to-influence; influence is
  earned through participation and trust.
- **The network is held up by its members.** Your agent holds your data; nodes are hosted by people,
  not by one company (the FlightRadar24 model: hobbyists carry the infrastructure).

## Operating Context

- The app's demo (full pipeline, seeded communities) is live at
  https://young-world-federalists.github.io/gloki-engage/. The beta build (sign-up, keys, vouching, one
  forum) exists on the `ui` branch and deploys only when Ouri merges to `server-side`.
- The waitlist is the YWF Buttondown account, username `YoungWorldFederalists` (Eston, 26 Oct 2026).
  The page posts the email and the chosen door as a tag to Buttondown's embed-subscribe endpoint.
- Partners: Ouri Poupko builds the backend and node runtime; Eston McKeague (YWF) owns the product,
  copy and this page.
- The page is reached from emails, WhatsApp groups and talks; it must work on a phone over mobile data.

## Capabilities and Constraints

- Confirmed capabilities to describe: key-based sign-up with no passwords; three account kinds
  (person, organisation, node contributor); verification by four people who know you (ask a member,
  invitations, a video call, a daily session); one shared forum (post, reply, like).
- **Claims the page may not make** (P12 H0 claims audit): "decentralized", "secure", "encrypted",
  "private" as finished facts. Say "built to run on community-operated nodes", say what is in test.
  Right now the key works like a password: whoever types it in is you.
- **The contribute door launches dark**: there is no runnable node yet (Eston asked Ouri for a repo or
  Docker image on 15 Oct). Until it exists, that door only records interest; the page says so.
- No communities in the beta; "join a community" collapses into "join Gloki", one membership.
- English only for the beta (Eston, 2026-10-23); fr/sw pages are a later step through the native-review
  packet.
- Settled 26 Oct 2026 (Eston): YWF named as builder; the agent row shown as Planned; contact by
  reply to the first waitlist email, plus hello@globaldemocracyinitiative.org.
- Settled 26–28 Oct 2026 (Eston): waitlist sign-ups never receive the YWF newsletter; GDI gets its own
  free Buttondown account, tagged by door. hello@ forwards to Eston (Cloudflare Email Routing).
- Terminology: "vouch" (people who know you confirm you are a real person), "agent" (the thing that
  holds your data; internal only: public copy says "your own record", since "agent" now reads as an AI agent, Eston 27 Oct 2026), "node" (a small server that keeps a copy of the network), "mandate" (a decision a
  community publishes), "door" (one of the three ways in).

## Brand Commitments

- Publisher: **Global Democracy Initiative**. Mark: `assets/gdi-mark.svg`, the network figure
  from Eston's 2022 GDI logo (YWF drive, "GDI Branding/Vector GDI Logos"), without its wordmark; the
  name is set in the page's display face.
- Product: **Gloki**. Mark: `assets/gloki-icon.png` (white figure-and-arcs on a brand-blue rounded square).
- Brand blue **#3b82f6** stays the accent. White text on this blue measures 3.68:1; the app keeps that
  as a locked exception, the landing page does not inherit it: body-size text is blue on white, not
  white on blue.
- The app's system-sans typography is the app's; the page may choose its own display voice
  (Eston, 2026-10-23: mark and brand blue fixed, the rest open).
- Voice: plain, concrete, honest about what is in test. No hype words, no "revolutionary", no
  stock photography of "diverse youth". A sentence a 16-year-old second-language reader clears.

## Evidence on Hand

- Product screenshots at 360px from the beta walk, light and dark:
  `/home/user/gloki-engage/docs/reviews/2026-10-23-s43-forum-bylines/` (forum with named bylines,
  profile) and `/home/user/gloki-engage/docs/reviews/2026-10-23-s43-critique-fixes/` (doors, keys,
  save your key, account kind, profile step, ready, verification hub, forum, profile).
- The mechanism in words: MASTER_TODO.md §1–§3 of gloki-engage; the 15 Oct 2026 "Plan for Gloki beta"
  thread.
- **Absent, never to be fabricated:** user numbers, testimonials, partner logos, press, funders,
  a launch date, a working node.

## Product Principles

1. The innovation is how you get in and how you hold it up; sell that, not the pipeline.
2. Say only what is true today; mark what is in test and what is next.
3. One reader, one door, one action: the page's job ends at the waitlist.
4. Usable unaided on a cheap phone over mobile data before it is beautiful on a laptop.
5. A global "we", not a region or a campaign: no single country or cause as the frame.

## Accessibility & Inclusion

WCAG AA text contrast (4.5:1) with no brand-blue exception; 44px targets; one h1; keyboard-complete;
readable at 360px with no horizontal scroll; under 200 KB; Lighthouse mobile ≥90 performance,
100 accessibility. Reading level: a 16-year-old reading English as a second language.
