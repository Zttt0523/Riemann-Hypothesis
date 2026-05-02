from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ZetaVisualizationConfig:
    sigma_min: float = -0.5
    sigma_max: float = 1.5
    t_min: float = 0.0
    t_max: float = 35.0
    nx: int = 180
    ny: int = 260
    mp_dps: int = 30
    pole_epsilon: float = 1e-10
    num_zeros: int = 5
    save: Path | None = None

    def __post_init__(self) -> None:
        if self.sigma_min >= self.sigma_max:
            msg = "sigma_min must be less than sigma_max"
            raise ValueError(msg)
        if self.t_min >= self.t_max:
            msg = "t_min must be less than t_max"
            raise ValueError(msg)
        if self.nx < 2:
            msg = "nx must be at least 2"
            raise ValueError(msg)
        if self.ny < 2:
            msg = "ny must be at least 2"
            raise ValueError(msg)
        if self.mp_dps < 1:
            msg = "mp_dps must be at least 1"
            raise ValueError(msg)
        if self.pole_epsilon <= 0:
            msg = "pole_epsilon must be positive"
            raise ValueError(msg)
        if self.num_zeros < 0:
            msg = "num_zeros must be non-negative"
            raise ValueError(msg)
