from riemann_viz.compute.zeros import find_zeros
from riemann_viz.config import ZetaVisualizationConfig


def test_first_zero() -> None:
    config = ZetaVisualizationConfig(num_zeros=1, mp_dps=30)
    zeros = find_zeros(config)
    assert len(zeros) == 1
    assert abs(zeros[0].t - 14.134725) < 1e-4
    assert zeros[0].index == 1
    assert abs(zeros[0].sigma - 0.5) < 1e-6


def test_multiple_zeros() -> None:
    config = ZetaVisualizationConfig(num_zeros=3, mp_dps=30)
    zeros = find_zeros(config)
    assert len(zeros) == 3
    assert zeros[0].t < zeros[1].t < zeros[2].t


def test_zeros_filtered_by_t_range() -> None:
    config = ZetaVisualizationConfig(t_min=20.0, t_max=25.0, num_zeros=10, mp_dps=30)
    zeros = find_zeros(config)
    for z in zeros:
        assert config.t_min <= z.t <= config.t_max
