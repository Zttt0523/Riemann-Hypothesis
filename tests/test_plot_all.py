import importlib.util
import tempfile
import unittest
from pathlib import Path

import numpy as np


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "src" / "assets" / "scripts" / "plot_all.py"

spec = importlib.util.spec_from_file_location("plot_all", SCRIPT_PATH)
plot_all = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(plot_all)


class PlotAllTests(unittest.TestCase):
    def test_gue_nearest_neighbor_density_is_normalized(self):
        spacing = np.linspace(0.0, 5.0, 2_000)

        density = plot_all.gue_nearest_neighbor_density(spacing)

        self.assertAlmostEqual(float(np.trapezoid(density, spacing)), 1.0, places=3)
        self.assertEqual(float(density[0]), 0.0)
        self.assertGreater(float(density.max()), 0.8)

    def test_riemann_prime_count_approx_tracks_logarithmic_integral_scale(self):
        x_values = np.logspace(2, 4, 200)

        approx = plot_all.riemann_prime_count_approx(x_values, 12)

        self.assertEqual(approx.shape, x_values.shape)
        self.assertTrue(np.isfinite(approx).all())
        self.assertLess(abs(float(approx[-1] - plot_all.li(x_values)[-1])), 500.0)

    def test_plot_can_render_to_custom_png_path(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            out_path = Path(tmp_dir) / "riemann-beauty.png"

            result = plot_all.plot_riemann_beauty(out_path=out_path, dpi=72)

            self.assertEqual(result, out_path)
            self.assertTrue(out_path.exists())
            self.assertEqual(out_path.read_bytes()[:8], b"\x89PNG\r\n\x1a\n")
            self.assertEqual(len(plot_all.compute_sha256(out_path)), 64)


if __name__ == "__main__":
    unittest.main()
