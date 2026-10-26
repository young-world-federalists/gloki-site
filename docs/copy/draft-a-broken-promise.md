# Home page draft A: "The promise the internet broke"

**Status:** draft for Eston, 26 Oct 2026. One of three parallel drafts. Follows `docs/positioning-gdi.md`
(v2, all §8 items locked) and the story spine in §7. Text in `[SQUARE BRACKETS]` is a placeholder or an
editor note and must not ship as it stands. Every quote and number is unverified until it has been
checked in a browser.

---

## 1. Headline options (h1)

1. **The internet promised to bring the world together**
2. **Keep the internet's first promise: a network of real people, where each person counts once**
3. **There will be no global democracy without technology**

**Recommended: option 1.** It is short enough for one or two lines on a phone. It names a hope the
reader already knows, and the rest of the page answers it. Option 3 is the line the one-pager calls the
page's opening line; in this draft it heads section 3, where the story spine places "the belief".

---

## 2. Page copy

### Hero

# The internet promised to bring the world together

The Global Democracy Initiative is building an open network for global democracy, where every member
is a real person, each person counts once, and no company or government is in charge.

[Button] Join the waitlist
[Text link] See what works today *(jumps to the status board)*

---

### What people hoped for

In the 1990s, many people believed the internet would bring the world together. Anyone could talk to
anyone, across any border. People hoped this would make the world more fair.

