---
name: Global Democracy Initiative
description: One figure, one person. An Isotype page that counts real people on white, with ink pictograms and a single blue for people who have been vouched in.
colors:
  paper: "#ffffff"
  field: "#f1f5fb"
  ink: "#111418"
  ink-soft: "#3b424b"
  ink-hover: "#2a3038"
  rule: "#d5dae1"
  brand-blue: "#3b82f6"
  blue-text: "#1d4ed8"
  vermilion: "#e0412b"
  vermilion-text: "#b42318"
  vermilion-wash: "#fff5f3"
  counterfeit-grey: "#7c848e"
typography:
  display:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "clamp(2rem, 1.25rem + 3.4vw, 3.75rem)"
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.012em"
  display-doc:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.9rem, 1.3rem + 2.4vw, 2.9rem)"
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.012em"
  headline:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.55rem, 1.15rem + 1.7vw, 2.35rem)"
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.008em"
  title:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "1.2rem"
    fontWeight: 500
    lineHeight: 1.25
  caption:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 500
    lineHeight: 1.3
  label:
    fontFamily: "Jost, Futura, Century Gothic, Trebuchet MS, sans-serif"
    fontSize: "1.05rem"
    fontWeight: 600
    lineHeight: 1
  lead:
    fontFamily: "Atkinson Hyperlegible, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.6
  body:
    fontFamily: "Atkinson Hyperlegible, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.6
  body-strong:
    fontFamily: "Atkinson Hyperlegible, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 700
    lineHeight: 1.6
  small:
    fontFamily: "Atkinson Hyperlegible, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.95rem"
    fontWeight: 400
    lineHeight: 1.6
rounded:
  focus: "2px"
  md: "6px"
  pill: "999px"
spacing:
  gutter: "1rem"
  gutter-wide: "1.5rem"
  stack: "1rem"
  section: "clamp(3rem, 2rem + 4vw, 5rem)"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "0 1.4rem"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.ink-hover}"
    textColor: "{colors.paper}"
  nav-link:
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "0 0.7rem"
    height: "44px"
  nav-link-hover:
    backgroundColor: "{colors.field}"
  nav-join:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    rounded: "{rounded.md}"
    padding: "0 0.7rem"
    height: "44px"
  input-email:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: "0.6rem 0.8rem"
    height: "48px"
  way-chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: "0.35rem 0.8rem 0.35rem 0.6rem"
    height: "44px"
  way-chip-selected:
    backgroundColor: "{colors.field}"
    textColor: "{colors.ink}"
  status-board:
    backgroundColor: "{colors.field}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  rule-box:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "1.25rem 1.25rem 1rem"
  warn-note:
    backgroundColor: "{colors.vermilion-wash}"
    textColor: "{colors.ink}"
    padding: "1rem 1.1rem"
  link:
    textColor: "{colors.blue-text}"
  not-yet:
    textColor: "{colors.vermilion-text}"
    typography: "{typography.body-strong}"
---

# Design System: Global Democracy Initiative

## Overview

**Creative North Star: "One Figure, One Person"**

The page counts people the way Isotype did. One pictogram is one real person, and the rule that lets a newcomer in (four people vouch) is drawn rather than explained. Everything else is a chart sheet around those figures: a white ground, ink type, thin ink rules between sections on an even rhythm, and one tinted field for the status board. The system is flat by conviction. Colour is spent only where it carries meaning: blue fills people who are in, vermilion marks what is not yet true.

Density is low and reading-first. The reader may be on a cheap phone, reading English as a second language, so body text is large (17px), set in a typeface designed for legibility, and held to a short measure. Headings are geometric and confident in the Futura lineage; they speak, the body reads. The world refuses two neighbours by name: the glowing node network and gradients of a crypto page, and the cream, serif, stock-photo NGO brochure.

The person pictogram is the system's one signature. It is the hero, the status-board legend, the radio marker in the sign-up form, and the avatar in the team list. Its fill state is a grammar, not decoration.

**Key Characteristics:**
- White ground, ink pictograms, flat colour only; no shadows, no gradients.
- One person pictogram (round head, tapered body, no face) reused everywhere.
- Brand blue fills figures and graphics; a darker blue carries every blue word.
- Vermilion means "not yet", in the same two-tone split.
- Jost for headings and controls, Atkinson Hyperlegible for all reading.
- Thin ink rules separate sections like a chart sheet.

