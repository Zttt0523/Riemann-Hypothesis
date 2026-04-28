# Riemann Hypothesis Encyclopedia — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Scaffold the mdBook project with bilingual configs, directory structure, validation scripts, CI/CD, and write Part I (Chapters 1–4) as initial content.

**Architecture:** Two fully self-contained mdBook configs (`book.zh.toml`, `book.en.toml`) build from mirrored `src/zh/` and `src/en/` trees. Shared assets, macros, and bibliography live at `src/` level. Validation scripts + CI enforce structural consistency.

**Tech Stack:** mdBook 0.4.52, mdbook-katex 0.9.4, KaTeX, GitHub Actions, GitHub Pages

---

### Task 1: Project Scaffolding

**Files:**
- Create: `book.zh.toml`
- Create: `book.en.toml`
- Create: `Makefile`
- Create: `README.md`
- Create: `CONTRIBUTING.md`

- [ ] **Step 1: Create book.zh.toml** (fully self-contained, Chinese)

```toml
[book]
authors = [""]
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

- [ ] **Step 2: Create book.en.toml** (fully self-contained, English)

```toml
[book]
authors = [""]
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

- [ ] **Step 3: Create Makefile**

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

check: check-links check-frontmatter

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

- [ ] **Step 4: Create README.md**

Project overview with setup instructions (install mdBook, mdbook-katex, Python deps; how to build, serve, and contribute).

- [ ] **Step 5: Create CONTRIBUTING.md**

Contribution guide covering: bilingual content conventions, frontmatter requirements, asset generation workflow, validation steps before PR.

- [ ] **Step 6: Commit**

```bash
git add book.zh.toml book.en.toml Makefile README.md CONTRIBUTING.md
git commit -m "chore: scaffold project with mdBook configs, Makefile, and docs"
```

---

### Task 2: Source Directory Structure

**Files:**
- Create: `src/zh/SUMMARY.md`
- Create: `src/en/SUMMARY.md`
- Create: `src/macros.tex`
- Create: `src/references.bib`
- Create: `src/index.html`
- Create: All part directories under `src/zh/` and `src/en/`
- Create: `src/assets/images/plots/`, `src/assets/images/animations/`, `src/assets/images/portraits/`, `src/assets/images/diagrams/`
- Create: `src/assets/data/`
- Create: `src/assets/scripts/`

- [ ] **Step 1: Create src/zh/SUMMARY.md**

Full chapter tree as specified in the design doc (32 chapters, 7 parts, preface, bibliography, index). Collapsible Part sections using `[Part Title]()` syntax.

- [ ] **Step 2: Create src/en/SUMMARY.md**

Mirror of zh/SUMMARY.md with English titles.

- [ ] **Step 3: Create src/macros.tex**

```latex
\gdef\RH{\text{RH}}
\gdef\Zeta{\zeta}
\gdef\ZetaS{\zeta(s)}
\gdef\critline{\text{Re}(s) = \tfrac{1}{2}}
\gdef\NT{\text{N}(\text{T})}
\gdef\Order#1{O\!\left(#1\right)}
\gdef\Li{\text{Li}}
```

- [ ] **Step 4: Create src/references.bib** (empty, with header comment)

- [ ] **Step 5: Create src/index.html** (language selector landing page)

- [ ] **Step 6: Create all part directories and placeholder chapter files**

32 chapter stub files under `src/zh/` (each with frontmatter and placeholder content). Mirror under `src/en/`.

- [ ] **Step 7: Create asset directories** (`src/assets/images/{plots,animations,portraits,diagrams}`, `src/assets/data/`, `src/assets/scripts/`)

- [ ] **Step 8: Commit**

```bash
git add src/
git commit -m "chore: create source directory structure with SUMMARY.md and stubs"
```

---

### Task 3: Validation Scripts

**Files:**
- Create: `scripts/check-links.sh`
- Create: `scripts/check-frontmatter.py`
- Create: `src/assets/scripts/plot_all.py`

- [ ] **Step 1: Create scripts/check-links.sh**

Shell script that:
- Finds all `.md` files under `src/zh/` and `src/en/`
- Extracts `[text](path.md)` and `![](path)` references
- Resolves each path relative to the source file's directory
- Reports dead links (file not found)

- [ ] **Step 2: Create scripts/check-frontmatter.py**

Python script that:
- Walks all `.md` files in `src/zh/` and `src/en/`
- Parses TOML frontmatter from each
- Validates: difficulty (★/★★/★★★), prerequisites format and existence, paths (green/blue/red), keywords count (2-6), zh-status/en-status values, missing-note when status=missing
- Checks directory parity: every `.md` in `src/en/` has counterpart in `src/zh/` (and vice versa), excluding SUMMARY.md, preface.md, bibliography.md, index.md
- Reports all violations with file:line

- [ ] **Step 3: Create src/assets/scripts/plot_all.py** (stub)

Python script skeleton with `--check` flag that compares SHA256 of script files against a manifest. Placeholder that exits 0 for now (no plots yet).

