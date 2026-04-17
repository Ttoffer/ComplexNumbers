"""Build apple-touch-icon.png (180x180): jewel-like tile + double-struck C (ℂ) + Re/Im colour hints."""
from __future__ import annotations

import math
import random
from PIL import Image, ImageDraw, ImageFont

SIZE = 180
R = int(SIZE * 0.224)
CX, CY = SIZE * 0.5, SIZE * 0.48


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def clamp01(t: float) -> float:
    return max(0.0, min(1.0, t))


def bg_rgb(nx: float, ny: float) -> tuple[int, int, int]:
    """Radial: deep blue centre → cyan → violet edge (Argand / complex-plane mood)."""
    dx, dy = nx - 0.5, ny - 0.48
    r = math.sqrt(dx * dx + dy * dy) * 1.35
    t = clamp01(r)
    ir, ig, ib = 30, 70, 140
    mr, mg, mb = 56, 189, 248
    pr, pg, pb = 120, 60, 200
    er, eg, eb = 8, 10, 28
    if t < 0.38:
        u = t / 0.38
        r_, g_, b_ = lerp(ir, mr, u), lerp(ig, mg, u), lerp(ib, mb, u)
    elif t < 0.72:
        u = (t - 0.38) / 0.34
        r_, g_, b_ = lerp(mr, pr, u), lerp(mg, pg, u), lerp(mb, pb, u)
    else:
        u = (t - 0.72) / 0.28
        r_, g_, b_ = lerp(pr, er, u), lerp(pg, eg, u), lerp(pb, eb, u)
    ang = math.atan2(dy, dx)
    tw = 0.5 + 0.5 * math.sin(ang * 2)
    r_ += 22 * tw * (1 - t) * 0.4
    g_ += 35 * tw * (1 - t) * 0.4
    b_ += 18 * tw * (1 - t) * 0.4
    return int(clamp01(r_ / 255) * 255), int(clamp01(g_ / 255) * 255), int(clamp01(b_ / 255) * 255)


def load_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        ("C:/Windows/Fonts/cambria.ttc", 0),
        ("C:/Windows/Fonts/cambriab.ttf", 0),
        ("C:/Windows/Fonts/seguiemj.ttf", 0),
        ("C:/Windows/Fonts/segoeuib.ttf", 0),
        ("C:/Windows/Fonts/arialbd.ttf", 0),
    ]
    for path, idx in candidates:
        try:
            return ImageFont.truetype(path, size, index=idx)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    rng = random.Random(42)
    img = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    px = img.load()
    for y in range(SIZE):
        for x in range(SIZE):
            r, g, b = bg_rgb(x / SIZE, y / SIZE)
            px[x, y] = (r, g, b, 255)

    mask = Image.new("L", (SIZE, SIZE), 0)
    mdraw = ImageDraw.Draw(mask)
    mdraw.rounded_rectangle((0, 0, SIZE - 1, SIZE - 1), radius=R, fill=255)
    img.putalpha(mask)

    gloss = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    gd = ImageDraw.Draw(gloss)
    gd.ellipse((SIZE * 0.08, SIZE * 0.04, SIZE * 0.92, SIZE * 0.48), fill=(255, 255, 255, 55))
    gd.ellipse((SIZE * 0.18, SIZE * 0.58, SIZE * 0.82, SIZE * 0.94), fill=(167, 139, 250, 38))
    img = Image.alpha_composite(img, gloss)

    draw = ImageDraw.Draw(img)
    for k in range(12):
        ang = k * 1.85 + 0.4
        rr = SIZE * (0.36 + 0.05 * math.sin(k * 1.2))
        sx = CX + rr * math.cos(ang)
        sy = CY + rr * math.sin(ang)
        br = 2 + (k % 3)
        a = 85 + rng.randint(0, 45)
        draw.ellipse((sx - br, sy - br, sx + br, sy + br), fill=(255, 250, 220, a))

    rim = Image.new("RGBA", (SIZE, SIZE), (0, 0, 0, 0))
    rd = ImageDraw.Draw(rim)
    for i, col in enumerate([(74, 222, 128, 95), (56, 189, 248, 100), (167, 139, 250, 80)]):
        o = 2 + i
        rd.rounded_rectangle((o, o, SIZE - 1 - o, SIZE - 1 - o), radius=max(2, R - o), outline=col, width=1)
    img = Image.alpha_composite(img, rim)
    draw = ImageDraw.Draw(img)

    font = load_font(88)
    ch = "\u2102"  # ℂ double-struck
    bbox = draw.textbbox((0, 0), ch, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (SIZE - tw) / 2 - bbox[0]
    ty = (SIZE - th) / 2 - bbox[1] - 4

    # If ℂ renders as tofu, bbox may be tiny — fallback to "i"
    if tw < 8 or th < 8:
        font = load_font(102)
        ch = "i"
        bbox = draw.textbbox((0, 0), ch, font=font)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        tx = (SIZE - tw) / 2 - bbox[0]
        ty = (SIZE - th) / 2 - bbox[1] - 6

    layers = [
        (5, 4, (74, 222, 128, 55)),
        (-4, -3, (167, 139, 250, 65)),
        (4, -3, (56, 189, 248, 70)),
        (0, 0, (251, 191, 36, 100)),
        (0, 0, (255, 255, 255, 200)),
    ]
    for ox, oy, rgba in layers:
        draw.text((tx + ox, ty + oy), ch, font=font, fill=rgba)

    out = "apple-touch-icon.png"
    img.save(out, "PNG", optimize=True)
    print("Wrote", out)


if __name__ == "__main__":
    main()
