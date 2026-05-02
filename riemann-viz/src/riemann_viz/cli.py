from pathlib import Path

import typer

from .app import run_contour
from .config import ZetaVisualizationConfig

app = typer.Typer(help="Riemann zeta function visualization toolkit.")


@app.callback()
def _main() -> None:
    """Riemann zeta function visualization toolkit."""


@app.command()
def contour(
    sigma_min: float = typer.Option(-0.5, help="Minimum σ value"),
    sigma_max: float = typer.Option(1.5, help="Maximum σ value"),
    t_min: float = typer.Option(0.0, help="Minimum t value"),
    t_max: float = typer.Option(35.0, help="Maximum t value"),
    nx: int = typer.Option(180, help="Grid resolution in σ direction"),
    ny: int = typer.Option(260, help="Grid resolution in t direction"),
    mp_dps: int = typer.Option(30, help="mpmath decimal precision"),
    num_zeros: int = typer.Option(5, help="Number of non-trivial zeros to mark"),
    save: Path | None = typer.Option(None, help="Output file path"),
) -> None:
    config = ZetaVisualizationConfig(
        sigma_min=sigma_min,
        sigma_max=sigma_max,
        t_min=t_min,
        t_max=t_max,
        nx=nx,
        ny=ny,
        mp_dps=mp_dps,
        num_zeros=num_zeros,
        save=save,
    )
    output = run_contour(config)
    typer.echo(f"Saved contour plot to {output}")
