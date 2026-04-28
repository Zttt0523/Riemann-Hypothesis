# Riemann Hypothesis Encyclopedia — Design Specification

## Overview

A systematic, encyclopedia-level introduction to the Riemann Hypothesis, spanning from elementary mathematics to advanced research topics. The project combines rigorous mathematical exposition with the biography of Bernhard Riemann and the broader historical context of prime number theory.

### Core Decisions

| Decision | Choice |
|----------|--------|
| Form | Static documentation site |
| Framework | mdBook v0.4.x (Rust toolchain) |
| Language | Bilingual (Chinese + English) |
| Audience | Multi-level (general readers → researchers) |
| Scope | 32 chapters across 7 Parts |
| Math rendering | KaTeX via `mdbook-katex` v0.9+ |
| Version control | Git, hosted on GitHub |
| Deployment | GitHub Pages, via GitHub Actions |
| Hosting | `https://<org>.github.io/riemann-hypothesis/` |

---

## Content Architecture: 7 Parts, 32 Chapters

### Difficulty Levels

- ★ Foundation — high school mathematics sufficient
- ★★ Intermediate — undergraduate mathematics expected
- ★★★ Advanced — graduate-level mathematics

### SUMMARY.md Structure

The `SUMMARY.md` in each language tracks the full chapter tree. Parts use nested lists for collapsible sidebar sections in mdBook. Part titles act as section headers; chapters are indented beneath.

```
# Riemann Hypothesis Encyclopedia

[Preface](preface.md)

- [Part I: Riemann's Life and Times]()
  - [Chapter 1: The Young Riemann](part-01-life/chapter-01-young-riemann.md)
  - [Chapter 2: Göttingen Years](part-01-life/chapter-02-goettingen.md)
  - [Chapter 3: Riemann's Collected Works](part-01-life/chapter-03-collected-works.md)
  - [Chapter 4: Riemann's Legacy](part-01-life/chapter-04-legacy.md)

- [Part II: Mathematical Foundations]()
  - [Chapter 5: Real Numbers and Limits](part-02-foundations/chapter-05-real-numbers.md)
  - [Chapter 6: Sequences and Series](part-02-foundations/chapter-06-sequences-series.md)
  - [Chapter 7: Functions and Continuity](part-02-foundations/chapter-07-functions-continuity.md)
  - [Chapter 8: Differential Calculus](part-02-foundations/chapter-08-differential-calculus.md)
  - [Chapter 9: Integral Calculus](part-02-foundations/chapter-09-integral-calculus.md)
  - [Chapter 10: Complex Numbers and Functions](part-02-foundations/chapter-10-complex-numbers.md)
  - [Chapter 11: Infinite Products](part-02-foundations/chapter-11-infinite-products.md)

- [Part III: Analytic Number Theory Foundations]()
  - [Chapter 12: Prime Numbers Through History](part-03-analytic-nt/chapter-12-prime-history.md)
  - [Chapter 13: Arithmetic Functions](part-03-analytic-nt/chapter-13-arithmetic-functions.md)
  - [Chapter 14: Dirichlet Series](part-03-analytic-nt/chapter-14-dirichlet-series.md)
  - [Chapter 15: The Prime Number Theorem](part-03-analytic-nt/chapter-15-pnt.md)

- [Part IV: The Riemann Zeta Function]()
  - [Chapter 16: Definition and Elementary Properties](part-04-zeta/chapter-16-zeta-definition.md)
  - [Chapter 17: Analytic Continuation](part-04-zeta/chapter-17-analytic-continuation.md)
  - [Chapter 18: The Functional Equation](part-04-zeta/chapter-18-functional-equation.md)
  - [Chapter 19: Zeros of the Zeta Function](part-04-zeta/chapter-19-zeros.md)
  - [Chapter 20: Special Values and the Riemann-Siegel Formula](part-04-zeta/chapter-20-special-values.md)

- [Part V: The Riemann Hypothesis]()
  - [Chapter 21: Statement and History of RH](part-05-rh/chapter-21-statement-history.md)
  - [Chapter 22: Equivalent Formulations](part-05-rh/chapter-22-equivalents.md)
  - [Chapter 23: Zero-Free Regions](part-05-rh/chapter-23-zero-free-regions.md)
  - [Chapter 24: Consequences of RH](part-05-rh/chapter-24-consequences.md)
  - [Chapter 25: Attempted Proofs and Approaches](part-05-rh/chapter-25-attempts.md)

- [Part VI: Related Conjectures and Generalizations]()
  - [Chapter 26: The Lindelöf Hypothesis](part-06-generalizations/chapter-26-lindelof.md)
  - [Chapter 27: L-Functions and the Selberg Class](part-06-generalizations/chapter-27-l-functions.md)
  - [Chapter 28: Montgomery's Pair Correlation](part-06-generalizations/chapter-28-montgomery.md)
  - [Chapter 29: Random Matrix Theory Connection](part-06-generalizations/chapter-29-random-matrices.md)
  - [Chapter 30: The Grand Riemann Hypothesis](part-06-generalizations/chapter-30-grand-rh.md)

- [Part VII: Reflections]()
  - [Chapter 31: Computational Verification](part-07-reflections/chapter-31-computation.md)
  - [Chapter 32: Philosophical and Cultural Impact](part-07-reflections/chapter-32-philosophy.md)

[Bibliography](bibliography.md)

[Index](index.md)
```

