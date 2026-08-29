# Sources

Upstream repos and the specific skills bookmarked from them. Paths verified against
clones on 2026-08-28. Skill counts are unique skill directories, excluding generated
docs trees and agent-format mirrors.

## Upstream repos

| Repo | Skills | License | Focus |
|---|---|---|---|
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 374 | MIT | Broad: engineering, marketing, finance, c-level, compliance |
| [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) | 107 | MIT | Design ops, research, systems, interaction, prototyping |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 68 | MIT | PM: discovery, strategy, go-to-market, analytics |
| [Owl-Listener/inclusive-design-skills](https://github.com/Owl-Listener/inclusive-design-skills) | 56 | MIT | Cognitive accessibility, adaptive interfaces, personas |
| [mgifford/accessibility-skills](https://github.com/mgifford/accessibility-skills) | 33 | AGPL-3.0 | WCAG technical a11y, axe rules, CI/CD |
| [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | 28 | MIT | Mental models, all prefixed `thinking-` |
| [cuellarfr/design-skills](https://github.com/cuellarfr/design-skills) | 10 | MIT | Broad UX buckets, coarse-grained |

Notes:

- mgifford/accessibility-skills is AGPL-3.0. Do not vendor its files into this repo.
  Link to it or use a submodule.
- cuellarfr/design-skills shares 3 of its 10 skills by name with
  Owl-Listener/designer-skills. Check for redundancy before indexing both.
- Cross-repo duplication otherwise is minimal, roughly ten name collisions in total.

## Bookmarked skills: alirezarezvani/claude-skills

Prefix all paths with `https://github.com/alirezarezvani/claude-skills/blob/main/`
(use `/tree/main/` for the folder entries).

| Skill | Path |
|---|---|
| capture | `productivity/capture/skills/capture/SKILL.md` |
| deep-work | `productivity/deep-work/skills/deep-work/SKILL.md` |
| roast | `productivity/roast/skills/roast/SKILL.md` |
| product-research | `research-ops/skills/product-research/SKILL.md` |
| senior-pm | `project-management/skills/senior-pm/SKILL.md` |
| feature-flags-architect | `engineering/skills/feature-flags-architect/SKILL.md` |
| prompt-governance | `engineering/prompt-governance/skills/prompt-governance/SKILL.md` |
| demo-video | `engineering/demo-video/skills/demo-video/SKILL.md` |

Folder-level bookmarks, not yet broken out into individual entries:

| Folder | Path | Contents |
|---|---|---|
| project-management | `project-management/skills/` | atlassian-admin, atlassian-templates, confluence-expert, jira-expert, meeting-analyzer, pm-skills, scrum-master, senior-pm, team-communications |
| product-team | `product-team/skills/` | competitive-teardown, experiment-designer, landing-page-generator, product-analytics, product-discovery, product-manager-toolkit, product-skills, product-strategist, roadmap-communicator, saas-scaffolder, spec-to-repo, ui-design-system, ux-researcher-designer |
| markdown-html | `markdown-html/skills/` | md-review, design-system, md-slides, markdown-html-orchestrator, md-document |

## Coverage

[INDEX.md](INDEX.md) indexes 639 skills across eleven categories: product management,
product team, productivity, design, engineering, marketing & growth, leadership &
strategy, business & finance, compliance & risk, accessibility, thinking models.
Categories with zero entries are left out rather than stubbed.

| Repo | Indexed | Basis |
|---|---:|---|
| alirezarezvani/claude-skills | 368 | Full repo, less 12 exact duplicates (the 34 bookmarked below are starred in INDEX.md) |
| Owl-Listener/designer-skills | 107 | Full repo |
| phuryn/pm-skills | 68 | Full repo |
| Owl-Listener/inclusive-design-skills | 58 | Full repo (56 unique names; `review` appears in 3 folders) |
| tjboudreaux/cc-thinking-skills | 28 | Full repo |
| cuellarfr/design-skills | 10 | Full repo |
| mgifford/accessibility-skills | 0 | AGPL-3.0 — not cloned, not indexed, not vendored |

Every indexed skill is vendored into [`vendor/`](vendor/), organised by category as
`vendor/<category>/<skill>/` rather than by source repo. Each skill folder carries its own
upstream `LICENSE`, `vendor/PROVENANCE.md` pins the commit each repo was taken at,
and `vendor/MANIFEST.tsv` maps every vendored path back to its upstream repo and path.

The 651 skills passing the link validity rule become 639 entries: claude-skills
ships 12 skills at two paths each with byte-identical contents, so one copy of each
is kept and the dropped path is recorded in `vendor/MANIFEST.tsv`.

Counts differ from the table at the top of this file, which was compiled earlier:
claude-skills holds 380 skill directories passing the link validity rule, not 374,
and inclusive-design-skills holds 58 (56 unique names). The per-repo figures above
were measured against the pinned clones.

Skill names are not unique across the index. `accessibility-audit`,
`design-critique`, and `ux-writing` each appear in both cuellarfr/design-skills and
Owl-Listener/designer-skills; `interview-script` and `summarize-interview` appear in
both designer-skills and pm-skills; `review` appears three times inside
inclusive-design-skills; and claude-skills has 14 internal name collisions across its
domain folders. INDEX.md lists every one and disambiguates by path.

## Link validity rule

A valid index target matches `(^|/)skills/<name>/SKILL.md` and contains neither
`/docs/` nor a dot-directory. The `skills/` directory may sit at the repo root
(cc-thinking-skills, design-skills) or under a grouping folder (the other four).
Anything else is generated documentation or an agent-format mirror (`.claude/`,
`.codex/`, `.gemini/`, `.hermes/`, `.vibe/`), not an installable skill. Enforced by
[`scripts/check-links.sh`](scripts/check-links.sh).
