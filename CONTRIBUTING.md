# Contributing

## Chapter Conventions

### File Naming
Use English slugs for all chapter files: `chapter-01-young-riemann.md`. Files are shared by name between `src/zh/` and `src/en/`.

### Frontmatter
Every chapter must include TOML frontmatter:

```markdown
---
difficulty: "★★"
prerequisites: [II-03, II-04]
paths: [blue, red]
keywords: [analytic continuation, Gamma, functional equation]
zh-status: complete
en-status: missing
en-missing-note: "English translation pending"
---
```

- `difficulty`: One of ★, ★★, ★★★ (required)
- `prerequisites`: List of part-chapter IDs (e.g., `II-03`) or `[]` if none (required)
- `paths`: One or more of green, blue, red (required)
- `keywords`: 2-6 keywords (required)
- `zh-status`/`en-status`: complete | draft | planned | missing
- `zh-missing-note`/`en-missing-note`: Required when status is `missing`

### Summary pages
`preface.md`, `bibliography.md`, and `index.md` use a simplified frontmatter with only `difficulty` and `keywords`.

## Before Submitting a PR

```bash
make check              # Run all validation
make build              # Verify build succeeds
```

If you modify any plot scripts under `src/assets/scripts/`, run:

```bash
make generate-assets    # Regenerate all assets
```

## Bilingual Workflow

- `zh/` and `en/` directory trees must mirror each other
- When adding a chapter, create stubs in both languages
- Set `zh-status`/`en-status` honestly — CI validates this
- Status `missing` requires a non-empty `missing-note` field