### Chapter Table with Difficulty and Paths

| Ch. | Title | Difficulty | Path |
|-----|-------|------------|------|
| 1 | The Young Riemann | ★ | 🟢🟡🔴 |
| 2 | Göttingen Years | ★ | 🟢🟡🔴 |
| 3 | Riemann's Collected Works | ★ | 🟢🟡🔴 |
| 4 | Riemann's Legacy | ★ | 🟢🟡🔴 |
| 5 | Real Numbers and Limits | ★ | 🟢🟡🔴 |
| 6 | Sequences and Series | ★ | 🟢🟡🔴 |
| 7 | Functions and Continuity | ★ | 🟡🔴 |
| 8 | Differential Calculus | ★ | 🟡🔴 |
| 9 | Integral Calculus | ★ | 🟡🔴 |
| 10 | Complex Numbers and Functions | ★★ | 🟡🔴 |
| 11 | Infinite Products | ★★ | 🟡🔴 |
| 12 | Prime Numbers Through History | ★ | 🟢🟡🔴 |
| 13 | Arithmetic Functions | ★★ | 🟡🔴 |
| 14 | Dirichlet Series | ★★ | 🟡🔴 |
| 15 | The Prime Number Theorem | ★★ | 🟢🟡🔴 |
| 16 | Definition and Elementary Properties | ★★ | 🟡🔴 |
| 17 | Analytic Continuation | ★★ | 🟡🔴 |
| 18 | The Functional Equation | ★★★ | 🔴 |
| 19 | Zeros of the Zeta Function | ★★★ | 🔴 |
| 20 | Special Values and Riemann-Siegel | ★★★ | 🔴 |
| 21 | Statement and History of RH | ★★ | 🟢🟡🔴 |
| 22 | Equivalent Formulations | ★★★ | 🔴 |
| 23 | Zero-Free Regions | ★★★ | 🔴 |
| 24 | Consequences of RH | ★★★ | 🔴 |
| 25 | Attempted Proofs and Approaches | ★★★ | 🔴 |
| 26 | The Lindelöf Hypothesis | ★★★ | 🔴 |
| 27 | L-Functions and the Selberg Class | ★★★ | 🔴 |
| 28 | Montgomery's Pair Correlation | ★★★ | 🔴 |
| 29 | Random Matrix Theory Connection | ★★★ | 🔴 |
| 30 | The Grand Riemann Hypothesis | ★★★ | 🔴 |
| 31 | Computational Verification | ★★ | 🟢🟡🔴 |
| 32 | Philosophical and Cultural Impact | ★ | 🟢🟡🔴 |

### Chapter Frontmatter Schema

Every chapter file begins with TOML frontmatter. All fields are required unless marked optional.

```markdown
---
difficulty: "★★"                              # ★ | ★★ | ★★★ (required)
prerequisites: [II-03, II-04]                 # part-chapter IDs, or [] (required)
paths: [blue, red]                            # green | blue | red (required)
keywords: [analytic continuation, Gamma]       # 2-6 keywords (required)
zh-status: complete                            # complete | draft | planned | missing (en/ chapters only)
zh-missing-note: "awaiting translator"         # required if zh-status = missing
en-status: complete                            # complete | draft | planned | missing (zh/ chapters only)
en-missing-note: "awaiting translator"         # required if en-status = missing
---
```

