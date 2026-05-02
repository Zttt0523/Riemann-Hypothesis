from pathlib import Path

from .compute.zeros import find_zeros
from .compute.zeta_grid import compute_zeta_grid
from .config import ZetaVisualizationConfig
from .plotting.contour_plotter import plot_contour


def run_contour(config: ZetaVisualizationConfig | None = None) -> Path:
    """End-to-end: compute grid, find zeros, render contour plot, return output path."""
    config = config or ZetaVisualizationConfig()
    result = compute_zeta_grid(config)
    zeros = find_zeros(config)
    output = plot_contour(result, zeros, config)
    return output
