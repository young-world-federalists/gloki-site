# Draft C: Keep the promise

**Angle:** technology broke this, and technology has to fix it. The status board is part of the
argument: after years of hype, we tell you exactly what works and what doesn't.
**Written:** 26 Oct 2026, against `docs/positioning-gdi.md` v2 (locked).
**Placeholders** are in square brackets and must be cleared before publish. Notes for Eston are
in *italics* and are not page copy.

---

## 1. Headline options

# There will be no global democracy without technology.

# The internet filled up with fake accounts. We are building a network of real people.

# Each person counts once. No company or government is in charge.

**Recommended: option 1.** It is the locked opening line, and it states the point of view in one
sentence. The promise sits right under it as the subline, so the reader gets the belief and the
plan before they scroll. Options 2 and 3 work as h2s or as share-card text.

---

## 2. Page copy

### Hero

# There will be no global democracy without technology.

The Global Democracy Initiative is building an open network for global democracy, where every
member is a real person, each person counts once, and no company or government is in charge.

You have heard big promises about technology before. So this page shows what works today and
what does not, one part at a time.

[Button] Join the waitlist  ·  [Link] See what works today

---

### The internet was supposed to bring us together

In the 1990s, many people believed the internet would bring the world together. They said it
would let anyone talk to anyone, across every border.

> [QUOTE: John Perry Barlow, "A Declaration of the Independence of Cyberspace", 1996. Expected
> line: "May it be more humane and fair than the world your governments have made before."
> UNVERIFIED, check on eff.org before use]

Some of that came true. You can talk to someone on another continent in a second. A student
anywhere can learn almost anything for free.

---

### What happened instead

Then the same tools were used to pull us apart.

The internet filled up with fake accounts. Some are run by machines. Some are run by people who
are paid to pretend. [NUMBER: sourced bot/fake-account figure needed]. When you read a comment
online, you often cannot tell if a real person wrote it.

Social media learned that anger keeps us looking at the screen. So it shows us more of what
makes us angry, and less of the people we disagree with.

Crypto promised money that no bank controls. For many people it became a way to lose money. In
2025, people in the United States reported losing [NUMBER: FBI IC3 2025 Internet Crime Report,
crypto losses about $11.4 billion, verify on ic3.gov] to crypto fraud. Crypto burned a lot of
trust. We feel it every time we tell someone we are building a network.

Now many people are afraid of AI. A machine can already write like a person. It is getting
harder to know who is real online.

Each time, the pattern was the same. The big promises came first. The truth came later.

---

### Why we still build with technology

We still believe there will be no global democracy without technology.

People in different countries cannot meet in one hall to make a decision together. Most of them
will never meet at all. If the people of the world are going to decide anything together, a
network has to carry their voices.

So we are not walking away from technology. The tools that broke our trust were built to sell
ads or to make a few people rich. We want to build one for a different job: helping people
decide things together, as equals.

---

### What democracy needs first

Before anyone votes, you have to know two things. Each voice belongs to one real person. And
each person counts once.

Inside one country, a government list usually does this job. Across borders, there is no such
list. Today's democracy apps use a city register, a list the organiser brings, tokens you can
buy, or no check at all. None of these
works across borders without a government, a company or money in the middle.

This is the missing piece. It is the part we are building.

---

### What we are building

GDI is building the network underneath. Gloki is the first app on it.

Here is how you get in. Four members of the network vouch for you. That means they confirm that
you are a real person. You do not upload an ID card or scan your face.

We cannot promise yet that this keeps out every fake account. That depends on how the four
people are chosen, and we have not settled that rule. When we do, this page will say which rule
we picked and why.

