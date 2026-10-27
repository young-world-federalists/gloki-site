# GDI positioning one-pager (draft for Eston to lock)

Draft, 27 Oct 2026. Written from `docs/brief-gdi-positioning.md`, `PRODUCT.md`, the gloki-engage
sovereignty spec (§1, §2, §6) and `docs/FOR_OURI_blind_servers.md` on `origin/ui`, the 15 and
23 Oct "Plan for Gloki beta" emails, Ouri's December 2025 PWP deck ("Gloki PWP_9 December 2025",
Drive) and Ouri's paper *Self-Sovereign Digital Agents for a Grassroots Digital Society*
(Poupko, Shapiro, Talmon; Drive, `The_Personal_Digital_Agent.pdf`).
Research sources for the story and the landscape: `docs/research-gdi-positioning.md`.

Nothing in here is page copy. Each section ends with what needs deciding and who decides it.

---

## 1. Decision first: what is "Gloki"?

The brief proposes **GDI = the commons, Gloki = the first app on it** (the Matrix/Element pattern).
Re-grounding turned up a problem with that split. Every source uses "Gloki" for the foundation,
not for the app:

- The 2023 white paper is titled *Gloki: Global Digital Voter Identity*.
- Ouri's December 2025 deck: "What is Gloki ID? A personal voter identity on your own device".
- The beta you agreed with Ouri on 15 Oct has **no democracy pipeline**. It is getting in
  (vouching), your own agent, hosting a node and one forum. The beta *is* the foundation.
- The democracy app already has its own name in the code: the repo is `gloki-engage`.

So there are two ways to split the names:

| | GDI | Gloki | The democracy app |
|---|---|---|---|
| **A. Brief** | The foundation | The app | (= Gloki) |
| **B. Recommended** | The mission and the people behind it | The foundation: one identity per person, your agent, a network members carry | **Gloki Engage** (or another name, later) |

**Recommendation: B.** It keeps the name the white paper, the deck and the beta already use for
the same thing. "Join Gloki" stays true: the beta is joining the network. It gives builders of
other democracy apps something with a name to build on ("works with Gloki"). And it doesn't
waste a brand on a pipeline that won't ship for months. The Matrix pattern still holds, with
Gloki in Matrix's position.

Under B, GDI is also the right name to be the face: an initiative, not a product, hosted by
YWF. That matches what PRODUCT.md already says it legally is.

**Decide (Eston):** A or B. Everything below is written for B. Under A, swap the two names.

---

## 2. Who the page is for, in order

1. **People building democracy apps** (civic tech, deliberation platforms, researchers who run
   assemblies). What they need is what most of them don't have: a way to know each voice is one
   real person, with no ID papers, no face scans and no company in the middle. *Ask: follow the
   build, join the developer list.*
2. **People who can carry the network** (someone with a server, a Raspberry Pi, or later a radio).
   The FlightRadar24 model. *Ask: register interest. The node image doesn't exist yet, so this door
   only records interest, and the page says so.*
3. **Funders and researchers.** Proof that the team is honest about status counts for a lot here
   (see §5). *Ask: read the status board and the white paper, write to hello@.*
4. **Future members.** People who want a say in global problems: academics and world federalists
   first, then the pilot sites. *Ask: join the waitlist.*

This reverses PRODUCT.md's current door order (solve global issues first). That follows from
positioning on the backend. If you'd rather keep "solve global issues" first because your first
invitees are world federalists, the story still works; the hero then has to explain the backend
in one line.

**Decide (Eston):** the door order, and whether this becomes three doors or four.

---

## 3. The one-sentence promise

The mission, stated as a mission, not as a product claim:

> **There will be no global democracy without technology. We are building the part every
> democracy app is missing: one real person, one vote, on a network its members carry.**

Two alternates, depending on how §1 and §2 land:

- "The internet was supposed to bring us together. We are building the part that can: a way for
  every person on Earth to have one voice, on a network nobody owns." (*"Nobody owns" is a claim.
  Use it only as a goal, e.g. "built so that no company or government owns it".*)
- "Global democracy needs a foundation. We're building it in the open: identity without ID papers,
  one person one vote, and a network carried by the people who use it."

**Decide (Eston):** pick one, or name what's wrong with all three.

---

## 4. The story, in four beats

1. **The hope.** In the 1990s, people believed the internet would bring the world together.
   (Quotes: only those marked VERIFIED in `docs/research-gdi-positioning.md`.)
