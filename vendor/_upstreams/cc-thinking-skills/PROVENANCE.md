# tjboudreaux/cc-thinking-skills

Provenance for the skills vendored from this upstream. The skills themselves are
**not** in this directory — see *Where the skills live* below.

| | |
|---|---|
| Upstream | https://github.com/tjboudreaux/cc-thinking-skills |
| Commit | [`7b8fece`](https://github.com/tjboudreaux/cc-thinking-skills/commit/7b8fece345dfaa11773be7152ccd194589cb5437) |
| Committed | 2026-08-07 |
| Vendored | 2026-08-29 |
| Skills vendored | 28 |
| License | MIT — see [LICENSE](LICENSE) |

## Where the skills live

`vendor/` is organised by category, not by source repo, so this upstream's skills are
spread across category directories:

`thinking-models` (28)

[MANIFEST.tsv](../../MANIFEST.tsv) maps every vendored path back to its upstream repo
and upstream path. To list just this upstream's skills:

```bash
awk -F'\t' '$2 == "cc-thinking-skills"' vendor/MANIFEST.tsv
```

## Refreshing

1. Clone tjboudreaux/cc-thinking-skills at a newer commit.
2. For each row in [MANIFEST.tsv](../../MANIFEST.tsv) with `upstream_repo` =
   `cc-thinking-skills`, copy the upstream directory named in `upstream_path` over the local
   directory named in `vendor_path`.
3. Update the commit and dates in this file.
4. Run `scripts/check-links.sh` and regenerate [INDEX.md](../../../INDEX.md) if any
   skill was added, removed, or renamed.

Do not edit the vendored files directly — changes belong upstream.