The network is built on Ouri Poupko's open-source node. Ouri is part of GDI. The node puts his
published research into practice. [LINK: Poupko, Shapiro, Talmon, "Self-Sovereign Digital Agents
for a Grassroots Digital Society", ICDCS 2022. UNVERIFIED, check on dblp.org before linking]

In the Gloki pilot, all members share one forum. You can post, reply and like. Voting comes
later, on a network that by then has real, vouched-for people in it.

---

### What works today, and what does not

After years of hype, you deserve a straight answer. This table lists every part of the plan and
where it really stands. Read it before you believe anything else on this page.

| What | Status | What that means today |
|---|---|---|
| You get in when four members vouch for you | **In test** | Works in the app. The rule for choosing the four people is not final. |
| One forum for all members | **In test** | Works in the app. |
| A node (a small server) that anyone can run | **Ready for developers** | You can run it on your own computer to build and test. It is not safe to run in public yet. |
| Records copied to many members' nodes | **Built, not yet tested on many computers** | The node can do this. We have only tested it on one computer, and our live demo runs on one node. |
| Nobody can post or vote as you | **Being built** | Today the node does not check who sends a request. |
| Your data on your own server | **Possible, not used yet** | The design allows it. In the demo, everyone's data sits on one server the project runs. |
| Servers that store your data but cannot read it (encryption) | **Being built** | Not done. Until it is, the project can see your data. |
| Nobody can see how you voted | **Planned** | A written plan. Nothing to use yet. |
| Leave and take your identity with you | **Planned** | A written plan. Nothing to use yet. |
| Lose your phone and keep your vote | **Planned** | A written plan. Nothing to use yet. |
| Reach places with no internet, by radio | **Research** | We are studying whether it can work. |

One thing is already true, because it is a rule and not a feature: **there will be no binding
vote on this network before an independent security audit.**

If you join the pilot, know this. Until encryption is ready, the people running the project can
see your data. When the full network is ready, your account may need to move to it. Ouri has
offered to write a tool that moves it for you, so you do not need to be vouched for twice.

---

### Where this came from

GDI started in 2021 as a coalition of seven organisations. They shared one idea: the world needs
a way to make decisions together.

In 2023, people from that group wrote a white paper about a global digital voter identity. They
called it Gloki. [LINK: 2023 white paper PDF] Many ideas changed once we started to build. Where
the paper and the app differ, the app is what counts, and this page describes the app.

The coalition is no longer active. Today GDI is a project of Young World Federalists, Inc.,
which is its legal and financial home.

---

### Three ways in

Pick the one that fits you.

**Build with us**
We need engineers and researchers to work on the back end with Ouri and Eston. The problems are
hard: proving that each action really came from you, encryption, servers that store data they
cannot read, getting many computers to agree on one record, and a safer language for the small
programs that run on the network. [OURI: his list of hard problems goes here] The node is called
the Identity Block Chain. Its code is open under GPL-3.0. [LINK: node repository]

**Carry the network**
Anyone can run the node today on their own computer, to build and test. A public node is not
safe to run yet. Tell us you want to carry the network, and we will write to you when it is.

**Join Gloki**
Gloki is the first app on the network. Join the waitlist for the pilot, and we will write to you
when there is a place.

**Funders:** if you want to talk about supporting this work, write to
hello@globaldemocracyinitiative.org.

---

### Waitlist form

**Heading:** Join the waitlist

**Field label:** Your email

**Door choice label:** How do you want to take part?
- Build with us
- Carry the network
- Join Gloki

**Button:** Add me to the list

**Privacy line:** We will only write to you about GDI and Gloki. Young World Federalists, Inc.
keeps this list. You can leave it at any time from any email we send.

*Note: "only about GDI and Gloki" follows Eston's rule in `docs/brief-gdi-positioning.md` that
waitlist sign-ups must not get the YWF newsletter. PRODUCT.md still lists this as open; confirm
the Buttondown tag setup matches before publish.*

**Footer credit:** Built on Ouri Poupko's open-source node. GDI is a project of Young World
Federalists, Inc.

---

*Body copy from the hero to the doors, excluding the status table, headings and placeholders:
about 970 words. The form microcopy is extra.*

---

## 3. Claims check

Every sentence that says what the technology does, mapped to its status-board row.

| Sentence on the page | Status-board row | Result |
|---|---|---|
| "GDI is building an open network ... every member is a real person, each person counts once, and no company or government is in charge." | Locked promise (§1), stated as "is building" | OK |
| "Four members of the network vouch for you. That means they confirm that you are a real person." | Get in when four people vouch for you: In test | OK (described as how you get in; table says In test) |
| "You do not upload an ID card or scan your face." | Same row | OK (true of the vouching design) |
| "We cannot promise yet that this keeps out every fake account." | Vouching note (§5) | OK (no fake-account resistance claimed) |
| "The network is built on Ouri Poupko's open-source node." | A node anyone can run: Available for developers | OK (locked credit line) |
| "The node puts his published research into practice." | §3 | OK; paper link is a placeholder, UNVERIFIED |
| "In the Gloki pilot, all members share one forum. You can post, reply and like." | One shared forum: In test | OK |
| "Voting comes later." | Gloki engagement mechanics: comes later (§5) | OK |
| Status table, all rows | Every §5 row, same status | OK |
| "There will be no binding vote on this network before an independent security audit." | Commitment (§5, H8) | OK (a policy, stated as true per §8) |
| "Until encryption is ready, the people running the project can see your data." | Encryption: Being built; pilot rule | OK |
| "Your account may need to move ... Ouri has offered to write a tool that moves it for you." | Pilot rule (§5) | OK (stated as an offer, not a feature) |
| "Anyone can run the node today on their own computer, to build and test. A public node is not safe to run yet." | A node anyone can run: Available for developers | OK |
| "The node is called the Identity Block Chain. Its code is open under GPL-3.0." | §3 | OK (the one use of "block chain") |
| Barlow quote | Sources A1 | Placeholder, UNVERIFIED |
| Fake-account figure | None in research | Placeholder, figure needed |
| Crypto losses figure | Sources B1 | Placeholder, UNVERIFIED |
| Paper link (ICDCS 2022) | Sources E | Placeholder, UNVERIFIED |
| 2023 white paper link | PRODUCT.md, Publisher | Placeholder, link needed |
| Ouri's list of hard problems | §4, [Ouri: the list] | Placeholder |