2. **What happened.** It divided us instead: feeds tuned for outrage, crypto that became a byword
   for scams, AI that people fear more than they trust. (One sourced fact per clause, from the
   research file. Where the evidence is contested, such as social media and polarisation, the copy
   says "many people believe" or cites the study's own wording. It does not overstate.)
3. **The turn.** Technology is not going away, and global problems don't stop at borders. There
   will be no global democracy without technology of some kind. So build the good version: fight
   fire with fire.
4. **What we build.** Three things, each with its status beside it (§5):
   - **One person, one vote.** You get in because people who know you vouch for you. No ID papers,
     no face scans, no tokens, nothing to buy.
   - **Your data stays yours.** Each person has their own agent that keeps their records. Groups
     share only what belongs to the group. (Ouri's paper calls this subsidiarity: each contract is
     copied only between the people who are part of it.)
   - **A network its members carry.** Nodes are run by people, not one company. Later, where the
     internet fails, messages can travel over radio.

The history section (2021 coalition, 2023 white paper, old motto "Assume global responsibility")
goes below the fold as "Where this comes from". It's context, not the plan.

---

## 5. True today vs. being built (needs Ouri's sign-off line by line)

This is the status board. It goes on the page as-is, in plain words. Every row marked **?** is
something the `ui` repo can't see; only Ouri can say.

| What | Status | Basis |
|---|---|---|
| A demo of the full democracy app (seeded data, runs in your browser) | **Live** | young-world-federalists.github.io/gloki-engage |
| Sign-up with a key instead of a password; three account kinds; one shared forum | **Built, in test** | Beta UI on `ui`. Today the key works like a password: whoever types it in is you |
| Getting in through four people who know you | **Built in the app, in test** | Verification hub and calls (S37–S38). **?** Whether the server enforces it |
| Your own agent that holds your records | **? Running on GDI's servers** | Agents ran for ~20 PWP members in Dec 2025 ("you are welcome to use ours"). Members don't run their own yet |
| Nodes hosted by members | **Planned** | Docker image requested 15 Oct; not available yet |
| 1. Nobody can act as you (signed writes) | **Planned** (H1) | `ui` has no client-side signing. **?** What `server-side` does |
| 2. Nobody can quietly rewrite the record | **Planned** (H3) | Ouri's paper: contracts replicate between their participants; the paper itself notes that participants who collude can rewrite a contract's history |
| 3. Nobody can read your ballot | **Planned** (H4) | Blind-server proposal; nothing built |
| 4. You can leave and take your identity with you | **Planned** | **?** |
| 5. Losing your phone doesn't lose your vote | **Planned** (H2) | Recovery through your vouchers; nothing built |
| Messages over radio where there's no internet (Reticulum) | **Research** | Spec H7 |

Rule for copy: a property can be described as **what we are building** at any status. It can be
described as **what Gloki does** only when its row says Live and Ouri has signed the row.

**Decide (Ouri):** each **?** row, and whether any "Planned" row is further along than this repo
shows.

---

## 6. Words

| Use | Avoid in headlines | Why |
|---|---|---|
| one person, one vote | "Sybil-resistant" | Jargon |
| people who know you vouch for you | "web of trust" (fine in the technical section) | Plain first |
| your agent / your own record | "self-sovereign identity", "personal ledger" | Plain first; both can appear once in the builders' section |
| a network its members carry | "decentralized" as a finished fact | Claims rule (PRODUCT.md, P12 H0) |
| a new internet (as a goal) | **"Web5"**, **"blockchain"** | Both read as crypto to the audience in beat 2. See below |

**Web5 and blockchain.** Ouri uses both: the December deck says "This is not a Web3 blockchain,
but Web5" and "Our unique blockchain", and compares the design to Jack Dorsey's Web5 and Tim
Berners-Lee's Solid. The ideas belong on the page (each person keeps their own record; no
mining, no tokens; Ouri's paper calls it capital-free). The words are the question.
Recommendation: no "Web5" or "blockchain" in a headline or the first screen. In the builders'
section, one honest paragraph: "Technically, each person runs their own small ledger, and
contracts run only among the people in them. There are no coins, no mining and no
speculation. If you know Solid or Web5, it is in that family." (See the research file, item D,
for whether Web5 is still a live project before naming it at all.)

**Decide (Eston + Ouri):** the Web5/blockchain rule, and the name of the foundation if B is chosen.

---

## 7. Waitlist (unchanged from the brief, recorded here so it isn't lost)

A separate Buttondown newsletter for GDI. Not the YWF list with tags. Waitlist sign-ups never
receive the YWF newsletter. `privacy.html` names the new list. Eston creates it (it's his
account); the form's action URL then changes in one place.

---

## Next steps once this is locked

1. Three copy drafts in parallel (the brief's angles a/b/c), each given this page, the PRODUCT.md
   voice rules and the claims rule.
2. Eston picks or merges.
3. New page concept (the network, not the sign-up line diagram), build, claims audit against §5.
