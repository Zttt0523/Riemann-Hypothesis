#!/usr/bin/env python3
"""plot_all.py — regenerate (and optionally check) all visualization assets."""

import hashlib
import json
import sys
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parent.parent
MANIFEST = ASSETS_DIR / "manifest.sha256"


def compute_sha256(filepath: Path) -> str:
    return hashlib.sha256(filepath.read_bytes()).hexdigest()


def generate():
    """Placeholder: regenerate all plots. Add real plotting code here."""
    plots_dir = ASSETS_DIR / "images" / "plots"
    plots_dir.mkdir(parents=True, exist_ok=True)

    manifest = {}
    # Example: for each .py script in this directory, regenerate corresponding outputs
    for script in sorted(Path(__file__).parent.glob("*.py")):
        if script.name == Path(__file__).name:
            continue
        # Placeholder: run script, collect outputs
        manifest[script.name] = compute_sha256(script)

    MANIFEST.write_text(json.dumps(manifest, indent=2))
    print(f"Assets generated. Manifest written to {MANIFEST}")


def check():
    """Check if generated assets are stale relative to their source scripts."""
    if not MANIFEST.exists():
        print("No manifest found. Run 'generate' first.")
        sys.exit(1)

    stored = json.loads(MANIFEST.read_text())
    stale = []

    for script in sorted(Path(__file__).parent.glob("*.py")):
        if script.name == Path(__file__).name:
            continue
        current_hash = compute_sha256(script)
        stored_hash = stored.get(script.name)
        if stored_hash is None or stored_hash != current_hash:
            stale.append(script.name)
            print(f"  STALE: {script.name} — hash changed, re-run generate-assets")

    if stale:
        print(f"\n{len(stale)} stale asset(s) found.")
        sys.exit(1)
    else:
        print("All assets up to date.")
        sys.exit(0)


if __name__ == "__main__":
    if "--check" in sys.argv:
        check()
    else:
        generate()
