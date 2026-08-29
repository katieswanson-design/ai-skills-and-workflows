# vendor/

Every skill listed in [INDEX.md](../INDEX.md) — 639 skills from six upstream repos,
all MIT-licensed — organised by category rather than by source repo.

These are third-party files. **Don't edit them here**; changes belong upstream. Your
own skills go in [`../skills/`](../skills/).

## Layout

```
vendor/<category>/<skill-name>/
  SKILL.md
  LICENSE          <- the upstream's license, so this folder stands alone
  ...any scripts and references the skill ships with
```

Three levels, so nothing is buried. The upstream domain nesting is gone — a skill
that lived at `claude-skills/c-level-advisor/skills/ceo-advisor/` is now simply
`leadership-strategy/ceo-advisor/`.

Every skill folder is self-contained: copy one anywhere and its license travels with
it.

| Category | Skills | | Category | Skills |
|---|---:|---|---|---:|
| `engineering/` | 152 | | `marketing-growth/` | 61 |
| `design/` | 96 | | `product-team/` | 51 |
| `product-management/` | 72 | | `compliance-risk/` | 26 |
| `leadership-strategy/` | 62 | | `thinking-models/` | 28 |
| `accessibility/` | 59 | | `business-finance/` | 20 |
| | | | `productivity/` | 12 |

Plus two things that aren't categories:

- **`MANIFEST.tsv`** — maps every vendored path back to its upstream repo and
  upstream path. This is what makes the reorganisation reversible and refreshable.
- **`PROVENANCE.md`** — which upstream each skill came from and the exact commit it
  was taken at, in one table.

## Name collisions

Skill names are unique within a category, which took two adjustments:

- **12 exact duplicates were dropped.** `alirezarezvani/claude-skills` ships some
  skills at two paths with byte-identical contents. One copy is kept; the dropped
  path is recorded in the last column of `MANIFEST.tsv`.
- **9 skills carry a `--suffix`** where the name genuinely collides between two
  different skills — `design-critique--designer-skills` vs
  `design-critique--design-skills`, `review--accessible-content` vs
  `review--cognitive-accessibility`, and so on. Across repos the suffix is the repo;
  within one repo it is the upstream parent folder.

## Licensing

Every vendored repo is MIT, across five copyright holders. MIT permits redistribution
provided the copyright notice and license text travel with the files — which is why
each skill folder has its own `LICENSE` rather than one central copy. Copy a skill
out and it stays compliant on its own; `check-links.sh` fails if any skill folder
loses its license.

`mgifford/accessibility-skills` is **not** vendored here. It is AGPL-3.0; link to it
or use a submodule instead.

## Keeping it current

[PROVENANCE.md](PROVENANCE.md) pins the exact upstream commit for each repo. To
refresh, clone the upstream at a newer commit and use `MANIFEST.tsv` to map each
vendored directory back to the path it came from. `../scripts/check-links.sh` verifies that every skill
INDEX.md lists exists here and is listed in the manifest.
