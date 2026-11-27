"""Dithered images for the GDI site. Pure Python, no dependencies.

Writes two 1-bit PNGs (ink on transparent) into assets/:
  dither-globe.png  240x240   a shaded globe centred on Africa and Europe
  dither-crowd.png  552x128   rows of the person pictogram, fading with distance; tiles sideways

Both are drawn small and shown at 2x with `image-rendering: pixelated`, so the dither stays visible.
The coastlines are a rough hand-made outline, good enough at this size; they are not map data.

Run from the repo root:  python3 docs/brand/2026-11-26-dither/make.py
"""
import math, struct, zlib, os

INK = (0x11, 0x14, 0x18)
BAYER = [[0,32,8,40,2,34,10,42],[48,16,56,24,50,18,58,26],[12,44,4,36,14,46,6,38],[60,28,52,20,62,30,54,22],
         [3,35,11,43,1,33,9,41],[51,19,59,27,49,17,57,25],[15,47,7,39,13,45,5,37],[63,31,55,23,61,29,53,21]]

def write_png(path, w, h, ink_at):
    """ink_at(x, y) -> True for an ink pixel. Palette PNG: 0 = ink, 1 = transparent."""
    raw = bytearray()
    for y in range(h):
        raw.append(0)
        byte = 0; n = 0
        for x in range(w):
            byte = (byte << 1) | (0 if ink_at(x, y) else 1); n += 1
            if n == 8: raw.append(byte); byte = 0; n = 0
        if n: raw.append(byte << (8 - n))
    def chunk(tag, data):
        return struct.pack('>I', len(data)) + tag + data + struct.pack('>I', zlib.crc32(tag + data) & 0xffffffff)
    png = b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 1, 3, 0, 0, 0))
    png += chunk(b'PLTE', bytes(INK) + b'\xff\xff\xff') + chunk(b'tRNS', b'\xff\x00')
    png += chunk(b'IDAT', zlib.compress(bytes(raw), 9)) + chunk(b'IEND', b'')
    open(path, 'wb').write(png)
    return len(png)

def dither(dark, x, y):
    return dark > (BAYER[y % 8][x % 8] + 0.5) / 64

def inside(poly, px, py):
    c = False; j = len(poly) - 1
    for i in range(len(poly)):
        xi, yi = poly[i]; xj, yj = poly[j]
        if (yi > py) != (yj > py) and px < (xj - xi) * (py - yi) / (yj - yi) + xi: c = not c
        j = i
    return c

# ---- Globe ---------------------------------------------------------------------------------
LAND = [
 [(-17,15),(-17,21),(-13,28),(-6,35),(10,37),(11,33),(20,31),(25,32),(34,31),(37,22),(43,12),(51,12),(42,-1),(40,-15),(35,-24),(27,-34),(18,-34),(12,-17),(14,-5),(9,4),(-8,4),(-13,8)],
 [(-9,37),(-9,43),(-1,43),(-4,48),(3,51),(8,54),(8,57),(12,56),(22,54),(28,60),(22,65),(14,65),(5,58),(5,62),(15,69),(28,71),(41,67),(60,69),(60,55),(50,45),(40,47),(30,45),(27,41),(23,38),(20,40),(13,45),(18,40),(15,38),(12,44),(3,43),(0,39),(-5,36)],
 [(60,69),(75,73),(105,78),(140,73),(180,68),(170,60),(160,60),(156,51),(142,54),(135,43),(128,36),(122,31),(120,22),(108,21),(105,9),(100,13),(103,1),(98,8),(94,16),(88,22),(80,15),(77,8),(72,20),(66,25),(57,25),(51,25),(56,18),(45,13),(43,12),(34,28),(36,36),(27,37),(27,41),(40,41),(50,45),(60,55)],
 [(-168,66),(-156,71),(-128,70),(-95,72),(-80,73),(-62,60),(-78,62),(-94,60),(-82,52),(-78,56),(-56,52),(-66,45),(-76,35),(-81,25),(-82,30),(-90,30),(-97,26),(-97,19),(-87,21),(-83,10),(-78,8),(-85,11),(-95,16),(-105,20),(-110,23),(-115,31),(-124,40),(-124,48),(-135,58),(-150,60),(-165,55),(-160,60)],
 [(-78,8),(-62,10),(-50,0),(-35,-6),(-39,-17),(-48,-27),(-58,-38),(-65,-45),(-68,-54),(-74,-50),(-72,-30),(-70,-18),(-80,-5)],
 [(114,-22),(122,-17),(131,-12),(137,-16),(142,-11),(146,-19),(153,-27),(150,-37),(140,-38),(131,-32),(115,-34)],
 [(-45,60),(-52,68),(-58,76),(-35,83),(-20,78),(-22,70)],
 [(44,-25),(50,-15),(47,-13),(43,-22)],
 [(-5,50),(-3,58),(-6,58),(1,53),(1,51)],
 [(-22,64),(-14,66),(-14,64),(-21,63)],
]
BOXES = [(min(p[0] for p in poly), max(p[0] for p in poly), min(p[1] for p in poly), max(p[1] for p in poly)) for poly in LAND]

