# Required Notice: Copyright Matthew Armstrong (https://github.com/The-Dorkknight)
# Licensed under the PolyForm Noncommercial License 1.0.0. No warranty.
"""Build paper/paper.html, docs/index.html (GitHub Pages) and the PDF from paper/paper.md.

python3 tools/build_paper.py
Needs pandoc and a Chromium or Chrome (set CHROME=/path/to/chrome if it is not found).
Then run tools/make_readme.py to refresh the README.
"""
import glob
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "paper")
PDF = os.path.join(P, "a-point-of-contention-v1.0.pdf")
TITLE = "A POINT of contention"
DESC = ("A proposed hybrid STL format that is CAD-friendly and slicer-compatible: the hardpoint STL, "
        "a hobbyist's field notes and a defensive publication. Matthew Armstrong, 15 October 2026.")


def pandoc(src_md, out_html):
    subprocess.run(["pandoc", src_md, "-f", "markdown-implicit_figures", "-s", "--css", "paper.css",
                    "--embed-resources", "--metadata", "lang=en-GB", "--metadata", "pagetitle=" + TITLE,
                    "-o", out_html], cwd=P, check=True)
    t = open(out_html, encoding="utf-8").read()
    t = t.replace("<head>", '<head>\n<meta name="description" content="%s">' % DESC, 1)
    open(out_html, "w", encoding="utf-8").write(t)


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for c in ("chromium", "chromium-browser", "google-chrome", "google-chrome-stable", "chrome",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"):
        if shutil.which(c) or os.path.exists(c):
            return c
    hits = sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    return hits[-1] if hits else None


def main():
    html = os.path.join(P, "paper.html")
    pandoc("paper.md", html)
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    shutil.copyfile(html, os.path.join(ROOT, "docs", "index.html"))   # the Pages copy
    open(os.path.join(ROOT, "docs", ".nojekyll"), "w").close()
    chrome = find_chrome()
    if not chrome:
        sys.exit("No Chromium or Chrome found: paper.html is built; print it to PDF from a browser.")
    subprocess.run([chrome, "--headless", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    "--force-color-profile=srgb", "--blink-settings=preferredColorScheme=1",
                    "--print-to-pdf=" + PDF, "file://" + html], check=True, stderr=subprocess.DEVNULL)
    print("built", html, PDF)


if __name__ == "__main__":
    main()
