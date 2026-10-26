# Persona review: synthesis (26 Oct 2026)

Seven reviews of copy drafts A, B and C: Thandiwe (pilot participant, Lilongwe), Dr. Giorgia
(researcher), Viktor (privacy skeptic), Lena (backend engineer), Samira (funder), Kofi (world
federalist), and an Impeccable `clarify` pass (method followed from its reference files; its
binary was not run). Lena's code claims were spot-checked against `ouripoupko/ibc` and hold.

## Rankings

| Reviewer | 1st | 2nd | 3rd |
|---|---|---|---|
| Thandiwe | C | A | B |
| Giorgia | B | A | C |
| Viktor | C | A | B |
| Lena | B | A | C |
| Samira | B | A | C |
| Kofi | A | C | B |

Experts rank B first and general readers rank it last. C wins the hero and the honesty. A is never
last: its story sections are the safest base. So: C's hero, A's story, B's substance moved to a
builder page.

## Findings raised by more than one reviewer

| # | Finding | Raised by | Severity |
|---|---|---|---|
| 1 | "The project" is never named. No team, roles, operator of the pilot node, legal home or decision process near the data warning | Viktor, Samira, Giorgia | Blocker |
| 2 | Join Gloki says nothing about cost, what the pilot is, who it is for, what happens after the email, or who vouches for the first people | Thandiwe, Kofi, Impeccable | Blocker |
| 3 | Causal claims stated as fact: "anger keeps us looking" (C), "people became more divided, and fraud grew" (B), "crypto burned trust" (C) | Giorgia | Blocker |
| 4 | Vouching oversold: "works in the app" / "we are testing this" when the pilot's rule has no server code; B's "fake accounts cannot pick each other". The node operator can also steer the random pick (timestamp from the receiving node's clock, `ibc.py:44`), and with no authentication anyone can call `approve` as any member | Viktor, Lena, Giorgia | Major |
| 5 | Impersonation understated: "your key works like a password" | Viktor (and our own check) | Major |
| 6 | B's builder section is technically wrong: consensus is not "what makes the node a blockchain"; partners are identities, not nodes; the node runs PBFT, not Cordial Miners; `nakamoto.py` is a stub. "Built, not tested across machines" oversells the consensus code (no signature checks, no view change) | Lena | Blocker for B's section |
| 7 | The Barlow quote fits badly: his Declaration told governments they have no place in cyberspace, which clashes with a democracy project | Kofi, Giorgia | Major |
| 8 | An 11-row, 3-column status table does not scan at 360px. Group rows under status headings, one line each | Thandiwe, Impeccable | Major |
| 9 | The first viewport has no email field or choice of way in | Impeccable | Major |
| 10 | The audit commitment is empty as worded: "binding" and "independent" are undefined | Viktor | Major |
| 11 | "Build with us" has no repo link, open-problems list, contact or decision process | Lena, Samira | Major |
| 12 | The app's licence is unstated; the node is GPL-3.0 | Samira, Lena | Major |
| 13 | The page never says what the network is for in democratic terms, or argues why global democracy is needed | Kofi, Giorgia | Major |
| 14 | Too long for a phone on paid data; reading-level traps: Cyberspace, Davos, "keeps us scrolling", "burned trust", hype, register, binding vote, carry the network | Thandiwe | Major |
| 15 | Terms drift (node/server/machine, vouch/verify, pilot/beta/demo, four people/four members) | Impeccable | Minor; glossary in `impeccable-clarify.md` §4 |

## Keep (named by two or more reviewers)

- C's hero line: "You have heard big promises about technology before. So this page shows what
  works today and what does not."
- A: "A student in Lagos can message a student in Lima in seconds" and "The internet connected
  us. It did not give us a fair way to decide anything together."
- B's headline "One person, one vote, across borders" (as an h2 or share line).
- The status board's column of plain consequences, especially "Until this is done, the project
  team can see your data."
- "Where the paper and the app differ, the app tells you what is true now."
- The audit commitment, once defined.

## Merge plan (draft D)

1. **Hero:** C's h1 and honesty line, then the email field and the choice of way in.
2. **Story:** A's short version, using A's hedged "more people now say" form for every empirical
   claim. No Barlow quote unless a better-fitting one is verified.
3. **What it is for:** one paragraph on the network's democratic purpose (Kofi, Giorgia).
4. **Who counts today:** B's four approaches, corrected (Polis is not a voting tool; Decidim
   supports several verification methods; mention random selection, as citizens' assemblies use).
5. **Status board:** grouped by status, one line per row, with a last-updated date. Vouching reads
   "shown in the demo; the server does not run the pilot's rule yet". Impersonation stated plainly.
6. **Who we are:** names, roles, the legal home, who runs the pilot node, how decisions are made.
7. **The pilot:** free, who it is for, what you do, who vouches first, and the data warning with
   the operator named.
8. **History:** B's section plus why the coalition stopped (Kofi).
9. **Three ways to take part**, with "Build with us" linking to a separate builder page (B's
   section, corrected per Lena, plus the open-problems list and repo link).
10. **Form:** A's structure, C's choice label, one button label, a complete message after sending.

## Needs Eston (facts only he can give)

See the session reply of 26 Oct for the list: team and decision process, the pilot operator, pilot
facts (who for, when, cost, first vouchers), the Barlow call, the audit wording, the builder page,
whether the pilot names a region or cause.
