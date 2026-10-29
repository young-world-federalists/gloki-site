"""Geometry and drawing helpers for the GDI mark proposals (2026-10-26).
Node centres and links are read from assets/gdi-mark.svg (the 2022 network figure)."""
import math, re, io, os
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import uharfbuzz as hb

SITE = '/home/user/gloki-site'
OUT = os.path.join(SITE, 'docs/brand/2026-10-26')

# Page palette (style.css :root, 2026-10-26)
INK, INK_SOFT, BLUE, BLUE_TEXT, VERM, VERM_TEXT = '#111418', '#3b424b', '#3b82f6', '#1d4ed8', '#e0412b', '#b42318'
# 2022 mark palette
M_ORANGE, M_GREEN, M_NAVY, M_DARK = '#EC623E', '#7BD484', '#165A99', '#22231A'

# 2022 node centres (r = 100) and links, measured from the file.
N = {'A': (750, 200), 'B': (731, 512), 'C': (218, 742), 'D': (550, 1007),
     'E': (1153, 742), 'F': (785, 823), 'G': (318, 465)}
FILL22 = {'A': M_ORANGE, 'B': M_GREEN, 'C': M_GREEN, 'D': M_ORANGE, 'E': M_ORANGE, 'F': M_NAVY, 'G': M_NAVY}
EDGES22 = [('A', 'G'), ('B', 'C'), ('F', 'G'), ('F', 'D'), ('D', 'C'), ('E', 'F'), ('E', 'B')]

def _cross(p1, p2, p3, p4):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = p1, p2, p3, p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))

# The two 2022 links that cross: G-F and B-C. A newcomer placed at the crossing
# sits between two linked pairs, which is exactly the vouching rule.
X = _cross(N['G'], N['F'], N['B'], N['C'])

def degrees(edges):
    d = {}
    for a, b in edges:
        d[a] = d.get(a, 0) + 1; d[b] = d.get(b, 0) + 1
    return d

def f(v): return ('%.1f' % v).rstrip('0').rstrip('.')

def square_box(pts, r, pad):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0, x1, y0, y1 = min(xs) - r, max(xs) + r, min(ys) - r, max(ys) + r
    side = max(x1 - x0, y1 - y0) + 2 * pad
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    return (cx - side / 2, cy - side / 2, side, side)

def graph_body(nodes, edges, r, w, node_fill, edge_stroke, rr=None):
    """Lines centre to centre under the discs. rr: per-node radius override."""
    rr = rr or {}
    out = []
    for a, b in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        out.append(f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" stroke="{edge_stroke(a, b)}" stroke-width="{f(w)}"/>')
    for k, (x, y) in nodes.items():
        out.append(f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(rr.get(k, r))}" fill="{node_fill(k)}"/>')
    return '\n  '.join(out)

def svg_doc(vb, body, title=None, w=None, h=None):
    size = f' width="{w}" height="{h}"' if w else ''
    t = f'<title>{title}</title>\n  ' if title else ''
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(f(v) for v in vb)}"{size}>\n  {t}{body}\n</svg>\n')

# ---------- text to outlines (Jost / Atkinson) ----------
_fonts = {}
def _font(name):
    if name not in _fonts:
        tt = TTFont(os.path.join(SITE, 'assets/fonts', name + '.woff2'))
        tt.flavor = None
        buf = io.BytesIO(); tt.save(buf); data = buf.getvalue()
        face = hb.Face(hb.Blob(data)); font = hb.Font(face)
        _fonts[name] = (TTFont(io.BytesIO(data)), font, face.upem)
    return _fonts[name]

def text_path(text, name='Jost-600', size=100, x=0, y=0, tracking=0.0):
    """Return (path d, advance) for text set at baseline (x, y), kerned by HarfBuzz."""
    tt, font, upem = _font(name)
    buf = hb.Buffer(); buf.add_str(text); buf.guess_segment_properties()
    hb.shape(font, buf, {'kern': True, 'liga': True})
    gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = size / upem; pen_x = 0; ds = []
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        g = order[info.codepoint]
        sp = SVGPathPen(gs, ntos=lambda v: ('%.2f' % v).rstrip('0').rstrip('.'))
        tp = TransformPen(sp, (s, 0, 0, -s, x + (pen_x + pos.x_offset) * s, y - pos.y_offset * s))
        gs[g].draw(tp)
        ds.append(sp.getCommands())
        pen_x += pos.x_advance + tracking * upem
    return ' '.join(d for d in ds if d), pen_x * s

def text_width(text, name='Jost-600', size=100, tracking=0.0):
    return text_path(text, name, size, 0, 0, tracking)[1]

# ---------- the page's person symbol ----------
PERSON = ('<circle cx="10" cy="5.2" r="4.6"/>'
          '<path d="M4.6 11.2H15.4Q17.4 11.2 17.6 13.4L18.6 25H15.8L15 17V39.2H10.9V27.5H9.1V39.2H5V17L4.2 25H1.4L2.4 13.4Q2.6 11.2 4.6 11.2Z"/>')

def contrast(a, b='#ffffff'):
    def lin(c):
        c /= 255; return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    def L(h):
        h = h.lstrip('#'); r, g, bb = [int(h[i:i + 2], 16) for i in (0, 2, 4)]
        return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(bb)
    la, lb = L(a), L(b); return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)