**`prerequisites` format**: Each entry is a slug like `II-03` meaning Part II, Chapter 3 in the current SUMMARY.md ordering. The part Roman numeral and chapter number within that part. Use `[]` for chapters with no prerequisites.

**`zh-status` / `en-status`**: Tracks bilingual parity. `complete` = full translation available; `draft` = partial translation exists; `planned` = gap acknowledged, chapter planned; `missing` = gap not yet addressed. When status is `missing`, the companion field `zh-missing-note` (or `en-missing-note`) is **required** and must be non-empty — this is the explicit acknowledgment mechanism. CI flags any chapter with `missing` status and no `missing-note`.

**Special files** (`preface.md`, `bibliography.md`, `index.md`): These use a simplified frontmatter with only `difficulty` and `keywords`. The validator accepts either the full chapter schema or this minimal schema.

### Reading Paths

Three curated paths guide different audiences. Path labels are included in chapter frontmatter. The `SUMMARY.md` sidebar shows all chapters; readers filter by path via the theme's optional path selector.

| Path | For | Chapters | Description |
|------|-----|----------|-------------|
| 🟢 Green | All readers | 11 | Biography, prime number stories, overview, philosophy. Minimal formulas. |
| 🟡 Blue | STEM undergraduates | 22 | Core mathematics: complex analysis → analytic number theory → ζ function → RH |
| 🔴 Red | Graduate / researchers | 32 | Full text including advanced topics and recent developments |

Cross-chapter references include difficulty badges:

```markdown
See also: [Prime Number Theorem](../part-03-analytic-nt/chapter-15-pnt.md) ★★
```

---

## Bilingual Strategy

### Directory Layout

```
src/
├── zh/                                  # Chinese content
│   ├── SUMMARY.md
│   ├── preface.md
│   ├── bibliography.md
│   ├── index.md
│   ├── part-01-life/
│   │   ├── chapter-01-young-riemann.md
│   │   ├── chapter-02-goettingen.md
│   │   ├── chapter-03-collected-works.md
│   │   └── chapter-04-legacy.md
│   ├── part-02-foundations/
│   │   └── ... (7 chapters)
│   ├── part-03-analytic-nt/
│   │   └── ... (4 chapters)
│   ├── part-04-zeta/
│   │   └── ... (5 chapters)
│   ├── part-05-rh/
│   │   └── ... (5 chapters)
│   ├── part-06-generalizations/
│   │   └── ... (5 chapters)
│   └── part-07-reflections/
│       └── ... (2 chapters)
├── en/                                  # English content (directory mirrors zh/)
│   ├── SUMMARY.md
│   └── ... (same structure)
├── assets/                              # Shared across languages
│   ├── images/
│   │   ├── plots/                       # Python-generated function plots
│   │   ├── animations/                  # GIF/WebM animations
│   │   ├── portraits/                   # Historical portraits
│   │   └── diagrams/                    # Hand-drawn style diagrams
│   ├── data/                            # Zero data, prime tables
│   └── scripts/                         # Plot generation scripts (Python)
├── macros.tex                           # KaTeX macros (shared)
└── references.bib                       # Shared BibTeX bibliography
```

### Conventions

- File names use English slugs (e.g., `chapter-01-young-riemann.md`), shared between languages
- Directory trees in `zh/` and `en/` mirror each other structurally
- All images and data live in shared `assets/`
- `macros.tex` and `references.bib` are shared at `src/` level
- Each chapter's frontmatter `zh-status`/`en-status` fields track translation parity
- CI validates that no chapter is `missing` without a non-empty `missing-note`

### Special Pages

**Preface** (`zh/preface.md`, `en/preface.md`):
- Introduces the project, the bilingual nature, and the three reading paths
- Explains the difficulty label system
- Documents the CJK search limitation for Chinese readers
- Acknowledges that the encyclopedia is a living work

**Bibliography** (`zh/bibliography.md`, `en/bibliography.md`):
- Curated list of cited works organized by topic (Primary Sources, Historical Works, Modern Expositions, Computational Work)
- Maintained as hand-curated Markdown for v1; `src/references.bib` also maintained for future tooling

