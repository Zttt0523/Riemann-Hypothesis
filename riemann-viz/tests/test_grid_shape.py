from riemann_viz.compute.zeta_grid import compute_zeta_grid
from riemann_viz.config import ZetaVisualizationConfig


def test_grid_shape() -> None:
    config = ZetaVisualizationConfig(nx=10, ny=12, mp_dps=15)
    result = compute_zeta_grid(config)
    assert result.zeta_re.shape == (12, 10)
    assert result.zeta_im.shape == (12, 10)
    assert result.sigma.shape == (10,)
    assert result.t.shape == (12,)
