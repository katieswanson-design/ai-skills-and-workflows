# vendor/

Vendored copies of every skill listed in [INDEX.md](../INDEX.md) — 651 skills from
six upstream repos, all MIT-licensed.

These are third-party files. **Don't edit them here**; changes belong upstream. Your
own skills go in [`../skills/`](../skills/).

## Layout

```
vendor/<repo-name>/<upstream-path>/SKILL.md
```

Skill directories keep their upstream paths, so a path in INDEX.md, a path here, and
a path in the upstream repo are all the same string. Each vendored repo also has:

- `LICENSE` — the upstream license, preserved as MIT requires
- `PROVENANCE.md` — upstream URL, the exact commit vendored, and how to refresh it

| Directory | Skills | Upstream | Scope |
|---|---:|---|---|
| `claude-skills/` | 380 | [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | Full repo |
| `designer-skills/` | 107 | [Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills) | Full repo |
| `pm-skills/` | 68 | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | Full repo |
| `inclusive-design-skills/` | 58 | [Owl-Listener/inclusive-design-skills](https://github.com/Owl-Listener/inclusive-design-skills) | Full repo |
| `cc-thinking-skills/` | 28 | [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | Full repo |
| `design-skills/` | 10 | [cuellarfr/design-skills](https://github.com/cuellarfr/design-skills) | Full repo |

`mgifford/accessibility-skills` is **not** vendored here. It is AGPL-3.0; link to it
or use a submodule instead.

## Licensing

Every vendored repo is MIT. MIT permits redistribution provided the copyright notice
and license text travel with the files, which is what the per-repo `LICENSE` files
are for. Keep them alongside any skill you copy elsewhere.

## Keeping it current

`PROVENANCE.md` in each directory pins the exact upstream commit, so you can diff
against a newer clone to see what changed. `../scripts/check-links.sh` verifies that
every skill INDEX.md lists actually exists here.
