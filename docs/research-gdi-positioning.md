# Research: GDI positioning (sources and verbatim text)

Collected 27 Oct 2026 by a research agent using web search only. **No page was opened**: the
environment blocked eff.org, archive.org and web.archive.org, and WebFetch failed DNS. "VERIFIED
(index)" means an exact-phrase search on the primary site returned the page; it is not a check
against the page itself. **Before any quote goes on the site, open its URL and check it word for
word.** The GitHub dates in D were fetched directly and are first-hand.


## How this was checked (read this first)

- **WebFetch did not work in this session.** Every host failed DNS (`getaddrinfo ENOTFOUND`), including eff.org and wikipedia.org. Direct `curl` was also blocked by the network policy (CONNECT 403) for eff.org, archive.org and web.archive.org. **I could not open any page, scan or archive.org copy.**
- So all text below comes from **WebSearch** results. When I ran an exact-phrase search limited to the primary source's domain and the tool returned that primary page with the sentence in it, I mark it **VERIFIED (index)**. That is weaker than reading the page myself: punctuation and line breaks may differ. Check every quote against the URL before it goes in print.
- **UNVERIFIED** means I found the text only in secondary sources, or not at all.
- GitHub facts in D came from fetching the repos directly with `git fetch --depth`, so those dates are first-hand.

---

## A. 1990s quotes: the internet will unite humanity

**A1. John Perry Barlow, "A Declaration of the Independence of Cyberspace" (Davos, 8 February 1996)**
Primary URL: https://www.eff.org/cyberspace-independence. A plain-text copy is also listed at https://w2.eff.org/Misc/Publications/John_Perry_Barlow/barlow_0296.declaration.txt
- "We are creating a world that all may enter without privilege or prejudice accorded by race, economic power, military force, or station of birth." **VERIFIED (index)**: an exact-phrase search on eff.org returned this page.
- "We will create a civilization of the Mind in Cyberspace. May it be more humane and fair than the world your governments have made before." **VERIFIED (index)**: the second sentence matched exactly, and the tool said it is the closing line, right after the "civilization of the Mind" sentence.
- The opening words, "Governments of the Industrial World, you weary giants of flesh and steel", were confirmed in the index. The rest of that sentence was not checked.
- Context: EFF describes the Declaration as a response to the US Telecommunications Act of 1996. It is a claim about sovereignty and freedom, not literally about peace.

**A2. Nicholas Negroponte, *Being Digital* (Knopf, 1995), Epilogue "An Age of Optimism"**
Online text of the book: https://archives.obs-us.com/obs/english/books/nn/ch19epi.htm (contents page: https://archives.obs-us.com/obs/english/books/nn/bdcont.htm)
- "It has four very powerful qualities that will result in its ultimate triumph: decentralizing, globalizing, harmonizing, and empowering." **VERIFIED (index)**: returned verbatim from the obs-us epilogue page.
- "Digital technology can be a natural force drawing people into greater world harmony." **VERIFIED (index) for the phrase only.** An exact-phrase search for "drawing people into greater world harmony" matched only the obs-us epilogue page. The full sentence as written here comes from secondary citations. One academic chapter prints it with a comma after "force" and gives the page as 230: https://wacclearinghouse.org/docs/books/usu/passions/chapter16.pdf
- "Like a force of nature, the digital age cannot be denied or stopped." **UNVERIFIED** (found only in a review quotation).
- "The harmonizing effect of being digital is already apparent…" **UNVERIFIED**. An exact-phrase search found no match on obs-us. It appears only on a secondary site (elon.edu Imagining the Internet).
- **Probable misattribution: the "nation-states" line.** "As we interconnect ourselves, many of the values of a nation-state will give way to those of both larger and smaller electronic communities." An exact-phrase search found no source at all. Do not use it until someone checks it against the book. "Harmonizing" is one of the four qualities in the epilogue. I found no primary text that pairs it with nation-states or "world peace".

