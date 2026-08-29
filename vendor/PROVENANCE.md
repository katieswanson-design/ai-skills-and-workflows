# Provenance

Where every vendored skill came from, and the exact upstream commit it was taken at.

The skills themselves live in the category folders — each skill directory carries its
own `LICENSE`, so any single skill can be copied out and stay compliant.
[MANIFEST.tsv](MANIFEST.tsv) maps every vendored path to its upstream path.

| Upstream | Skills | Commit | Committed | Copyright |
|---|---:|---|---|---|
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 368 | [`19392f7`](https://github.com/alirezarezvani/claude-skills/commit/19392f7a08264ed00486a251f5b2098321771f94) | 2026-08-26 | Copyright (c) 2025 Alireza Rezvani |
| [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) | 107 | [`20e34c4`](https://github.com/Owl-Listener/designer-skills/commit/20e34c4a587e5eb09fcdf8351fa97b3ad761b31e) | 2026-08-08 | Copyright (c) 2026 MC Dean |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 68 | [`18468a9`](https://github.com/phuryn/pm-skills/commit/18468a95b427e70e258b51389796367c6f684e7d) | 2026-07-03 | Copyright (c) 2026 Pawel Huryn |
| [Owl-Listener/inclusive-design-skills](https://github.com/Owl-Listener/inclusive-design-skills) | 58 | [`6e0740f`](https://github.com/Owl-Listener/inclusive-design-skills/commit/6e0740f04b2130af60bc57abe3401b91e460e70d) | 2026-06-09 | Copyright (c) 2026 MC Dean |
| [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | 28 | [`7b8fece`](https://github.com/tjboudreaux/cc-thinking-skills/commit/7b8fece345dfaa11773be7152ccd194589cb5437) | 2026-08-07 | Copyright (c) 2025 TJ Boudreaux |
| [cuellarfr/design-skills](https://github.com/cuellarfr/design-skills) | 10 | [`b41750a`](https://github.com/cuellarfr/design-skills/commit/b41750affc03669988b649380756bc17fa427a09) | 2026-08-23 | Copyright (c) 2026 Carlos C. |

All six are MIT. Vendored 2026-08-29.

## Which categories each upstream landed in

| Upstream | Categories |
|---|---|
| `claude-skills` | `engineering` (150), `leadership-strategy` (62), `marketing-growth` (61), `compliance-risk` (26), `product-team` (22), `business-finance` (20), `product-management` (13), `productivity` (12), `design` (2) |
| `designer-skills` | `design` (87), `product-team` (20) |
| `pm-skills` | `product-management` (59), `product-team` (7), `engineering` (2) |
| `inclusive-design-skills` | `accessibility` (58) |
| `cc-thinking-skills` | `thinking-models` (28) |
| `design-skills` | `design` (7), `product-team` (2), `accessibility` (1) |

To list one upstream's skills:

```bash
awk -F'\t' '$2 == "designer-skills"' vendor/MANIFEST.tsv
```

## Duplicates dropped

`claude-skills` ships 12 skills at two paths each with byte-identical
contents. One copy of each was kept; the dropped upstream path is recorded in the
last column of [MANIFEST.tsv](MANIFEST.tsv).

## Refreshing

1. Clone the upstream at a newer commit.
2. For each [MANIFEST.tsv](MANIFEST.tsv) row with that `upstream_repo`, copy the
   directory at `upstream_path` over the local directory at `vendor_path`.
3. Re-place the skill's `LICENSE` (upstream copies do not carry one per skill).
4. Update the commit and date above.
5. Run `../scripts/check-links.sh` and regenerate [INDEX.md](../INDEX.md) if any
   skill was added, removed, or renamed.

Do not edit vendored files directly — changes belong upstream.

## Not vendored

[mgifford/accessibility-skills](https://github.com/mgifford/accessibility-skills) is
AGPL-3.0. It is not copied into this repo at all — link to it or use a submodule.
