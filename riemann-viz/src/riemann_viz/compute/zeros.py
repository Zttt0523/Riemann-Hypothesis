import mpmath

from ..config import ZetaVisualizationConfig
from ..models import ZetaZero


def find_zeros(config: ZetaVisualizationConfig) -> list[ZetaZero]:
    """Return non-trivial zeros of ζ whose imaginary parts lie in [t_min, t_max].

    Returns up to ``config.num_zeros`` zeros.  May return fewer if the
    t-range does not contain enough zeros.  mpmath decimal precision is
    restored to its original value on exit.
    """
    mp = mpmath.mp
    original_dps = mp.dps
    mp.dps = config.mp_dps

    try:
        zeros: list[ZetaZero] = []
        k = 1
        while len(zeros) < config.num_zeros:
            root = mpmath.zetazero(k)
            sigma = float(root.real)
            t = float(root.imag)
            if t > config.t_max:
                break
            if config.t_min <= t <= config.t_max:
                zeros.append(ZetaZero(index=k, sigma=sigma, t=t))
            k += 1
        return zeros
    finally:
        mp.dps = original_dps