**A3. Al Gore, remarks at the ITU's first World Telecommunication Development Conference, Buenos Aires, 21 March 1994**
Primary URLs: ITU prepared remarks https://search.itu.int/history/HistoryDigitalCollectionDocLibrary/4.144.57.en.104.pdf. Reprints: http://vlib.iue.it/history/internet/algorespeech.html and http://web.simmons.edu/~chen/nit/NIT'94/94-Appendices-367.html
- "These highways--or, more accurately, networks of distributed intelligence--will allow us to share information, to connect, and to communicate as a global community." **VERIFIED (index)**: matched on the Simmons reprint. Only the part from "networks of distributed intelligence" onward came back in the snippet; the opening words "These highways--or, more accurately," are from memory and were not checked.
- "Our goal is a kind of global conversation, in which everyone who wants can have his or her say." **VERIFIED (index)**: ITU and Simmons copies.
- "And the distributed intelligence of the GII will spread participatory democracy." **VERIFIED (index)**: ITU copy.
- "new Athenian Age of democracy" **UNVERIFIED**. It appears only in a secondary paper (https://arxiv.org/pdf/1412.2078) and did not match on itu.int, iue.it or simmons.edu.
- Note: secondary sources say this speech is often mis-cited as the "Al Gore invented the Internet" moment. That phrase is not in the speech.

**A4. Bill Gates, *The Road Ahead* (1995): UNVERIFIED**
The Elon/Pew predictions database (https://www.elon.edu/u/imagining/?p=25252) paraphrases a passage saying that if the information highway helps citizens of one country understand their neighbours, and so reduces international tensions, that alone could justify its cost. I could not get the exact wording; an exact-phrase search failed. Do not quote it yet.

**A5. Peter Schwartz and Peter Leyden, "The Long Boom", *Wired*, July 1997: UNVERIFIED**
Secondary sources (New Statesman, https://www.newstatesman.com/ideas/2022/07/end-long-boom-neoliberal-fantasy) report the cover promising "25 years of prosperity, freedom, and a better environment". wired.com is blocked to the search tool and the original is paywalled, so this was not verified. I found no source for the phrase "ease tensions throughout the world".

**A6. Howard Rheingold, *The Virtual Community* (1993): useful as a contrast, not a peace prediction**
Primary URL: https://www.rheingold.com/vc/book/intro.html. **VERIFIED (index)**:
- "But the technology will not in itself fulfill that potential; this latent technical power must be used intelligently and deliberately by an informed population."
- "The odds are always good that big power and big money will find a way to control access to virtual communities."

Esther Dyson: not researched; I ran out of time for it.

**Tally:** I have 4 sources with verbatim lines confirmed in the search index: Barlow (3 lines), Negroponte (1 full line plus 1 phrase), Gore (3 lines) and Rheingold (a caveat, not a prediction). None were checked by opening the page.

---

## B. "Technology now divides us": sourced facts

**B1. Crypto fraud losses: FBI IC3 2025 Internet Crime Report (published April 2026)**
URL: https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf. Press release: https://www.fbi.gov/news/press-releases/cryptocurrency-and-ai-scams-bilk-americans-of-billions
- Report text (index): "cryptocurrency investment fraud was the highest source of financial losses to Americans in 2025 with $7.2 billion reported in losses."
- Totals: 1,008,597 complaints, up from 859,532 in 2024. Losses were "nearly $21 billion" (press release), a 26% increase on 2024.
- The report also gives about $11.37 billion in losses linked to cryptocurrency. The search tool said the PDF table layout was unclear, so check this number in the report.
- Caveat (FBI San Diego release): these figures, based largely on victim reports, "are believed to significantly underrepresent actual losses." They are US complaints only.

**B2. Public concern about AI: Pew Research Center**
- 18 Aug 2026 short read, survey of 22–28 June 2026: https://www.pewresearch.org/short-reads/2026/08/18/young-adults-in-the-us-are-increasingly-wary-of-ai-concerned-it-will-take-jobs/
  - "52% of Americans say they are more concerned than excited about the increased use of AI in daily life, up from 37% in 2021." **VERIFIED (index).**
  - 9% are more excited than concerned and 37% are equally excited and concerned. For the first time a majority of under-30s (55%) are more concerned than excited.
- 16 Sep 2026: https://www.pewresearch.org/short-reads/2026/09/16/democrats-are-now-more-worried-than-republicans-about-ai-and-its-impact-on-jobs/ reports 56% of Democrats versus 49% of Republicans.
- Global data: Pew, 17 Sep 2026, https://www.pewresearch.org/global/2026/09/17/concerns-about-ai-are-especially-widespread-in-high-income-countries/ (not checked in detail).
- Caveat: these are US adults only, except the global report.

**B3. Social media and polarisation: the evidence is contested**
- **Evidence for an effect.** Piccardi et al., *Science*, 27 Nov 2025, "Reranking partisan animosity in algorithmic social media feeds alters affective polarization": https://www.science.org/doi/10.1126/science.adu5584
  - Design: a preregistered field experiment with 1,256 X users before the 2024 US election.
  - Result: re-ranking feeds for one week shifted feelings toward the other party by more than 2 degrees on a 0–100 feeling thermometer, in both directions.
  - The authors call the effect roughly comparable to about three years of change in affective polarization. They say it "remains unknown if these effects persist over time."
- **Evidence for an effect on ideology.** Gauthier et al., *Nature* 652 (2026), "The political effects of X's feed algorithm": https://www.nature.com/articles/s41586-026-10098-2
  - Design: 4,965 US users randomly assigned an algorithmic or a chronological feed for 7 weeks in 2023.
  - Result: the algorithmic feed moved opinions toward conservative positions and raised right-leaning content by 2.9 percentage points. Switching from algorithmic back to chronological had no effect on attitudes (summary: https://www.nature.com/articles/d41586-026-00486-z).
  - This study is about ideological direction, not polarisation as such.
- **Evidence against a large effect.** Nyhan et al., *Nature* 620, 137–144 (2023), "Like-minded sources on Facebook are prevalent but not polarizing", the Meta 2020 election studies.
  - Secondary descriptions say that reducing exposure to like-minded sources "does not measurably affect affective polarization or ideological extremity."
  - In companion studies, swapping to a chronological feed also showed no detectable effect.
  - I did not get the abstract's own wording. Critics note the study was run in partnership with Meta.
- **Honest summary for copy:** high-quality experiments disagree. Short-term feed changes on X measurably shifted attitudes, while Meta's 2020 experiments found little or no change in polarisation.

---

## C. Landscape: democracy, deliberation and identity tools active now

| Project | What it is | Identity / Sybil resistance | Hosting | Ballot secrecy | Source |
|---|---|---|---|---|---|
| **Decidim** | Open-source participatory democracy platform (Barcelona origin) | Admin-chosen "authorizations": organisation census (CSV of emails), SMS code, ID-document upload or in-person check, postal-letter code, ephemeral verification | Self-hosted per organisation (central server per instance) | Not established in sources checked | https://docs.decidim.org/en/develop/customize/authorizations.html ; https://docs.decidim.org/en/develop/admin/participants/authorizations/census.html |
| **Polis (pol.is)** | Open-source opinion-mapping and consensus tool (Computational Democracy Project); used by vTaiwan | Default is no login to vote; optional social login; single-use URLs or owner-supplied `xid` for verified-but-anonymous runs; no built-in one-person-one-vote | Hosted service or self-hosted | Votes are on comments, not ballots; identity not revealed to owners unless `xid` is used | https://compdemocracy.org/Identity |
| **Taiwan Join** | Government e-petition platform; 5,000 signatures within 60 days requires an official response | Secondary source says login via Facebook/Google, and proposers need Taiwanese nationality or residence; phone step not confirmed | Central (government) | Not applicable | https://www.dlri.co.jp:443/files/ld/159658.pdf ; https://faunalytics.org/do-online-petitions-actually-change-policy/ |
| **Loomio** | Group decision-making software (cooperative) | Email one-time link or code, optional password; SAML/OAuth SSO | Hosted SaaS or self-hosted | Anonymous poll option exists (3.x); implementation changed across releases | https://help.loomio.com/en/user_manual/users/sign_in ; https://newreleases.io/project/github/loomio/loomio/release/v3.0.22 |
| **Helios** | Open-source web voting with verifiable tallies | Election administrator's voter list or login (auth not covered in sources) | Central server | Homomorphic encryption, trustee decryption; "does not satisfy receipt freeness nor coercion resistance"; server must be trusted not to break secrecy | https://en.wikipedia.org/wiki/Helios_Voting ; https://lsv.ens-paris-saclay.fr/Projects/anr-avote/RAPPORTS/deliv4-3.pdf |
| **Vocdoni / DAVINCI** | Voting protocol and app (Barcelona) | Census Merkle tree of eligible keys; how keys are issued (email, SMS, CSV) is organiser-defined (not confirmed) | Own chain (Vochain); DAVINCI is a ZK rollup on Ethereum | zk-SNARK voter anonymity; DAVINCI adds threshold homomorphic encryption | https://vocdoni.io/en/blog/anonymous-voting-zksnarks ; https://ictlogy.net/bibliography/reports/projects.php?idp=5935 |
| **Rarimo Freedom Tool** | ZK voting app used for citizen-run polls (Russia/Iran claims are promotional) | Biometric passport NFC chip read on phone (government document, no KYC server) | Decentralised (Rarimo zk-rollup L2) | ZK proof severs link between passport and vote | https://rarimo.medium.com/introducing-freedom-tool-15709e9eaa73 ; https://ethereum.org/apps/freedom-tool/ |
| **World ID (World / Worldcoin)** | Proof-of-personhood network | Iris scan by "Orb" (biometric); also selfie and government-ID tiers; about 12M Orb-verified (secondary, 2026) | Company-run hardware plus on-chain protocol | ZK proofs of uniqueness (vendor claim) | https://axios.com/2026/04/17/worldcoin-zoom-shopify-retail-partnership ; https://www.forrester.com/blogs/worldcoin-orb-identity-verification-device-faces-headwinds-in-mass-adoption |
| **Proof of Humanity (Kleros)** | On-chain registry of humans | Photo plus video holding ETH address; vouching by registered users; ETH deposit; challenges go to Kleros court | Decentralised (Ethereum) | Not a voting system; registry is public | https://github.com/kleros/kleros-docs/commit/d8e047d58e82af66086723f22c64a3078f975988 ; https://gov.proofofhumanity.id/t/preventing-vouchallenges-while-incentivizing-a-web-of-trust/1498 |
| **Human Passport (ex-Gitcoin Passport)** | Sybil score from aggregated "stamps" | Stamps (government ID, phone, on-chain history) plus ML model-based detection; apps set thresholds (e.g. score above 20) | Hybrid (company service plus on-chain attestations) | Not a ballot | https://human.tech/blog/human-passport-x-gitcoin-grants-defending-gg23-with-model-based-sybil-detection |
| **Holonym / Human ID** | Zero-knowledge identity | zk-KYC from government ID ("190 countries"), phone, liveness; issues ZK attestations | Foundation-run issuers plus on-chain proofs | Not a ballot | https://docs.human.tech/tech/human-id |
| **BrightID / Aura** | Social-graph uniqueness | Person-to-person connections; Aura "players" verify; older count about 65k users. No 2025 status found | Decentralised node network | Not a ballot | https://forum.brightid.org/t/aura-a-new-verification-for-brightid/393 |
| **Idena** | Proof-of-personhood blockchain | Synchronised worldwide "flip" puzzle sessions each epoch; no ID. Sources are older | Decentralised (own chain) | Not a ballot | https://ethresear.ch/t/can-anyone-come-up-with-attacks-for-idena/6260 |
| **Circles (v2, Gnosis)** | Personal-currency UBI on a trust graph | Trust links between people; docs call this "soft sybil protection" | Decentralised (Gnosis Chain) | Not a ballot | https://docs.aboutcircles.com/overview |
| **Democracy Earth** | Liquid-democracy protocol "Sovereign" | Historically tied to Proof of Humanity (podcast) | Decentralised (design) | Not established | https://github.com/DemocracyEarth/paper. **No 2024–26 activity found; status unclear** |
| **Agora (Swiss)** | Blockchain voting company | Not established | Not established | Not established | The 2018 Sierra Leone "first blockchain election" claim was **denied by the NEC**; Agora was an accredited observer with a partial deployment: https://www.theregister.com/2018/03/21/no_sierra_leone_did_not_run_the_worlds_first_blockchain_election/ |
| **Global Assembly 2021** | 100-person global citizens' assembly on climate, timed to COP26 | Geographic sortition: 100 population-weighted random points, then participants recruited via local organisations (in person, not digital ID) | Central organiser | Not applicable | https://en.wikipedia.org/wiki/Global_Assembly ; https://globalassemblyorg-p84kb.kinsta.page/the-core-assembly.html |
| **DemocracyNext** | Research and action institute for citizens' assemblies (sortition, deliberation, rotation); 2025 partner cities Kerewan, Vilnius, Esch-sur-Alzette | Civic lottery, run offline | Not a software platform | Not applicable | https://www.demnext.org/uploads/DemNext-Impact-Report-2025.pdf |
| **Stanford Online Deliberation Platform** | AI-moderated video small-group deliberation (Deliberative Polling); "over 100,000 deliberation hours in over 35 countries" (2025 talk) | Scientific samples recruited by survey firms (e.g. NORC) | Central (Stanford) | Not applicable | https://deliberation.stanford.edu/tools-and-resources/online-deliberation-platform |
| **Talk to the City (AI Objectives Institute, 2023–)** | Open-source tool that uses an LLM to cluster opinions; used with Polis data | None of its own (it analyses input) | Self-host / open source | Not applicable | https://civictech.guide/listing/talk-to-the-city |

Not researched with sources: Stand With Crypto (only a launch article found: https://www.ghacks.net/?p=200624; sign-up method unconfirmed) and Esther Dyson.

**What the evidence shows (neutral).** None of the systems above combines all three of these: one-person-one-vote that works across borders, no central operator, and secret ballots.
- **Hosted deliberation and voting tools** (Decidim, Loomio, Polis, Helios, Join, Stanford) identify people through email, SMS, social login, organiser lists or government processes. They run on central servers chosen by the organiser. Ballot secrecy, where it exists (Helios), depends on trusting that server or its trustees.
- **Decentralised proof-of-personhood systems** get uniqueness from one of four sources:
  - biometrics (World ID's iris Orb);
  - government documents (Freedom Tool passports, Holonym zk-KYC);
  - social vouching or trust graphs (Proof of Humanity, BrightID, Circles);
  - synchronous puzzles (Idena).
  Most of them are tied to crypto tokens, chains or deposits. Social-graph projects report small user bases or stale status.
- **ZK anonymous voting** exists (Vocdoni, Freedom Tool), but it depends on an eligibility list or ID document supplied from outside the system.
- **Global deliberation** (Global Assembly, DemocracyNext) relies on offline sortition and facilitation, not digital identity.

---

## D. Web5 / TBD, and Solid

**TBD wound down: announced 7 November 2024.** Source: Block Q3 2024 Shareholder Letter, https://s29.q4cdn.com/628966176/files/doc_financials/2024/q3/Shareholder_Letter_Block_3Q24.pdf
- The search index returned the letter's wording as: "scaling back our investment in TIDAL and winding down TBD". The letter frames the move as making room for its bitcoin mining initiative and the Bitkey self-custody wallet.
- TechCrunch, 7 Nov 2024: "Block is also shutting down TBD, a Bitcoin-focused arm of the business that previously set out to build a decentralized internet, dubbed 'Web5.'" https://techcrunch.com/2024/11/07/block-scales-back-tidal-investment-and-shutters-tbd-in-favor-of-bitcoin-mining/

**Code moved to DIF and is now dormant.** I fetched the repos directly on 2026-10-27.
- https://github.com/decentralized-identity/dwn-sdk-js. Last commit **2024-10-23**: "update version for new release (#828)".
- https://github.com/decentralized-identity/web5-js. Last commit **2024-10-22**: "Version Packages (#962)".
- The old `TBD54566975/*` URLs return the same history, which suggests the repos were transferred.
- **DWN spec** https://github.com/decentralized-identity/decentralized-web-node. The last change to `spec/spec.md` was **2024-09-04** ("Add `prune` functionality to `RecordsDelete` section. (#305)"). The latest commits (2026-10-02, 2026-10-07, 2026-10-21) touch only `docs/agenda.md`, i.e. meeting notes. One commit message says "Document DIF meeting notes from October 2, 2024" even though it was committed on 2026-10-02.
- The dwn-sdk-js README says the specification "is in a draft state". **Conclusion: the code has not been maintained since October 2024; some activity continues at DIF in meeting notes only.**

**Solid (Tim Berners-Lee / Inrupt): active in 2026 through W3C standardisation.**
- The W3C chartered the Linked Web Storage Working Group in September 2024, running to 8 September 2026: https://www.w3.org/2024/09/linked-web-storage-wg-charter.html
- W3C news, 31 Mar 2026: "the Linked Web Storage Working Group published today a First Public Working Draft of Linked Web Storage Protocol 1.0": https://www.w3.org/news/2026/first-public-working-draft-linked-web-storage-protocol-1-0/
- I found no 2025–26 Inrupt or Berners-Lee announcements. Whether the charter was extended after September 2026 was not checked.