def is_land(lon, lat):
    for poly, (x0, x1, y0, y1) in zip(LAND, BOXES):
        if x0 <= lon <= x1 and y0 <= lat <= y1 and inside(poly, lon, lat): return True
    return False

def globe(size=240, lon0=18, lat0=8):
    c = (size - 1) / 2; R = size / 2 - 1.5
    s0, c0 = math.sin(math.radians(lat0)), math.cos(math.radians(lat0))
    L = (-0.45, 0.5, 0.74)
    def at(x, y):
        u = (x - c) / R; v = (c - y) / R; r2 = u * u + v * v
        if r2 > 1.0: return False
        if r2 > (1 - 1.6 / R) ** 2: return True                      # the rim, a solid ink line
        z = math.sqrt(1 - r2)
        lat = math.degrees(math.asin(max(-1, min(1, z * s0 + v * c0))))
        lon = lon0 + math.degrees(math.atan2(u, z * c0 - v * s0))
        lon = (lon + 180) % 360 - 180
        lam = max(0.0, u * L[0] + v * L[1] + z * L[2])
        if is_land(lon, lat): dark = 0.97 - 0.30 * lam
        else: dark = 0.05 + 0.20 * (1 - lam) + 0.30 * (1 - z) ** 2
        return dither(dark, x, y)
    return size, size, at

# ---- Crowd ---------------------------------------------------------------------------------
# The person pictogram on its 20 x 40 box (curved shoulders squared off).
BODY = [(4.6,11.2),(15.4,11.2),(17.4,11.8),(17.6,13.4),(18.6,25),(15.8,25),(15,17),(15,39.2),(10.9,39.2),(10.9,27.5),(9.1,27.5),(9.1,39.2),(5,39.2),(5,17),(4.2,25),(1.4,25),(2.4,13.4),(2.6,11.8)]
def in_person(fx, fy):
    if (fx - 10) ** 2 + (fy - 5.2) ** 2 <= 4.6 ** 2: return True
    return 11.2 <= fy <= 39.2 and 1.4 <= fx <= 18.6 and inside(BODY, fx, fy)

def crowd(w=552, h=128):
    # (figures across the tile, figure height, feet y, darkness, half-step offset): far rows first
    rows = [(36, 26, 34, 0.16, 0), (28, 36, 56, 0.30, 1), (22, 48, 84, 0.52, 0), (16, 66, 126, 1.0, 1)]
    def at(x, y):
        hit = None
        for n, fh, feet, dark, off in rows:
            pitch = w / n; scale = fh / 40.0
            lx = (x + 0.5 + (pitch / 2 if off else 0)) % pitch
            fx = (lx - pitch / 2) / scale + 10
            fy = (y + 0.5 - (feet - fh)) / scale
            if 0 <= fy <= 40 and in_person(fx, fy): hit = dark         # nearer rows are drawn over farther ones
        return hit is not None and (hit >= 1.0 or dither(hit, x, y))
    return w, h, at

if __name__ == '__main__':
    os.makedirs('assets', exist_ok=True)
    for name, (w, h, at) in (('dither-globe.png', globe()), ('dither-crowd.png', crowd())):
        print(name, w, 'x', h, write_png(os.path.join('assets', name), w, h, at), 'bytes')
