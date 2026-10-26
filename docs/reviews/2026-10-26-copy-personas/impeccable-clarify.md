# Impeccable `clarify` review: home-page drafts A, B, C (26 Oct 2026)

Review only. Context was read directly, because the Impeccable launcher is blocked in this session. Mode: Persuade. Claims are locked; one is flagged only where it is unclear or inconsistent.

## 1. Persuade test (first viewport, 360px)

**A.** The h1 names a feeling, not the offer. Until the subline, a reader sees an essay about the internet. The action hierarchy is right (one button, one text link), but the button only jumps to the form. Nothing in view that only GDI can prove.

**B.** The clearest offer ("One person, one vote, across borders"). But the h1 is two sentences (about 5 lines on a phone), and about 70 words follow it, repeating "one real person, counted once" three times. The buttons fall below the fold, and two equal buttons with "See what works today" first leave the primary action unclear.

**C.** The h1 is a belief, but the promise sits right under it, and "this page shows what works today and what does not" is the only hero line specific to this project. It has the clearest action hierarchy.

**All three:** the form is not in the first viewport, which the surface contract requires, and none states the fact only this product has: **you get in when four people vouch for you**. It is locked, in test, and belongs in the hero.

## 2. Message hierarchy

| Block | Fact needed now | Next action | Context that changes the decision | Best |
|---|---|---|---|---|
| Hero | Each person counts once; four people vouch you in | Email + way in, in view | Most parts are not built yet | C |
| Status board | Two things work in the app; the rest doesn't yet | Join | The project team can see your data; the audit rule | C wording, A columns, B date |
| Build with us | Engineers and researchers wanted | Pick it in the form | GPL-3.0; Ouri's list | C |
| Carry the network | A public node is not safe yet; this records interest | Leave your email | You can run it on your own computer today | A |
| Join Gloki | The pilot is one shared forum | Join the waitlist | Your data is visible to the team; your account may have to move | A + C's "we will write" |
| Form | One email, one way in | Button | Newsletter or not; how to leave | A |

## 3. Clarify audit

| Draft | Quoted text | Issue | Fix |
|---|---|---|---|
| All | hero "[Button] Join the waitlist" | Missing consequence | Put the working form in the first viewport. |
| B | "One person, one vote, across borders. We are building the part that is missing." | Phone scanability | First sentence is the h1; the second becomes the subline. |
| A, B | "Join the waitlist" / "Join the list" with Build selected | Vague label | One button, "Sign me up", then a complete after-message for each way in. |
| A | "I want to build" / "I want to host a node" | Inconsistent terms | Cut the per-door buttons: one form, one button. |
| A, B | "Choose your door" / "Which door is yours?" | Jargon, translation risk | C's "How do you want to take part?" |
| All | "only … about GDI and Gloki" (B: "about GDI") | Inconsistent claim | The newsletter question is still open; use one line once Eston decides. |
| A vs B | "Check your inbox" vs "Check your email to confirm" | Missing consequence | Check Buttondown's opt-in. If it is double: "Confirm your email to finish." |
| C | "when there is a place" | Unclear claim | Suggests a cap on places that nobody has stated: "when the pilot opens". |
| C | "Four members of the network vouch for you" | Inconsistent with locked wording | "four people vouch for you". |
| B | "In the pilot, everyone's data sits on one project server" | Inconsistent claim | The fact is about the demo, and the pilot hasn't started. |
| A, C | "Ready for developers"; "not yet tested on many computers" | Inconsistent label | "Available for developers"; "not tested across computers". |
| A | "Today your key works like a password" | Jargon | Introduce the key first: "You sign in with a key." |
| B, C | "binding vote" | Jargon | Keep A's gloss: "one whose result counts for real". |
| A, B | "a safer language for contracts" | Ambiguous term | C's "small programs that run on the network". |
| B | "we will write when it is" | Ambiguous | "…when it is safe to run." |
| B | "we will tell you what the project can see" | Missing consequence | Say it now, at the door. |
| B, C | 11-row, 3-column board | Phone scanability | At 360px, group the rows under status headings, one line each with an optional note. |
| All | "[LINK: 2023 white paper PDF]", "[Link: Privacy]" | Link text | "Read the 2023 white paper (PDF, size)"; "How we use your email". |
| A, C | "keeps us scrolling", "pull us apart", "burned a lot of trust" | Translation risk | Use plain verbs: "divide us", "made people distrust". |

## 4. Glossary for the merged page

| Use | Avoid |
|---|---|
| **vouch**, vouched for | verify, verified, approve |
| **four people** (locked) | four members, people who know you |
| **node** (a small server that keeps a copy of the network) | server, machine |
| **your own computer** | machine, locally |
| **the network** | platform; "blockchain" except once in the builder copy |
| **Gloki** (the first app) | beta, the pilot app |
| **the pilot** (what the waitlist joins) | beta, test, launch |
| **the demo** (today's build, one node) | pilot |
| **the project team** (who can see your data) | the people running the project |
| **ways to take part** | door, ways in |
| **waitlist** | the list |
| **back end** | backend |
| **Status labels** from the board, unchanged | Ready for developers, Not built yet |

## 5. Merge recommendation

- **Hero: C,** with the locked vouching fact added and the working form in view. B's "One person, one vote" becomes the missing-piece h2.
- **Story: C's order and sentences.** Fold the AI paragraph into the one on fake accounts. Add A's "a student in Lagos can message a student in Lima" and B's four-answer list on who counts.
- **Status board: C's rows and notes, grouped by status,** plus B's date, A's definitions of Planned and Research, and the audit rule set apart. B's builder section and plan table move to a linked page or a collapsed block.
- **History: B.** **Ways to take part: C,** plus A's data notice on Join Gloki.
- **Form: A's structure,** C's choice label, one button and three after-messages.
