import mpmath
import numpy as np
from numpy.typing import NDArray

from ..config import ZetaVisualizationConfig
from ..models import ZetaGridResult


def compute_zeta_grid(config: ZetaVisualizationConfig) -> ZetaGridResult:
    """Evaluate ζ(s) on a regular grid in the σ-t plane.

    The pole at s = 1 is skipped (left as NaN). Any evaluation point that
    raises a mpmath error is also left as NaN.  mpmath decimal precision
    is restored to its original value on exit.
    """
    mp = mpmath.mp
    original_dps = mp.dps
    mp.dps = config.mp_dps

    try:
        sigma = np.linspace(config.sigma_min, config.sigma_max, config.nx)
        t = np.linspace(config.t_min, config.t_max, config.ny)

        zeta_re: NDArray[np.float64] = np.full((config.ny, config.nx), np.nan)
        zeta_im: NDArray[np.float64] = np.full((config.ny, config.nx), np.nan)

        for i, ti in enumerate(t):
            for j, sj in enumerate(sigma):
                if abs(sj - 1.0) < config.pole_epsilon and abs(ti) < config.pole_epsilon:
                    continue  # skip pole at s=1
                try:
                    s = mpmath.mpc(sj, ti)
                    z = mpmath.zeta(s)
                    zeta_re[i, j] = float(z.real)
                    zeta_im[i, j] = float(z.imag)
                except (ValueError, ZeroDivisionError):
                    pass  # leave as nan

        return ZetaGridResult(sigma=sigma, t=t, zeta_re=zeta_re, zeta_im=zeta_im)
    finally:
        mp.dps = original_dps
