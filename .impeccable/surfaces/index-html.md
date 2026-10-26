---
version: 1
slug: "index-html"
primary_target: "index.html"
related_targets: []
---

## Scope

gloki.app landing page, one route (`index.html`), mode Persuade. Reader: an academic or world federalist, a civic-tech person, or someone with a server, arriving from an email or a WhatsApp link, on a phone as often as a laptop. Job: understand what Gloki is, find their door, join the waitlist. Action: email + door → Buttondown (username placeholder until Eston supplies it). Proof: the real mechanism drawn as the journey; two real app screenshots. Constraints: PRODUCT.md claims rules (no "decentralized"/"secure"; contribute door launches dark), English only, under 200 KB, no third-party request, AA contrast with no brand-blue exception, 360px first.

## Direction contract

THESIS: The page is a line diagram of how you get into Gloki and how you hold it up: three lines (the doors) converge at one interchange, You, and the journey's stations are the real steps. It refuses the category's hero-plus-three-cards and the device mockup.

OWN-WORLD: Beck-style transit diagram. White ground; a 45°-and-straight line grammar; brand blue #3b82f6 as the main line, two further line colours for the other doors (a deep teal and a warm amber, both AA on white for their labels); black station ticks and interchange roundels with white centres; zone bands as pale blue washes. Display type Hammersmith One (Johnston-descended), text Cabin. Station nameplates (black bar, white uppercase) label every control; the roundel is the brand mark's cousin, never a TfL copy.

STORY: In one look: you get in because people who know you vouch for you; nothing to pay or upload. Then: which line is mine (solve, build, contribute); what the stations are (create a key, save it, four people vouch, verified, the forum); what is in test and what is next; join.

FIRST VIEWPORT: Desktop: the diagram fills the viewport left to right, three lines entering from the left edge, converging at a large interchange roundel right of centre labelled YOU; the nameplate above reads the one-line hook; the roundel holds the email field and the Join button. Mobile: the same diagram vertical, lines entering from the top, roundel-form in the lower half within the first screen. The mark sits top-left as the "line map" title plate; nav is the three line names.

FORM: The line diagram, position 1 of my ordered list of seven (chosen by Eston as the pick over the assigned #5). seed:9407b0d190575a4d

SIGNATURE: On load the lines draw themselves once (stroke-dashoffset, ~1.2s ease-out); on scroll each section's station lights (fill) when it enters view. Reduced motion: lines drawn, no animation.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Adaptations (cited at the finish review)

- The interchange is a pill-box (28px radius, 5px ink border), not a circle: the Persuade rule wants the action in its working form, and a circle cannot hold a labelled field, a button and a three-way radio legibly. A roundel survives as the YOU plate at its head.
- The hook is the page's one h1 in display type on white, not a reversed nameplate: one h1 and AA contrast; a 3.6rem reversed plate would be a poster.
- Nav is the three line names plus Join (fix 8 applied). Lines enter from beyond the left edge of the viewport; diagonals are 45°; the trunk leaves the box edge.

## Adaptations, 26 Oct 2026 (GDI as publisher)

- The header's title plate is the Global Democracy Initiative (network mark + name, "GDI" under 1100px); Gloki moves to a kicker above the h1 with its own mark and the Line map plate. The hook, diagram and form are untouched.
- "Who is building it" becomes the GDI section: the 2021 plan, "Gloki is that plan, being built", three values, and the YWF hosting line. Footer and two new pages (imprint.html, privacy.html) name Young World Federalists, Inc. as publisher.

## Unresolved

Whether waitlist sign-ups also get the YWF newsletter; who reads hello@; DNS cutover once the domain transfer completes; the status-board wording for "your own agent holding your data" (shown as Planned until Eston confirms what the beta's agent does).
