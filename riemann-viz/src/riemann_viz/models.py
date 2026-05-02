from dataclasses import dataclass

import numpy as np
from numpy.typing import NDArray


@dataclass
class ZetaGridResult:
    sigma: NDArray[np.float64]
    t: NDArray[np.float64]
    zeta_re: NDArray[np.float64]
    zeta_im: NDArray[np.float64]


@dataclass(frozen=True)
class ZetaZero:
    index: int
    sigma: float
    t: float
