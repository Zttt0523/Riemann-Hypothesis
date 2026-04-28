#!/usr/bin/env python3
"""plot_all.py — generate Riemann Hypothesis visualization assets."""

import hashlib
import json
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import ScalarFormatter

ASSETS_DIR = Path(__file__).resolve().parent.parent
MANIFEST = ASSETS_DIR / "manifest.sha256"


def compute_sha256(filepath: Path) -> str:
    return hashlib.sha256(filepath.read_bytes()).hexdigest()


# ── mathematical helpers ──────────────────────────────────────────

def sieve_primes(limit: int) -> np.ndarray:
    """Sieve of Eratosthenes up to `limit`."""
    is_prime = np.ones(limit + 1, dtype=bool)
    is_prime[:2] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            is_prime[p * p : limit + 1 : p] = False
    return np.flatnonzero(is_prime)


def li(x: np.ndarray) -> np.ndarray:
    """Logarithmic integral Li(x), computed via scipy if available else trapezoidal."""
    from scipy.special import exp1 as _exp1
    # li(x) = Ei(ln x)   for x > 0, x != 1
    # Use -exp1(-ln x + i0) trick — works for real x > 1
    with np.errstate(divide="ignore", invalid="ignore"):
        out = -_exp1(-np.log(np.where(x <= 1, np.nan, x)))
    return out


def prime_count(x_vals, primes):
    """π(x) for array x_vals using binary search on primes."""
    return np.searchsorted(primes, x_vals, side="right")


# known first ~100 non-trivial zeta zeros (imaginary parts)
ZETA_ZEROS = np.array([
    14.134725, 21.022040, 25.010857, 30.424876, 32.935062,
    37.586178, 40.918719, 43.327073, 48.005151, 49.773832,
    52.970321, 56.446248, 59.347044, 60.831779, 65.112544,
    67.079811, 69.546402, 72.067158, 75.704691, 77.144840,
    79.337375, 82.910381, 84.735493, 87.425275, 88.809111,
    92.491899, 94.651344, 95.870634, 98.831194, 101.317851,
    103.725538, 105.446623, 107.168611, 111.029535, 111.874659,
    114.320221, 116.226680, 118.790783, 121.370125, 122.946829,
    124.256819, 127.516684, 129.578704, 131.087689, 133.497737,
    134.756510, 138.116042, 139.736209, 141.123707, 143.111846,
    146.000982, 147.422765, 150.053520, 150.925258, 153.024694,
    156.112909, 157.597591, 158.849988, 161.188964, 163.030710,
    165.537069, 167.184440, 169.094515, 169.911976, 173.411537,
    174.754191, 176.441434, 178.377408, 179.916484, 182.207078,
    184.874468, 185.598784, 187.228923, 189.416159, 192.026656,
    193.079727, 195.265397, 196.876482, 198.015310, 201.264752,
    202.493594, 204.189672, 205.394697, 207.906258, 209.576510,
    211.690863, 213.347919, 214.547045, 216.169539, 219.067596,
    220.714919, 221.430706, 224.007000, 224.983325, 227.421444,
    229.337413, 231.250189, 231.987235, 233.693404, 236.524230,
    237.769820, 239.555437, 241.049160, 242.823271,
])


def riemann_explicit_formula(x: np.ndarray, n_zeros: int) -> np.ndarray:
    """Riemann explicit formula approximation: ψ₀(x) ≈ x - Σ_{|γ|≤T} x^ρ/ρ - ln(2π)."""
    total = x.astype(np.float64).copy()
    for k in range(min(n_zeros, len(ZETA_ZEROS))):
        gamma = ZETA_ZEROS[k]
        rho = 0.5 + 1j * gamma
        term = -(x ** rho) / rho
        total += term.real  # zeros come in conjugate pairs — the sum is real
    total -= np.log(2 * np.pi)
    return total


