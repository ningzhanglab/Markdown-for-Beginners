#!/usr/bin/env python3
"""Build website/_docs from the Markdown files that live in the repository folders.

The original .md files stay the single source of truth. This script only copies
them (with small, mechanical adjustments for the website) so there is nothing to
keep in sync by hand.

Run from anywhere:   python website/prepare.py
"""
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(HERE, "_docs")

H = "01_Markdown_Handbooks"
C = "02_Markdown_Cheat_Sheets"
T = "03_Markdown_Templates"
S = "00_Start_Here"

# source file (relative to repo root) -> page path inside the site
PAGES = {
    f"{S}/Markdown_First_Note.md": "start-here/first-note.md",
    f"{S}/Markdown_Practice_Exercises.md": "start-here/exercises.md",
    f"{S}/Markdown_Troubleshooting.md": "start-here/troubleshooting.md",
    f"{S}/Markdown_Glossary.md": "start-here/glossary.md",
    f"{C}/Markdown_Simple_Cheat_Sheet.md": "cheat-sheets/simple.md",
    f"{C}/Markdown_Advanced_Cheat_Sheet.md": "cheat-sheets/advanced.md",
    f"{H}/Markdown_Beginner_Handbook.md": "handbooks/beginner-handbook.md",
    f"{H}/Markdown_Setup_and_Editors_Guide.md": "handbooks/setup-and-editors.md",
}

# files that other pages may mention by name -> (page path, link label)
NAMED = {
    "Markdown_Glossary": ("start-here/glossary.md", "Glossary"),
    "Markdown_Troubleshooting": ("start-here/troubleshooting.md", "Why doesn't mine look right?"),
    "Markdown_Practice_Exercises": ("start-here/exercises.md", "Practice Exercises"),
    "Markdown_Simple_Cheat_Sheet": ("cheat-sheets/simple.md", "Simple Cheat Sheet"),
    "Markdown_Advanced_Cheat_Sheet": ("cheat-sheets/advanced.md", "Advanced Cheat Sheet"),
    "Markdown_Beginner_Handbook": ("handbooks/beginner-handbook.md", "Beginner Handbook"),
    "Markdown_Setup_and_Editors_Guide": ("handbooks/setup-and-editors.md", "Setup and Editors Guide"),
}

def discover_pdfs():
    found = []
    for folder in (S, H, C, T):
        d = os.path.join(ROOT, folder)
        for name in sorted(os.listdir(d)):
            if name.endswith(".pdf"):
                found.append(f"{folder}/{name}")
    return found


TEMPLATES = [
    ("Minimal note", "A very simple note.", f"{T}/Markdown_Template_01_Minimal_Note.md"),
    ("Research notes", "Daily research notes or a project log.", f"{T}/Markdown_Template_02_Research_Notes.md"),
    ("Project README", "Describe a project on GitHub.", f"{T}/Markdown_Template_03_Project_README.md"),
    ("Class notes", "Notes for a class or lecture.", f"{T}/Markdown_Template_04_Class_Notes.md"),
    ("Weekly plan", "A weekly plan with daily task lists.", f"{T}/Markdown_Template_05_Weekly_Plan.md"),
    ("Meeting notes", "Decisions and action items from a meeting.", f"{T}/Markdown_Template_06_Meeting_Notes.md"),
]

REPO_BLOB = "https://github.com/ningzhanglab/Markdown-for-Beginners/blob/main/"
RAW = "https://raw.githubusercontent.com/ningzhanglab/Markdown-for-Beginners/main/"


def read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def write(rel, text):
    path = os.path.join(OUT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def page_title(src):
    """PDF build settings live in build/<name>.yaml; the title there names the page."""
    yml = os.path.join(ROOT, "build", os.path.basename(src)[:-3] + ".yaml")
    if os.path.exists(yml):
        with open(yml, encoding="utf-8") as f:
            m = re.search(r'^title:\s*"?(.*?)"?\s*$', f.read(), re.M)
        if m:
            return m.group(1)
    return None


def open_details(text):
    """GitHub shows <details> as-is; MkDocs needs markdown="1" to format what is inside."""
    return outside_fences(text, lambda part: re.sub(r"<details>", '<details markdown="1">', part))


def outside_fences(text, fn):
    """Apply fn to the parts of text that are not inside fenced code blocks."""
    out, buf, fence = [], [], None
    for line in text.split("\n"):
        m = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence is None and m:
            out.append(fn("\n".join(buf))) if buf else None
            buf = []
            fence = m.group(1)
            out.append(line)
        elif fence is not None:
            out.append(line)
            if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence) and line.strip() == m.group(1):
                fence = None
        else:
            buf.append(line)
    if buf:
        out.append(fn("\n".join(buf)))
    return "\n".join(out)


