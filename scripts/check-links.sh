#!/usr/bin/env bash
#
# check-links.sh — validate every skill entry in INDEX.md.
#
# Enforces the link validity rule from SOURCES.md and checks that each row is
# internally consistent. Offline by default; needs nothing beyond coreutils.
#
#   ./scripts/check-links.sh
#   ./scripts/check-links.sh --clones ~/src/upstreams
#   ./scripts/check-links.sh --remote
#
# Exits 0 if everything passes, 1 otherwise.

set -uo pipefail

INDEX="${INDEX:-INDEX.md}"
CLONES=""
REMOTE=0

usage() {
  cat <<'EOF'
check-links.sh — validate every skill entry in INDEX.md.

Checks, per row:
  * the path satisfies the link validity rule in SOURCES.md
  * the GitHub URL and the path column agree
  * the linked skill name matches its directory
  * the description is non-empty
  * the vendored copy exists under vendor/<category>/ and is listed in MANIFEST.tsv
  * the skill folder carries its own LICENSE
  * no (repo, path) pair appears twice

Then checks the category summary table against the rows below it.

Usage: ./scripts/check-links.sh [options]

Options:
  --clones DIR   Also verify each path exists under DIR/<repo-name>/, where DIR
                 holds local clones named after the upstream repo, e.g.
                 DIR/designer-skills/, DIR/pm-skills/.
  --remote       Also HTTP-check every GitHub URL (needs curl; slow, and GitHub
                 may rate-limit a few hundred unauthenticated requests).
  --index FILE   Index file to check (default: INDEX.md, or $INDEX).
  -h, --help     Show this help.
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --clones) CLONES="${2:-}"; shift 2 ;;
    --remote) REMOTE=1; shift ;;
    --index)  INDEX="${2:-}"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown option: $1" >&2; usage >&2; exit 2 ;;
  esac
done

cd "$(dirname "$0")/.." || exit 2

[ -f "$INDEX" ] || { echo "error: $INDEX not found" >&2; exit 2; }
if [ -n "$CLONES" ] && [ ! -d "$CLONES" ]; then
  echo "error: --clones directory not found: $CLONES" >&2; exit 2
fi
if [ "$REMOTE" -eq 1 ] && ! command -v curl >/dev/null 2>&1; then
  echo "error: --remote needs curl" >&2; exit 2
fi

# A skill row looks like:
#   | [name](vendor/CATEGORY/name/SKILL.md) | desc | [`PATH`](https://github.com/OWNER/REPO/blob/main/PATH) |
# optionally prefixed with a star marking a SOURCES.md bookmark.
# Anchored at both ends so the category summary table (which also starts with
# "| [") and descriptions containing backticks are not picked up.
ROW='^\| [^[]*\[[^]]+\]\(vendor/[^)]+\) \| .* \| \[`[^`]+`\]\(https://github\.com/[^/]+/[^/]+/blob/main/[^)]+\) \|$'

FAIL=0
note() { printf '  %-14s %s\n' "$1" "$2"; FAIL=$((FAIL+1)); }

rows=$(grep -E "$ROW" "$INDEX")
total=$(printf '%s\n' "$rows" | grep -c .)
[ "$total" -eq 0 ] && { echo "error: no skill rows matched — has the row format changed?" >&2; exit 2; }
echo "checking $total skill rows in $INDEX"

echo
echo "structure, link rule, and internal consistency:"
seen=$(mktemp); trap 'rm -f "$seen"' EXIT

