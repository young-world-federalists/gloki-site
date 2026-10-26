# Draft B: Infrastructure for one person, one vote

**For:** Eston, to pick or merge with drafts A and C. **Date:** 26 Oct 2026. **Not committed.**
**Angle:** lead with the missing part (is this one real person, counted once?), then show what GDI
builds and where each part stands. Written mainly for builders, researchers and funders, at a
reading level a 16-year-old second-language reader on a phone can follow.
**Sources:** `docs/positioning-gdi.md` (locked), `PRODUCT.md`, `docs/research/2026-10-26-sources.md`.
Anything in `[BRACKETS]` is a placeholder or a note to Eston/Ouri and must not ship as is.
**Length:** about 1,000 words of body copy, excluding tables, placeholders and form labels.

---

## 1. Headline options

1. `# One person, one vote, across borders. We are building the part that is missing.`
2. `# A vote for the whole world has to know that each voter is one real person`
3. `# An open network where every member is a real person, counted once`

**Recommended: option 1.** It names the goal readers already know (one person, one vote), adds the
part that makes it new (across borders), and says honestly that the work is in progress. Option 3
repeats the promise, which already sits three lines below it in the hero.

---

## 2. Page copy

### Hero

`# One person, one vote, across borders. We are building the part that is missing.`

There will be no global democracy without technology. And every vote must first answer one
question: is this one real person, counted once?

The Global Democracy Initiative is building an open network for global democracy, where every
member is a real person, each person counts once, and no company or government is in charge.

We build it in the open, and this page says plainly what works today and what does not.

Buttons: **See what works today** (jumps to the status board) · **Join the waitlist** (jumps to the form)

---

### How tools decide who counts today

Most democracy software was made for one city, one country or one organisation. To decide who
may take part, it uses one of four answers.

- **A government register.** You are checked against a list of residents. This cannot cover
  many countries at once.
- **The organiser's list.** The people running the vote decide who is on it.
- **Money.** Votes are weighted by the tokens you hold.
- **No check.** Anyone can take part, so one person could be counted many times.

Each is a sensible choice for the job it was made for. None of them works across borders without
a government, a company or money in the middle. That is the part GDI is building.

---

### What happened to the internet's promise

In the 1990s, many people said the internet would bring the world together.

> [QUOTE — John Perry Barlow, "A Declaration of the Independence of Cyberspace", Davos, 8 Feb 1996,
> closing line beginning "We will create a civilization of the Mind in Cyberspace…". UNVERIFIED:
> check the exact words on eff.org/cyberspace-independence before use]

It did connect us. It also filled up with fake accounts and bots
[NUMBER — share of accounts or traffic that are fake or automated; no source found yet, find one
and verify]. People became more divided, and fraud grew: in 2025, losses reported to the FBI from
cryptocurrency fraud reached [NUMBER — about $11.37bn, a record, FBI IC3 2025 Internet Crime
Report; verify on ic3.gov].

When one person can make a thousand accounts, counting voices tells you very little. A vote that
includes the whole world can only happen online, so the tools for it have to know who is real.

---

### What GDI builds

GDI is building the network underneath: a way to know that each member is one real person, and a
shared record that members keep themselves, with no company or government in charge.

The network is built on Ouri Poupko's open-source node. Ouri is part of GDI, and the node puts his
published research into practice.

**Gloki is the first app on the network.** In the pilot, you get in when four people vouch for
you, and you join one shared forum. Ways to discuss and vote come later.

#### Where each part stands

[DATE — last updated, e.g. 26 October 2026]

| What we are building | Status | What that means today |
|---|---|---|
| You get in when four people vouch for you | **In test** | We are testing this in the Gloki app. We have not yet chosen the final rule for who the four people are. |
| One shared forum for all members | **In test** | You can post, reply and like in the pilot app. |
| A node anyone can run | **Available for developers** | Developers can run it on their own computer. It is not yet safe to run as a public server. |
| Records copied across members' nodes | **Built, not tested across machines** | The code does this. So far we have only tried it on one machine. |
| Nobody can act as you | **Being built** | Today your key works like a password. Anyone who has it can act as you. |
| Your data on your own server | **Possible, not yet used** | The design allows it. In the pilot, everyone's data sits on one project server. |
| Encryption, so servers cannot read your data | **Being built** | Until this is done, the project team can see your data. |
| Nobody can read your ballot | **Planned** | In our plan. Not built yet. |
| Leave and keep your identity | **Planned** | In our plan. Not built yet. |
| Losing your phone does not lose your vote | **Planned** | In our plan. Not built yet. |
| Reaching places without internet, by radio | **Research** | We are studying whether this can work. |

