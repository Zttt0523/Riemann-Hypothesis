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
from matplotlib.colors import LinearSegmentedColormap

ASSETS_DIR = Path(__file__).resolve().parent.parent
MANIFEST = ASSETS_DIR / "manifest.sha256"
MANIFEST_KEY = Path(__file__).name


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
    """Logarithmic integral Li(x) = Ei(log x), for x > 1."""
    from scipy.special import expi as _expi

    with np.errstate(divide="ignore", invalid="ignore"):
        return _expi(np.log(np.where(x <= 1, np.nan, x)))


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
        total += 2.0 * term.real  # conjugate zeros make the contribution real
    total -= np.log(2 * np.pi)
    return total


def riemann_prime_count_approx(x: np.ndarray, n_zeros: int) -> np.ndarray:
    """A visual Riemann-von Mangoldt approximation to the prime-counting curve."""
    from scipy.special import expi as _expi

    x = np.asarray(x, dtype=np.float64)
    log_x = np.log(x)
    approx = li(x).astype(np.float64)
    for gamma in ZETA_ZEROS[: min(n_zeros, len(ZETA_ZEROS))]:
        rho = 0.5 + 1j * gamma
        approx -= 2.0 * np.real(_expi(rho * log_x))
    return approx


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


THEME = {
    "bg": "#070a12",
    "panel": "#0c1220",
    "panel_edge": "#263246",
    "grid": "#334155",
    "text": "#f2f6ff",
    "muted": "#9aa7b8",
    "blue": "#64b5ff",
    "cyan": "#7dd3fc",
    "coral": "#ff6b5f",
    "gold": "#ffd166",
    "violet": "#c084fc",
    "mint": "#7ee787",
}

PRIME_CMAP = LinearSegmentedColormap.from_list(
    "prime_harmonics",
    [THEME["blue"], THEME["violet"], THEME["coral"], THEME["gold"]],
)


def style_axis(ax, *, grid: bool = True) -> None:
    """Apply the shared dark mathematical-plate style."""
    ax.set_facecolor(THEME["panel"])
    ax.tick_params(colors=THEME["muted"], labelsize=9)
    ax.xaxis.label.set_color(THEME["muted"])
    ax.yaxis.label.set_color(THEME["muted"])
    ax.title.set_color(THEME["text"])
    for spine in ax.spines.values():
        spine.set_color(THEME["panel_edge"])
        spine.set_linewidth(0.8)
    if grid:
        ax.grid(True, color=THEME["grid"], alpha=0.22, linewidth=0.6)
    ax.set_axisbelow(True)


def glow_line(ax, x, y, *, color: str, lw: float = 1.6, alpha: float = 0.95, label=None):
    """Draw a crisp line with a restrained glow underneath."""
    for width, glow_alpha in ((7.5, 0.055), (4.2, 0.08)):
        ax.plot(x, y, color=color, lw=width, alpha=glow_alpha, solid_capstyle="round")
    return ax.plot(x, y, color=color, lw=lw, alpha=alpha, label=label, solid_capstyle="round")


def annotate_panel(ax, label: str, title: str, subtitle: str | None = None) -> None:
    """Place compact panel title text inside the axis to avoid layout collisions."""
    text_box = {"facecolor": THEME["panel"], "edgecolor": "none", "alpha": 0.82, "pad": 2.0}
    ax.text(
        0.018,
        0.985,
        label,
        transform=ax.transAxes,
        ha="left",
        va="top",
        color=THEME["gold"],
        fontsize=9,
        fontweight="bold",
        bbox=text_box,
        zorder=20,
    )
    ax.text(
        0.075,
        0.985,
        title,
        transform=ax.transAxes,
        ha="left",
        va="top",
        color=THEME["text"],
        fontsize=11,
        fontweight="bold",
        bbox=text_box,
        zorder=20,
    )
    if subtitle:
        ax.text(
            0.075,
            0.928,
            subtitle,
            transform=ax.transAxes,
            ha="left",
            va="top",
            color=THEME["muted"],
            fontsize=8.2,
            bbox=text_box,
            zorder=20,
        )


def normalized_zero_spacings(gammas: np.ndarray) -> np.ndarray:
    """Nearest-neighbor zero spacings normalized to mean 1."""
    spacings = np.diff(np.asarray(gammas, dtype=float))
    return spacings / spacings.mean()