**Index** (`zh/index.md`, `en/index.md`):
- Alphabetical index of key terms, people, and theorems with links to relevant chapters
- Compiled gradually as chapters are written; a script may assist but manual curation ensures quality

### Language Selector Landing Page

A single `src/index.html` (outside zh/ and en/) serves as the root landing page. It:

- Auto-detects browser language via `navigator.language` and redirects to `/zh/` or `/en/`
- Falls back to a two-button choice screen if JavaScript is disabled
- Provides explicit links: "中文版 | English Version"
- Lives at the repository root and is copied to `book/index.html` during the build

```html
<!DOCTYPE html>
<html>
<head><meta charset="utf-8"><title>Riemann Hypothesis Encyclopedia</title></head>
<body>
  <h1>Riemann Hypothesis Encyclopedia</h1>
  <p><a href="/zh/">中文版</a> | <a href="/en/">English Version</a></p>
  <script>/* auto-redirect based on navigator.language */</script>
</body>
</html>
```

---

## Math Rendering

### Engine: KaTeX + `mdbook-katex` v0.9+

**Version constraint**: `mdbook-katex >= 0.9.0` with `mdbook ~0.4`. Tested against mdBook 0.4.40 and mdbook-katex 0.9.1.

### Configuration (`book.zh.toml` / `book.en.toml`)

Two fully self-contained config files for the two language builds. Each includes all preprocessor and output settings. There is no config inheritance — mdBook reads only the file passed via `--config`.

**Version constraint**: mdBook ~0.4.52, mdbook-katex ~0.9.4. CI installs the latest matching semver via `cargo-binstall` (pre-built binaries). The `--locked` flag ensures reproducible dependency resolution.

**`book.zh.toml`** (fully self-contained):

```toml
[book]
authors = ["..."]
language = "zh"
title = "黎曼猜想：从历史到未来"
src = "src/zh"
site-url = "/zh/"

[preprocessor.katex]
after = ["links"]

[preprocessor.katex.katex]
macros = "src/macros.tex"
no-css = false

[output.html]
mathjax-support = false
site-url = "/zh/"
git-repository-url = "https://github.com/<org>/riemann-hypothesis"
edit-url-template = "https://github.com/<org>/riemann-hypothesis/edit/main/src/zh/{path}"
```

**`book.en.toml`** (fully self-contained):

```toml
[book]
authors = ["..."]
language = "en"
title = "The Riemann Hypothesis: From History to the Future"
src = "src/en"
site-url = "/en/"

[preprocessor.katex]
after = ["links"]

[preprocessor.katex.katex]
macros = "src/macros.tex"
no-css = false

[output.html]
mathjax-support = false
site-url = "/en/"
git-repository-url = "https://github.com/<org>/riemann-hypothesis"
edit-url-template = "https://github.com/<org>/riemann-hypothesis/edit/main/src/en/{path}"
```

A convenience `book.toml` may optionally exist at the project root for one-language local development (e.g., pointing to `src/zh`), but is not required for the build.

### Custom Macros (`src/macros.tex`)

Located under `src/` so `mdbook-katex` resolves it relative to the book root:

```latex
\gdef\RH{\text{RH}}
\gdef\Zeta{\zeta}
\gdef\ZetaS{\zeta(s)}
\gdef\critline{\text{Re}(s) = \tfrac{1}{2}}
\gdef\NT{\text{N}(\text{T})}
\gdef\Order#1{O\!\left(#1\right)}
\gdef\Li{\text{Li}}
```

### Inline and Display Math

- Inline: `$\zeta(s) = \sum_{n=1}^{\infty} \frac{1}{n^s}$`
- Display: standard `$$ ... $$` blocks

---

## Citation Management

### Strategy: Shared BibTeX + Per-Chapter Footnotes

- All references live in `src/references.bib` (BibTeX format)
- Chapters cite using `[Author, Year]` style, e.g.: `[Riemann, 1859]`
- Full bibliography is rendered at `zh/bibliography.md` and `en/bibliography.md`
- Each Part also includes a "Further Reading" section at its end chapter

### Bibliography Chapter

`zh/bibliography.md` and `en/bibliography.md` list all cited works organized by topic:

```markdown
# Bibliography

## Primary Sources
- Riemann, B. (1859). *Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse.*
  Monatsberichte der Berliner Akademie.

## Historical Works
- ...

## Modern Expositions
- ...
```

