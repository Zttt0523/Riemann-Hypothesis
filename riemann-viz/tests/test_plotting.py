import tempfile
from pathlib import Path

from riemann_viz.config import ZetaVisualizationConfig
from riemann_viz.models import ZetaGridResult, ZetaZero
from riemann_viz.plotting.contour_plotter import plot_contour

import numpy as np


def _make_minimal_result() -> ZetaGridResult:
    sigma = np.linspace(-0.5, 1.5, 10)
    t = np.linspace(0.0, 5.0, 12)
    zeta_re = np.random.default_rng(42).standard_normal((12, 10))
    zeta_im = np.random.default_rng(43).standard_normal((12, 10))
    return ZetaGridResult(sigma=sigma, t=t, zeta_re=zeta_re, zeta_im=zeta_im)


def test_plot_contour_saves_file() -> None:
    result = _make_minimal_result()
    zeros = [ZetaZero(index=1, sigma=0.5, t=14.134)]
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "test_contour.png"
        config = ZetaVisualizationConfig(save=out)
        returned = plot_contour(result, zeros, config)
        assert returned == out
        assert out.exists()
        assert out.read_bytes()[:8] == b"\x89PNG\r\n\x1a\n"


def test_plot_contour_creates_parent_dirs() -> None:
    result = _make_minimal_result()
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "nested" / "dir" / "plot.png"
        config = ZetaVisualizationConfig(save=out)
        plot_contour(result, [], config)
        assert out.exists()
