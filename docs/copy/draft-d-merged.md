# Draft D: merged home page and builder page

**Status:** merge of drafts A, B and C, 26 Oct 2026, built on the persona review
(`docs/reviews/2026-10-26-copy-personas/SYNTHESIS.md`) and Eston's answers of the same day.
Text in `[BRACKETS]` is a placeholder or an editor note and doesn't ship. Every quote, number and
paper link stays unverified until it has been checked in a browser.

Terms follow the glossary in `docs/reviews/2026-10-26-copy-personas/impeccable-clarify.md` §4:
vouch (never verify), four people, node, your own computer, the network, Gloki, the pilot (what
the waitlist joins), the demo (today's build), the project team, ways to take part, waitlist.

---

# Part 1. Home page

## Hero (first screen)

# There will be no global democracy without technology.

The Global Democracy Initiative is building an open network for global democracy, where every
member is a real person, each person counts once, and no company or government is in charge.

You have heard big promises about technology before. So this page shows what works today and what
does not.

**[Form, in the first screen]**
- Label: **Your email**
- Label: **How do you want to take part?**
  - Join Gloki, the first app
  - Build with us
  - Carry the network
- Button: **Sign up**
- Under the button: Free. We only write to you about GDI and Gloki.
- Link: See what works today *(jumps to the status board)*

---

## The internet connected us

In the 1990s, many people hoped the internet would bring the world together. Anyone could talk to
anyone, across any border.

Part of that came true. A student in Lagos can message a student in Lima in seconds.

But the internet never learned who is real. One person can make a hundred accounts. A computer
program can pretend to be a person. [NUMBER: sourced figure on fake or automated accounts needed]
When you cannot tell real people from fake ones, you cannot count opinions fairly, and you cannot
hold a fair vote.

In many countries, more people now say the internet and social media have made people more
divided. [SOURCE: Pew Research Center, Global Attitudes 2026; check the wording and figure on the
page before use] Online scams have grown too. In 2025, people in the United States reported losing
[NUMBER: FBI IC3 2025 report, crypto-related losses, about US$11.4 billion; verify on ic3.gov] to
scams that used cryptocurrency.

The internet connected us. It did not give us a fair way to decide anything together.

---

## What the network is for

Some problems belong to everyone. Climate, pandemics and war do not stop at borders. Yet there is
no place where people from every country can raise a shared problem, talk it through and decide
together.

People who work for a democratic world have proposed answers: a world parliament, global
citizens' assemblies, worldwide votes on a question. Each one needs something first: a way to know
that each voice belongs to one real person, counted once, in any country.

The whole world will never meet in one hall. If people everywhere are going to decide things
together, a network has to carry their voices. That is why we still build with technology.

---

## Who counts, and how tools decide today

Democracy software has to decide who may take part. Tools made for one city, country or
organisation use one of these answers:

- **A list of residents** from a city or a government. It works inside one country and stops at
  the border.
- **A list from the organiser.** The people running the vote decide who is on it.
- **Random selection.** A small group is chosen by lot, as citizens' assemblies do. It is good for
  deep discussion, but most people never take part.
- **Tokens.** People who hold more of a digital token get more say.
- **Tools that do not hold votes.** Some tools gather opinions from anyone, without a check, and
  are not built to count one vote per person.

Each answer fits the job it was made for. None of them lets people everywhere take part, one vote
each, without a government, a company or money in the middle. That is the part we are building.

### One person, one vote, across borders

You get in when four people vouch for you. To vouch means to confirm that you are a real person.
You do not upload an ID card, scan your face or pay anything.

We have not yet chosen the rule for which four people vouch for you. That rule decides how well
the network keeps out fake accounts, so we make no promise about fake accounts until it is chosen.
When it is, this page will say which rule we picked and why.

---

## What works today, and what does not

Last updated: [DATE]. We change this list when things change.

**In the demo app**
- Four people vouch for you. The app shows the steps; the network does not run the rule yet.
- One shared forum, where members post and reply.

**For developers**
- A node anyone can run on their own computer. A node is a small server that keeps a copy of the
  network. It is not safe to run in public yet.

**Early code**
- Copying records to many members' nodes. The code exists. It does not yet check signatures, and
  we have not run it across separate computers.

**Being built**
- Nobody can act as you. Today the network does not check who sends a request. Other members can
  see your key, so someone could act as you.
- Servers that store your data without being able to read it. Until this is done, the project
  team can see your data.

**Possible, not used yet**
- Your data on your own node. The design allows it. In the demo, everyone's data sits on one node.

**Planned:** nobody can see how you voted · you can leave and take your identity with you · losing
your phone does not lose your vote.

**Research:** reaching places without internet, by radio.

*Planned* means it is in our design and building has not started. *Research* means we are still
finding out whether it can work.

### A rule we keep today

**There will be no binding vote on this network before an independent security audit.** A binding
vote is any vote whose result we present as a decision of the members. We will publish the full
audit report, including any problems not yet fixed.
[EDITOR: also write this rule into the repository's README.]

---

## Who we are

**Eston McKeague** leads the project and builds the Gloki app. He is president of the Young World
Federalists.

**Ouri Poupko** wrote the node the network runs on, and the research behind it. [LINK: Ouri's
papers, verify on dblp.org/pid/234/6110.html]

We are two volunteers, and for now the two of us make the decisions. Builders who join are welcome
in that discussion.

GDI is a project of **Young World Federalists, Inc.**, a nonprofit registered in the United
States. It is GDI's legal and financial home.

---

## The pilot

The pilot is the first group of people on Gloki. It is **free**: nothing to pay, no tokens,
nothing to buy.

**Who it is for.** The first members are world citizens: people in the Young World Federalists'
chapters, and others who already work across borders. Anyone can join the waitlist.

**What you do.** You make a key, four people vouch for you, and you join one shared forum to post
and reply. Ways to discuss and vote together come later.

**Who vouches first.** The first few members vouch for each other, starting with the two of us.
After that, members vouch for newcomers.

**Before you join, please know this.** Ouri Poupko runs the pilot's node on Google Cloud. Until
encryption is built, the project team can see your data, and until signing is built, another member
could act as you. When the full network is ready, your account may need to move to it. We plan a
tool that moves it for you, so nobody has to be vouched for twice.
[EDITOR: the pilot opens only once signing is in place? Eston to decide; if yes, say so here.]

---

## Where this started

GDI began in 2021 as a coalition of seven organisations working for democracy at a world scale. In
2023, some of us wrote a white paper, "Gloki: Global Digital Voter Identity".
[LINK: 2021 concept note] [LINK: 2023 white paper PDF]

The coalition is no longer active. [EDITOR: one plain sentence on why, if Eston wants it.] In 2026
we started again from first principles, as a project of the Young World Federalists.

The idea has changed as we built it. The paper describes some things the app does not do, such as
software that checks profile photos. Where the paper and the app differ, the app tells you what is
true now.

---

## Three ways to take part

**Join Gloki.** Join the waitlist for the pilot. We will write when it opens and tell you how to
get vouched in.

**Build with us.** We need engineers and researchers to work on the network with Ouri and Eston:
proving that each request really comes from you, encryption, getting many computers to agree on one
record, and a safer language for the small programs that run on the network.
[Link] Read how it works and what is open *(the builder page)*

**Carry the network.** You can run the node on your own computer today, to build and test. A node
in public is not safe yet. Sign up and we will write when it is.

**Funders.** To talk about supporting this work, write to hello@globaldemocracyinitiative.org.
[EDITOR: link a one-page funder brief here once it exists.]

---

## Form: after sending

Shown in place of the form, by choice:
- **Join Gloki:** Thank you. Check your inbox and confirm your email. We will write when the pilot
  opens.
- **Build with us:** Thank you. Check your inbox and confirm your email. We will send you the list
  of open problems.
- **Carry the network:** Thank you. Check your inbox and confirm your email. We will write when a
  public node is safe to run.

[EDITOR: "confirm your email" assumes Buttondown double opt-in is on, as the README plans.]

**Privacy line (under the form and in the footer):** Young World Federalists, Inc. keeps this list
on Buttondown. We only write to you about GDI and Gloki, and you can leave from any email we send.
[Link] Privacy

**Footer credit:** Built on Ouri Poupko's open-source node. GDI is a project of Young World
Federalists, Inc.

---

# Part 2. Builder page (`/build`)

## How the network works, and what is open

This page is for engineers and researchers. It says exactly what the code does today, so you can
decide whether to help.

### The node

The network runs on the **Identity Block Chain**, Ouri Poupko's open-source node (GPL-3.0). It puts
his research on self-sovereign digital agents into practice: software that holds one person's data
and acts only for them. [LINK: repository github.com/ouripoupko/ibc] [LINK: "Self-Sovereign Digital
Agents for a Grassroots Digital Society", ICDCS 2022, verify]

- Each person is an **agent**. An agent registers on a node and acts through it.
- Rules live in **contracts**: small Python programs. Every agent that joins a contract is a
  **partner** on it and keeps a copy of its state.
- A write to a contract goes through an agreement step among that contract's partners (a
  PBFT-style protocol), so the copies stay the same. There is no single global chain.
- The node ships as a Docker image and listens only on your own computer by default.

### The vouching rule in the code

Ouri's community contract picks two existing links in the trust graph at random, which gives four
members. All four must approve the newcomer, and the newcomer takes a place between them, so every
member keeps exactly four links. Random choice matters: people making fake accounts cannot pick
each other. [LINK: "Building a Sybil-Resilient Digital Community Utilizing Trust-Graph
Connectivity", IEEE/ACM ToN 2021, verify; open version arXiv:1901.00752]

The pilot app also tests vouching by people you choose. That version has no server code yet. Until
we choose one rule, we make no claim about keeping out fake accounts.

### Known gaps

- **No authentication.** Anyone who knows an agent's identity string and node address can send
  requests as that agent. Identity strings are visible to other partners.
- **Agreement does not check signatures** yet, and has no view change. It has not been run across
  separate machines.
- **The random pick can be steered.** It is seeded with a timestamp set by the node that receives
  the request, so whoever runs that node can influence which four members are chosen.
- **Contracts are plain Python** in a sandbox, not a language designed for safe contracts.
- **No encryption** of stored data yet.

### Open problems

[OURI: his list of hard problems goes here.] The gaps above are where we would start: signed
requests, signature checks in agreement, randomness no single node can steer, encryption, a safer
contract language, and testing across machines.

### The protections we plan

| On the home page | How | Status |
|---|---|---|
| Your phone signs everything you do | Keys made on the device, unlocked with a passkey | Being built |
| Lose your phone, and your vouchers can let you back in | Vouchers confirm you again, after a waiting period | Planned |
| Nobody can change records quietly | Signed append-only logs copied across nodes | Being built |
| Servers store your data without reading it | Encryption, blind servers | Being built |
| Prove you may vote without saying who you are | Semaphore | Planned |
| Votes counted while still locked | ElectionGuard threshold keys | Planned |
| Check that the app you run is the code we published | Signed releases, CSP and SRI | Planned |
| Nodes can hide where they are | Tor onion services | Research |
| Reaching places without internet | Reticulum over LoRa radio | Research |
| Text messages for reminders, never for votes | SMS and USSD | Research |

[LINK: sovereignty and security plan, Eston to confirm it can be public]

### BrightID and GDI

BrightID also uses vouching. It lets people prove to other apps that they use only one account. GDI
is building the whole foundation a democracy needs on one network its members run: who counts,
where the record lives and, later, how votes are counted. The protections that would set it apart
technically are still being built.

### Licence and how we decide

The node is GPL-3.0. The Gloki app's licence is not set yet. [EDITOR: AGPL-3.0 proposed; needs
Ouri's agreement as co-author.] For now Ouri and Eston make the decisions. Contributors are welcome
in that discussion.

**Get in touch:** hello@globaldemocracyinitiative.org, or sign up with "Build with us" and we
will send you the open problems.

---

## Claims check (changes since drafts A–C)

| Sentence | Basis | Check |
|---|---|---|
| "the network does not run the rule yet" (vouching) | Pilot rule has no server code (positioning §5 note) | OK |
| "Other members can see your key, so someone could act as you" | ibc API docs: no authentication; `get_partners` returns agent ids; forum rows carry keys | OK |
| "Copying records … does not yet check signatures, and we have not run it across separate computers" | `consensus/pbft.py`; Lena's review | OK. Positioning §5 row updated to "Early code" |
| "Ouri Poupko runs the pilot's node on Google Cloud" | Ouri on the call: "The server is what I have running on Google" | OK; [Ouri, before publish] |
| "We are two volunteers, and for now the two of us make the decisions" | Eston, 26 Oct | OK |
| "The first few members vouch for each other, starting with the two of us" | `community_contract.py` (first members join without random pick); Eston, 26 Oct | OK |
| "Free: nothing to pay, no tokens, nothing to buy" | Eston, 26 Oct | OK |
| Audit rule with definition and published report | Eston, 26 Oct (tightened per Viktor) | OK, a policy |
| "The random pick can be steered…" | `ibc.py:44` timestamp from the receiving node; `common/state.py` seeds `random` with it | OK |
| "There is no single global chain" | PBFT runs per contract; `consensus/nakamoto.py` is a stub | OK |
| Barlow quote | Dropped (Kofi, Giorgia) | n/a |
