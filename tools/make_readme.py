# Required Notice: Copyright Matthew Armstrong (https://github.com/The-Dorkknight)
# Licensed under the PolyForm Noncommercial License 1.0.0. No warranty.
"""Write README.md: the whole paper, so the repo's front page on GitHub reads like the PDF.

python3 tools/make_readme.py        (run after editing paper/paper.md; standard library only)

GitHub cannot show a PDF inside a README, so the README is the paper itself, generated from
paper/paper.md with its figure paths adjusted, plus a contents list and a short "about this
repository" section at the end. Edit paper/paper.md, never README.md.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "paper", "paper.md")
OUT = os.path.join(ROOT, "README.md")
PDF = "paper/a-point-of-contention-v1.0.pdf"
SITE = "https://The-Dorkknight.github.io/a-point-of-contention/"


def slug(heading):
    """GitHub's anchor for a heading."""
    s = re.sub(r"[^\w\- ]", "", heading.strip().lower())
    return s.replace(" ", "-")


def main():
    md = open(SRC, encoding="utf-8").read()
    md = md.replace("](figures/", "](paper/figures/")
    lines = md.split("\n")
    if lines[2].startswith("## "):          # the subtitle is a line under the title, not a section
        lines[2] = "**" + lines[2][3:].strip() + "**"
    md = "\n".join(lines)

    sections = re.findall(r"^## (.+)$", md, flags=re.M)
    contents = " · ".join("[%s](#%s)" % (h.split(". ", 1)[-1] if h[0].isdigit() else h, slug(h)) for h in sections)
    nav = ("📄 **[PDF](%s)** · 🌐 [Web page](%s) · 🔧 [The FreeCAD and Fusion plug-ins](https://github.com/The-Dorkknight/hardpoint-stl) · "
           "[About this repository](#about-this-repository)\n\n"
           "<sub>This page is the full paper (the same text and figures as the PDF).</sub>\n\n"
           "**Contents:** %s\n" % (PDF, SITE, contents))
    i = md.index("\n> **Status:")
    md = md[:i] + "\n" + nav + md[i:]

    about = """
---

## About this repository

| Path | What |
|---|---|
| [`paper/paper.md`](paper/paper.md) | The paper (this page is generated from it) |
| [`%s`](%s) | The paper as a PDF |
| [`paper/figures/`](paper/figures/) | Figures |
| [`code/hstl.py`](code/hstl.py) | Reference reader and writer (Python, standard library only) |
| [`data/`](data/) | Example files, each as a hardpoint STL and a plain STL with the same triangles |
| [`notes/`](notes/) | The full research notes, the format specification, and how to archive this paper as prior art |
| [`tools/`](tools/) · [`tests/`](tests/) | Rebuild the PDF, web page and README; checks |
| [`docs/`](docs/) | The web version for GitHub Pages |

The FreeCAD workbench and Fusion add-in live in the separate
[`hardpoint-stl`](https://github.com/The-Dorkknight/hardpoint-stl) repository.

To rebuild: `python3 tools/build_paper.py` (pandoc and Chromium), then `python3 tools/make_readme.py`.
GitHub's **Cite this repository** button uses [`CITATION.cff`](CITATION.cff).

**Join in:** run the checks in section 9 and post results with photos as an issue or discussion, write an exporter
for another CAD program, make a converter that uses the labels better, or point out prior art I missed.
Everyone who contributes gets credited in the next version.

**Licence:** paper text and figures [CC BY-SA 4.0](LICENSE.md); code in `code/` and `tools/`
[PolyForm Noncommercial 1.0.0](LICENSE-CODE.md) (source-available, not open source); the methods described are
dedicated to the public as a defensive publication. Not legal advice.
""" % (PDF, PDF)
    note = "<!-- GENERATED from paper/paper.md by tools/make_readme.py. Edit the paper, then run the tool. -->\n"
    open(OUT, "w", encoding="utf-8").write(note + md.rstrip() + "\n" + about)
    print("wrote", OUT, len(md.split("\n")), "lines,", len(sections), "sections")


if __name__ == "__main__":
    main()
