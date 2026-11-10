"""Prépare les images d'une app pour le site, puis met à jour assets.json.

Usage (depuis la racine du dépôt) :
  python _tools/add_app_assets.py <slug> <icone-1024.png> <accent #hex> "<sous-titre>" <capture1.png> [capture2 ...]
  python _tools/add_app_assets.py --site      (régénère seulement images/og/site.png)

Produit :
  images/<slug>.png         512x512 RGBA     (icône brute)
  images/<slug>-512.png     512x512 RGB      (page de l'app, données structurées)
  images/<slug>-160.webp    160x160          (cartes de la grille)
  images/shots/<slug>-N.webp 440 px de large (captures App Store 6.9", 4 max)
  images/og/<slug>.png      1200x630         (carte de partage réseaux sociaux)
  images/og/site.png        1200x630         (toutes les icônes, dans l'ordre d'APPS)
Puis : ajouter l'entrée dans APPS de build.py et lancer `python _tools/build.py`.
"""
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = os.path.join(ROOT, "images")
FONTS = "C:/Windows/Fonts"
BOLD = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 96)
REG = ImageFont.truetype(os.path.join(FONTS, "segoeui.ttf"), 40)
SMALL_B = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 30)
BIG = ImageFont.truetype(os.path.join(FONTS, "segoeuib.ttf"), 76)
SUB = ImageFont.truetype(os.path.join(FONTS, "segoeui.ttf"), 36)


def rounded(im, size, radius_ratio=0.225):
    im = im.convert("RGBA").resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size - 1, size - 1), int(size * radius_ratio), fill=255)
    im.putalpha(mask)
    return im


def hex2rgb(h):
    return tuple(int(h[i:i + 2], 16) for i in (1, 3, 5))


def gradient(w, h, c1, c2):
    g = Image.new("RGB", (w, h))
    px = g.load()
    for x in range(w):
        t = x / (w - 1)
        col = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
        for y in range(h):
            px[x, y] = col
    return g


def og_app(slug, icon, name, subtitle, accent, cta):
    ac = hex2rgb(accent)
    dark = tuple(int(c * 0.35) for c in ac)
    bg = gradient(1200, 630, dark, (18, 20, 30))
    bg.paste(r := rounded(icon, 300), (100, 165), r)
    d = ImageDraw.Draw(bg)
    d.text((460, 240), name, font=BOLD, fill="white")
    d.text((460, 350), subtitle, font=REG, fill=(232, 232, 240))
    light = tuple(min(255, int(c * 1.25) + 30) for c in ac)
    d.text((460, 425), cta, font=SMALL_B, fill=light)
    bg.save(os.path.join(IMG, "og", f"{slug}.png"), optimize=True)


def site_slugs():
    src = open(os.path.join(ROOT, "_tools", "build.py"), encoding="utf-8").read()
    return re.findall(r'"slug":\s*"([^"]+)"', src)


def og_site():
    slugs = site_slugs()
    bg = Image.new("RGB", (1200, 630), (21, 22, 26))
    d = ImageDraw.Draw(bg)
    d.text((80, 105), "Florian Marcel", font=BIG, fill="white")
    d.text((80, 195), "Applications iPhone gratuites : jeux, jouets & outils", font=SUB, fill=(160, 166, 178))
    n = len(slugs)
    size = min(120, int((1200 - 160) / (n * 0.92)))
    step = (1200 - 160 - size) / max(1, n - 1)
    for i, s in enumerate(slugs):
        ic = rounded(Image.open(os.path.join(IMG, f"{s}-512.png")), size)
        bg.paste(ic, (int(80 + i * step), 360 if i % 2 == 0 else 430), ic)
    bg.save(os.path.join(IMG, "og", "site.png"), optimize=True)
    print("images/og/site.png:", n, "icônes")


def main():
    if sys.argv[1:] == ["--site"]:
        return og_site()
    slug, icon_path, accent, subtitle, *shots = sys.argv[1:]
    name = next((m for m in re.findall(r'"slug":\s*"' + slug + r'",\s*"name":\s*"([^"]+)"',
                 open(os.path.join(ROOT, "_tools", "build.py"), encoding="utf-8").read())), slug)
    icon = Image.open(icon_path).convert("RGBA")
    icon.resize((512, 512), Image.LANCZOS).save(os.path.join(IMG, f"{slug}.png"), optimize=True)
    icon.convert("RGB").resize((512, 512), Image.LANCZOS).save(os.path.join(IMG, f"{slug}-512.png"), optimize=True)
    icon.convert("RGB").resize((160, 160), Image.LANCZOS).save(os.path.join(IMG, f"{slug}-160.webp"), quality=90)
    os.makedirs(os.path.join(IMG, "shots"), exist_ok=True)
    out = []
    for i, p in enumerate(shots[:4], 1):
        im = Image.open(p).convert("RGB")
        w = 440
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(os.path.join(IMG, "shots", f"{slug}-{i}.webp"), quality=82)
        out.append({"src": f"images/shots/{slug}-{i}.webp", "w": w, "h": h})
    live = re.search(r'"slug":\s*"' + slug + r'"[^}]*?"live":\s*False', open(os.path.join(ROOT, "_tools", "build.py"), encoding="utf-8").read(), re.S)
    og_app(slug, icon, name, subtitle, accent, "Bientôt sur l'App Store" if live else "Gratuit sur l'App Store")
    path = os.path.join(ROOT, "_tools", "assets.json")
    data = json.load(open(path, encoding="utf-8"))
    data[slug] = {"accent": accent, "shots": out}
    json.dump(data, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{slug}: icônes, {len(out)} captures, og ; assets.json mis à jour")
    og_site()


main()
