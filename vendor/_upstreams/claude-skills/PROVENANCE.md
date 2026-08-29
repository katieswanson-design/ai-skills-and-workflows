# alirezarezvani/claude-skills

Provenance for the skills vendored from this upstream. The skills themselves are
**not** in this directory — see *Where the skills live* below.

| | |
|---|---|
| Upstream | https://github.com/alirezarezvani/claude-skills |
| Commit | [`19392f7`](https://github.com/alirezarezvani/claude-skills/commit/19392f7a08264ed00486a251f5b2098321771f94) |
| Committed | 2026-08-26 |
| Vendored | 2026-08-29 |
| Skills vendored | 368 |
| License | MIT — see [LICENSE](LICENSE) |

## Where the skills live

`vendor/` is organised by category, not by source repo, so this upstream's skills are
spread across category directories:

`engineering` (150), `leadership-strategy` (62), `marketing-growth` (61), `compliance-risk` (26), `product-team` (22), `business-finance` (20), `product-management` (13), `productivity` (12), `design` (2)

[MANIFEST.tsv](../../MANIFEST.tsv) maps every vendored path back to its upstream repo
and upstream path. To list just this upstream's skills:

```bash
awk -F'\t' '$2 == "claude-skills"' vendor/MANIFEST.tsv
```

12 further skill directories in this upstream held byte-identical
copies of skills already vendored here; one copy of each was kept. The dropped
upstream paths are in the last column of [MANIFEST.tsv](../../MANIFEST.tsv).

## Refreshing

1. Clone alirezarezvani/claude-skills at a newer commit.
2. For each row in [MANIFEST.tsv](../../MANIFEST.tsv) with `upstream_repo` =
   `claude-skills`, copy the upstream directory named in `upstream_path` over the local
   directory named in `vendor_path`.
3. Update the commit and dates in this file.
4. Run `scripts/check-links.sh` and regenerate [INDEX.md](../../../INDEX.md) if any
   skill was added, removed, or renamed.

Do not edit the vendored files directly — changes belong upstream.
