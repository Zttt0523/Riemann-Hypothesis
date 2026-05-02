# riemann-viz

Professional visualization toolkit for the Riemann zeta function ζ(s). Generates contour plots showing where the real and imaginary parts of ζ(s) vanish in the critical strip, overlaid with the critical line Re(s) = 1/2 and non-trivial zeros.

## Installation

This project lives inside the `Riemann-Hypothesis` monorepo and uses a shared [uv](https://docs.astral.sh/uv/) workspace.

```bash
cd Riemann-Hypothesis
uv sync --package riemann-viz
```

## CLI Usage

```bash
riemann-viz contour \
  --sigma-min -0.5 \
  --sigma-max 1.5 \
  --t-min 0 \
  --t-max 35 \
  --nx 180 \
  --ny 260 \
  --mp-dps 30 \
  --num-zeros 5 \
  --save outputs/zeta_contour.png
```

All flags are optional and default to the values shown above.

## Python API

```python
from pathlib import Path

from riemann_viz.app import run_contour
from riemann_viz.config import ZetaVisualizationConfig

config = ZetaVisualizationConfig(
    sigma_min=-0.5,
    sigma_max=1.5,
    t_min=0,
    t_max=35,
    nx=180,
    ny=260,
    mp_dps=30,
    num_zeros=5,
    save=Path("my_contour.png"),
)

output = run_contour(config)
print(f"Saved to {output}")
```

You can also call the layers individually:

```python
from riemann_viz.compute.zeta_grid import compute_zeta_grid
from riemann_viz.compute.zeros import find_zeros
from riemann_viz.plotting.contour_plotter import plot_contour

config = ZetaVisualizationConfig()
grid = compute_zeta_grid(config)      # ZetaGridResult
zeros = find_zeros(config)             # list[ZetaZero]
plot_contour(grid, zeros, config)      # saves PNG
```

## Mathematical Notes

The Riemann zeta function is defined by the Dirichlet series

$$\zeta(s) = \sum_{n=1}^{\infty} n^{-s}, \quad \operatorname{Re}(s) > 1.$$

This series diverges outside the half-plane Re(s) > 1. However, ζ admits a unique **analytic continuation** to the entire complex plane (minus a simple pole at s = 1). The `mpmath.zeta` function implements this continuation, so `riemann-viz` can evaluate ζ at any point in the critical strip 0 < Re(s) < 1 and beyond.

**Pole at s = 1.** The point s = 1 is a simple pole where ζ(s) → ∞. Grid evaluation automatically skips this point and leaves it as NaN in the output arrays. The skip tolerance is controlled by the `pole_epsilon` config parameter (default: 10⁻¹⁰).

## Development

```bash
# Run linter
uv run --package riemann-viz ruff check riemann-viz/src riemann-viz/tests

# Run tests
uv run --package riemann-viz pytest riemann-viz/tests/ -v
```
