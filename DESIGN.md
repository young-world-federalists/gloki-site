---
name: Gloki
description: The line diagram of how you get into Gloki and how you hold it up, drawn on white in a Beck-style transit grammar.
colors:
  paper: "#ffffff"
  wash: "#eff6ff"
  wash-2: "#e0ecff"
  ink: "#111827"
  ink-soft: "#374151"
  ink-muted: "#4b5563"
  solve: "#3b82f6"
  solve-text: "#1d4ed8"
  build: "#0f766e"
  build-text: "#0f766e"
  contribute: "#d97706"
  contribute-text: "#b45309"
  status-good: "#047857"
  status-plan: "#b45309"
  status-later: "#4b5563"
  focus: "#b45309"
typography:
  display:
    fontFamily: "Hammersmith One, Gill Sans, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.9rem, 1.1rem + 3.4vw, 3.6rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.005em"
  headline:
    fontFamily: "Hammersmith One, Gill Sans, Trebuchet MS, sans-serif"
    fontSize: "clamp(1.5rem, 1rem + 2vw, 2.4rem)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.005em"
  title:
    fontFamily: "Hammersmith One, Gill Sans, Trebuchet MS, sans-serif"
    fontSize: "1.25rem"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.005em"
  lede:
    fontFamily: "Cabin, Gill Sans, Segoe UI, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  body:
    fontFamily: "Cabin, Gill Sans, Segoe UI, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  caption:
    fontFamily: "Cabin, Gill Sans, Segoe UI, sans-serif"
    fontSize: "0.9rem"
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: "normal"
  label:
    fontFamily: "Hammersmith One, Gill Sans, Trebuchet MS, sans-serif"
    fontSize: "0.8rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.06em"
rounded:
  plate: "2px"
  control: "8px"
  panel: "12px"
  interchange: "28px"
  pill: "999px"
spacing:
  field: "0.3rem"
  form: "0.6rem"
  gutter: "1rem"
  stack: "1.25rem"
  sub: "2rem"
  section-top: "3.5rem"
  section-bottom: "2.5rem"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "0 1.3rem"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.solve-text}"
    textColor: "{colors.paper}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.title}"
    rounded: "{rounded.pill}"
    padding: "0 1.3rem"
    height: "48px"
  button-ghost-hover:
    backgroundColor: "{colors.wash}"
    textColor: "{colors.ink}"
  plate:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    rounded: "{rounded.plate}"
    padding: "0.45em 0.7em 0.4em"
  plate-solve:
    backgroundColor: "{colors.solve-text}"
    textColor: "{colors.paper}"
  plate-build:
    backgroundColor: "{colors.build}"
    textColor: "{colors.paper}"
  plate-contribute:
    backgroundColor: "{colors.contribute-text}"
    textColor: "{colors.paper}"
  input-email:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.control}"
    padding: "0 0.9rem"
    height: "48px"
  interchange:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.interchange}"
    padding: "1rem 1.25rem 0.9rem"
  board-head:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper}"
    typography: "{typography.label}"
    padding: "0.8rem 1rem"
  nav-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    padding: "0.55rem 0.1rem"
    height: "44px"
---

# Design System: Gloki

## Overview

**Creative North Star: "The Line Map"**

Gloki's landing page is a transit diagram, not a brochure. The ground is white paper; everything on it is either a line, a station, or a nameplate. Three coloured lines are the three ways in (Solve, Build, Contribute); they run straight or at 45°, cross a pale blue zone band, and meet at one interchange, which is the reader, holding the only form on the page. The system borrows Beck's discipline (a fixed stroke, round caps, black-ringed white stations, uppercase plates) and nothing else of his: the roundel is the brand mark's cousin, never a TfL copy.

The tone is plain and literal. Headings are a single rounded humanist display face at one weight; body copy is a quiet humanist sans held to a 46-character measure; colour appears only where it means something (a line, its plate, a status). Density is low and the rhythm is editorial: more air above a heading than below it, one idea per station. Depth is almost absent; the one shadow on the page belongs to the interchange and nothing else.

Confirmed rejections, from the build and from PRODUCT.md: no hero-plus-three-cards, no device mockup, no stock photography, no hype words, and no brand blue behind or inside body-size text.