- [ ] **Step 4: Commit**

```bash
git add scripts/ src/assets/scripts/
git commit -m "feat: add validation scripts for links, frontmatter, and asset freshness"
```

---

### Task 4: CI/CD Pipeline

**Files:**
- Create: `.github/workflows/deploy.yml`

- [ ] **Step 1: Create .github/workflows/deploy.yml**

As specified in the design doc: two jobs (build-and-deploy, deploy), cargo-binstall for mdBook, artifact passing, permissions: contents: write for deploy.

- [ ] **Step 2: Commit**

```bash
git add .github/
git commit -m "ci: add GitHub Actions deploy pipeline"
```

---

### Task 5: Custom Theme

**Files:**
- Create: `theme/css/custom.css`
- Create: `theme/book.js`

- [ ] **Step 1: Create theme/css/custom.css**

Minimal custom CSS: Chinese font stack, KaTeX display tweaks, path-selector styling placeholder.

```css
:root {
  --zh-font-stack: "Noto Serif SC", "Source Han Serif SC", "SimSun", serif;
  --mono-font-stack: "JetBrains Mono", "Source Code Pro", "Courier New", monospace;
}

[lang="zh"] body {
  font-family: var(--zh-font-stack);
}

.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
}
```

- [ ] **Step 2: Create theme/book.js** (empty placeholder for v2 language switcher)

- [ ] **Step 3: Commit**

```bash
git add theme/
git commit -m "feat: add custom mdBook theme with Chinese font stack"
```

---

### Task 6: Chapter 1 — The Young Riemann (ZH + EN stubs)

**Files:**
- Create: `src/zh/part-01-life/chapter-01-young-riemann.md`
- Create: `src/en/part-01-life/chapter-01-young-riemann.md`

- [ ] **Step 1: Write Chinese chapter stub**

Frontmatter + placeholder content:
```markdown
---
difficulty: "★"
prerequisites: []
paths: [green, blue, red]
keywords: [Riemann, biography, childhood, Germany, Gauss]
zh-status: complete
en-status: missing
en-missing-note: "English translation pending"
---

# 第一章：少年黎曼

> 难度：★ | 路径：🟢🟡🔴

## 出生与家庭

伯恩哈德·黎曼（Georg Friedrich Bernhard Riemann）于 1826 年 9 月 17 日出生在汉诺威王国布雷塞伦茨村（今属德国下萨克森州）...

[Content to be developed]
```

- [ ] **Step 2: Write English chapter stub** (mirror, with en-status: draft or planned)

- [ ] **Step 3: Commit**

```bash
git add src/zh/part-01-life/chapter-01-young-riemann.md src/en/part-01-life/chapter-01-young-riemann.md
git commit -m "feat: add Chapter 1 stub (The Young Riemann, zh/en)"
```

---

### Task 7: Chapters 2–4 Stubs

**Files:**
- Create: `src/zh/part-01-life/chapter-02-goettingen.md`
- Create: `src/en/part-01-life/chapter-02-goettingen.md`
- Create: `src/zh/part-01-life/chapter-03-collected-works.md`
- Create: `src/en/part-01-life/chapter-03-collected-works.md`
- Create: `src/zh/part-01-life/chapter-04-legacy.md`
- Create: `src/en/part-01-life/chapter-04-legacy.md`

- [ ] **Step 1: Write all Chinese stubs** (Chapters 2–4, frontmatter + titles + placeholder content)

- [ ] **Step 2: Write all English stubs** (mirrors)

- [ ] **Step 3: Commit**

```bash
git add src/zh/part-01-life/ src/en/part-01-life/
git commit -m "feat: add Part I chapter stubs (Chapters 2-4)"
```

---

### Task 8: Verify Build

- [ ] **Step 1: Install mdBook and mdbook-katex**

```bash
cargo install mdbook --version "=0.4.40" --locked
cargo install mdbook-katex --version "=0.9.1" --locked
```

- [ ] **Step 2: Build Chinese version**

```bash
make build-zh
```
Expected: build succeeds, `book/zh/` contains HTML files with KaTeX-rendered math.

- [ ] **Step 3: Build English version**

```bash
make build-en
```
Expected: build succeeds.

- [ ] **Step 4: Full build**

```bash
make build
```
Expected: both builds succeed, `book/index.html` present.

- [ ] **Step 5: Run validation**

```bash
make check-frontmatter
make check-links
```
Expected: both pass with zero errors.

- [ ] **Step 6: Serve locally**

```bash
make serve-zh
```
Open browser at `http://localhost:3000`, verify: sidebar navigation works, chapters display, math rendering functional.

- [ ] **Step 7: Commit any fixes**

---

### Task 9: Initialize Git Repository

- [ ] **Step 1: Initialize git and create initial commit**

```bash
git init
git add -A
git commit -m "chore: initial commit — Riemann Hypothesis Encyclopedia scaffold"
```
