# Review by Dr. Giorgia (political scientist, digital democracy and deliberation)

## 1. First 60 seconds

**A.** "The internet promised to bring the world together." I think this is a civic-tech essay, and I keep reading because the hero sentence is concrete. I would pick "Build with us" only if the research is real. I would check the papers first.

**B.** "One person, one vote, across borders. We are building the part that is missing." This is a position claim, and a rather bold one. I read on to see who "the missing part" is missing for. The four-way taxonomy tells me quickly whether they know the field. Door: none yet, but I'd click "See what works today".

**C.** "There will be no global democracy without technology." My first reaction is "no, that is the claim you have to prove". I read on because the subline says they'll show me what does not work. Door: none.

## 2. Full read: where I got lost, suspicious, convinced

- Convinced (all): the status board and "Until encryption is built, the project can see your data." Pilots that say this are rare. It buys real trust.
- Suspicious (B): "It also filled up with fake accounts and bots... People became more divided, and fraud grew." Flat causal chain with no hedge.
- Suspicious (C): "Social media learned that anger keeps us looking at the screen. So it shows us more of what makes us angry, and less of the people we disagree with." This asserts a filter-bubble mechanism the literature disputes.
- Suspicious (C): "Crypto promised money that no bank controls. For many people it became a way to lose money." The FBI figure is fraud involving crypto, not crypto itself.
- Lost (C): "Now many people are afraid of AI. A machine can already write like a person." It is not tied to the argument.
- Suspicious (A, B, C): "Today's democracy apps use a city register, a list the organiser brings, tokens you can buy, or no check at all." See finding 2.
- Lost (B): "Random choice matters: people making fake accounts cannot pick each other." Then the next sentence says "we make no claim about stopping fake accounts." Which is it?
- Convinced (B): the plain glosses beside each paper, and "Each is a sensible choice for the job it was made for."
- Gap (all): "Before anyone votes, you have to know two things" (C). Nothing about who sets the question, who is bound by the result, or how people deliberate.

## 3. Ranking

1. **B**: fairest taxonomy, the only draft that says why random vouchers matter and lists three papers with authors. It buries the research behind a "for builders" heading.
2. **A**: most careful with causal claims (Pew is about what people say, not about what caused it). The research section is thinnest.
3. **C**: best argument that technology is needed, but the weakest on causal claims (anger, crypto, AI).

## 4. Findings

**Blocker**

1. **Contested causal claims stated as fact** (B: "People became more divided, and fraud grew"; C: the "anger" paragraph, "Crypto burned a lot of trust", "harder to know who is real online"). A page whose selling point is honesty cannot assert the polarisation mechanism. Fix: use A's form ("more people now say...") with a source, or cut.

**Major**

2. **The taxonomy flattens very different tools** (A "Today's democracy tools check...", C "Today's democracy apps use..."; the positioning lists Consul, Decidim, Vocdoni, Polis, Democracy Earth). Polis is an opinion-mapping tool, not a voting tool, so "no check" is a design choice there, not a gap. Decidim offers several verification methods. Sortition (citizens' assemblies, deliberative polls) is missing, and it answers "who counts" by random selection. The nearest rivals (BrightID, Proof of Humanity, Worldcoin) are named only in B. Fix: keep B's "sensible choice for the job it was made for", name the tools or drop the generalisation, and say that none of this is about deliberation.
3. **"Each person counts once" is stronger than Sybil-resilience research can give.** Without a trusted authority, Sybil attacks can only be bounded (Douceur), not removed. Trust-graph results hold under assumptions about honest-region connectivity and attack edges. "Every member is a real person" (all heroes) and "no one in charge" pull against that. Fix: say "limits fake accounts" in the research section and state the assumption in one line.
4. **Research credibility gap.** "The node puts his published research into practice" (A, B, C) while the pilot uses vouching by people you choose, which "has no server code yet" and carries no fake-account claim. The paper's guarantee therefore does not apply to the pilot. Fix: say which paper's mechanism the pilot implements today.
5. **Random vouchers vs. "confirm that you are a real person"** (B, C). If the four are chosen at random, they are strangers. What do they check? That question decides whether the mechanism is more than a ritual. The page should answer it.
6. **Identity is treated as the precondition of legitimacy** (C "What democracy needs first"; B "every vote must first answer one question"). One person, one vote is necessary, not sufficient. Legitimacy also needs agenda-setting, deliberation, inclusion and a body the result binds. "No binding vote before an audit" (all) never says binding on whom.
7. **Why global democracy?** Draft A's "The whole world cannot meet in one room" and draft C's "a network has to carry their voices" show that technology is needed *if* global decisions are made. They do not show that a global electorate is desirable or feasible. Transnational assemblies (e.g. 2021 Global Assembly) exist and are never mentioned.
8. **Barlow as "the promise"** (A, B, C). His Declaration is a cyber-libertarian text against governments, not a promise to bring the world together. Fix: say "some early internet writers hoped", or use a quote that actually makes that promise.
9. **The offline third.** "A student anywhere can learn almost anything" (C). Billions are still offline (ITU figure needed). Radio is only "Research". A global-democracy page should say who is excluded by the design today.

**Minor**

10. Waitlist: say whether the pilot gathers research data and who the data controller is (see section 5).
11. B's "Random choice matters" and the "we make no claim" line need reconciling (see 5 above).

**Sources the page needs**: bot/fake-account share; Pew divided claim (A only, fine if checked); FBI IC3 figure (and label it as fraud involving crypto); the AI-fear claim (survey); "many people believed" in the 1990s; the anger/echo-chamber claim (or cut); any claim about how many people are offline.

## 5. What a researcher needs (questions the page or a linked page must answer)

- Evaluation: what will you measure in the pilot (admission of fake accounts under a red-team test? inclusion by country and gender? retention?) and who sees the results, including negative ones?
- Threat model: which attacker is assumed, and how many members must be corrupt before the guarantee fails?
- Ethics: is there a research-ethics review or an independent advisor? Are pilot members told they are in an experiment? Is GDPR consent separate from the waitlist?
- The vouching graph is a map of social ties that "the project can see". Who is the controller, how long is it kept, and what protects a dissident vouched into the network?
- Data access: can outside researchers get anonymised graph and activity data? Under what conditions?
- Who is in charge today? The demo runs on one node the project operates, and YWF Inc. is the legal host. How does that square with "no one in charge", and what is the governance path?
- Funding and conflicts: who pays, and who decides if the pilot "worked"?
- Which deliberative design will Gloki test, and against what baseline?

## 6. Keep list

1. "We build it in the open, and this page says plainly what works today and what does not." (B)
2. The status table with "Where it stands" and its column of plain consequences, especially "Until this is done, the project team can see your data." (B/C)
3. "We cannot promise yet that this keeps out every fake account. That depends on how the four people are chosen..." (C)
4. "Each is a sensible choice for the job it was made for." (B) plus the paper list with glosses (B)
5. A's Pew phrasing: "more people now say..." (a perception claim, correctly worded).

## 7. Would I act?

**Yes, cautiously: "Build with us", as a researcher.** I would write to ask about an evaluation plan, not join the waitlist. The one thing that would change my answer to "no": if the Sybil-resistance paper cannot be tied to what the pilot actually runs, or if there is no ethics or data-protection statement for pilot members.
