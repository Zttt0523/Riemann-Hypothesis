import tempfile
from pathlib import Path

from typer.testing import CliRunner

from riemann_viz.cli import app

runner = CliRunner()


def test_contour_command_saves_file() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "cli_test.png"
        result = runner.invoke(app, [
            "contour",
            "--nx", "8",
            "--ny", "10",
            "--mp-dps", "15",
            "--num-zeros", "1",
            "--save", str(out),
        ])
        assert result.exit_code == 0
        assert out.exists()
        assert f"Saved contour plot to {out}" in result.output


def test_contour_command_help() -> None:
    result = runner.invoke(app, ["contour", "--help"])
    assert result.exit_code == 0
    assert "--sigma-min" in result.output
    assert "--num-zeros" in result.output
