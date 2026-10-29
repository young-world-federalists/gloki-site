# GDI mark and home page: three routes (26 Oct 2026)

For Eston. Nothing on the live site has changed; everything is in this folder.

**What the 2022 mark is.** `assets/gdi-mark.svg` has **seven** nodes and seven links, not eight. Their link counts are 1, 2, 2, 2, 2, 2 and 3: a ring of five with a two-link tail, and no node has four links. Two of its links cross (top-left to bottom-centre, and centre to left). The page's rule is that a newcomer takes a place between two linked pairs, so both links move to the newcomer and it has four. A node placed at that crossing follows the rule exactly, and the lines stay where they are. Routes B and C use this.

Contrast is WCAG 2 relative luminance, computed in code (`src/geom.py`, and again in the sheets). "Field" is the status-board background `#f1f5fb`. Text needs 4.5:1; graphics need 3:1.

## Route A: the page takes the mark's colours

**What changes.** The page palette moves toward the mark. Mark orange becomes "not yet", mark navy becomes the link colour, the mark's line colour becomes the ink, and a darker green from the mark marks "works now" on the status board. The mark itself is not touched. New 16px and 32px masters draw the same graph with heavier lines.

| Role | Now | Route A | On white | On field |
|---|---|---|---|---|
| Ink: text, buttons | `#111418` | `#22231A` (mark lines) | 15.87 | 14.50 |
| Ink soft | `#3b424b` | `#45463C` | 9.57 | 8.75 |
| Links, focus ring (text) | `#1d4ed8` | `#165A99` (mark navy) | 7.10 | 6.49 |
| Vouched-in figures (graphic) | `#3b82f6` | unchanged | 3.68 | 3.36 |
| "Not yet" figures, rule (graphic) | `#e0412b` | `#EC623E` (mark orange) | 3.29 | 3.01 |
| "Not yet" words (text) | `#b42318` | `#B93A13` (same hue as mark orange) | 5.71 | 5.22 |
| "Works now" figure and label | ink | `#2A7F35` (darkened mark green) | 5.02 | 4.59 |
| Mark green as drawn | – | `#7BD484`, mark only | 1.81 | 1.66 |

Mark green cannot carry meaning on white at 1.81:1, so it stays inside the mark. Mark orange passes as a graphic on the field only just (3.01), and fails as text (3.29).

**Stays fixed:** the mark file, brand blue, the fonts and the Isotype figures.

**Risk:** once orange means "not yet" on the page, the mark's three orange nodes read as three people not yet in. The first screen barely changes (see the sheet), and the mark still looks like the coloured node network the page's direction refuses. At 16px it is still a cluster of coloured dots, and the green dots nearly disappear.

## Route B: the mark joins the Isotype (recommended)

**What changes.** All seven nodes and all seven 2022 links stay in place, so the silhouette is kept. The mark is redrawn in the page's ink, with heavier lines (stroke 28 on node radius 84, against 17.7 on 100 before). One brand-blue node, the newcomer, sits where the two links cross. It has four links, and the mark now shows the rule the page shows. The 16px master is only the newcomer and the four members it sits between, an X with a blue centre, because nothing smaller survives at 16px. The lockup sets the name in Jost 600.

| Role | Hex | On white | On field |
|---|---|---|---|
| Ink: text and the mark | `#111418` | 18.47 | 16.88 |
| Ink soft | `#3b424b` | 10.16 | 9.29 |
| Links (text) | `#1d4ed8` | 6.70 | 6.13 |
| Vouched-in figures, newcomer in the mark (graphic) | `#3b82f6` | 3.68 | 3.36 |
| "Not yet" figures (graphic) | `#e0412b` | 4.23 | 3.87 |
| "Not yet" words (text) | `#b42318` | 6.57 | 6.01 |

**Stays fixed:** brand blue, the whole page palette, the 2022 node positions and links. **Decision for Eston:** this drops the mark's orange, green and navy and adds one node. That changes a commitment you set, so it needs your yes.

