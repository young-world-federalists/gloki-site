"""Build every SVG for the 2026-10-26 GDI brand proposals.
Run: python3 make.py   (needs fonttools, brotli, uharfbuzz). PNGs come from shoot.js."""
import os, shutil, re, json
from geom import *

def out(rel, s):
    p = os.path.join(OUT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(s); return p

# ------------------------------------------------------------------ palettes
PAL = {
  'a': dict(ink=M_DARK, ink_soft='#45463C', blue=BLUE, blue_text=M_NAVY, verm=M_ORANGE, verm_text='#B93A13', go='#2A7F35'),
  'b': dict(ink=INK, ink_soft=INK_SOFT, blue=BLUE, blue_text=BLUE_TEXT, verm=VERM, verm_text=VERM_TEXT, go=None),
  'c': dict(ink=INK, ink_soft=INK_SOFT, blue=BLUE, blue_text=BLUE_TEXT, verm=VERM, verm_text=VERM_TEXT, go=None),
}

# ------------------------------------------------------------------ marks
NX = dict(N); NX['X'] = X
# Route B/C links: the 2022 links, with G-F and B-C each split at the newcomer.
# Drawn, the lines are identical: G-X-F and B-X-C are the same straight strokes.
EDGES_X = [('A', 'G'), ('G', 'X'), ('X', 'F'), ('B', 'X'), ('X', 'C'), ('F', 'D'), ('D', 'C'), ('E', 'F'), ('E', 'B')]
assert degrees(EDGES_X)['X'] == 4

def tight_box(nodes, r, pad):
    xs = [p[0] for p in nodes.values()]; ys = [p[1] for p in nodes.values()]
    return (min(xs) - r - pad, min(ys) - r - pad, max(xs) - min(xs) + 2 * (r + pad), max(ys) - min(ys) + 2 * (r + pad))

def knock(k, x, y, r, gap):
    """A paper-coloured ring so the newcomer reads in one colour."""
    return f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r + gap)}" fill="#fff"/>'

def mark(route, size='full', mono=None):
    """route a/b/c; size full|32|16; mono=a colour for one-colour versions."""
    if route == 'a':
        if size == 'full' and not mono:
            return open(os.path.join(SITE, 'assets/gdi-mark.svg')).read()
        nodes, edges = N, EDGES22
        fill = (lambda k: mono) if mono else (lambda k: FILL22[k])
        stroke = lambda a, b: mono or M_DARK
    else:
        nodes, edges = NX, EDGES_X
        if route == 'b':
            fill = lambda k: mono or (BLUE if k == 'X' else INK)
            stroke = lambda a, b: mono or INK
        else:
            fill = lambda k: mono or (BLUE if k == 'X' else FILL22[k])
            stroke = lambda a, b: mono or M_DARK
    if size == '16':
        return favicon16(route, mono)
    if size == 'full':
        r, w = {'a': (100, 17.7), 'b': (84, 28), 'c': (100, 17.7)}[route]
        rr = {'X': 84} if route == 'c' else None
        vb = tight_box(nodes, r, 8)
    else:  # 32px master: heavier links, bigger nodes, square
        r, w = {'a': (122, 44), 'b': (100, 44), 'c': (116, 44)}[route]
        rr = {'X': 96} if route == 'c' else None
        vb = square_box(list(nodes.values()), r, 30)
    body = ''
    # one-colour newcomer: ring of paper around it so it still reads as placed on the crossing
    if mono and route in 'bc':
        lines = graph_body(nodes, edges, r, w, fill, stroke, rr).split('\n  ')
        circles = [l for l in lines if l.startswith('<circle')]; ls = [l for l in lines if l.startswith('<line')]
        xr = (rr or {}).get('X', r)
        xc = [c for c in circles if f'cx="{f(X[0])}"' in c][0]
        others = [c for c in circles if c is not xc]
        body = '\n  '.join(ls + others + [knock('X', X[0], X[1], xr, w * 0.9), xc])
    else:
        body = graph_body(nodes, edges, r, w, fill, stroke, rr)
    title = {'a': 'GDI mark (2022 network figure)', 'b': 'GDI mark: the 2022 figure with a newcomer at the crossing',
             'c': 'GDI mark: the 2022 figure with a newcomer at the crossing'}[route]
    return svg_doc(vb, body, title)