> [QUOTE: John Perry Barlow, "A Declaration of the Independence of Cyberspace", Davos, 8 Feb 1996.
> Verify the closing line on eff.org before use: "We will create a civilization of the Mind in
> Cyberspace. May it be more humane and fair than the world your governments have made before."]

Barlow hoped the online world would be fairer than the one governments had built. Many people shared that hope.

---

### What happened

Part of that hope came true. A student in Lagos can message a student in Lima in seconds.

But the internet never learned who is real. One person can make a hundred accounts. A computer
program can pretend to be a person. [NUMBER: sourced bot/fake-account figure needed] When you cannot
tell real people from fake ones, you cannot count opinions fairly. You cannot hold a fair vote.

The big platforms show each of us whatever keeps us scrolling. In many countries, more people now say
the internet and social media have made people more divided. [SOURCE: Pew Research Center, Global
Attitudes 2026, "Growing shares across countries say the internet and social media have made people
more divided". Fetch the page and check the wording before use.]

Scams moved online as well. In 2025 alone, people told the FBI they had lost
[NUMBER: FBI IC3 2025 Internet Crime Report, cryptocurrency-related losses, about US$11.4 billion,
verify the exact figure in the report on ic3.gov] in scams that used cryptocurrency.

A few companies own the places where most of us talk online. They write the rules, and they can change
them at any time. The internet connected us. It did not give us a fair way to decide anything together.

---

### There will be no global democracy without technology

We think the 1990s hope was right. The tools built since then were not made for it.

Climate change does not stop at borders, and neither does disease. Yet there is no place where people
from every country can decide something together. The whole world cannot meet in one room. If people
everywhere are ever going to decide things together, they will do it through technology.

---

### The missing piece

A vote only works if each voice belongs to one real person.

Today's democracy tools check this in different ways. Some use a city or national register. Some trust
a list that the organiser gives them. Some do not check at all. Some give more say to people who hold
more digital tokens.

None of these works across borders without a government, a company or money in the middle. That is
the piece we are working on: a way to know that each voice is one real person, in any country, with no
one in charge of the list.

---

### What we are building

GDI builds the network. **Gloki** is the first app on it.

The network is built on Ouri Poupko's open-source node. Ouri is part of GDI. His node puts his
published research into practice.
[LINK: Ouri's papers. Candidates from the sources file, all unverified, check on
dblp.org/pid/234/6110.html before linking: "Self-Sovereign Digital Agents for a Grassroots Digital
Society" (ICDCS 2022) and "Building a Sybil-Resilient Digital Community Utilizing Trust-Graph
Connectivity" (IEEE/ACM Transactions on Networking, 2021; the title itself is not yet confirmed).]

**How you get in.** You get in when four people vouch for you. To vouch means to confirm that you are a
real person. We are testing this now in the Gloki app. We are still deciding how the four people are
chosen.

**Who carries the network.** The plan is that each record is copied to many members' nodes, so no
single company or government holds it. A node is a small server that keeps a copy of the network. The
node can already copy records between members. We have not yet tested this across separate machines,
and our live demo runs on one node.

**What is not ready.** Some important parts are not built yet. Today your key works like a password:
anyone who has it can act as you. We are building a way for your phone to sign everything you do, so
nobody else can post or vote as you. We are also building encryption, so servers can store your data
without being able to read it. Until that is done, the project can see your data.

One rule is true today. **There will be no binding vote before an independent security audit.** A
binding vote is one whose result counts for real.

Here is where each part stands. We will change this list when things change.

| What | Where it stands |
|---|---|
| You get in when four people vouch for you | **In test**, in the Gloki app |
| One shared forum for all members | **In test** |
| A node anyone can run | **Ready for developers.** It runs on your own computer only, for now |
| Records copied across members' nodes | **Built, not yet tested** across separate machines |
| Nobody else can act as you | **Being built** |
| Your data on your own server | **Possible, not yet used.** In the demo, everyone's data sits on one project node |
| Encryption: servers that store your data but cannot read it | **Being built** |
| Nobody can read your ballot | **Planned** |
| You can leave and take your identity with you | **Planned** |
| Losing your phone does not lose your vote | **Planned** |
| Reaching places without internet, by radio | **Research** |

*Planned* means it is in our design and building has not started. *Research* means we are still
studying whether it can work.

---

### Where this started

GDI began in 2021 as a coalition of organisations that wanted democracy at a world scale. In 2023,
some of us wrote a white paper about a global voter identity.
[LINK: 2023 white paper PDF] [LINK: old GDI homepage, kept as history]

The idea has changed since then. The paper describes some things the app does not do today, such as
software that checks profile photos. Where the paper and the app differ, the app tells you what is true
now.

The coalition is no longer active. GDI is now a project of Young World Federalists, Inc.

---

### Three ways to take part

Pick the door that fits you.

#### Build with us

We need engineers and researchers to work on the backend with Ouri and Eston. The node is called the
Identity Block Chain, and its code is open under the GPL-3.0 licence. The hard problems include signing
every write, encryption, servers that store data without being able to read it, agreement between
nodes, and a safer language for contracts.
[OURI: his list of hard problems replaces the sentence above.]

[Button] I want to build

#### Carry the network

Anyone can run the node today on their own computer, for development. It comes as a Docker image. A
public node is not safe to run yet. Tell us you want to host one, and we will write to you when it is
safe.

[Button] I want to host a node

#### Join Gloki

Gloki is the first app on the network. The pilot starts with one shared forum, where members post and
reply. Ways to discuss and vote together come later.

Please know this before you join. Until encryption is built, the project team can see your data. When
we move to the full network, your data may need to move too. We plan a tool that moves it for you, so
nobody has to be vouched for twice.

[Button] Join the waitlist

If you fund work like this, please write to hello@globaldemocracyinitiative.org.

---

### Waitlist form

**Section heading:** Leave your email

**Field label:** Email address
**Field hint:** We will only use it to write to you about GDI and Gloki.

**Door choice label:** Choose your door
- Build with us
- Carry the network
- Join Gloki

**Button:** Join the waitlist

**Privacy line:** Young World Federalists, Inc. keeps this list on Buttondown. You can leave it at any
time with one click. [Link: Privacy] [EDITOR: still open whether waitlist sign-ups also receive the YWF
newsletter. If they do, this line must say so.]

**After sending:** Thank you. Check your inbox for an email from us. You can reply to it with any
question.

---

## 3. Claims check

Every sentence above that describes what the technology does or will do, mapped to its row in the
one-pager's status board (§5) or protections table.

| Sentence on the page | Status-board row | Check |
|---|---|---|
| "is building an open network ... every member is a real person, each person counts once, and no company or government is in charge" | §1 promise, locked; framed as "is building" | OK |
| "You get in when four people vouch for you ... We are testing this now in the Gloki app." | Get in when four people vouch for you: In test | OK. Uses "vouch", not "people who know you"; no claim to stop fake accounts |
| "We are still deciding how the four people are chosen." | Note on vouching (rule not picked) | OK |
| "The plan is that each record is copied to many members' nodes, so no single company or government holds it." | Records copied across members' nodes: Built, not tested across machines | OK. Framed as a plan |
| "The node can already copy records between members. We have not yet tested this across separate machines, and our live demo runs on one node." | Same row | OK |
| "Today your key works like a password: anyone who has it can act as you." | Nobody can act as you: Being built | OK. States the gap plainly |
| "We are building a way for your phone to sign everything you do, so nobody else can post or vote as you." | Protections: "Your phone signs everything you do": Being built | OK |
| "We are also building encryption, so servers can store your data without being able to read it. Until that is done, the project can see your data." | Encryption; servers that can't read your data: Being built. Pilot rule | OK |
| "There will be no binding vote before an independent security audit." | Protections: H8, a commitment we can make today | OK. Stated as true, as locked in §8 |
| Status-board table, all 11 rows | §5 rows, same order and statuses | OK. "Available for developers" shown as "Ready for developers"; "Research" kept as a label |
| "Anyone can run the node today on their own computer, for development. It comes as a Docker image. A public node is not safe to run yet." | A node anyone can run: Available for developers (local only by default) | OK |
| "The pilot starts with one shared forum, where members post and reply." | One shared forum: In test | OK |
| "Ways to discuss and vote together come later." | §5 note: engagement mechanics belong to Gloki, "comes later" | OK |
| "Until encryption is built, the project team can see your data. When we move to the full network, your data may need to move too." | Pilot rule | OK |
| "We plan a tool that moves it for you, so nobody has to be vouched for twice." | Pilot rule (Ouri's offer of a migration tool) | OK as a plan. [Ouri, before publish: confirm the offer stands] |
| "The node is called the Identity Block Chain, and its code is open under the GPL-3.0 licence." | §3; A node anyone can run (GPL-3.0) | OK. The page's only "blockchain" |
| "His node puts his published research into practice." | §3 | Placeholder: paper links unverified |
| "In 2025 alone, people told the FBI they had lost [NUMBER] ..." | Not a technology claim (sources file B1) | Placeholder |
| "[NUMBER: sourced bot/fake-account figure needed]" | Not a technology claim (missing from research) | Placeholder |
| "more people now say the internet and social media have made people more divided" | Not a technology claim (sources file B3) | Placeholder |
| Barlow quote | Not a technology claim (sources file A1) | Placeholder |

**Not on the page, on purpose:** the words encrypted, secure, private, decentralized and anonymous as
facts; ballot secrecy, data ownership or radio as working; resistance to fake accounts; the names of the
2021 partners; Web5; "four people who know you".
