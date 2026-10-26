# Lena (34, backend / distributed systems, Berlin): review of drafts A, B, C

Checked against `ibc` and `community_contract.py` (server-side).

## 1. First 60 seconds

**A.** "The internet promised to bring the world together." Nice, but it's a manifesto opener and I've read it before. The second sentence ("open network... no company or government is in charge") is what keeps me scrolling. "See what works today" is the link I'd tap. Door: Build, after the board.

**B.** "One person, one vote, across borders. We are building the part that is missing." Better: it names a technical problem (Sybil resistance across jurisdictions). "This page says plainly what works today and what does not" is the line that makes me read on. Door: Build.

**C.** "There will be no global democracy without technology." A slogan, with a sentence after it about hype. The honesty is promised before I've seen any project. I keep reading, a bit more sceptical.

## 2. Full read: where I got lost or convinced

- Convinced (A, B, C): the status board. "Nobody can act as you / Being built" with "Today the node does not check who sends a request" (C). That matches the API docs ("No built-in authentication... there's no password, signature, or token").
- Suspicious (B): "Nodes called partners agree on one shared, ordered record. This is called consensus, and it is what makes the node a blockchain." See findings 1 and 2.
- Suspicious (A, B, C): "Records copied across members' nodes: Built". The code is `pbft.py`, and it contains `# I should check signatures and digest, but I am lazy` and `# should wait on time out from request to change view`. Without signature checks or view change, "built" oversells it.
- Lost (A, B, C): "Carry the network". I can run a Docker node, but it joins nothing. What would carrying mean later?
- Lost (all): who decides? "no company or government is in charge", yet Ouri and Eston are the only named backend people and YWF is the fiscal host.

## 3. Ranking

1. **B.** The only draft with an architecture section for builders. It needs fixing but it is the right shape.
2. **A.** The cleanest board and the best "Carry the network" text. It has no builder depth.
3. **C.** The most preamble. Its best contribution is the per-row "what that means today" column, which B also has.

## 4. Findings

1. **blocker** (B). "consensus, and it is what makes the node a blockchain." Wrong and oversold. In the code, consensus runs **per contract**, among that contract's partners, using a PBFT-style three-phase protocol. Blocks are lists of requests, hashed but not chained to a previous hash. The only Nakamoto code is a commented stub, so there is no global ledger. A fair description is "a replicated, ordered log per contract, agreed by BFT among its partners". Fix: drop the sentence or say that. A reader who knows the field will read this as marketing.
2. **major** (B). "Nodes called partners". Partners are agent identities on a contract, each with an address, not nodes. Fix: "the agents on a contract (its partners)".
3. **major** (A, B, C). "Built, not yet tested across machines". Add the known gaps: message signatures are not checked, there is no view change, and 3 partners tolerate zero Byzantine faults (n=3 gives f=0). We would call this a prototype. Fix: one more clause in the row.
4. **major** (B). The Cordial Miners (DISC 2023) link under "papers on consensus". The node runs PBFT, not Cordial Miners. I'd assume the paper is implemented. Fix: say "related research" or drop it.
5. **major** (B). "Random choice matters: people making fake accounts cannot pick each other." The contract does use `random(timestamp(), ...)`, but the timestamp is set by the receiving node (`ibc.py`: `datetime.now()`), so a requester running their own node could try to grind it. The contract picks two non-overlapping edges, i.e. four linked members, not "four members at random". Also, with no authentication, anyone can call `approve` as any member. Fix: "random" needs an adversary model, or the claim should shrink to "designed so that". Also, the contract's 4-regular property starts only at 5 members.
6. **major** (A, B, C). "Build with us" has no repo link. C has `[LINK: node repository]`, A and B have none. I also see no architecture sketch, no issue list, no contact other than the waitlist (hello@ is for funders), no chat, and nothing on how decisions get made. I'd drop an issue on the repo, but I'd have to guess where. Fix: repo, three to five concrete open problems with issue links, a contact (Matrix room or email), and one line on decision-making.
7. **major** (all). Licence. The node is GPL-3.0. The app is unlicensed, which legally means all rights reserved. I'd contribute to the node. I would not contribute to the app until the licence is settled. Say which part is open, and "AGPL for the app" if that is the plan. Note that GPL does not bind hosted forks, which matters for a network.

## 5. Keep list

- B: "We build it in the open, and this page says plainly what works today and what does not."
- C: "Nobody can post or vote as you / Being built / Today the node does not check who sends a request."
- B: "Until we settle the rule, we make no claim about stopping fake accounts."
- A/B/C: "There will be no binding vote before an independent security audit." (a commitment, not a feature)
- A: "A public node is not safe to run yet. Tell us you want to host one, and we will write to you when it is safe."

## 6. Specific answers

**"Blockchain".** I associate the word with crypto, but here it only appears as "Identity Block Chain" in the node's name. That is the right level. Use it once, as in A, and describe the mechanism in B's builder section. Don't use it as a selling word.

**Honesty.** It makes the project more credible, but only where it is precise. "In test", "Being built" and "Planned" are useful. Add a date and a link to the code behind each row.

**Carry the network.** Today it means "run a local dev node that connects to nothing public". Later is undefined. Say what "safe" depends on (auth, signed writes), and what a hosted node would do (be a partner on which contracts?).

## 7. Would I act?

**Maybe, Build with us.** Not today: no repo link, no contact, no open-problem list. I would star the repo and read `pbft.py`. One thing would change my answer to yes: a linked list of open problems with a Matrix or email contact.
