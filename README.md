# ai-skills-and-workflows

A curated index of Claude skills drawn from several upstream repos, plus a place
for my own.

- **[SOURCES.md](SOURCES.md)** — the upstream repos, their licenses, and the
  specific skills bookmarked from each. Also holds the link validity rule that
  distinguishes an installable skill from generated docs or an agent-format mirror.
- **[INDEX.md](INDEX.md)** — the curated index: bookmarked skills grouped by
  category, each with the `description` from its upstream frontmatter.
- **`skills/`** — my own skills.
- **`vendor/`** — vetted external skills actually installed here.

## Licensing

Upstreams are MIT except `mgifford/accessibility-skills`, which is AGPL-3.0 and is
linked rather than vendored. Anything copied into `vendor/` keeps its upstream
license and attribution.
