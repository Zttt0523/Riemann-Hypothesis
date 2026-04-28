# 黎曼猜想百科全书 / Riemann Hypothesis Encyclopedia

A systematic, bilingual (Chinese + English) encyclopedia-level introduction to the Riemann Hypothesis, spanning from elementary mathematics to advanced research topics. Built with [mdBook](https://github.com/rust-lang/mdBook).

## Reading Paths

| Path | For | Chapters | Description |
|------|-----|----------|-------------|
| 🟢 Green | All readers | 11 | Biography, prime number stories, overview, philosophy. Minimal formulas. |
| 🟡 Blue | STEM undergraduates | 22 | Core mathematics: complex analysis → analytic number theory → ζ function → RH |
| 🔴 Red | Graduate / researchers | 32 | Full text including advanced topics and recent developments |

## Setup

### Prerequisites

- [Rust toolchain](https://rustup.rs/) (for mdBook and mdbook-katex)
- Python 3.12+ (for asset generation and validation)

### Install

```bash
cargo install mdbook --version "=0.4.40" --locked
cargo install mdbook-katex --version "=0.9.1" --locked
pip install "matplotlib>=3.8" "numpy>=1.26"
```

### Build

```bash
make build       # Build both Chinese and English
make serve-zh    # Serve Chinese version locally
make serve-en    # Serve English version locally
```

### Validate

```bash
make check              # Run all checks
make check-frontmatter  # Validate chapter frontmatter
make check-links        # Check internal links
make check-assets       # Check asset freshness
```

## Project Structure

```
src/
├── zh/                  # Chinese content (SUMMARY.md + 32 chapters)
├── en/                  # English content (mirrors zh/)
├── assets/              # Shared images, data, scripts
├── macros.tex            # KaTeX global macros
├── references.bib        # Shared BibTeX bibliography
└── index.html            # Language selector landing page
```

## Known Limitations (v1)

- Chinese full-text search is incomplete (elasticlunr.js does not support CJK segmentation)
- No in-page language switcher (use browser back to landing page)
- Interactive D3.js visualizations deferred to v2

## License

TBD
