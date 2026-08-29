# ai-skills-and-workflows

A curated index of Claude skills drawn from several upstream repos, plus a place
for my own.

- **[SOURCES.md](SOURCES.md)** — the upstream repos, their licenses, and the
  specific skills bookmarked from each. Also holds the link validity rule that
  distinguishes an installable skill from generated docs or an agent-format mirror.
- **[INDEX.md](INDEX.md)** — the curated index: 305 skills grouped by
  category, each with a one-line description from its upstream frontmatter and a
  verified source path.
- **`skills/`** — my own skills.
- **`vendor/`** — vetted external skills actually installed here.
- **`scripts/`** — maintenance scripts. See [Scripts](#scripts).

## Licensing

Upstreams are MIT except `mgifford/accessibility-skills`, which is AGPL-3.0 and is
linked rather than vendored. Anything copied into `vendor/` keeps its upstream
license and attribution.

## Scripts

### `scripts/check-links.sh`

Validates every skill entry in `INDEX.md`. Run it after editing the index, or in
CI — it exits non-zero if anything fails.

For each row it checks that:

- the path satisfies the [link validity rule](SOURCES.md#link-validity-rule) —
  `skills/<name>/SKILL.md`, at the repo root or under a grouping folder, with no
  `/docs/` segment and no dot-directory (`.claude/`, `.codex/`, and friends), so
  generated docs and agent-format mirrors can't slip in;
- the GitHub URL and the path column agree;
- the linked skill name matches its directory;
- the description is non-empty;
- no `(repo, path)` pair appears twice.

It then checks the category summary table at the top of `INDEX.md` against the rows
below it, so the counts can't drift as entries are added.

```bash
./scripts/check-links.sh
```

Two optional checks. The default run is offline and needs nothing beyond coreutils;
neither of these is required for the index to be valid.

Verify each path exists in local clones of the upstream repos, where `DIR` holds
clones named after each repo (`DIR/designer-skills/`, `DIR/pm-skills/`, …):

```bash
./scripts/check-links.sh --clones ~/src/upstreams
```

Verify every URL actually resolves on GitHub. Needs `curl`, takes a while, and
GitHub may rate-limit a few hundred unauthenticated requests:

```bash
./scripts/check-links.sh --remote
```

`--index FILE` checks a different file; `--help` lists everything.
