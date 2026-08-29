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

## Category gaps

[INDEX.md](INDEX.md) is organized into five categories: product management, product
team, productivity, design, engineering. Categories with zero entries are left out
rather than stubbed.

Two areas are currently unrepresented because nothing has been bookmarked for them:

| Gap | Repo that would fill it | Note |
|---|---|---|
| Accessibility | [mgifford/accessibility-skills](https://github.com/mgifford/accessibility-skills) | 33 skills, WCAG technical a11y, axe rules, CI/CD. AGPL-3.0 — link or submodule only, do not vendor. |
| Thinking models | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | 28 skills, mental models, all prefixed `thinking-`. MIT. |

Add bookmarks from either repo and the matching category can be created in INDEX.md.

More broadly: five of the seven upstream repos above have no bookmarks recorded yet
(designer-skills, pm-skills, inclusive-design-skills, cc-thinking-skills,
design-skills). Every entry currently in INDEX.md comes from
alirezarezvani/claude-skills.

## Link validity rule

A valid index target ends in `/skills/<name>/SKILL.md` and contains neither `/docs/`
nor a dot-directory. Anything else is generated documentation or an agent-format
mirror (`.claude/`, `.codex/`, `.gemini/`, `.hermes/`, `.vibe/`), not an installable
skill. Worth enforcing with a link-check script once the repo exists.
