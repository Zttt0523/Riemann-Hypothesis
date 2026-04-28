#!/usr/bin/env python3
"""Generate Gaussian primes visualization for the appendix."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent

# ── Gaussian integer utilities ────────────────────────────────────

def gaussian_norm(a, b):
    """N(a+bi) = a² + b²."""
    return a * a + b * b


def is_gaussian_prime(a, b):
    """Determine whether a+bi is a Gaussian prime.

    Rules:
    - If a=0, then bi is prime iff |b| is prime ≡ 3 mod 4
    - If b=0, then a is prime iff |a| is prime ≡ 3 mod 4
    - If a≠0, b≠0, then a+bi is prime iff N(a+bi) is a rational prime
    """
    if a == 0:
        p = abs(b)
        return p % 4 == 3 and _is_rational_prime(p)
    if b == 0:
        p = abs(a)
        return p % 4 == 3 and _is_rational_prime(p)
    n = gaussian_norm(a, b)
    return _is_rational_prime(n)


def _is_rational_prime(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def gaussian_primes(radius):
    """Return all Gaussian primes within a given radius from origin."""
    pts = []
    for a in range(-radius, radius + 1):
        for b in range(-radius, radius + 1):
            if a == 0 and b == 0:
                continue
            if is_gaussian_prime(a, b):
                pts.append((a, b))
    return pts


# ── Plot ──────────────────────────────────────────────────────────

def generate():
    radius = 30
    pts = gaussian_primes(radius)
    xs = [a for a, _ in pts]
    ys = [b for _, b in pts]

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor("#070a12")
    fig.patch.set_facecolor("#070a12")

    # Gaussian integer grid (light)
    for a in range(-radius, radius + 1):
        ax.axvline(a, color="#334155", lw=0.3, alpha=0.4)
    for b in range(-radius, radius + 1):
        ax.axhline(b, color="#334155", lw=0.3, alpha=0.4)

    # Unit circle
    theta = np.linspace(0, 2*np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), color="#9aa7b8", lw=0.5, alpha=0.3)

    # Gaussian primes
    ax.scatter(xs, ys, s=18, color="#ff6b5f", alpha=0.92, edgecolors="none", zorder=5)

    # Mark 5 = (2+i)(2-i) explicitly
    for pt in [(2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
        ax.scatter(pt[0], pt[1], s=50, color="#ffd166", edgecolors="#ff6b5f", lw=1.2, zorder=6)

    # Mark 3 (inert) on axes
    ax.scatter(3, 0, s=70, color="#64b5ff", edgecolors="white", lw=1.2, zorder=7)
    ax.scatter(-3, 0, s=70, color="#64b5ff", edgecolors="white", lw=1.2, zorder=7)

    # Annotations
    ax.annotate("$3$ (inert)\n$3\\equiv 3\\ (\\mathrm{mod}\\ 4)$", (3, 0), (8, 8),
                color="#64b5ff", fontsize=10, arrowprops=dict(arrowstyle="->", color="#64b5ff", lw=0.8))

    ax.annotate("$(2+i)$", (2, 1), (8, 5), color="#ffd166", fontsize=10,
                arrowprops=dict(arrowstyle="->", color="#ffd166", lw=0.8))
    ax.annotate("$(2-i)$", (2, -1), (8, -4), color="#ffd166", fontsize=10,
                arrowprops=dict(arrowstyle="->", color="#ffd166", lw=0.8))

    ax.annotate("$5 = (2+i)(2-i)$\n(split)  $5\\equiv 1\\ (\\mathrm{mod}\\ 4)$",
                (-22, 18), (-8, 24), color="#ffd166", fontsize=11,
                bbox=dict(facecolor="#0c1220", edgecolor="#ffd166", alpha=0.85, pad=4),
                ha="center")

    ax.annotate("$2 = -i(1+i)^2$\n(ramified)", (-21, -21), (-21, -27),
                color="#c084fc", fontsize=10,
                bbox=dict(facecolor="#0c1220", edgecolor="#c084fc", alpha=0.7, pad=3),
                ha="center")

    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_aspect("equal")
    ax.set_xticks([-20, -10, 0, 10, 20])
    ax.set_yticks([-20, -10, 0, 10, 20])
    ax.tick_params(colors="#9aa7b8", labelsize=9)
    ax.set_xlabel("Re (real axis)", color="#9aa7b8", fontsize=11)
    ax.set_ylabel("Im (imaginary axis)", color="#9aa7b8", fontsize=11)
    ax.set_title("Gaussian Primes in the Complex Plane  $\mathbb{Z}[i]$\n"
                 "Split  ·  Inert  ·  Ramified",
                 color="#f2f6ff", fontsize=15, fontweight="bold", pad=14)

    for spine in ax.spines.values():
        spine.set_color("#263246")
        spine.set_linewidth(0.8)

    out = ASSETS_DIR / "images" / "plots" / "gaussian-primes.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved → {out}")


if __name__ == "__main__":
    generate()
