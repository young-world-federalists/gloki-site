---
version: 2
slug: "index-html"
primary_target: "index.html"
related_targets: ["build.html", "imprint.html", "privacy.html"]
---

## Scope

GDI home page (`index.html`) plus the builder page (`build.html`), mode Persuade. Reader: a world
citizen or YWF chapter member from a WhatsApp link on a phone; a builder, researcher or funder on a
laptop. Job: understand that GDI is building a network where each real person counts once, see
honestly what works, and sign up for one of three ways to take part. Action: email plus choice of
way to take part, sent to the GDI Brevo list. Proof: the four-link vouching mechanism shown, and the status
board. Copy: `docs/copy/draft-d-merged.md` (locked). Constraints: PRODUCT.md claims rules and
`docs/positioning-gdi.md`; English only; under 200 KB; no third-party request except the waitlist's Brevo form script and Cloudflare Turnstile; AA contrast with no
brand-blue exception; 360px first; one h1.

## Direction contract

THESIS: The page counts people the way Isotype did: one figure is one real person, and the
four-link rule is shown, not explained. It refuses the glowing node network and gradients of the
crypto page, and the cream, serif, stock-photo NGO brochure.

OWN-WORLD: White ground; ink-black pictogram people authored as SVG in one Arntz-like system (round
head, tapered body, no faces); brand blue #3b82f6 fills people who have been vouched in; vermilion
marks "not yet". Flat colour only, no outlines on solid figures, no shadows, no gradients. Headings
in Jost (geometric, Futura lineage), body in Atkinson Hyperlegible. Rules are thin ink lines;
sections sit on an even rhythm like a chart sheet.

STORY: In one look: real people, each counted once, getting in when four people vouch. Then: why
global democracy needs this; what works today, as a figure legend; who we are; the pilot; three
ways to take part.

FIRST VIEWPORT: Phone: the GDI mark and name; the h1 in Jost; a block of pictogram figures where a
newcomer arrives in its gap, four short links draw to it from the people around it, and the five
turn blue (29 Oct: the old links between pairs are no longer shown, since the page no longer
describes the random-pairs rule);
the caption "You get in when four people vouch for you."; then the email field, the three ways to
take part and the Sign up button, all inside the first screen. Desktop: copy and form on the left,
the figure block large on the right.

FORM: Direction A "One figure, one person" (Isotype), position 1 of 7 on our ordered list, chosen by
Eston. seed: none (roll blocked by the harness, not run; Eston told 26 Oct; his acceptance is not recorded)

SIGNATURE: Once, on load, the newcomer slides into its gap and the four links draw, then the four
turn blue (about 1.4s, ease-out). Reduced motion shows the end state. The status board reuses the
figure as its legend: solid = in test or available, half-filled = being built or early code,
outline = planned or possible, dotted outline = research.

FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Unresolved

- Done 28 Oct: the waitlist is its own GDI Brevo list (PR #3); Brevo's confirmation email and
  `/confirmed` carry the after-sign-up messages.
- The hero caption "You get in when four people who know you vouch for you." reads as present
  fact while vouching is in test; Eston to decide (29 Oct).
- Phone first screen (29 Oct): the email field and the three choices fit at 360×740 and 390×844, but
  the Turnstile check (148px compact) pushes the button about 180px below the fold. Reordering the
  button above the check would break focus order and is the waitlist session's call; left as is.
- Ouri's problem list, status-board sign-off and the app licence; paper links checked in a browser.
