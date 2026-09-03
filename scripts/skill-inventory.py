#!/usr/bin/env python3
"""Inventory every skill in this repo, so successive runs can be diffed.

    python3 scripts/skill-inventory.py > inventory/baseline-YYYY-MM-DD.md
    diff inventory/baseline-A.md inventory/baseline-B.md

Reports, in a deterministic order:
  1. counts per category
  2. duplicate declared names (two SKILL.md files claiming one name)
  3. cross-references between skills, each marked RESOLVED or DANGLING
  4. LICENSE copyright holders, and which skills each covers
  5. the full skill table

The cross-reference check is the reason this exists. Skills point at each
other by name in prose; nothing but this validates those pointers, so a
move or delete breaks them silently.
"""
import os, re, sys, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")

def declared_name(path):
    """Frontmatter name via the line-2 convention, falling back to a scan."""
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            lines = [next(fh, "") for _ in range(12)]
    except OSError:
        return None
    m = re.match(r'^name:\s*(.+?)\s*$', lines[1] if len(lines) > 1 else "")
    if not m:
        for ln in lines:
            m = re.match(r'^name:\s*(.+?)\s*$', ln)
            if m:
                break
    return m.group(1).strip().strip('"\'') if m else None

def license_holder(skill_dir):
    """Nearest LICENSE at or above the skill dir, within skills/."""
    d = skill_dir
    while d.startswith(SKILLS):
        p = os.path.join(d, "LICENSE")
        if os.path.isfile(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                for ln in fh:
                    m = re.search(r'Copyright \(c\)\s*(.+?)\s*$', ln)
                    if m:
                        return m.group(1)
            return "(LICENSE, no copyright line)"
        d = os.path.dirname(d)
    return "(none)"

def category(path):
    rel = os.path.relpath(path, SKILLS)
    return rel.split(os.sep)[0]

# ---------------------------------------------------------------- collect
skills = []
for dirpath, dirnames, filenames in os.walk(SKILLS):
    dirnames[:] = [d for d in dirnames if not d.startswith(".")]
    if "SKILL.md" in filenames:
        p = os.path.join(dirpath, "SKILL.md")
        skills.append({
            "path": os.path.relpath(p, ROOT),
            "dir":  os.path.relpath(dirpath, ROOT),
            "name": declared_name(p) or "(no name)",
            "cat":  category(p),
            "lic":  license_holder(dirpath),
        })
skills.sort(key=lambda s: s["path"])
by_name = collections.defaultdict(list)
for s in skills:
    by_name[s["name"]].append(s)
known = set(by_name)

# ------------------------------------------------------------ cross-refs
# A backticked hyphenated token is only a *skill pointer* when prose frames it
# as one. Without that test the scan drowns in Tailwind classes, ARIA
# attributes, CSS properties and tier labels. Two sources, by confidence:
#
#   description  — this repo puts skill-to-skill routing in frontmatter
#                  ("For X, use `y`"), so any token there is a candidate.
#   body         — only when the word "skill" sits next to the token, or the
#                  line is an explicit "Chains:" list.
#
# A pointer whose target is a known skill is RESOLVED. One whose target is
# unknown is DANGLING — either stale after a rename, or aimed at a plugin
# skill that lives outside this repo.
TOKEN = r'`([a-z0-9]+(?:-[a-z0-9]+)+)`'

# Targets that legitimately live outside this repo. A pointer to one of these
# is expected, not breakage — it resolves wherever the named plugin is
# installed, and would only "dangle" for someone cloning this repo alone.
# Keys are exact names, or a "prefix-*" glob. Add to this list rather than
# letting known-external targets sit in the unknown pile, where they drown
# out the pointers that are actually broken.
EXTERNAL = {
    "figma-use": "Figma plugin — official skill shipped with the Figma MCP server",
    "cs-*":      "c-level-agents plugin — advisor agents and chief-of-staff routing",
    "yt-dlp":    "external CLI tool — a dependency, not a skill",
}

# On tools: one entry is fine, several would be a signal. If external binaries
# (ffmpeg, docker, pnpm) start accumulating here, the detector is matching tool
# references it should not, and the fix belongs there rather than in this list.

def external_source(target):
    """Return the provenance note for a known-external target, else None."""
    if target in EXTERNAL:
        return EXTERNAL[target]
    for key, note in EXTERNAL.items():
        if key.endswith("*") and target.startswith(key[:-1]):
            return note
    return None

def desc_field(body):
    m = re.search(r'^description:\s*(.+?)(?=^\w+:|^---)', body, re.M | re.S)
    return m.group(1) if m else ""

def framed_in_body(body):
    """Tokens the prose explicitly calls a skill, or lists under Chains:."""
    hits = set()
    for m in re.finditer(TOKEN, body):
        window = body[max(0, m.start() - 60):m.end() + 60]
        if re.search(r'\bskills?\b', window, re.I) or re.search(r'chains?\s*:', window, re.I):
            hits.add(m.group(1))
    return hits

refs = []
for s in skills:
    try:
        body = open(os.path.join(ROOT, s["path"]), encoding="utf-8", errors="replace").read()
    except OSError:
        continue
    candidates = {t: "description" for t in re.findall(TOKEN, desc_field(body))}
    for t in framed_in_body(body):
        candidates.setdefault(t, "body")
    for target, src in sorted(candidates.items()):
        if target == s["name"]:
            continue
        if target in known:
            kind = "RESOLVED"
        elif external_source(target):
            kind = "EXTERNAL"
        else:
            kind = "DANGLING"
        refs.append((s["name"], target, kind, src, s["path"]))
refs.sort()

# ---------------------------------------------------------------- report
out = sys.stdout.write
out("# Skill inventory\n\n")
out("Generated by `scripts/skill-inventory.py`. Diff two runs to see what a\n"
    "reorg changed. Counts are derived, not hand-maintained.\n\n")
out("- **Skills (SKILL.md files):** %d\n" % len(skills))
out("- **Distinct declared names:** %d\n" % len(by_name))
out("- **Duplicate names:** %d\n" % sum(1 for v in by_name.values() if len(v) > 1))
out("- **Categories:** %d\n" % len({s["cat"] for s in skills}))
out("- **Cross-references:** %d resolved, %d external, %d unknown\n\n"
    % (sum(1 for r in refs if r[2] == "RESOLVED"),
       sum(1 for r in refs if r[2] == "EXTERNAL"),
       sum(1 for r in refs if r[2] == "DANGLING")))

out("## Categories\n\n| Category | Skills |\n|---|---|\n")
for cat, n in sorted(collections.Counter(s["cat"] for s in skills).items()):
    out("| %s | %d |\n" % (cat, n))

out("\n## Duplicate declared names\n\n")
dups = {k: v for k, v in by_name.items() if len(v) > 1}
if not dups:
    out("None.\n")
for name in sorted(dups):
    out("**`%s`**\n\n" % name)
    for s in dups[name]:
        out("- `%s` — LICENSE: %s\n" % (s["path"], s["lic"]))
    out("\n")

out("\n## Cross-references\n\n")
out("Only pointers the prose frames as skill references are counted. See the\n"
    "cross-refs comment in the script for the rule.\n\n")
dangling = [r for r in refs if r[2] == "DANGLING"]
out("### Unknown — target is not a skill here and is not a known external\n\n")
out("These are the actionable ones: a stale pointer after a rename, or a\n"
    "dependency nobody declared. Everything expected is in the next section.\n\n")
if dangling:
    out("| From | To | Found in | Source file |\n|---|---|---|---|\n")
    for src, tgt, _, where, path in dangling:
        out("| `%s` | `%s` | %s | `%s` |\n" % (src, tgt, where, path))
    out("\n")
else:
    out("None.\n\n")

ext = [r for r in refs if r[2] == "EXTERNAL"]
out("### External — expected, resolves where the named plugin is installed\n\n")
if ext:
    out("| Target | Pointers | Provenance |\n|---|---|---|\n")
    for tgt in sorted({r[1] for r in ext}):
        out("| `%s` | %d | %s |\n"
            % (tgt, sum(1 for r in ext if r[1] == tgt), external_source(tgt)))
    out("\nThese would read as broken to someone cloning this repo on its own.\n"
        "That is a portability decision, not a defect. Extend `EXTERNAL` in this\n"
        "script when a new plugin dependency appears.\n\n")
else:
    out("None.\n\n")
out("### Resolved\n\n")
for src, tgt, _, where, _ in [r for r in refs if r[2] == "RESOLVED"]:
    out("- `%s` → `%s`  *(%s)*\n" % (src, tgt, where))

out("\n## LICENSE copyright holders\n\n| Holder | Skills |\n|---|---|\n")
for holder, n in sorted(collections.Counter(s["lic"] for s in skills).items(),
                        key=lambda kv: (-kv[1], kv[0])):
    out("| %s | %d |\n" % (holder, n))

out("\n## All skills\n\n| Category | Declared name | Path | LICENSE |\n|---|---|---|---|\n")
for s in skills:
    out("| %s | `%s` | `%s` | %s |\n" % (s["cat"], s["name"], s["dir"], s["lic"]))
