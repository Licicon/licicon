# -*- coding: utf-8 -*-
"""Genera imágenes para compartir (1200x630) en /assets/og/. Requiere Pillow y las fuentes en _build/fonts/."""
import os, random, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter
sys.path.insert(0, os.path.dirname(__file__))
from contenido import MARCAS
B = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(B)
F = os.path.join(B, "fonts")
W, H = 1200, 630
GOLD = (212, 175, 55); GOLD2 = (184, 153, 90); TXT = (235, 231, 222); C0 = (8, 9, 11)

def font(name, size, var):
    f = ImageFont.truetype(os.path.join(F, name), size)
    try: f.set_variation_by_name(var)
    except Exception: pass
    return f

def spaced(d, xy, text, f, fill, track, anchor_center=True):
    widths = [d.textlength(c, font=f) for c in text]
    total = sum(widths) + track * (len(text) - 1)
    x = xy[0] - total / 2 if anchor_center else xy[0]
    for c, w in zip(text, widths):
        d.text((x, xy[1]), c, font=f, fill=fill); x += w + track
    return total

def red(img, seed=7):
    random.seed(seed); d = ImageDraw.Draw(img, "RGBA")
    pts = [(random.uniform(0, W), random.uniform(0, H)) for _ in range(60)]
    for i, p in enumerate(pts):
        for q in pts[i+1:]:
            dist = ((p[0]-q[0])**2 + (p[1]-q[1])**2) ** .5
            if dist < 170: d.line([p, q], fill=GOLD + (int(40 * (1 - dist/170)),), width=1)
        d.ellipse([p[0]-1.4, p[1]-1.4, p[0]+1.4, p[1]+1.4], fill=GOLD + (120,))
    # viñeta
    v = Image.new("L", (W, H), 0); vd = ImageDraw.Draw(v)
    vd.ellipse([W*.18, H*.02, W*.82, H*.98], fill=255); v = v.filter(ImageFilter.GaussianBlur(160))
    dark = Image.new("RGB", (W, H), C0)
    return Image.composite(img, dark, v)

def licicon():
    img = red(Image.new("RGB", (W, H), C0))
    d = ImageDraw.Draw(img, "RGBA")
    emb = Image.open(os.path.join(ROOT, "assets/licicon-emblema-lg.png")).convert("RGBA").resize((118, 114), Image.LANCZOS)
    img.paste(emb, (W//2 - 59, 88), emb)
    d.ellipse([W//2-74, 145-74, W//2+74, 145+74], outline=GOLD + (170,), width=1)
    spaced(d, (W//2, 238), "LICICON", font("CormorantGaramond[wght].ttf", 82, b"Regular"), TXT, 30)
    d.line([(W//2-150, 352), (W//2+150, 352)], fill=GOLD + (200,), width=1)
    spaced(d, (W//2, 372), "ESTRUCTURA · CUMPLIMIENTO · TECNOLOGÍA", font("Montserrat[wght].ttf", 17, b"Medium"), GOLD2, 7)
    marks = [Image.open(os.path.join(ROOT, f"assets/marcas/mark/{m['slug']}.png")).convert("RGBA") for m in MARCAS]
    hh = 44; ms = [mk.resize((int(mk.width*hh/mk.height), hh), Image.LANCZOS) for mk in marks]
    gap = 46; total = sum(m.width for m in ms) + gap*(len(ms)-1); x = (W-total)//2
    for mk in ms:
        a = mk.split()[3].point(lambda v: int(v*.62)); mk.putalpha(a); img.paste(mk, (x, 462), mk); x += mk.width + gap
    spaced(d, (W//2, 560), "licicon.com", font("Montserrat[wght].ttf", 15, b"Regular"), (120, 116, 108), 3)
    img.save(os.path.join(ROOT, "assets/og/licicon.jpg"), quality=90)

def marca(m):
    bg = tuple(int(m["logo_bg"][i:i+2], 16) for i in (1, 3, 5))
    img = Image.new("RGB", (W, H), bg); d = ImageDraw.Draw(img)
    dark = sum(bg) < 200
    logo = Image.open(os.path.join(ROOT, "assets/marcas", m["logo"])).convert("RGB")
    logo.thumbnail((720, 400), Image.LANCZOS)
    img.paste(logo, ((W-logo.width)//2, 70 + (400-logo.height)//2))
    sub = (150, 146, 138) if dark else (110, 104, 94)
    d.line([(W//2-60, 520), (W//2+60, 520)], fill=sub, width=1)
    spaced(d, (W//2, 540), "UNA FIRMA DEL GRUPO LICICON", font("Montserrat[wght].ttf", 15, b"Medium"), sub, 5)
    img.save(os.path.join(ROOT, f"assets/og/{m['slug']}.jpg"), quality=90)

if __name__ == "__main__":
    licicon()
    for m in MARCAS: marca(m)
    print("OG listas")