while IFS= read -r line; do
  name=$(printf '%s' "$line" | sed -E 's#^\| [^[]*\[([^]]+)\].*#\1#')
  vend=$(printf '%s' "$line" | sed -E 's#^\| [^[]*\[[^]]+\]\(([^)]+)\).*#\1#')
  path=$(printf '%s' "$line" | sed -E 's#.*\[`([^`]+)`\]\([^)]+\) \|$#\1#')
  url=$( printf '%s' "$line" | sed -E 's#.*\[`[^`]+`\]\(([^)]+)\) \|$#\1#')
  desc=$(printf '%s' "$line" | sed -E 's#^\| [^[]*\[[^]]+\]\([^)]+\) \| ##; s# \| \[`[^`]+`\]\([^)]+\) \|$##')
  slug=$(   printf '%s' "$url" | sed -E 's#^https://github\.com/([^/]+/[^/]+)/blob/main/.*#\1#')
  urlpath=$(printf '%s' "$url" | sed -E 's#^https://github\.com/[^/]+/[^/]+/blob/main/##')
  repo=${slug#*/}

  # Link validity rule (SOURCES.md): skills/<name>/SKILL.md, either at the repo
  # root or under a grouping folder, with no /docs/ or dot-directory anywhere.
  printf '%s' "$path" | grep -qE '(^|/)skills/[^/]+/SKILL\.md$' \
    || note "RULE-SHAPE" "$slug :: $path"
  printf '%s' "$path" | grep -qE '(^|/)(docs|\.[^/]+)/' \
    && note "RULE-EXCLUDE" "$slug :: $path"

  [ "$urlpath" = "$path" ] || note "URL-MISMATCH" "$slug :: path column says $path, url says $urlpath"

  dir=$(basename "$(dirname "$vend")")
  [ "$dir" = "$name" ] || note "NAME-MISMATCH" "$slug :: link says $name, directory is $dir"

  [ -n "$(printf '%s' "$desc" | tr -d '[:space:]')" ] || note "EMPTY-DESC" "$slug :: $name"

  if grep -qxF "$slug|$path" "$seen" 2>/dev/null; then
    note "DUPLICATE" "$slug :: $path"
  else
    printf '%s|%s\n' "$slug" "$path" >> "$seen"
  fi

  case "$vend" in vendor/*/*/SKILL.md) ;; *) note "VENDOR-LINK" "$slug :: odd vendor path $vend" ;; esac
  grep -qF "$(printf '%s' "$vend" | sed 's#^vendor/##; s#/SKILL\.md$##')	" vendor/MANIFEST.tsv \
    || note "NOT-IN-MANIFEST" "$vend"
  # every skill folder carries its own license, so a skill copied out stays compliant
  [ -f "$(dirname "$vend")/LICENSE" ] || note "NO-LICENSE" "$(dirname "$vend")"
  [ -f "$vend" ] || note "VENDOR-MISSING" "$vend"

  if [ -n "$CLONES" ] && [ ! -f "$CLONES/$repo/$path" ]; then
    note "NO-LOCAL-FILE" "$repo/$path"
  fi
done <<EOF
$rows
EOF
[ "$FAIL" -eq 0 ] && echo "  ok — $total rows"

# The summary table at the top of INDEX.md must agree with the rows below it.
echo
echo "category counts:"
counts=$(awk '
  /^## /   { cat = substr($0, 4); next }
  /^\| /  { if (cat != "" && $0 ~ /blob\/main\//) n[cat]++ }
  END      { for (c in n) printf "%s\t%d\n", c, n[c] }
' "$INDEX" | sort)
while IFS="$(printf '\t')" read -r cat n; do
  [ -z "$cat" ] && continue
  claimed=$(grep -E "^\| \[$cat\]\(#" "$INDEX" | sed -E 's#.*\| *([0-9]+) *\|$#\1#')
  if [ -z "$claimed" ]; then
    note "NO-TOC-ENTRY" "$cat (counted $n)"
  elif [ "$claimed" != "$n" ]; then
    note "COUNT-MISMATCH" "$cat: summary table says $claimed, counted $n"
  else
    printf '  %-22s %s\n' "$cat" "$n"
  fi
done <<EOF
$counts
EOF

claimed_total=$(grep -E '^\| \*\*Total\*\* \| \*\*[0-9]+\*\* \|$' "$INDEX" | sed -E 's#.*\*\*([0-9]+)\*\*.*#\1#')
if [ -n "$claimed_total" ] && [ "$claimed_total" != "$total" ]; then
  note "TOTAL-MISMATCH" "summary table says $claimed_total, counted $total"
fi

if [ "$REMOTE" -eq 1 ]; then
  echo
  echo "remote URL check ($total requests, this takes a while):"
  bad=$(printf '%s\n' "$rows" \
    | sed -E 's#^\| \[[^]]+\]\(([^)]+)\).*#\1#' \
    | xargs -P 8 -I{} sh -c 'c=$(curl -sS -o /dev/null -w "%{http_code}" -L --max-time 20 "$1"); [ "$c" = 200 ] || echo "$c $1"' _ {})
  if [ -n "$bad" ]; then
    printf '%s\n' "$bad" | while read -r l; do note "HTTP" "$l"; done
  else
    echo "  ok — all $total URLs returned 200"
  fi
fi

echo
if [ "$FAIL" -eq 0 ]; then
  echo "PASS — $total rows, no problems"
  exit 0
else
  echo "FAIL — $FAIL problem(s)"
  exit 1
fi