## Colors

A near-monochrome ink-on-white sheet with one meaningful blue and one warning vermilion, each split into a graphics tone and a darker text tone.

### Primary
- **Vouched Blue** (brand-blue): fills the figures of people who have been vouched in, the new links that join a newcomer to its four vouchers, the team avatars, and the figure inside a selected sign-up choice. It is a graphics colour only (3.68:1 on white); it never sets text, and white text never sits on it. This blue is fixed by the brand.
- **Word Blue** (blue-text): every blue word: links, the focus ring, text selection (white text on Word Blue), `accent-color` and the caret (6.7:1 on white, 6.1:1 on the field).

### Secondary
- **Not-Yet Vermilion** (vermilion): the graphics tone for "not yet": the 1px rule on the left of a warning note, and the start colour of the newcomer before it turns blue.
- **Not-Yet Words** (vermilion-text): the "Not yet:" lead-in on status items and the bold opener of a warning note (6.6:1 on white).
- **Warning Wash** (vermilion-wash): the faint ground behind a warning note; used only there.

### Neutral
- **Paper** (paper): the page ground, and the ground of controls and the rule box.
- **Chart Field** (field): the cool tint behind the status board, the hover ground of nav links, and the ground of a selected sign-up choice.
- **Ink** (ink): headings, body text, solid figures, section rules, control borders, the primary button and the nav "Sign up" button.
- **Soft Ink** (ink-soft): secondary text: the hero promise, "last updated" lines, the legend, fine print, figure captions on the builder page, the footer (10.2:1 on white).
- **Pressed Ink** (ink-hover): hover ground of ink buttons.
- **Hairline** (rule): light separators between list items inside a section and the border of an unselected sign-up choice. Never a section divider.
- **Counterfeit Grey** (counterfeit-grey): solid figure copies that stand for fake accounts in the story count. Nowhere else.