def favicon16(route, mono=None):
    """Hand-placed on a 16-unit grid. Route a: the whole 2022 graph, scaled and nudged
    so no two nodes touch. Routes b/c: the newcomer and the four members it sits between."""
    if route == 'a':
        P = {'A': (9, 2.5), 'B': (8.6, 7), 'C': (2.3, 10), 'D': (6.2, 13.6), 'E': (13.8, 9.8), 'F': (10.2, 11), 'G': (3.2, 5.6)}
        fill = (lambda k: mono) if mono else (lambda k: FILL22[k])
        body = graph_body(P, EDGES22, 1.85, 1.1, fill, lambda a, b: mono or M_DARK)
        return svg_doc((0, 0, 16, 16), body, 'GDI favicon, 16px master')
    P = {'G': (3.5, 4.2), 'B': (12.6, 5.0), 'C': (3.0, 11.6), 'F': (12.8, 12.6), 'X': (7.9, 8.2)}
    E = [('X', 'G'), ('X', 'B'), ('X', 'C'), ('X', 'F')]
    if route == 'b':
        fill = lambda k: mono or (BLUE if k == 'X' else INK); st = lambda a, b: mono or INK
    else:
        fill = lambda k: mono or (BLUE if k == 'X' else FILL22[k]); st = lambda a, b: mono or M_DARK
    body = graph_body(P, E, 2.15, 1.4, fill, st, {'X': 2.5})
    if mono:
        parts = body.split('\n  ')
        xc = parts[-1]
        body = '\n  '.join(parts[:-1] + [knock('X', 7.9, 8.2, 2.5, 1.1), xc])
    return svg_doc((0, 0, 16, 16), body, 'GDI favicon, 16px master')

def inner(svg):
    """Strip <svg> wrapper; return (viewBox tuple, inner markup)."""
    vb = tuple(float(v) for v in re.search(r'viewBox="([^"]+)"', svg).group(1).split())
    body = re.sub(r'^.*?<svg[^>]*>', '', svg, flags=re.S)
    body = re.sub(r'</svg>\s*$', '', body)
    body = re.sub(r'<title>.*?</title>', '', body)
    return vb, body.strip()

def place(svg, x, y, h):
    """Place an SVG's content at (x, y) with height h; returns (markup, width)."""
    vb, body = inner(svg)
    s = h / vb[3]
    return (f'<g transform="translate({f(x)} {f(y)}) scale({s:.5f}) translate({f(-vb[0])} {f(-vb[1])})">{body}</g>', vb[2] * s)

def lockup(route, mono=None):
    ink = mono or PAL[route]['ink']
    m = mark(route, 'full', mono)
    H = 120
    g, mw = place(m, 0, 0, H)
    size = 52; cap = 0.70 * size  # Jost cap height ~ 700/1000
    gap = 34
    d, tw = text_path('Global Democracy Initiative', 'Jost-600', size, mw + gap, H / 2 + cap / 2)
    W = mw + gap + tw
    body = f'{g}\n  <path fill="{ink}" d="{d}"/>'
    return svg_doc((-4, -4, W + 8, H + 8), body, 'Global Democracy Initiative')

