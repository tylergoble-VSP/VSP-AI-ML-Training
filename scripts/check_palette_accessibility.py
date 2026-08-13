#!/usr/bin/env python3
"""Colour-vision-deficiency check for the VSP chart palette (SI-10).

Method: Machado, Oliveira & Fernandes (2009) severity-1.0 simulation matrices applied in
linear-RGB, then CIEDE2000 perceptual distance in CIELAB (D65). Also reports greyscale
(relative luminance) separation for print/photocopy safety.
"""
import itertools
import numpy as np

PALETTE = {
    "navy-light":     "#59709c",
    "green":          "#65a74e",
    "yellow":         "#ffe86b",
    "green-lightest": "#97f377",
}

# Machado et al. 2009, severity 1.0, linear-RGB
M = {
    "protanopia": np.array([[0.152286, 1.052583, -0.204868],
                            [0.114503, 0.786281,  0.099216],
                            [-0.003882, -0.048116, 1.051998]]),
    "deuteranopia": np.array([[0.367322, 0.860646, -0.227968],
                              [0.280085, 0.672501,  0.047413],
                              [-0.011820, 0.042940, 0.968881]]),
    "tritanopia": np.array([[1.255528, -0.076749, -0.178779],
                            [-0.078411, 0.930809,  0.147602],
                            [0.004733,  0.691367,  0.303900]]),
}


def hex_to_srgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4)])


def to_linear(c):
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def to_srgb(c):
    c = np.clip(c, 0, 1)
    return np.where(c <= 0.0031308, c * 12.92, 1.055 * c ** (1 / 2.4) - 0.055)


def simulate(srgb, kind):
    return to_srgb(M[kind] @ to_linear(srgb))


def srgb_to_lab(srgb):
    lin = to_linear(srgb)
    xyz = np.array([[0.4124564, 0.3575761, 0.1804375],
                    [0.2126729, 0.7151522, 0.0721750],
                    [0.0193339, 0.1191920, 0.9503041]]) @ lin
    white = np.array([0.95047, 1.0, 1.08883])
    t = xyz / white
    f = np.where(t > (6 / 29) ** 3, np.cbrt(t), t / (3 * (6 / 29) ** 2) + 4 / 29)
    return np.array([116 * f[1] - 16, 500 * (f[0] - f[1]), 200 * (f[1] - f[2])])


def ciede2000(lab1, lab2):
    L1, a1, b1 = lab1
    L2, a2, b2 = lab2
    kL = kC = kH = 1.0
    C1, C2 = np.hypot(a1, b1), np.hypot(a2, b2)
    Cbar = (C1 + C2) / 2
    G = 0.5 * (1 - np.sqrt(Cbar ** 7 / (Cbar ** 7 + 25 ** 7))) if Cbar > 0 else 0.5
    a1p, a2p = (1 + G) * a1, (1 + G) * a2
    C1p, C2p = np.hypot(a1p, b1), np.hypot(a2p, b2)
    h1p = np.degrees(np.arctan2(b1, a1p)) % 360
    h2p = np.degrees(np.arctan2(b2, a2p)) % 360
    dLp = L2 - L1
    dCp = C2p - C1p
    if C1p * C2p == 0:
        dhp = 0.0
    elif abs(h2p - h1p) <= 180:
        dhp = h2p - h1p
    elif h2p - h1p > 180:
        dhp = h2p - h1p - 360
    else:
        dhp = h2p - h1p + 360
    dHp = 2 * np.sqrt(C1p * C2p) * np.sin(np.radians(dhp) / 2)
    Lbp = (L1 + L2) / 2
    Cbp = (C1p + C2p) / 2
    if C1p * C2p == 0:
        hbp = h1p + h2p
    elif abs(h1p - h2p) <= 180:
        hbp = (h1p + h2p) / 2
    elif h1p + h2p < 360:
        hbp = (h1p + h2p + 360) / 2
    else:
        hbp = (h1p + h2p - 360) / 2
    T = (1 - 0.17 * np.cos(np.radians(hbp - 30)) + 0.24 * np.cos(np.radians(2 * hbp))
         + 0.32 * np.cos(np.radians(3 * hbp + 6)) - 0.20 * np.cos(np.radians(4 * hbp - 63)))
    dTheta = 30 * np.exp(-(((hbp - 275) / 25) ** 2))
    Rc = 2 * np.sqrt(Cbp ** 7 / (Cbp ** 7 + 25 ** 7))
    Sl = 1 + (0.015 * (Lbp - 50) ** 2) / np.sqrt(20 + (Lbp - 50) ** 2)
    Sc = 1 + 0.045 * Cbp
    Sh = 1 + 0.015 * Cbp * T
    Rt = -np.sin(np.radians(2 * dTheta)) * Rc
    return np.sqrt((dLp / (kL * Sl)) ** 2 + (dCp / (kC * Sc)) ** 2 + (dHp / (kH * Sh)) ** 2
                   + Rt * (dCp / (kC * Sc)) * (dHp / (kH * Sh)))


def relative_luminance(srgb):
    lin = to_linear(srgb)
    return float(0.2126 * lin[0] + 0.7152 * lin[1] + 0.0722 * lin[2])


names = list(PALETTE)
base = {n: hex_to_srgb(PALETTE[n]) for n in names}
views = {"normal": {n: base[n] for n in names}}
for k in M:
    views[k] = {n: simulate(base[n], k) for n in names}

print("VSP chart palette (SI-10) — colour-vision-deficiency check")
print("Method: Machado et al. 2009 severity-1.0 simulation; CIEDE2000 in CIELAB (D65)\n")

print("Pairwise CIEDE2000 distance (lower = harder to tell apart)")
header = f"{'pair':34}" + "".join(f"{v:>14}" for v in views)
print(header)
print("-" * len(header))
rows = []
for a, b in itertools.combinations(names, 2):
    ds = {v: ciede2000(srgb_to_lab(views[v][a]), srgb_to_lab(views[v][b])) for v in views}
    rows.append((a, b, ds))
    print(f"{a + ' / ' + b:34}" + "".join(f"{ds[v]:>14.1f}" for v in views))

print("\nGreyscale (relative luminance, 0-1) — print / photocopy safety")
for n in names:
    print(f"  {n:16} {relative_luminance(base[n]):.3f}")
lums = sorted(relative_luminance(base[n]) for n in names)
print(f"  smallest gap between adjacent luminances: {min(np.diff(lums)):.3f}")

print("\nVerdict thresholds: <10 = risky for small marks; <5 = effectively the same colour")
worst = {}
for a, b, ds in rows:
    for v in views:
        if v == "normal":
            continue
        if ds[v] < 15:
            worst.setdefault(v, []).append((f"{a} / {b}", ds[v]))
for v, items in worst.items():
    print(f"\n  {v}: {len(items)} pair(s) under 15")
    for pair, d in sorted(items, key=lambda x: x[1]):
        flag = "EFFECTIVELY IDENTICAL" if d < 5 else ("RISKY" if d < 10 else "marginal")
        print(f"    {pair:34} dE00={d:5.1f}  {flag}")
if not worst:
    print("\n  No pair falls under 15 in any simulated view.")
