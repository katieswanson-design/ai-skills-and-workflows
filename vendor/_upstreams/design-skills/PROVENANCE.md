# cuellarfr/design-skills

Provenance for the skills vendored from this upstream. The skills themselves are
**not** in this directory — see *Where the skills live* below.

| | |
|---|---|
| Upstream | https://github.com/cuellarfr/design-skills |
| Commit | [`b41750a`](https://github.com/cuellarfr/design-skills/commit/b41750affc03669988b649380756bc17fa427a09) |
| Committed | 2026-08-23 |
| Vendored | 2026-08-29 |
| Skills vendored | 10 |
| License | MIT — see [LICENSE](LICENSE) |

## Where the skills live

`vendor/` is organised by category, not by source repo, so this upstream's skills are
spread across category directories:

`design` (7), `product-team` (2), `accessibility` (1)

[MANIFEST.tsv](../../MANIFEST.tsv) maps every vendored path back to its upstream repo
and upstream path. To list just this upstream's skills:

```bash
awk -F'\t' '$2 == "design-skills"' vendor/MANIFEST.tsv
```

## Refreshing

1. Clone cuellarfr/design-skills at a newer commit.
2. For each row in [MANIFEST.tsv](../../MANIFEST.tsv) with `upstream_repo` =
   `design-skills`, copy the upstream directory named in `upstream_path` over the local
   directory named in `vendor_path`.
3. Update the commit and dates in this file.
4. Run `scripts/check-links.sh` and regenerate [INDEX.md](../../../INDEX.md) if any
   skill was added, removed, or renamed.

Do not edit the vendored files directly — changes belong upstream.