# ------------------------------------------------------------------ share image
def crowd_from_page():
    """Read the hero figure from index.html so the share image matches the page."""
    html = open(os.path.join(SITE, 'index.html')).read()
    fig = re.search(r'<figure class="crowd">(.*?)</figure>', html, re.S).group(1)
    vb = [float(v) for v in re.search(r'viewBox="([^"]+)"', fig).group(1).split()]
    uses = re.findall(r'<use href="#person" class="([^"]+)" x="([\d.]+)" y="([\d.]+)"', fig)
    links = re.findall(r'<line class="link-new" x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"', fig)
    return vb, [(c, float(x), float(y)) for c, x, y in uses], [tuple(map(float, l)) for l in links]

def og(route):
    P = PAL[route]; W, H = 1200, 630
    vb, uses, links = crowd_from_page()
    # keep the seven middle columns (newcomer in the middle)
    xs = sorted({x for _, x, _ in uses}); mid = xs[len(xs) // 2]
    keep = [u for u in uses if abs(u[1] - mid) <= 72.1]
    x0 = mid - 72 - 2; fw = 168
    s = 2.35
    base = 548  # shared baseline: caption under the crowd, domain under the headline
    ox, oy = 1200 - 72 - fw * s, base - 40 - vb[3] * s
    parts = [f'<rect width="{W}" height="{H}" fill="#fff"/>']
    # crowd
    g = [f'<g transform="translate({f(ox)} {f(oy)}) scale({s}) translate({f(-x0)} 0)">']
    for x1, y1, x2, y2 in links:
        g.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{P["blue"]}" stroke-width="2" stroke-linecap="round"/>')
    for c, x, y in keep:
        col = P['blue'] if 'p-blue' in c else P['ink']
        g.append(f'<g fill="{col}" transform="translate({f(x)} {f(y)})">{PERSON}</g>')
    g.append('</g>')
    parts.append(''.join(g))
    fig_h = vb[3] * s
    cap_d, cap_w = text_path('You get in when four people vouch for you.', 'Jost-500', 25, 0, 0)
    cx = ox + (fw * s - cap_w) / 2
    parts.append(f'<path fill="{P["ink"]}" transform="translate({f(cx)} {f(base)})" d="{cap_d}"/>')
    # lockup top-left
    m, mw = place(mark(route, 'full'), 72, 60, 50)
    parts.append(m)
    d, _ = text_path('Global Democracy Initiative', 'Jost-600', 26, 72 + mw + 16, 60 + 25 + 9)
    parts.append(f'<path fill="{P["ink"]}" d="{d}"/>')
    # headline
    lines = ['There will be no', 'global democracy', 'without technology.']
    y = 236
    for ln in lines:
        d, w = text_path(ln, 'Jost-600', 70, 72, y, -0.012)
        parts.append(f'<path fill="{P["ink"]}" d="{d}"/>'); y += 76
    d, _ = text_path('globaldemocracyinitiative.org', 'AtkinsonHyperlegible-700', 24, 72, 548)
    parts.append(f'<path fill="{P["blue_text"]}" d="{d}"/>')
    return svg_doc((0, 0, W, H), '\n  '.join(parts), 'There will be no global democracy without technology.', W, H)

# ------------------------------------------------------------------ write
if __name__ == '__main__':
    files = []
    for r in 'abc':
        ink = PAL[r]['ink']
        files += [out(f'route-{r}/{r}-mark.svg', mark(r, 'full')),
                  out(f'route-{r}/{r}-favicon-32.svg', mark(r, '32')),
                  out(f'route-{r}/{r}-favicon-16.svg', mark(r, '16')),
                  out(f'route-{r}/{r}-mark-mono.svg', mark(r, 'full', ink)),
                  out(f'route-{r}/{r}-favicon-16-mono.svg', mark(r, '16', ink)),
                  out(f'route-{r}/{r}-lockup.svg', lockup(r)),
                  out(f'route-{r}/{r}-lockup-mono.svg', lockup(r, ink)),
                  out(f'share/og-{r}.svg', og(r))]
    json.dump(PAL, open(os.path.join(OUT, 'src/palettes.json'), 'w'), indent=1)
    print('\n'.join(os.path.relpath(p, OUT) for p in files))