**Key Characteristics:**
- White paper, black ink, three line colours, one pale wash: the whole palette.
- A 10-unit round-capped stroke is the line; a 20px white disc with a 4px ink ring is the station.
- The nameplate (black bar, white uppercase display type, 2px corners) labels every control.
- Dashed stroke means a planned line; the dash is the honesty marker, not decoration.
- One authored moment: the lines draw themselves on load, then stations light as they enter view.

## Colors

Paper and ink carry the page; three line colours each come in a stroke value and, where needed, a darker text value, so that nothing readable falls below AA.

### Primary
- **Solve Blue** (`solve`): the brand blue and the main line. Used only as a stroke or a small fill: the 10-unit line, the 18×6 nav swatch, the 26×8 radio swatch, the vertical route bar. It is 3.68:1 on white, which is enough for a 6px-and-up stroke and never for text.
- **Solve Ink** (`solve-text`): the same line at reading strength (6.7:1 on white, 6.2:1 on the wash). Links, the coloured words in the h1, the Solve nameplate and plate-rect, and the primary button's hover fill.

### Secondary
- **Build Teal** (`build` / `build-text`): the second line. One value serves both stroke and text (5.5:1 on white, 5.0:1 on the wash); `build-text` is currently an alias of `build`.

### Tertiary
- **Contribute Amber** (`contribute`): the third line's stroke, always dashed (3.2:1 on white: a stroke, never text).
- **Contribute Ink** (`contribute-text`): its text and plate value (5.0:1 on white, 4.6:1 on the wash). Also the page's focus ring and the Planned status.

### Neutral
- **Paper** (`paper`): the page ground, the station centre, the interchange, the inputs.
- **Zone Wash** (`wash`): the zone-2 band in the diagram, alternate table rows, and the background of alternating sections (Three lines in, Who is building it).
- **Deep Wash** (`wash-2`): text selection only.
- **Ink** (`ink`): rules, ticks, station rings, nameplates, headings, the primary button, the 3px section rules.
- **Soft Ink** (`ink-soft`): body text (10.3:1).
- **Muted Ink** (`ink-muted`): captions, fine print, footer, placeholders, the "zone" labels in the diagram (7.6:1).
- **Status Good / Plan / Later** (`status-good`, `status-plan`, `status-later`): the three dot-and-word states of the status board (green dot, dashed amber ring, muted grey dot).