For v1, the bibliography is maintained as a hand-curated Markdown chapter to keep tooling simple. A BibTeX file in `src/references.bib` is also maintained for potential future integration with `mdbook-bib`.

### Citation Format Convention

All chapters use the same format:
- In-text: `[Riemann, 1859]` or `[Edwards, 1974, §2.3]`
- The foot-of-chapter or bibliography chapter provides full details
- Hyperlinked when possible (e.g., to DOI or arXiv)

---

## Visualization Strategy

### V1 (Initial Release): Static + Animated

| Tier | Technology | Use Case |
|------|-----------|----------|
| Static plots | Python/Matplotlib → SVG | Function graphs, prime distributions, zero locations |
| Animated | Manim → GIF/WebM | Analytic continuation, function equation symmetry |

### V2 (Future): Interactive

| Tier | Technology | Use Case |
|------|-----------|----------|
| Interactive | D3.js / embedded standalone HTML | Zero explorer, prime spiral |

Interactive visualizations are deferred to v2 because they require custom engineering around mdBook's static output pipeline (iframes or custom JS injection through `theme/book.js`). A single D3 prototype should be validated before committing interactive content to the main scope.

### Asset Pipeline

All generation scripts live in `assets/scripts/`. A `Makefile` target regenerates all assets:

```makefile
generate-assets:
    cd assets/scripts && python plot_all.py

check-assets:
    cd assets/scripts && python plot_all.py --check
```

The `--check` flag compares hashes of input scripts against a `<asset>.sha256` manifest file and exits non-zero if any output is stale relative to its source. This uses content hashing rather than mtime, which is reliable across `git checkout` and CI runs. The manifest is regenerated alongside each image during `generate-assets`.

Generated images are committed to the repository. Scripts are the source of truth.

---

## Repository Infrastructure

```
riemann-hypothesis/
├── src/                               # Content source
│   ├── zh/                            # Chinese Markdown chapters
│   ├── en/                            # English Markdown chapters
│   ├── assets/                        # Shared images, data, scripts
│   ├── macros.tex                     # KaTeX macros
│   ├── references.bib                 # Shared bibliography
│   └── index.html                     # Language selector landing page
├── theme/                             # Custom mdBook theme
│   ├── css/custom.css
│   └── book.js
├── scripts/
│   ├── check-links.sh                 # Dead link checker
│   └── check-frontmatter.py           # Frontmatter consistency validator
├── book.toml                          # Base mdBook config
├── book.zh.toml                       # Chinese build config
├── book.en.toml                       # English build config
├── Makefile                           # Top-level command entry
├── README.md
├── CONTRIBUTING.md
└── .github/
    └── workflows/
        └── deploy.yml                 # CI/CD pipeline
```

### Build Process (`Makefile`)

```makefile
.PHONY: build build-zh build-en check clean generate-assets check-assets

build: build-zh build-en
    cp src/index.html book/

build-zh:
    mdbook build --config book.zh.toml -d book/zh

build-en:
    mdbook build --config book.en.toml -d book/en

generate-assets:
    cd src/assets/scripts && python plot_all.py

check-assets:
    cd src/assets/scripts && python plot_all.py --check

check: check-links check-frontmatter check-assets

check-links:
    bash scripts/check-links.sh

check-frontmatter:
    python scripts/check-frontmatter.py src/zh src/en

clean:
    rm -rf book/

serve-zh:
    mdbook serve --config book.zh.toml -d book/zh --open

serve-en:
    mdbook serve --config book.en.toml -d book/en --open
```

**Design rationale**: Two separate config files (`book.zh.toml`, `book.en.toml`) eliminate the broken sed approach from the initial draft. Each config specifies its own `src` and `site-url`. The build is deterministic and testable. For local development, `make serve-zh` and `make serve-en` let authors preview one language at a time.

### CI/CD Pipeline (`.github/workflows/deploy.yml`)

The pipeline uses a single job that validates, builds, and conditionally deploys. Build artifacts are passed via `upload-artifact`/`download-artifact` to avoid re-building.

