#!/usr/bin/env bash
# check-links.sh — validate internal links and asset references in mdBook source
set -euo pipefail

SRC_DIR="${1:-src}"
ERRORS=0

echo "=== Checking internal links ==="

while IFS= read -r -d '' file; do
    dir="$(dirname "$file")"
    # Match [text](path.md) — markdown links
    while IFS= read -r line; do
        link="${line##*](}"
        link="${link%)}"
        # Skip external URLs
        [[ "$link" =~ ^https?:// ]] && continue
        # Skip anchor-only links
        [[ "$link" =~ ^# ]] && continue
        # Skip empty
        [[ -z "$link" ]] && continue

        # Resolve relative to the source file's directory
        resolved="$(cd "$dir" && realpath -m "$link" 2>/dev/null || echo "$dir/$link")"
        # Determine base src directory (zh or en)
        if [[ "$file" == *"/zh/"* ]]; then
            src_base="$(echo "$SRC_DIR/zh" )"
        else
            src_base="$(echo "$SRC_DIR/en" )"
        fi

        # Check if file exists
        full_path="$src_base/${link#./}"
        # Handle relative paths
        rel="$(realpath --relative-to="$src_base" "$resolved" 2>/dev/null || true)"
        if [[ -n "$rel" ]] && [[ -f "$src_base/$rel" ]]; then
            :
        elif [[ -f "$full_path" ]]; then
            :
        else
            echo "  BROKEN: $file -> $link"
            ERRORS=$((ERRORS + 1))
        fi
    done < <(grep -oP '\[([^\]]*)\]\(([^)]+\.md)\)' "$file" || true)
done < <(find "$SRC_DIR/zh" "$SRC_DIR/en" -name '*.md' -print0 2>/dev/null)

echo "=== Checking image references ==="
while IFS= read -r -d '' file; do
    while IFS= read -r line; do
        img="${line##*](}"
        img="${img%)}"
        [[ "$img" =~ ^https?:// ]] && continue
        [[ -z "$img" ]] && continue

        # Resolve relative to src/
        resolved="$SRC_DIR/${img#./}"
        if [[ ! -f "$resolved" ]]; then
            echo "  MISSING IMAGE: $file -> $img"
            ERRORS=$((ERRORS + 1))
        fi
    done < <(grep -oP '!\[([^\]]*)\]\(([^)]+\.(png|svg|jpg|jpeg|gif|webm))\)' "$file" || true)
done < <(find "$SRC_DIR/zh" "$SRC_DIR/en" -name '*.md' -print0 2>/dev/null)

echo ""
if [[ $ERRORS -eq 0 ]]; then
    echo "All links valid."
else
    echo "$ERRORS broken link(s) found."
    exit 1
fi