def hardy_Z_scalar(t: float) -> float:
    """Hardy Z(t) from the Riemann-Siegel main sum (first approximation)."""
    if t < 1:
        return np.nan
    m = int(np.sqrt(t / (2 * np.pi)))
    theta = (t / 2.0) * np.log(t / (2 * np.pi)) - t / 2.0 - np.pi / 8.0
    s = 0.0
    for n in range(1, m + 1):
        s += np.cos(theta - t * np.log(n)) / np.sqrt(n)
    return 2.0 * s


def compute_Z(t_vals: np.ndarray) -> np.ndarray:
    """Vectorized Hardy Z(t)."""
    return np.array([hardy_Z_scalar(t) for t in t_vals])


# ── Main plot function ───────────────────────────────────────────

def plot_riemann_beauty():
    """Generate the showcase figure: primes, zeros, and the critical line."""
    print("Computing prime data...")
    primes = sieve_primes(50_000)

    fig = plt.figure(figsize=(18, 12))
    fig.patch.set_facecolor("#0d1117")

    # ── Panel A: Prime counting function with Riemann corrections ──
    ax1 = fig.add_axes([0.06, 0.55, 0.42, 0.40])
    ax1.set_facecolor("#0d1117")

    x_fine = np.logspace(2, 4.7, 2000)
    pi_vals = np.array([prime_count(np.array([x]), primes)[0] for x in x_fine])
    ax1.plot(x_fine, pi_vals, color="#58a6ff", lw=2.2, alpha=0.95, label=r"$\pi(x)$")

    li_vals = li(x_fine)
    ax1.plot(x_fine, li_vals, color="#f0883e", lw=1.8, ls="--", label=r"$\operatorname{Li}(x)$")

    colors = ["#d2a8ff", "#a5d6ff", "#79c0ff", "#56d364"]
    for idx, nz in enumerate([5, 20, 50, 100]):
        approx = riemann_explicit_formula(x_fine, nz)
        approx_pi = approx / np.log(x_fine) if np.all(x_fine > 1) else approx
        approx_pi = approx / np.log(x_fine)
        ax1.plot(x_fine, approx_pi, color=colors[idx], lw=1.0, alpha=0.8,
                 label=f"RH explicit ({nz} zeros)")

    ax1.set_xscale("log")
    ax1.legend(loc="upper left", fontsize=9, framealpha=0.3,
               facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")
    ax1.set_title("A. The Prime Counting Function  π(x)  and Riemannʼs Explicit Formula",
                  color="#e6edf3", fontsize=13, fontweight="bold", pad=12)
    ax1.tick_params(colors="#8b949e")
    ax1.grid(True, alpha=0.12, color="#8b949e")
    for spine in ax1.spines.values():
        spine.set_color("#30363d")

    # ── Panel B: Hardy Z-function — the music of the zeros ──
    ax2 = fig.add_axes([0.55, 0.55, 0.42, 0.40])
    ax2.set_facecolor("#0d1117")

    t_vals = np.linspace(1, 220, 4000)
    Z_vals = compute_Z(t_vals)

    ax2.plot(t_vals, Z_vals, color="#58a6ff", lw=1.0, alpha=0.85)
    ax2.fill_between(t_vals, 0, Z_vals, color="#58a6ff", alpha=0.06)

    # Mark known zeros on the x-axis
    zero_mask = ZETA_ZEROS <= 220
    ax2.scatter(ZETA_ZEROS[zero_mask], np.zeros(sum(zero_mask)),
                color="#f85149", s=12, zorder=5, marker="o", facecolors="none", lw=1.2)

    ax2.axhline(0, color="#30363d", lw=1.0, alpha=0.5)
    ax2.set_title("B. The Hardy  Z(t)  Function — Zeros as Sign Changes on the Critical Line",
                  color="#e6edf3", fontsize=13, fontweight="bold", pad=12)
    ax2.set_xlabel(r"$t$", color="#8b949e", fontsize=11)
    ax2.tick_params(colors="#8b949e")
    ax2.grid(True, alpha=0.12, color="#8b949e")
    for spine in ax2.spines.values():
        spine.set_color("#30363d")

    # ── Panel C: Prime spiral (Sacks spiral variant) ──
    ax3 = fig.add_axes([0.06, 0.06, 0.28, 0.38])
    ax3.set_facecolor("#0d1117")
    ax3.set_aspect("equal")

    n_max = 12_000
    primes_arr = sieve_primes(n_max)
    prime_set = set(primes_arr.tolist())
    theta_vals = np.sqrt(np.arange(1, n_max + 1)) * 2 * np.pi
    r = np.sqrt(np.arange(1, n_max + 1))
    xs_all = r * np.cos(theta_vals)
    ys_all = r * np.sin(theta_vals)

    ax3.scatter(xs_all[::6], ys_all[::6], s=0.15, color="#30363d", alpha=0.6, rasterized=True)
    for p in primes_arr:
        ax3.scatter(xs_all[p - 1], ys_all[p - 1], s=2.0, color="#f85149", alpha=0.9, rasterized=True)

    ax3.set_title("C. Prime Spiral\n(Sacks / Ulam variant)",
                  color="#e6edf3", fontsize=12, fontweight="bold", pad=10)
    ax3.tick_params(colors="#8b949e")
    for spine in ax3.spines.values():
        spine.set_color("#30363d")

    # ── Panel D: Pair correlation of ζ zeros (Montgomery–Dyson) ──
    ax4 = fig.add_axes([0.38, 0.06, 0.28, 0.38])
    ax4.set_facecolor("#0d1117")

    alpha = np.linspace(1e-10, 3.5, 500)
    sinc = np.sin(np.pi * alpha) / (np.pi * alpha)
    r2_gue = 1.0 - sinc ** 2

    # Use known zeros to compute empirical pair correlation
    gammas = ZETA_ZEROS[:95]  # first 95 zeros
    # Normalize by average density
    N = len(gammas)
    avg_spacing = (gammas[-1] - gammas[0]) / N
    diffs = np.diff(gammas) / avg_spacing

    ax4.hist(diffs, bins=60, density=True, color="#58a6ff", alpha=0.55,
             edgecolor="#58a6ff", linewidth=0.3, label="ζ zeros (empirical, 95 zeros)")

    ax4.plot(alpha, r2_gue, color="#f0883e", lw=2.0, label="GUE prediction  $R_2(\\alpha)$")

    ax4.set_xlim(0, 3.5)
    ax4.set_ylim(0, 1.25)
    ax4.legend(loc="upper right", fontsize=8.5, framealpha=0.3,
               facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")
    ax4.set_title("D. Montgomery Pair Correlation\nζ zeros match GUE Random Matrix",
                  color="#e6edf3", fontsize=12, fontweight="bold", pad=10)
    ax4.set_xlabel("Normalized spacing  α", color="#8b949e", fontsize=10)
    ax4.tick_params(colors="#8b949e")
    ax4.grid(True, alpha=0.12, color="#8b949e")
    for spine in ax4.spines.values():
        spine.set_color("#30363d")

    # ── Panel E: The critical line — zeros and symmetry ──
    ax5 = fig.add_axes([0.70, 0.06, 0.27, 0.38])
    ax5.set_facecolor("#0d1117")

    t_mesh = np.linspace(-2.5, 2.5, 400)
    s_mesh = np.linspace(-2.5, 2.5, 400)
    T, S = np.meshgrid(t_mesh, s_mesh)
    R = T + 1j * S

    # Approximate log|zeta| via first few terms of Dirichlet series (rough but suggestive)
    approx_val = np.zeros_like(R, dtype=np.float64)
    s0 = 0.5 + 1j * T  # evaluate on vertical strip

    for n in range(1, 30):
        approx_val += (1.0 / (n ** 0.5)) * np.cos(S * np.log(n)) / np.sqrt(
            (T - 0.5)**2 + (S)**2 + 1e-6
        )

    # Simpler: draw the landscape conceptually
    # Show zeros as bright points on the critical line
    ax5.fill_between([-2.5, 2.5], -2.5, 2.5, color="#0d1117")
    ax5.axhline(0, color="#30363d", lw=0.8)
    ax5.axvline(0.5, color="#f0883e", lw=2.0, ls="--", alpha=0.7,
                label=r"Critical line  $\operatorname{Re}(s)=\frac{1}{2}$")

    # Plot first 30 zeros on the critical line
    for k in range(min(30, len(ZETA_ZEROS))):
        gamma = ZETA_ZEROS[k] / 8.0  # scale down for display
        if gamma > 2.5:
            break
        ax5.scatter(0.5, gamma, color="#f85149", s=25, zorder=5, marker="o",
                    facecolors="none", lw=1.5)
        ax5.scatter(0.5, -gamma, color="#f85149", s=25, zorder=5, marker="o",
                    facecolors="none", lw=1.5)

    # Mark trivial zeros on negative real axis
    trivial_positions = [-2, -4]
    for tx in trivial_positions:
        ax5.scatter(tx, 0, color="#8b949e", s=20, marker="x", alpha=0.6)

    ax5.set_xlim(-2.5, 2.5)
    ax5.set_ylim(-2.5, 2.5)
    ax5.legend(loc="upper left", fontsize=8, framealpha=0.3,
               facecolor="#161b22", edgecolor="#30363d", labelcolor="#c9d1d9")
    ax5.set_title("E. The Zeros of  ζ(s)\nTrivial & Non-Trivial",
                  color="#e6edf3", fontsize=12, fontweight="bold", pad=10)
    ax5.set_xlabel("Re(s)", color="#8b949e", fontsize=10)
    ax5.set_ylabel("Im(s)  (scaled ×1/8)", color="#8b949e", fontsize=10)
    ax5.tick_params(colors="#8b949e")
    for spine in ax5.spines.values():
        spine.set_color("#30363d")

    # ── Global title ──
    fig.suptitle(
        "The Riemann Hypothesis  —  Primes, Zeros, and the Critical Line",
        color="#e6edf3", fontsize=18, fontweight="bold", y=0.98,
    )

    # Subtitle
    fig.text(0.5, 0.935,
             "Panel A–B: The explicit formula links primes to ζ zeros.  Panel C: Primes naturally form spiral patterns.  "
             "Panel D: Zero spacings follow GUE random matrix statistics (Montgomery–Dyson).  Panel E: All non‑trivial zeros lie on Re(s)=1/2.",
             ha="center", va="top", color="#8b949e", fontsize=9.5)

    # Footer
    fig.text(0.5, 0.005, "Riemann Hypothesis Encyclopedia  ·  https://github.com/<org>/riemann-hypothesis",
             ha="center", va="bottom", color="#484f58", fontsize=8, fontstyle="italic")

    out_path = ASSETS_DIR / "images" / "plots" / "riemann-beauty.png"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=200, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved → {out_path}")
    return out_path


# ── CLI ───────────────────────────────────────────────────────────

def generate():
    """Regenerate all plots."""
    plots_dir = ASSETS_DIR / "images" / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    manifest = {}
    out = plot_riemann_beauty()
    manifest["plot_riemann_beauty.py"] = compute_sha256(Path(__file__))

    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"Manifest written → {MANIFEST}")


def check():
    """Check if generated assets are stale."""
    if not MANIFEST.exists():
        print("No manifest found. Run 'generate' first.")
        sys.exit(1)
    stored = json.loads(MANIFEST.read_text())
    script_hash = compute_sha256(Path(__file__))
    if stored.get("plot_riemann_beauty.py") != script_hash:
        print("  STALE: plot_riemann_beauty.py — re-run generate-assets")
        sys.exit(1)
    print("All assets up to date.")
    sys.exit(0)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        generate()