### Named Rules (optional, powerful)
**The Stroke-Not-Text Rule.** `solve` (#3b82f6) and `contribute` (#d97706) are strokes and swatches only. Any character set in a line's colour uses that line's `-text` value, and no body-size text is ever white on brand blue.

**The Two-Value Line Rule.** Every line colour exists as a pair: a stroke value for the diagram and a text value for words and plates. Adding a line means adding both and checking both against paper and wash.

**The One Wash Rule.** Tinted ground is one pale blue, used for zone bands and alternating sections; there is no second tint and no grey.

## Typography

**Display Font:** Hammersmith One (self-hosted woff2, OFL), with Gill Sans and Trebuchet MS as fallbacks.
**Body Font:** Cabin 400/500/600 (self-hosted woff2, OFL), with Gill Sans and Segoe UI as fallbacks.

**Character:** A Johnston-descended rounded sans for everything that is a label on the map (headings, nameplates, nav, buttons, field labels, table heads), and a warm humanist sans at reading size for everything the reader reads. Both are one family of feeling; the display face is never bolded and the body face is never used above 1.15rem.

### Hierarchy
- **Display** (400, `clamp(1.9rem, 1.1rem + 3.4vw, 3.6rem)`, 1.1): the single h1, balanced, 22ch max, with the key phrase set in Solve Ink. Fixed at 1.9rem under 760px.
- **Headline** (400, `clamp(1.5rem, 1rem + 2vw, 2.4rem)`, 1.1): section h2s. Fixed at 1.6rem under 760px.
- **Title** (400, 1.25rem, 1.1): station h3s, carrying a numbered ink tag. The three terminal h3s step up to 1.6rem and take their line's text colour.
- **Lede** (400, 1.15rem, 1.55): the one paragraph under the h1, 46ch, with the product name at 600. Drops to 0.98rem / 1.45 under 760px.
- **Body** (400, 1.0625rem, 1.55): all prose, held to a 46ch measure (`--measure`), pretty-wrapped. 500 is used for the first column of the status board and 600 for the "who" phrase that opens each terminal's paragraph.
- **Caption** (400, 0.9rem): figcaptions at 0.85rem, fine print and footer at 0.9–0.95rem, in Muted Ink.
- **Label** (400, 0.8rem, 0.06em, uppercase, display face): the nameplate and the table head. Nav links (0.95rem), field labels (0.95rem) and status words (0.95rem) are display face in sentence case.

### Named Rules (optional)
**The One Weight Rule.** Hammersmith One ships at 400 only; hierarchy comes from size and the plate, never from weight.

**The 46ch Rule.** Prose never runs wider than 46 characters; the diagram, not the paragraph, is what spans the viewport.

## Layout

One centred column, `min(100%, 74rem)` wide with a 1rem gutter on each side, holds everything; section backgrounds alternate paper and wash across the full width. Sections take 3.5rem above and 2.5rem below; an h2 has 0.75rem beneath it and a sub-lede 2rem beneath that. The route list indents 3.4rem for its 10px line and 20px stations with 2.2rem between stops. Forms stack on a 0.6rem gap with 0.3rem between a label and its field.

The hero is a three-row grid: h1, lede, then a stage with a 1200/600 aspect ratio holding the desktop SVG. The interchange sits in the same grid cell as the stage, placed by pure CSS at `margin-left: 50%`, `margin-top: 4.5%`, `width: 31.5%` (max 30rem), so the form lands at the convergence point with scripting off. From 760px the "who" grid is two equal columns and the proof stations run text beside a 220px screenshot.

Under 760px the diagram swaps for a vertical 360/160 SVG whose three lines enter from the top and feed the interchange directly below it; a row of three small plates names the lines above the SVG; the nav collapses to short labels and a full-width row; the status board hides its Notes column; the interchange corner drops to 22px. Under 420px the nav shrinks to 0.82rem with 12px swatches. There is no horizontal scroll at 360px.

## Elevation & Depth

The system is flat. Hierarchy is drawn with ink rules (3px section rules, 2px table rules, 5px interchange border, 4px station rings, 2px input borders), not with shadow, and tinted ground is the single pale wash. One exception exists and is deliberate: the interchange carries a soft downward shadow so that it reads as sitting on top of the diagram it interrupts.

### Shadow Vocabulary (if applicable)
- **Interchange lift** (`box-shadow: 0 10px 24px -14px rgba(17, 24, 39, 0.45)`): the interchange only.

### Named Rules (optional)
**The Ink-Rule Rule.** Separation is a black rule, never a shadow or a grey line. The interchange is the one surface allowed to float, because it is the one surface that lies over the map.

## Shapes

Round-capped strokes and hard-edged plates. Lines are 10-unit strokes with round caps and joins, running straight or at exactly 45°; the planned line is the same stroke dashed in path-length units (`--dash`: 0.03 0.022 on the desktop paths, 0.12 0.09 on the mobile paths, about a 36/26px dash on both), so it dashes whether or not the draw-on runs. Stations are 20px white discs with a 4px ink ring that fills with ink when lit. Nameplates have barely-rounded 2px corners (3px rx inside the SVG). Controls are 8px (inputs, the brand mark); panels are 12px (status board, screenshot frames); the interchange is a 28px pill-box with a 5px ink border (22px under 760px); buttons are fully round pills. Swatches that stand for a line (nav, radios, route bars) are short rounded bars at half their height, and the Contribute swatch is always a repeating dash.

## Components

### Buttons
Decisive and ink-black; a button is a nameplate the reader can press.
- **Shape:** full pill (999px), 48px tall, `0 1.3rem` side padding, display face at 1.05rem with 0.02em tracking.
- **Primary:** ink background, paper text. Used for "Join the waitlist".
- **Hover / Focus:** background shifts to Solve Ink with a 1px lift, 160ms ease-out; active returns to rest. Focus is the global 3px Contribute-Ink outline at 3px offset.
- **Ghost:** transparent with a 2px ink border and ink text; hover fills with the wash. Used for the three "Join this line" links.

### Chips
The nameplate, the diagram's label grammar, used for every control label on the page.
- **Style:** ink bar, paper uppercase display text at 0.8rem with 0.06em tracking, 2px corners, `0.45em 0.7em 0.4em` padding.
- **State:** three line variants swap the bar for the line's text colour (`plate--solve`, `plate--build`, `plate--contribute`). The same plate appears as the "Line map · beta" title plate beside the mark, the "YOU · INTERCHANGE" heading, the station number tags, and the line tags after terminal headings ("first invitees", "planned line").

### Cards / Containers
- **Interchange** (the form's container): 28px pill-box, paper background, 5px ink border, `1rem 1.25rem 0.9rem` padding, the one shadow. On desktop it overlays the convergence point of the diagram.
- **Status board:** 3px ink border, 12px corners, clipped; a table with ink header (nameplate typography), 2px ink row rules, wash on even rows, tabular numerals.
- **Screenshot frames:** 3px ink border, 12px corners, 220px wide (200px under 760px), Muted Ink caption beneath.
- **Terminals** (the three lines): a 3px ink rule above each (none on the first), a 56px column holding a 10px vertical bar in the line's colour with a station at its head, and the title in the line's text colour.

### Inputs / Fields
- **Style:** 48px tall, 2px ink border, 8px corners, paper background, ink text at 1.05rem, Muted Ink placeholder, display-face label above on a 0.3rem gap.
- **Radios:** native 20px radios with ink accent colour, each in a 44px-tall row with a 26×8 line swatch before the label; the Contribute option carries "(planned)" in Muted Ink.
- **Focus:** the global ring, 3px solid Contribute Ink at 3px offset, 2px radius.

### Navigation
- **Style:** display face at 0.95rem, ink text, 44px tall targets, each link preceded by an 18×6 bar in its line's colour (dashed for Contribute, ink for Join). Hover underlines at 0.3em offset. Under 760px the long names give way to one-word short names and the nav spans the header's full width; the header is closed by a 3px ink rule.
- **Brand:** the mark at 36px with 8px corners, "Gloki" in display face at 1.35rem, and the title plate (hidden under 760px).

### The Line Diagram
The signature. Two inline SVGs (1200×600 desktop, 360×160 mobile), aria-hidden, drawn entirely from the tokens: paper ground, a wash zone band, three `.line` paths (`stroke-width: var(--line-w)`, round caps), `.station` discs, `.plate-rect` nameplates with `.terminal` text (18px uppercase display, paper), `.label` text (15px display, ink) and `.small` text (13.5px body face, Muted Ink). Each path carries `pathLength="1"`; on load the lines draw in over 1.3s on `cubic-bezier(0.16, 1, 0.3, 1)` with 0.15s, 0.3s and 0.9s stagger (the trunk last), the dashed line animating to its `--dash` pattern, and the labels and stations fade in at 1.1s over 0.6s. Under `prefers-reduced-motion`, everything is drawn and still. The route list on the Stations section repeats the grammar in CSS: a 10px Solve bar and 20px stations whose rings fill with ink (300ms) as each stop enters view.

### Status
- **Style:** display face at 0.95rem, a 10px dot before the word in `currentColor`. In test is Status Good; Planned is Status Plan with a 7px dashed ring instead of a dot; Later is Status Later.

## Do's and Don'ts

### Do:
- **Do** draw with the line grammar: 10-unit round-capped strokes, straight or at 45°, 20px stations with a 4px ink ring, and a nameplate for every label.
- **Do** use the dashed stroke (`--dash` on a `pathLength="1"` path, or the repeating-gradient swatch) for anything planned and not yet real; the dash is how the page tells the truth.
- **Do** set every line's words in its `-text` value and check it against both paper and wash (AA, 4.5:1 or better).
- **Do** hold prose to 46ch in Cabin 400 at 1.0625rem / 1.55, and keep all headings in Hammersmith One at 400.
- **Do** separate with ink rules (3px between sections, 2px inside tables) and alternate paper and wash for section ground.
- **Do** keep every target 44px or taller, the focus ring 3px Contribute Ink at 3px offset, and the h1 singular.

### Don't:
- **Don't** set text in `solve` (#3b82f6) or `contribute` (#d97706), and don't put white text on brand blue at body size; use `solve-text` and `contribute-text`.
- **Don't** add a shadow to anything but the interchange; depth here is an ink rule.
- **Don't** introduce a second tint, a grey rule, a gradient fill, or a bold weight of the display face.
- **Don't** replace the diagram with cards, a device mockup, or photography; the map is the hero and the form sits inside it.
- **Don't** copy TfL: no bar-and-circle roundel, no Johnston; the station ring and the plate are the whole borrowing.