**Risk:** it is still dots and lines, which some readers will take as a network diagram. The 16px icon is a crop, not the whole mark. In the one-colour version the newcomer looks like the other nodes, though its four links still meet there. The newcomer sits close to two neighbours (a gap of 73 units in a drawing about 1,120 units wide).

## Route C: one person added to the 2022 mark (lighter B)

**What changes.** The 2022 drawing and its colours stay exactly as they are. One node in brand blue is added at the crossing. The page does not change. The 16px master is the newcomer and its four, in the 2022 colours.

Palette: the page values are the same as in Route B. Colours used only in the mark have no contrast minimum, because logos are exempt: orange 3.29, navy 7.10, green 1.81, lines 15.87, newcomer blue 3.68.

**Stays fixed:** the 2022 drawing and colours, brand blue and the page. **Decision for Eston:** the mark gains one node.

**Risk:** the mark now has four colours, which is busier than either A or B, and the mismatch between the mark and the page stays. Green still fades. The newcomer nearly touches two nodes (a gap of 57 units).

## Social share image

`share/og-b.png` is 1200×630, built with the page's real headline and hero figure (read from `index.html`) and the domain. `og-a` and `og-c` differ only in the mark and ink. WhatsApp needs the PNG, given as an absolute URL. The file is 75 KB, and the page never loads it, so the 200 KB budget does not change. Not tested on a device: when WhatsApp shows a small preview, it may crop the image to a square from the centre.

## Recommendation

**Route B.** It keeps the 2022 silhouette, uses only the page's two colours, and makes the mark say what the page says: one new person, four links. It is also the only route whose 16px icon reads as something, the X with a blue centre. If the mark has to stay exactly as it is, take Route A, but only the new 16px and 32px masters and the share image. In my view, the palette swap costs more than it gains.

If you pick B, these files and lines change (line numbers as of 26 Oct, 22:20):

- `assets/gdi-mark.svg`: replace with `route-b/b-mark.svg`.
- Add `assets/gdi-icon-32.svg` (from `b-favicon-32.svg`), `assets/gdi-icon-16.svg` (from `b-favicon-16.svg`) and `assets/og-image.png` (from `share/og-b.png`).
- `index.html` line 13, `build.html` 9, `imprint.html` 9, `privacy.html` 9: set the icon `href` to `assets/gdi-icon-16.svg`.
- `index.html` line 33, `build.html` 29, `imprint.html` 17, `privacy.html` 17: set the header `img src` to `assets/gdi-icon-32.svg`.
- `index.html` after line 11: add `og:image` (`https://globaldemocracyinitiative.org/assets/og-image.png`), `og:image:width` 1200, `og:image:height` 630 and `og:image:alt`.
- `PRODUCT.md` line 112 and `README.md` line 9: describe the mark as the 2022 figure with a newcomer at the crossing.
- `style.css`: no change.

For Route C, swap the same files using `route-c/`. Route A also changes `style.css` lines 13, 14, 17, 18, 19 and 178, plus a new `--go` token.

## Files

- `route-a/`, `route-b/`, `route-c/`: for each route, `*-mark.svg` (full size), `*-favicon-32.svg`, `*-favicon-16.svg`, `*-mark-mono.svg`, `*-favicon-16-mono.svg`, `*-lockup.svg` and `*-lockup-mono.svg` (name outlined in Jost 600). `a-mark.svg` is identical to the live mark.
- `share/og-{a,b,c}.svg` and `.png`.
- `sheets/sheet-{a,b,c}.png`: the mark at 16, 32, 64 and 200px, 1× pixel views, browser tabs, lockups, the palette with computed ratios, and the live `index.html` recoloured at desktop and 360px. `sheets/sheet.html?route=a` renders a sheet when the site is served.
- `src/`: `make.py` (geometry, outlines, share images) and `shoot.js` (PNGs). To rebuild, run `python3 make.py`, then `node shoot.js` with `python3 -m http.server 8765` running in the site root.