def link_named_files(text, page):
    """Turn mentions like `../05_X/Markdown_Simple_Cheat_Sheet.pdf` into links to the page."""
    here = os.path.dirname(page)
    pat = re.compile(
        r"(?P<wrap>`|\*\*)(?:\.\./)?(?:\d\d_[A-Za-z_]+/)?(?P<stem>Markdown_[A-Za-z_]+)\.(?:pdf|md)(?P=wrap)"
    )

    def repl(m):
        target = NAMED.get(m.group("stem"))
        if not target or target[0] == page:
            return m.group(0)
        rel = os.path.relpath(target[0], here or ".").replace(os.sep, "/")
        label = f"**{target[1]}**" if m.group("wrap") == "**" else target[1]
        return f"[{label}]({rel})"

    return outside_fences(text, lambda part: pat.sub(repl, part))


def pdf_note(src, page):
    pdf = src[:-3] + ".pdf"
    if not os.path.exists(os.path.join(ROOT, pdf)):
        return ""
    rel = os.path.relpath("downloads/" + os.path.basename(pdf), os.path.dirname(page)).replace(os.sep, "/")
    return f"*Printable version: [download the PDF]({rel}).*\n"


def add_after_first_heading(body, note):
    if not note:
        return body
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("# "):
            return "\n".join(lines[: i + 1] + ["", note] + lines[i + 1:])
    return note + "\n" + body


def fence_for(text):
    longest = max([len(m) for m in re.findall(r"`+", text)] + [2])
    return "`" * (longest + 1)


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)

    # hand-written site pages
    for name, dest in (("index.md", "index.md"), ("practice.md", "start-here/practice.md")):
        with open(os.path.join(HERE, "pages", name), encoding="utf-8") as f:
            write(dest, f.read())

    # content pages copied from the repository folders
    for src, page in PAGES.items():
        title, body = page_title(src), read(src)
        body = open_details(body)
        body = link_named_files(body, page)
        body = add_after_first_heading(body, pdf_note(src, page))
        head = f'---\ntitle: "{title}"\n---\n\n' if title else ""
        write(page, head + body)

    # templates page, generated from the real template files
    parts = [
        "---\ntitle: Templates\n---\n",
        "# Templates\n",
        "Copy a template, paste it into a new `.md` file or the [practice editor](start-here/practice.md), "
        "and replace the example text with your own.\n",
    ]
    for label, blurb, src in TEMPLATES:
        text = read(src).rstrip("\n") + "\n"
        pdf = os.path.basename(src)[:-3] + ".pdf"
        fence = fence_for(text)
        parts.append(f"## {label}\n")
        parts.append(f"{blurb} [Download the `.md` file]({RAW}{src}) · [PDF](downloads/{pdf})\n")
        parts.append(f"{fence}markdown\n{text}{fence}\n")
    write("templates.md", "\n".join(parts))

    # PDFs
    for pdf in discover_pdfs():
        dest = os.path.join(OUT, "downloads", os.path.basename(pdf))
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(ROOT, pdf), dest)

    # starters for the practice editor, read from the same source files
    starters = [{"label": "My first note", "text": read(f"{S}/Markdown_First_Note.md")}]
    for label, _, src in TEMPLATES:
        starters.append({"label": f"Template: {label}", "text": read(src)})
    write("assets/starters.json", json.dumps(starters, ensure_ascii=False, indent=1))

    # static assets
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(OUT, "assets"), dirs_exist_ok=True)
    print(f"Prepared {OUT}")


if __name__ == "__main__":
    sys.exit(main())
