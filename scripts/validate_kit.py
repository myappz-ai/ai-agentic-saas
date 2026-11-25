#!/usr/bin/env python3
"""Checks for the AI Agentic SaaS kit. Run: python3 scripts/validate_kit.py

1. Every skills/<name>/SKILL.md has valid YAML frontmatter, a name that matches its folder and a description.
2. JSON manifests parse, and the version is the same in plugin.json, marketplace.json, the README badge and the CHANGELOG.
3. The skill count in plugin.json and the README matches the skills/ folder.
4. Relative links in Markdown files point to files that exist.
5. No secrets or personal data: tokens, keys, email addresses, phone numbers, chat IDs, long numeric IDs.

External links are checked separately (--external) and only warn, because some sites block bots.
"""
import json, re, sys, urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
errors = []
def err(msg): errors.append(msg)

# 1. skills
skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
for d in skills:
    f = d / "SKILL.md"
    if not f.exists():
        err(f"{d.relative_to(ROOT)}: missing SKILL.md"); continue
    t = f.read_text(encoding="utf-8")
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if not m:
        err(f"{f.relative_to(ROOT)}: no YAML frontmatter"); continue
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        err(f"{f.relative_to(ROOT)}: frontmatter is not valid YAML ({str(e).splitlines()[0]})"); continue
    name, desc = fm.get("name"), fm.get("description")
    if name != d.name: err(f"{f.relative_to(ROOT)}: name '{name}' must match folder '{d.name}'")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name or "") or len(name) > 64:
        err(f"{f.relative_to(ROOT)}: name must be lowercase-hyphenated, 64 characters max")
    if not isinstance(desc, str) or not desc.strip(): err(f"{f.relative_to(ROOT)}: description is missing")
    elif len(desc) > 1024: err(f"{f.relative_to(ROOT)}: description is {len(desc)} characters (max 1024)")

# 2. manifests and versions
def load(p):
    try: return json.loads((ROOT / p).read_text(encoding="utf-8"))
    except Exception as e: err(f"{p}: invalid JSON ({e})"); return {}
plugin = load(".claude-plugin/plugin.json")
market = load(".claude-plugin/marketplace.json")
for p in [".mcp.json", ".cursor/mcp.json", "hooks/hooks.json"]:
    if (ROOT / p).exists(): load(p)
for k in ["name", "version", "description", "license"]:
    if k not in plugin: err(f"plugin.json: missing '{k}'")
if not market.get("plugins"): err("marketplace.json: no plugins listed")
v = plugin.get("version")
versions = {"plugin.json": v, "marketplace.json metadata": (market.get("metadata") or {}).get("version")}
versions.update({f"marketplace.json plugin {x.get('name')}": x.get("version") for x in market.get("plugins", [])})
readme = (ROOT / "README.md").read_text(encoding="utf-8")
b = re.search(r"badge/version-([0-9.]+)-", readme); versions["README badge"] = b and b.group(1)
c = re.search(r"^## ([0-9]+\.[0-9]+\.[0-9]+)", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"), re.M); versions["CHANGELOG top entry"] = c and c.group(1)
for where, ver in versions.items():
    if ver != v: err(f"version mismatch: {where} says {ver}, plugin.json says {v}")

# 3. skill count
n = len(skills)
for where, text in [("plugin.json description", plugin.get("description", "")), ("README.md", readme)]:
    for m in re.finditer(r"\b(\d+) skills\b", text):
        if int(m.group(1)) != n: err(f"{where}: says {m.group(1)} skills, skills/ has {n}")

# 4. relative links
mds = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
for p in mds:
    t = p.read_text(encoding="utf-8", errors="ignore")
    t = re.sub(r"```.*?```", "", t, flags=re.S)
    for m in re.finditer(r"\]\((?!https?:|#|mailto:)([^)\s]+)\)", t):
        target = m.group(1).split("#")[0]
        if target and not (p.parent / target).exists():
            err(f"{p.relative_to(ROOT)}: broken link '{m.group(1)}'")

# 5. secrets and personal data
RULES = {
    "private key": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "token or key": r"\b(gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|sk-[A-Za-z0-9_-]{20,}|xox[abpors]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_-]{35}|EAA[A-Za-z0-9]{30,}|eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,})",
    "secret in URL": r"[?&](api[_-]?key|token|access_token|secret|key)=[A-Za-z0-9_\-]{16,}",
    "email address": r"\b[A-Za-z0-9._%+-]+@(?!example\.(com|org|net)\b)(?!users\.noreply\.github\.com\b)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "phone number": r"(?<![\w/.])\+\d{1,3}[\s-]?\(?\d{2,5}\)?[\s-]?\d{3,5}[\s-]?\d{3,5}\b",
    "Slack ID": r"\b[UCGWT]0[A-Z0-9]{7,10}\b",
    "long numeric ID": r"(?<![\d.,])\d{12,}(?![\d.,])",
}
SKIP = {".git", "node_modules"}
for p in ROOT.rglob("*"):
    if not p.is_file() or SKIP & set(p.parts) or p.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".ttf", ".woff2", ".zip"}:
        continue
    if p.name == "validate_kit.py": continue
    for i, line in enumerate(p.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
        for what, rx in RULES.items():
            m = re.search(rx, line)
            if m:
                err(f"{p.relative_to(ROOT)}:{i}: possible {what}: {m.group(0)[:40]}")

# external links (warn only)
if "--external" in sys.argv:
    seen = set()
    for p in mds:
        for u in re.findall(r"https?://[^\s)>\"'`*]+", p.read_text(encoding="utf-8", errors="ignore")):
            u = u.rstrip(".,;:")
            if u in seen or re.search(r"example|your-|<|\{|localhost|\[", u): continue
            seen.add(u)
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 link-check"})
                code = urllib.request.urlopen(req, timeout=15).status
            except Exception as e:
                code = getattr(e, "code", str(e)[:40])
            if code not in (200, 301, 302, 403, 429, 999):
                print(f"::warning::{p.relative_to(ROOT)}: {u} returned {code}")

if errors:
    print("\n".join(errors)); print(f"\n{len(errors)} problem(s)."); sys.exit(1)
print(f"kit check passed: {n} skills, version {v}")
