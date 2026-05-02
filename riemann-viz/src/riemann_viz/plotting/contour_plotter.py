from pathlib import Path

import matplotlib.pyplot as plt

from ..config import ZetaVisualizationConfig
from ..models import ZetaGridResult
from ..models import ZetaZero


def plot_contour(
    result: ZetaGridResult,
    zeros: list[ZetaZero],
    config: ZetaVisualizationConfig,
) -> Path:
    """Render Re ζ = 0 and Im ζ = 0 contour lines, the critical line, and zero markers.

    Returns the path to the saved PNG file.
    """
    fig, ax = plt.subplots(figsize=(8, 10))

    ax.contour(
        result.sigma, result.t, result.zeta_re,
        levels=[0], colors="blue", linewidths=0.8,
    )
    ax.contour(
        result.sigma, result.t, result.zeta_im,
        levels=[0], colors="red", linewidths=0.8,
    )

    ax.axvline(
        x=0.5, color="gold", linestyle="--", linewidth=1.5,
        label=r"$\operatorname{Re}(s)=\frac{1}{2}$",
    )

    for z in zeros:
        ax.plot(0.5, z.t, "ko", markersize=4)

    ax.set_xlabel(r"$\sigma$")
    ax.set_ylabel(r"$t$")
    ax.set_title(
        r"$\zeta(s)$ contour lines: "
        r"$\operatorname{Re}\,\zeta=0$ (blue), "
        r"$\operatorname{Im}\,\zeta=0$ (red)",
    )
    ax.legend()

    output = config.save or Path("outputs/zeta_contour.png")
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=150, bbox_inches="tight")
    plt.close(fig)

    return output