**Our commitment:** there will be no binding vote on this network before an independent security
audit.

**If you join the pilot:** until encryption is built, the project team can see your data. Later,
your account may have to move to the full network. We plan a tool that moves it for you, so you
should not need to be vouched for twice.

---

### How it works, for builders

**The node.** Ouri's node is called the Identity Block Chain. A node is a small server that keeps a
copy of the network's records. The code is under GPL-3.0 (a licence that keeps the code and changes
to it open). It runs locally from a Docker image (a package that runs the same on any computer).

**The record.** Nodes called partners agree on one shared, ordered record. This is called
consensus, and it is what makes the node a blockchain. We have run three partners on one machine,
but not yet across machines.

**The rules.** Rules live in contracts, small Python programs on the node. Ouri's community
contract picks four members at random to vouch for a newcomer. All four must approve, and every
member keeps exactly four links. Random choice matters: people making fake accounts cannot pick
each other. The pilot app also tests vouching by people you choose, which has no server code yet.
Until we settle the rule, we make no claim about stopping fake accounts.

**What is missing.** The node has no authentication yet (a check that a request comes from you).
Signed writes and encryption are being built.

**The research.** Ouri's papers on self-sovereign digital agents (software that holds one person's
data and acts only for them) and on consensus:

- [LINK — "Self-Sovereign Digital Agents for a Grassroots Digital Society", Poupko, Shapiro,
  Talmon, ICDCS 2022, verify on dblp]
- [LINK — "Building a Sybil-Resilient Digital Community Utilizing Trust-Graph Connectivity",
  Poupko, Shahaf, Shapiro, Talmon, IEEE/ACM Transactions on Networking 2021, verify on dblp;
  open version arXiv:1901.00752]. A Sybil attack is one person running many fake accounts.
- [LINK — "Cordial Miners: Fast and Efficient Consensus for Every Eventuality", Keidar, Naor,
  Poupko, Shapiro, DISC 2023, verify on dblp]

**BrightID and GDI.** BrightID also uses vouching. It lets people prove to other apps that they use
only one account. GDI is building the whole foundation a democracy needs, on one network its
members run: who counts, where the record lives and, later, how votes are counted. The code is open
for anyone to reuse. The technical differences we plan, such as locked ballots, are not built yet.

**The plan, in plain words.** Only the last row is true today.
[LINK — sovereignty spec, Eston to confirm it can be public]

