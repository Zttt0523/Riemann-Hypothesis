.PHONY: build build-zh build-en check clean generate-assets check-assets

build: build-zh build-en
	cp src/index.html book/

build-zh:
	MDBOOK_BOOK__TITLE="黎曼猜想：从历史到未来" \
	MDBOOK_BOOK__SRC="src/zh" \
	MDBOOK_BOOK__LANGUAGE="zh" \
	MDBOOK_OUTPUT__HTML__SITE_URL="/zh/" \
	MDBOOK_OUTPUT__HTML__EDIT_URL_TEMPLATE="https://github.com/<org>/riemann-hypothesis/edit/main/src/zh/{path}" \
	mdbook build -d book/zh

build-en:
	MDBOOK_BOOK__TITLE="The Riemann Hypothesis: From History to the Future" \
	MDBOOK_BOOK__SRC="src/en" \
	MDBOOK_BOOK__LANGUAGE="en" \
	MDBOOK_OUTPUT__HTML__SITE_URL="/en/" \
	MDBOOK_OUTPUT__HTML__EDIT_URL_TEMPLATE="https://github.com/<org>/riemann-hypothesis/edit/main/src/en/{path}" \
	mdbook build -d book/en

generate-assets:
	uv run python src/assets/scripts/plot_all.py

check-assets:
	uv run python src/assets/scripts/plot_all.py --check

check: check-links check-frontmatter

check-links:
	bash scripts/check-links.sh

check-frontmatter:
	uv run python scripts/check-frontmatter.py src/zh src/en

clean:
	rm -rf book/

serve-zh:
	MDBOOK_BOOK__TITLE="黎曼猜想：从历史到未来" \
	MDBOOK_BOOK__SRC="src/zh" \
	MDBOOK_BOOK__LANGUAGE="zh" \
	MDBOOK_OUTPUT__HTML__SITE_URL="/zh/" \
	mdbook serve -d book/zh --open

serve-en:
	MDBOOK_BOOK__TITLE="The Riemann Hypothesis: From History to the Future" \
	MDBOOK_BOOK__SRC="src/en" \
	MDBOOK_BOOK__LANGUAGE="en" \
	MDBOOK_OUTPUT__HTML__SITE_URL="/en/" \
	mdbook serve -d book/en --open
