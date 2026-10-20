# Required Notice: Copyright Matthew Armstrong (https://github.com/The-Dorkknight)
# Licensed under the PolyForm Noncommercial License 1.0.0. No warranty.
"""Checks for this repository (standard library only): python3 tests/check_repo.py

1. every relative link and image in the Markdown files exists, and every #anchor matches a heading
2. README.md is exactly what tools/make_readme.py makes from paper/paper.md
3. the example files verify as hardpoint STL, and the plain twins do not
"""
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
bad = []


def slug(h):
    return re.sub(r"[^\w\- ]", "", h.strip().lower()).replace(" ", "-")


for f in ["README.md", "CONTRIBUTING.md", "THIRD_PARTY.md", "SECURITY.md", "LICENSE.md", "data/README.md",
          "notes/PUBLISHING_AS_PRIOR_ART.md", "paper/paper.md"]:
    s = open(f, encoding="utf-8").read()
    base = os.path.dirname(f)
    for p in re.findall(r"\]\(([^)#\s]+)\)", s):
        if not p.startswith(("http", "mailto")) and not os.path.exists(os.path.join(base, p)):
            bad.append("%s: missing %s" % (f, p))
    heads = {slug(h) for h in re.findall(r"^#{1,6} (.+)$", s, flags=re.M)}
    for a in re.findall(r"\]\(#([^)]+)\)", s):
        if a not in heads:
            bad.append("%s: no heading for #%s" % (f, a))

old = open("README.md", encoding="utf-8").read()
try:
    subprocess.run([sys.executable, "tools/make_readme.py"], check=True, stdout=subprocess.DEVNULL)
    new = open("README.md", encoding="utf-8").read()
finally:
    open("README.md", "w", encoding="utf-8").write(old)
if old != new:
    bad.append("README.md is out of date: run tools/make_readme.py")

for name in ("bracket", "knob"):
    for kind, want in (("hardpoint", 0), ("plain", 1)):
        r = subprocess.run([sys.executable, "code/hstl.py", "verify", "data/%s_%s.stl" % (name, kind)],
                           capture_output=True, text=True)
        if (r.returncode == 0) != (want == 0):
            bad.append("data/%s_%s.stl: unexpected verify result (exit %d)" % (name, kind, r.returncode))

print("\n".join(bad) if bad else "repository checks passed")
sys.exit(1 if bad else 0)