```yaml
name: Deploy
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install Python deps
        run: pip install "matplotlib>=3.8" "numpy>=1.26"

      - name: Install mdBook and mdbook-katex (pre-built binaries)
        run: |
          curl -L https://github.com/cargo-bins/cargo-binstall/releases/latest/download/cargo-binstall-x86_64-unknown-linux-musl.tgz | tar xz
          ./cargo-binstall --no-confirm mdbook@0.4.52 mdbook-katex@0.9.4

      - name: Check frontmatter consistency
        run: make check-frontmatter

      - name: Check links
        run: make check-links

      - name: Check asset freshness
        run: make check-assets

      - name: Build
        run: make build

      - name: Upload build artifact
        uses: actions/upload-artifact@v4
        with:
          name: book
          path: book/

  deploy:
    needs: build-and-deploy
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - name: Download build artifact
        uses: actions/download-artifact@v4
        with:
          name: book
          path: book/

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./book
```

### Validation Scripts

- **`check-links.sh`** — validates all `[text](path.md)` cross-chapter internal links and `![](path.png)` asset references by checking file existence under `src/`
- **`check-frontmatter.py`** — reads every `.md` file in `src/zh/` and `src/en/`, parses TOML frontmatter, and validates against the schema:
  - `difficulty` is one of ★/★★/★★★ (required for chapters, optional for preface/bib/index)
  - `prerequisites` entries match `^[IVX]+-\d{2}$` pattern and each referenced chapter file exists
  - `paths` contains only `green`/`blue`/`red`
  - `zh-status`/`en-status` values are valid enum members
  - If status is `missing`, the corresponding `missing-note` field is present and non-empty
  - `keywords` array has 2-6 entries
  - **Directory parity check**: every `.md` file in `src/en/` has a corresponding file in `src/zh/` (and vice versa), excluding `SUMMARY.md`, `preface.md`, `bibliography.md`, and `index.md`. Missing counterparts are flagged as errors.
  - `preface.md`, `bibliography.md`, `index.md` accept a minimal schema (difficulty + keywords only)
- **`make check-assets`** — runs `plot_all.py --check` which compares SHA256 hashes of source scripts against the manifest file for each generated asset, detecting uncommitted or stale images

---

## Cross-Cutting Concerns

### Sidebar Navigation

mdBook supports collapsible sections via nested list indentation in `SUMMARY.md`. With 32 chapters across 7 parts, the sidebar will be long but manageable. Each Part is a collapsible section header (using `[Part Title]()` with no link target). Readers can collapse Parts they're not currently reading. This is the default mdBook behavior and requires no custom code.

### Dark Mode

mdBook ships with three themes (light, coal, navy) and a theme toggle in the header. This is sufficient for v1. The built-in coal and navy themes provide dark mode experiences. Custom CSS in `theme/css/custom.css` may adjust color variables if needed.

### Search (CJK Limitation)

mdBook's built-in search uses elasticlunr.js, which does not support Chinese text segmentation. For v1, this is a **documented known limitation**. The README and preface will note that full-text search of Chinese content produces incomplete results. English search works correctly.

A future iteration may integrate `lunr-languages` with CJK tokenizer support or use an external search provider like Algolia DocSearch.

### SEO

For v1, SEO is a **documented deferred concern**. mdBook generates clean semantic HTML which provides basic search engine accessibility. Proper `hreflang` tags, canonical URLs, and sitemaps for the bilingual site require custom `index.hbs` template overrides or post-build processing — deferred to v2.

### Language Switcher

For v1, the language selector on the root landing page is the only cross-language navigation. Once a reader enters the Chinese or English book, there is no in-page language toggle to jump to the equivalent page in the other language. This is a **documented limitation** for v1.

A v2 enhancement will inject a language toggle button into the mdBook header via `theme/book.js`, mapping the current page path to its counterpart in the other language. This requires JavaScript injected through mdBook's `additional-js` config option and a path-mapping convention (Chapter N in zh/ ↔ Chapter N in en/).

---

## Design Principles

1. **Difficulty transparency** — every chapter clearly labeled; no reader surprised by required background
2. **Progressive depth** — Parts I-II accessible to anyone; later parts assume cumulative knowledge
3. **Language parity** — zh/ and en/ are first-class citizens; parity tracked via frontmatter
4. **Reproducible assets** — all plots generated from scripts with staleness detection
5. **Content before tooling** — complex tooling only where it serves the reader; default to simple Markdown + KaTeX
6. **Explicit over implicit** — frontmatter validates every chapter; dead links caught by CI; asset staleness detected automatically