def gue_nearest_neighbor_density(spacing: np.ndarray) -> np.ndarray:
    """GUE Wigner-Dyson nearest-neighbor spacing density."""
    s = np.asarray(spacing, dtype=float)
    return (32.0 / np.pi**2) * s**2 * np.exp((-4.0 / np.pi) * s**2)


def prime_spiral_points(limit: int) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Sacks-style prime spiral coordinates for all integers and primes."""
    numbers = np.arange(1, limit + 1)
    theta = np.sqrt(numbers) * 2.0 * np.pi
    radius = np.sqrt(numbers)
    x_all = radius * np.cos(theta)
    y_all = radius * np.sin(theta)
    primes = sieve_primes(limit)
    prime_idx = primes - 1
    return x_all, y_all, x_all[prime_idx], y_all[prime_idx], primes


# ── Main plot function ───────────────────────────────────────────

def plot_riemann_beauty(out_path: Path | None = None, dpi: int = 220) -> Path:
    """Generate the showcase figure: primes, zeros, and the critical line."""
    print("Computing prime data...")
    prime_limit = 110_000
    primes = sieve_primes(prime_limit)

    fig = plt.figure(figsize=(20, 13.5), facecolor=THEME["bg"])
    gs = fig.add_gridspec(
        2,
        6,
        left=0.055,
        right=0.97,
        bottom=0.075,
        top=0.835,
        wspace=0.34,
        hspace=0.43,
        height_ratios=[1.05, 0.95],
    )

    ax1 = fig.add_subplot(gs[0, 0:3])
    ax2 = fig.add_subplot(gs[0, 3:6])
    ax3 = fig.add_subplot(gs[1, 0:2])
    ax4 = fig.add_subplot(gs[1, 2:4])
    ax5 = fig.add_subplot(gs[1, 4:6])
    for ax in (ax1, ax2, ax3, ax4, ax5):
        style_axis(ax)

    # ── Panel A: Prime counting and the explicit formula ──
    x_fine = np.logspace(2, 5, 1_800)
    pi_vals = prime_count(x_fine, primes)
    li_vals = li(x_fine)

    glow_line(ax1, x_fine, pi_vals, color=THEME["blue"], lw=2.2, label=r"$\pi(x)$")
    ax1.plot(
        x_fine,
        li_vals,
        color=THEME["gold"],
        lw=1.7,
        ls=(0, (5, 3)),
        alpha=0.9,
        label=r"$\operatorname{Li}(x)$",
    )

    correction_colors = [THEME["violet"], THEME["cyan"], THEME["mint"]]
    for color, nz in zip(correction_colors, [8, 32, 96], strict=True):
        approx_pi = riemann_prime_count_approx(x_fine, nz)
        ax1.plot(x_fine, approx_pi, color=color, lw=1.05, alpha=0.7, label=f"{nz} zero echoes")

    ax1.set_xscale("log")
    ax1.set_xlim(x_fine[0], x_fine[-1])
    ax1.set_ylim(0, pi_vals[-1] * 1.08)
    ax1.set_xlabel(r"$x$")
    ax1.set_ylabel(r"count")
    annotate_panel(
        ax1,
        "A",
        "Primes Answer a Wave",
        r"$\pi(x)$ is pulled toward order by the first non-trivial zeros.",
    )
    ax1.legend(
        loc="upper left",
        bbox_to_anchor=(0.02, 0.84),
        fontsize=8.5,
        framealpha=0.28,
        facecolor=THEME["panel"],
        edgecolor=THEME["panel_edge"],
        labelcolor=THEME["text"],
    )

    residual_ax = ax1.inset_axes([0.55, 0.16, 0.40, 0.28])
    style_axis(residual_ax)
    residual_ax.set_facecolor("#080d18")
    residual = pi_vals - li_vals
    approx_residual = riemann_prime_count_approx(x_fine, 96) - li_vals
    residual_ax.plot(x_fine, residual, color=THEME["coral"], lw=0.9, alpha=0.95)
    residual_ax.plot(x_fine, approx_residual, color=THEME["mint"], lw=0.9, alpha=0.75)
    residual_ax.axhline(0, color=THEME["grid"], lw=0.7)
    residual_ax.set_xscale("log")
    residual_ax.set_title(r"$\pi(x)-\operatorname{Li}(x)$", color=THEME["muted"], fontsize=7.5, pad=4)
    residual_ax.tick_params(labelsize=6.8, pad=1)

    # ── Panel B: Hardy Z-function ──
    t_vals = np.linspace(6.5, 240, 4_800)
    z_vals = compute_Z(t_vals)
    glow_line(ax2, t_vals, z_vals, color=THEME["blue"], lw=1.2)
    ax2.fill_between(t_vals, 0, z_vals, where=z_vals >= 0, color=THEME["blue"], alpha=0.08)
    ax2.fill_between(t_vals, 0, z_vals, where=z_vals < 0, color=THEME["violet"], alpha=0.08)

    zero_mask = ZETA_ZEROS <= t_vals[-1]
    visible_zeros = ZETA_ZEROS[zero_mask]
    ax2.vlines(visible_zeros, -0.18, 0.18, color=THEME["coral"], lw=0.8, alpha=0.5)
    ax2.scatter(
        visible_zeros,
        np.zeros_like(visible_zeros),
        s=18,
        facecolors=THEME["panel"],
        edgecolors=THEME["coral"],
        linewidths=1.1,
        zorder=5,
    )
    ax2.axhline(0, color=THEME["panel_edge"], lw=0.9)
    ax2.set_xlim(t_vals[0], t_vals[-1])
    ax2.set_xlabel(r"height $t$ on $s=\frac{1}{2}+it$")
    ax2.set_ylabel(r"Hardy $Z(t)$")
    annotate_panel(
        ax2,
        "B",
        "The Critical-Line Music",
        "Each coral bead marks a sign change where ζ vanishes.",
    )

    # ── Panel C: Prime spiral ──
    ax3.set_aspect("equal")
    x_all, y_all, x_prime, y_prime, spiral_primes = prime_spiral_points(18_000)
    harmonic_color = np.sin(np.log(spiral_primes) * ZETA_ZEROS[0]) + np.cos(
        np.log(spiral_primes) * ZETA_ZEROS[1] / 2.0
    )
    ax3.scatter(x_all[::5], y_all[::5], s=0.18, color=THEME["grid"], alpha=0.45, rasterized=True)
    ax3.scatter(
        x_prime,
        y_prime,
        c=harmonic_color,
        cmap=PRIME_CMAP,
        s=3.4,
        alpha=0.92,
        linewidths=0,
        rasterized=True,
    )
    ax3.scatter([0], [0], s=28, color=THEME["gold"], alpha=0.95)
    ax3.set_xticks([])
    ax3.set_yticks([])
    annotate_panel(
        ax3,
        "C",
        "Prime Spiral Harmonics",
        "Irregular primes reveal diagonal and radial resonances.",
    )

    # ── Panel D: Zero spacings and random matrix rhythm ──
    spacings = normalized_zero_spacings(ZETA_ZEROS)
    spacing_grid = np.linspace(0, 3.4, 600)
    density = gue_nearest_neighbor_density(spacing_grid)
    ax4.hist(
        spacings,
        bins=np.linspace(0, 3.4, 34),
        density=True,
        color=THEME["blue"],
        alpha=0.48,
        edgecolor=THEME["cyan"],
        linewidth=0.35,
        label="unfolded ζ zeros",
    )
    glow_line(
        ax4,
        spacing_grid,
        density,
        color=THEME["gold"],
        lw=2.0,
        label="GUE Wigner-Dyson",
    )
    ax4.axvline(1.0, color=THEME["coral"], lw=1.0, ls=":", alpha=0.85)
    ax4.set_xlim(0, 3.4)
    ax4.set_ylim(0, max(density.max(), 1.0) * 1.22)
    ax4.set_xlabel("normalized nearest spacing")
    ax4.set_ylabel("density")
    annotate_panel(
        ax4,
        "D",
        "Random-Matrix Rhythm",
        "The zeros repel each other like eigenvalues.",
    )
    ax4.legend(
        loc="upper right",
        fontsize=8.2,
        framealpha=0.28,
        facecolor=THEME["panel"],
        edgecolor=THEME["panel_edge"],
        labelcolor=THEME["text"],
    )

    # ── Panel E: Critical strip and zero constellation ──
    ax5.axvspan(0, 1, color=THEME["blue"], alpha=0.055)
    ax5.axvline(0, color=THEME["panel_edge"], lw=0.9)
    ax5.axvline(1, color=THEME["panel_edge"], lw=0.9)
    ax5.axvline(0.5, color=THEME["gold"], lw=2.0, ls=(0, (6, 4)), alpha=0.9)
    ax5.axhline(0, color=THEME["panel_edge"], lw=0.9)

    positive = ZETA_ZEROS[:64]
    scaled = np.log1p(positive) / np.log1p(positive[-1]) * 3.05
    y_zeros = np.concatenate([-scaled[::-1], scaled])
    x_zeros = np.full_like(y_zeros, 0.5)
    sizes = np.linspace(13, 30, len(y_zeros))
    ax5.scatter(x_zeros, y_zeros, s=sizes * 3.0, color=THEME["coral"], alpha=0.08, linewidths=0)
    ax5.scatter(
        x_zeros,
        y_zeros,
        s=sizes,
        facecolors=THEME["panel"],
        edgecolors=THEME["coral"],
        linewidths=1.05,
        zorder=5,
    )
    for tx in [-2, -4]:
        ax5.scatter(tx, 0, s=42, marker="x", color=THEME["muted"], alpha=0.8, linewidths=1.5)
    ax5.text(0.53, 2.95, r"$\operatorname{Re}(s)=\frac{1}{2}$", color=THEME["gold"], fontsize=9)
    ax5.text(0.04, -3.18, "critical strip", color=THEME["muted"], fontsize=8)
    ax5.text(-4.25, 0.20, "trivial zeros", color=THEME["muted"], fontsize=8)
    ax5.set_xlim(-4.4, 1.45)
    ax5.set_ylim(-3.35, 3.35)
    ax5.set_xlabel(r"$\operatorname{Re}(s)$")
    ax5.set_ylabel(r"compressed $\operatorname{Im}(s)$")
    annotate_panel(
        ax5,
        "E",
        "The Critical Strip Constellation",
        "RH says every non-trivial zero lives on the golden meridian.",
    )

    # ── Global framing ──
    fig.text(
        0.5,
        0.965,
        "The Riemann Hypothesis",
        ha="center",
        va="top",
        color=THEME["text"],
        fontsize=30,
        fontweight="bold",
    )
    fig.text(
        0.5,
        0.926,
        "Primes become music when heard through the zeros of ζ(s)",
        ha="center",
        va="top",
        color=THEME["gold"],
        fontsize=14,
    )
    fig.text(
        0.5,
        0.895,
        "Explicit formula  ·  Hardy Z-function  ·  Prime spirals  ·  GUE spacing  ·  Critical line",
        ha="center",
        va="top",
        color=THEME["muted"],
        fontsize=10,
    )
    fig.text(
        0.5,
        0.028,
        "Riemann Hypothesis Encyclopedia  ·  generated from src/assets/scripts/plot_all.py",
        ha="center",
        va="bottom",
        color="#596275",
        fontsize=8,
        fontstyle="italic",
    )

    output = out_path or ASSETS_DIR / "images" / "plots" / "riemann-beauty.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=dpi, bbox_inches="tight", pad_inches=0.22, facecolor=fig.get_facecolor())
    plt.close(fig)
    print(f"Saved → {output}")
    return output


# ── CLI ───────────────────────────────────────────────────────────

def generate():
    """Regenerate all plots."""
    plots_dir = ASSETS_DIR / "images" / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    manifest = {}
    plot_riemann_beauty()
    manifest[MANIFEST_KEY] = compute_sha256(Path(__file__))

    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n")
    print(f"Manifest written → {MANIFEST}")


def check():
    """Check if generated assets are stale."""
    if not MANIFEST.exists():
        print("No manifest found. Run 'generate' first.")
        sys.exit(1)
    stored = json.loads(MANIFEST.read_text())
    script_hash = compute_sha256(Path(__file__))
    if stored.get(MANIFEST_KEY) != script_hash:
        print(f"  STALE: {MANIFEST_KEY} — re-run generate-assets")
        sys.exit(1)
    print("All assets up to date.")
    sys.exit(0)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        generate()