| Protection | How (for builders) | Status |
|---|---|---|
| Your phone signs everything you do, so nobody can post or vote as you | Keys made on the device, opened with a passkey (the phone's own screen lock) | Being built |
| Lose your phone, and the people who vouched for you can let you back in | Vouchers confirm you again, after a waiting period | Planned |
| Every record is copied to many members' servers, so nobody can change it quietly | Signed append-only logs (records that can be added to but never edited) | Being built |
| Servers store your data without being able to read it | Encryption with blind servers (servers that hold data they cannot open) | Being built |
| You can prove you may vote without saying who you are | Semaphore (a way to prove you belong to a group without showing which member you are) | Planned |
| Votes are counted while still locked, and no single server can open one | ElectionGuard threshold keys (several key holders must work together to open the count) | Planned |
| You can check that the app you run is the code we published | Signed releases, plus browser checks on loaded code (CSP/SRI) | Planned |
| Nodes can hide where they are | Tor onion services (servers reached without showing their address) | Research |
| Reaching places without internet, by radio | Reticulum over LoRa (a network that runs over long-range radio) | Research |
| Text messages for reminders only, never for votes | SMS and USSD (phone text and menu codes) | Research |
| No binding vote before an independent security audit | A policy | **A commitment we make today** |

---

### Where GDI comes from

GDI began in 2021 as a coalition of seven organisations.
[LINK — 2021 concept note or old GDI homepage, Eston to supply] In 2023, some of us wrote a white
paper, "Gloki: Global Digital Voter Identity". [LINK — 2023 white paper PDF, Eston to supply]

The coalition is no longer active. GDI is now a project of Young World Federalists, Inc., its legal
and fiscal host.

The idea has changed as we built it. The paper describes things the app does not do, such as
software checks on profile photos. Where the two differ, trust the status board.

---

### Choose your door

**1. Build with us.** We need engineers and researchers to work on the backend with Ouri Poupko and
Eston McKeague. Open problems include signed writes, encryption, servers that store data without
being able to read it, consensus, and a safer language for contracts.
[OURI — his list of hard problems goes here]

**2. Carry the network.** Developers can run the node on their own computer today. A public node is
not safe to run yet. Leave your email and we will write when it is.

**3. Join Gloki.** Join the waitlist for the pilot. Before you start, we will tell you what the
project can see.

**Funders:** to talk with us, write to hello@globaldemocracyinitiative.org.

---

### Waitlist form

- **Field label:** Your email
- **Door choice (label):** Which door is yours?
  - Build with us
  - Carry the network
  - Join Gloki
- **Button:** Join the list
- **Privacy line:** We use your email only to write to you about GDI. Young World Federalists,
  Inc. keeps the list on Buttondown, and you can leave it at any time. [LINK — privacy page]
  [ESTON — if sign-ups also get the general YWF newsletter, say so here]
- **After sign-up:** Thank you. Check your email to confirm. You can reply to it with questions.

---

## 3. Claims check

Every sentence on the page that says what the technology does, mapped to its status-board row
(`positioning-gdi.md` §5).

| Sentence on the page (short form) | Status-board row | Result |
|---|---|---|
| "The Global Democracy Initiative is building an open network… every member is a real person, each person counts once, and no company or government is in charge." | §1 promise, locked; framed as "is building" | OK |
| "GDI is building… a way to know that each member is one real person, and a shared record that members keep themselves" | Four people vouch (In test); Records copied (Built, not tested) | OK, "is building" |
| "The network is built on Ouri Poupko's open-source node." | A node anyone can run (Available for developers) | OK, locked credit line |
| "In the pilot, you get in when four people vouch for you" | Four people vouch (In test) | OK, says "pilot" and "four people vouch", not "who know you" |
| "…and you join one shared forum." | One shared forum (In test) | OK |
| "Ways to discuss and vote come later" | §5 note: engagement belongs to Gloki, "comes later" | OK |
| Status table, all 11 rows | Same 11 rows, same statuses | OK |
| "There will be no binding vote… before an independent security audit." | Commitment row (H8) | OK, locked as true |
| "Until encryption is built, the project team can see your data… your account may have to move to the full network." | Pilot rule; Encryption (Being built) | OK |
| "We plan a tool that moves it for you" | Pilot rule (Ouri offered the tool) | OK as a plan; [Ouri, before publish] |
| "Developers can run it on their own computer… GPL-3.0… runs locally from a Docker image" | A node anyone can run (Available for developers) | OK |
| "Nodes called partners agree on one shared, ordered record… it is what makes the node a blockchain. We have run three partners on one machine, but not yet across machines." | Records copied (Built, not tested across machines) | OK; "what makes it a blockchain" is our framing, [Ouri, before publish] |
| "Ouri's community contract picks four members at random to vouch for a newcomer. All four must approve, and every member keeps exactly four links." | Four people vouch, Basis column (`community_contract.py`) | OK; [Ouri, before publish] |
| "The pilot app also tests vouching by people you choose, which has no server code yet… we make no claim about stopping fake accounts." | Vouching note | OK |
| "The node has no authentication yet… Signed writes and encryption are being built." | Nobody can act as you; Encryption (both Being built) | OK |
| "Today your key works like a password. Anyone who has it can act as you." | Nobody can act as you (Being built) | OK |
| "BrightID also uses vouching. It lets people prove to other apps that they use only one account." | Sources C11 (VERIFIED) | OK |
| "The technical differences we plan, such as locked ballots, are not built yet." | Nobody can read your ballot (Planned) | OK |
| "Rules live in contracts, small Python programs on the node." | A node anyone can run (Available for developers) | OK |
| "Open problems include signed writes, encryption, servers that store data without being able to read it, consensus" | Nobody can act as you; Encryption (Being built) | OK, framed as open problems |
| "A public node is not safe to run yet." | A node anyone can run (Available for developers) | OK |
| Protections table, 11 rows | §5 plain-words table, same statuses | OK |
| Paper titles and authors | Sources Part E (UNVERIFIED) | Placeholder |
| Barlow quote | Sources A1 (UNVERIFIED) | Placeholder |
| Bot or fake-account figure | None in sources | Placeholder, source missing |
| Crypto fraud figure | Sources B1 (UNVERIFIED) | Placeholder |

**Words the page never uses as working claims:** encrypted, secure, private, decentralized,
anonymous, ballot secrecy, data ownership, radio. "Encryption", "radio" and "locked ballots" appear
only next to Being built, Planned or Research. "Blockchain" appears once, in the builders section;
"Identity Block Chain" is the node's name. "Web5" is not used.
