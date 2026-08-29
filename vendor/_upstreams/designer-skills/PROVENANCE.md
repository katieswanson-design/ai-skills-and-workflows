# Owl-Listener/designer-skills

Provenance for the skills vendored from this upstream. The skills themselves are
**not** in this directory — see *Where the skills live* below.

| | |
|---|---|
| Upstream | https://github.com/Owl-Listener/designer-skills |
| Commit | [`20e34c4`](https://github.com/Owl-Listener/designer-skills/commit/20e34c4a587e5eb09fcdf8351fa97b3ad761b31e) |
| Committed | 2026-08-08 |
| Vendored | 2026-08-29 |
| Skills vendored | 107 |
| License | MIT — see [LICENSE](LICENSE) |

## Where the skills live

`vendor/` is organised by category, not by source repo, so this upstream's skills are
spread across category directories:

`design` (87), `product-team` (20)

[MANIFEST.tsv](../../MANIFEST.tsv) maps every vendored path back to its upstream repo
and upstream path. To list just this upstream's skills:

```bash
awk -F'\t' '$2 == "designer-skills"' vendor/MANIFEST.tsv
```

## Refreshing

1. Clone Owl-Listener/designer-skills at a newer commit.
2. For each row in [MANIFEST.tsv](../../MANIFEST.tsv) with `upstream_repo` =
   `designer-skills`, copy the upstream directory named in `upstream_path` over the local
   directory named in `vendor_path`.
3. Update the commit and dates in this file.
4. Run `scripts/check-links.sh` and regenerate [INDEX.md](../../../INDEX.md) if any
   skill was added, removed, or renamed.

Do not edit the vendored files directly — changes belong upstream.
