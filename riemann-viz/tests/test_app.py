import tempfile
from pathlib import Path

from riemann_viz.app import run_contour
from riemann_viz.config import ZetaVisualizationConfig


def test_run_contour_saves_file() -> None:
    config = ZetaVisualizationConfig(nx=8, ny=10, mp_dps=15, num_zeros=1)
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "app_test.png"
        config = ZetaVisualizationConfig(
            nx=8, ny=10, mp_dps=15, num_zeros=1, save=out,
        )
        result = run_contour(config)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 0