The mark (`assets/gdi-mark.svg`, Eston's decision 26 Oct 2026, route B in `docs/brand/2026-10-26/`) is the 2022 GDI network figure redrawn in the page's two colours: seven ink nodes and links in their 2022 positions, plus one brand-blue newcomer where two of the 2022 links cross, so it sits between two linked pairs with four links, the page's vouching rule. The header and the favicon use their own masters (`assets/gdi-icon-32.svg`, `assets/gdi-icon-16.svg`); at 16px the icon is only the newcomer and its four. The mark uses no colour outside the page palette.

### Named Rules
**The Two-Tone Rule.** Every hue has a graphics tone and a words tone. Brand blue (#3b82f6) and vermilion (#e0412b) fill shapes and lines; text in those hues uses #1d4ed8 and #b42318. No text sits in brand blue, and no text sits on it.

**The Blue Means In Rule.** A blue figure is a person who is in, or you choosing to be. Never use blue to decorate, to tint a section, or to colour a heading.

**The Counterfeit Grey Rule.** Grey (#7c848e) solid figures exist only to show fake accounts in a count. No legend state uses grey; a grey figure must never be read as a status.

## Typography

**Display Font:** Jost (with Futura, Century Gothic, Trebuchet MS), self-hosted at 500 and 600.
**Body Font:** Atkinson Hyperlegible (with Segoe UI, Helvetica Neue, Arial), self-hosted at 400 and 700.

**Character:** A geometric Futura-lineage voice for what the page says aloud, paired with a typeface built for low-vision legibility for everything the reader has to read. The pairing is the Isotype pairing restated for a phone.

### Hierarchy
- **Display** (Jost 600, fluid 2rem to 3.75rem, 1.06): the single h1 of the home page. Balanced wrapping, slight negative tracking.
- **Display (doc pages)** (Jost 600, fluid 1.9rem to 2.9rem, 1.06): the h1 of the builder, imprint and privacy pages.
- **Headline** (Jost 600, fluid 1.55rem to 2.35rem, 1.12): section h2s. The history disclosure summary uses Jost 600 at a smaller fluid size (1.3rem to 1.7rem).
- **Title** (Jost 500, 1.2rem, 1.25): h3s in team bios, ways to take part and the rule box; status-board group titles sit at 1.15rem with their figure glyph.
- **Caption** (Jost 500, 1.05rem, 1.3; 1.3rem from 56rem): the hero figure caption. The figure speaks in the display voice.
- **Label** (Jost 600, 1.05rem, 1): buttons. Nav links use Jost 500 at body size.
- **Lead** (Atkinson 400, 1.125rem, 1.6): the hero promise and section lead paragraphs.
- **Body** (Atkinson 400, 1.0625rem, 1.6): all reading text, held to a 38rem measure.
- **Body strong** (Atkinson 700): bold lead-ins that name a status item, a fact or a person's org; form labels and the fieldset legend.
- **Small** (Atkinson 400, 0.95rem, 1.6): legend, fine print, "how" lines in the builder plan, diagram captions, footer.

### Named Rules
**The Speak and Read Rule.** Jost is for headings, nav, buttons, the figure caption and the disclosure summary. Anything a reader must read in sentences is Atkinson Hyperlegible. Never set a paragraph in Jost.

**The No-Caps Rule.** No uppercase labels, no letter-spaced kickers, no eyebrows above headings. A heading starts the section by itself.

## Layout

A single centred column with a 72rem maximum and a 1rem side gutter that widens to 1.5rem from 40rem. Prose (paragraphs and lists) is held to a 38rem measure; the rule box, the history disclosure and the builder plan widen to 44 to 46rem. Sections stack on an even vertical rhythm (the fluid `section` padding, 3rem to 5rem), each opened by a 1px ink rule, so the page reads like ruled chart sheets.

Built 360px first. On a phone the hero order is: h1, the figure block, the sign-up form, then the promise, so the email field and Sign up fit the first screen. From 56rem the hero becomes two columns (about 1.05 : 1, 3.5rem apart): h1, promise and form on the left, the figure block centred on the right. Paired text sections, the status-board groups and the team list go two-up at 56rem and 40rem respectively; the three ways to take part go three-up at 56rem. Nav labels shorten below 30rem ("GDI", "Builders"), and the "What works today" nav link appears only from 44rem.

Every standalone interactive target is at least 44px tall (buttons and the email field 48px). Inline prose links fall under the WCAG 2.5.8 inline exception and keep their text height.

## Elevation & Depth

The system is flat. There are no shadows anywhere, at rest or on hover. Depth is conveyed only by ground tone (the Chart Field behind the status board against Paper), by rules (1px ink between sections, 1px hairline inside lists), and by 2px ink borders that enclose something the reader must act on or keep (the email field, the rule box).

### Named Rules
**The Flat Sheet Rule.** No box-shadow, no gradient, no glow, no blur. If something needs to stand out, give it an ink border or the field tint.

## Shapes

Corners are gently rounded at one radius (6px) for buttons, nav links, the email field and the rule box; sign-up choices are full pills. The focus ring rounds at 2px. Rules are straight hairlines: 1px ink for section tops and the footer, 1px hairline grey between list items, 2px ink as the top edge of each "way to take part" and as the border of the rule box and email field.

The recurring silhouette is the person pictogram: a 20 by 40 unit figure with a round head (radius 4.6), a tapered body, arms held slightly out, two legs, no face. It is defined once as an SVG symbol and reused at every size. Its fill state is the status grammar:

- **Solid ink:** works now.
- **Half-filled** (outline, filled below the waist): being built, or early code.
- **Outline** (2px ink stroke, no fill): planned or possible.
- **Dotted outline** (1.8px dashed ink stroke): research.

In the hero, figures stand in rows of thirteen on a 24-unit pitch and 56-unit row step; links between figures are lines (new links 2px brand blue with round caps; old links 1.4px ink, gone in the end state).

### Named Rules
**The One Glyph Rule.** The person pictogram is the only illustration and the only icon. Legend, radio marker, team avatar and diagram all reuse the same symbol; the only other drawn marks are the GDI mark and the plus/minus of the history disclosure. No icon library, no second figure drawing, no faces.

**The Four States Rule.** Status is shown by how a figure is filled, never by a new colour. Solid, half, outline, dotted: four states, in that order, always with a word beside them.

## Components

### Buttons
Plain, dark and certain: an ink slab with white type.
- **Shape:** gently rounded (6px).
- **Primary:** Ink ground, white Jost 600 label at 1.05rem, 48px tall, 1.4rem side padding. Used for Sign up in the form; the nav "Sign up" is the same treatment at 44px.
- **Hover / Focus:** ground darkens to Pressed Ink; focus shows the shared 3px Word Blue outline at a 3px offset.
- No secondary button. A second action is a bold text link ("How it works and what is open") with a 44px target.

### Chips (sign-up choices)
- **Style:** full pill, Paper ground, 1px Hairline border, a small outline figure as the radio marker, body text label, 44px tall. The native radio sits invisibly over the whole chip.
- **State:** selected turns the border Ink, the ground Chart Field, and fills the figure Vouched Blue. Keyboard focus draws the 3px Word Blue outline around the chip.

### Cards / Containers
- **Rule box** (the one promise the project keeps): Paper ground, 2px Ink border, 6px radius, 1.25rem padding, 44rem max, sitting on the status board's field.
- **Warning note:** Warning Wash ground, a 1px vermilion rule on the left, 1rem by 1.1rem padding, bold Not-Yet Words opener, 38rem measure.
- **Status board:** a full-width section on Chart Field; a figure legend, then groups each titled by a figure glyph and a Jost title, items separated by hairlines.
- No shadows on any container (see Elevation & Depth).

### Inputs / Fields
- **Style:** Paper ground, 2px Ink border, 6px radius, 48px tall, body type; label above in Atkinson 700. Placeholder is a mid grey (#5b636d, 6.1:1).
- **Focus:** the shared 3px Word Blue outline at a 3px offset.

### Navigation
- **Style:** a 60px header row under a 1px Hairline: the GDI mark at 32px plus the name in Jost 600 on the left; Jost 500 nav links on the right, 44px tall, rounded 6px.
- **States:** hover tints the link with Chart Field; the last item is the ink "Sign up" button.
- **Mobile:** below 30rem the name becomes "GDI" and "For builders" becomes "Builders"; the in-page "What works today" link appears from 44rem.

### Links
- Word Blue, 1px underline at a 0.18em offset; hover thickens the underline to 2px. Footer links use Soft Ink. Standalone links carry 44px targets; inline links in prose take the WCAG 2.5.8 inline exception.

### The Vouching Figure Block (signature)
The hero: three rows of ink figures with a gap in the middle row. On load, once, the newcomer drops into the gap (0.7s), the two old links between neighbouring pairs fade, four short blue links draw from the newcomer to the four vouchers, and the vouchers and newcomer turn Vouched Blue, about 1.4s in all on an expressive ease-out. With reduced motion the end state shows at once. Caption in the Caption style: "You get in when four people vouch for you." The builder page repeats the rule as a static before/after diagram in the same figures.

### Story Count
A row of figures at a smaller size: one ink figure, then twelve Counterfeit Grey copies, showing one person making many accounts.

## Do's and Don'ts

### Do:
- **Do** draw every person with the one pictogram symbol, and let its fill carry status: solid works now, half-filled being built, outline planned, dotted research.
- **Do** keep brand blue (#3b82f6) for figures, links between figures and the selected-choice figure; use #1d4ed8 for every blue word, the focus ring and selection.
- **Do** mark what is not true yet with bold #b42318 "Not yet:" text, and keep vermilion #e0412b for graphics.
- **Do** open each section with a 1px ink rule and the fluid section padding, so the page keeps its chart-sheet rhythm.
- **Do** set headings, nav, buttons and the figure caption in Jost; set every sentence in Atkinson Hyperlegible at 17px or larger, on a 38rem measure.
- **Do** keep every standalone target at 44px or more, buttons and fields at 48px, and show the 3px Word Blue focus ring on everything focusable.
- **Do** show the end state of any motion under `prefers-reduced-motion`.

### Don't:
- **Don't** set text in brand blue or put white text on brand blue; that pairing is the app's exception, not the page's.
- **Don't** add shadows, gradients, glows, or a glowing node-network illustration; the world refuses the crypto page.
- **Don't** use cream grounds, serif display type or stock photography; the world refuses the NGO brochure.
- **Don't** give figures faces, outlines on solid fills, or a second drawing style; there is one pictogram.
- **Don't** use grey figures for anything but fake accounts in a count.
- **Don't** use hairline grey as a section divider; section rules are ink.
- **Don't** thicken the warning note's vermilion side rule beyond 1px or turn it into a coloured stripe on other containers.
- **Don't** treat the yellow `mark.todo` placeholders as part of the system; they are a temporary editorial device and must be removed before launch.
- **Don't** add uppercase kickers, eyebrows or letter-spaced labels above headings.
