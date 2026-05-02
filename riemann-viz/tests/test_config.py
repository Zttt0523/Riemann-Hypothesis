import pytest

from riemann_viz.config import ZetaVisualizationConfig


def test_default_config() -> None:
    config = ZetaVisualizationConfig()
    assert config.sigma_min == -0.5
    assert config.sigma_max == 1.5
    assert config.t_min == 0.0
    assert config.t_max == 35.0
    assert config.nx == 180
    assert config.ny == 260
    assert config.mp_dps == 30
    assert config.num_zeros == 5
    assert config.save is None


def test_custom_config() -> None:
    config = ZetaVisualizationConfig(sigma_min=-1.0, t_max=50.0, nx=100)
    assert config.sigma_min == -1.0
    assert config.t_max == 50.0
    assert config.nx == 100


def test_invalid_sigma_range() -> None:
    with pytest.raises(ValueError, match="sigma_min must be less than sigma_max"):
        ZetaVisualizationConfig(sigma_min=2.0, sigma_max=1.0)


def test_invalid_t_range() -> None:
    with pytest.raises(ValueError, match="t_min must be less than t_max"):
        ZetaVisualizationConfig(t_min=50.0, t_max=10.0)


def test_invalid_nx() -> None:
    with pytest.raises(ValueError, match="nx must be at least 2"):
        ZetaVisualizationConfig(nx=1)


def test_invalid_ny() -> None:
    with pytest.raises(ValueError, match="ny must be at least 2"):
        ZetaVisualizationConfig(ny=1)


def test_invalid_mp_dps() -> None:
    with pytest.raises(ValueError, match="mp_dps must be at least 1"):
        ZetaVisualizationConfig(mp_dps=0)


def test_invalid_pole_epsilon() -> None:
    with pytest.raises(ValueError, match="pole_epsilon must be positive"):
        ZetaVisualizationConfig(pole_epsilon=0)


def test_invalid_num_zeros() -> None:
    with pytest.raises(ValueError, match="num_zeros must be non-negative"):
        ZetaVisualizationConfig(num_zeros=-1)
