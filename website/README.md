# Website source

The site is built from the Markdown files in the numbered folders at the top of
this repository. **Edit those originals**, not anything in `website/_docs/`.

| Path | What it is |
|---|---|
| `prepare.py` | Copies the originals into `_docs/` (hiding the PDF build settings at the top of each file) and generates the templates page and the practice editor's examples |
| `mkdocs.yml` | Site settings and navigation |
| `pages/` | The two pages written only for the website: the home page and the practice-editor page |
| `assets/` | The practice editor script and a little CSS |

## Preview on your own computer

```bash
pip install -r website/requirements.txt
python website/prepare.py
mkdocs serve --config-file website/mkdocs.yml
```

Open the address it prints (usually <http://127.0.0.1:8000>). Re-run `prepare.py`
after editing any original `.md` file.

## Publishing

`.github/workflows/site.yml` builds the site on every pull request (a broken link
fails the build) and publishes it to GitHub Pages when changes reach `main`.
One-time setup: **Settings → Pages → Source: GitHub Actions**.

## PDFs

The PDFs are copied as they are. After changing a `.md` file that has a PDF, rebuild it:

```bash
pandoc 05_Markdown_Cheat_Sheets/Markdown_Simple_Cheat_Sheet.md \
  -o 05_Markdown_Cheat_Sheets/Markdown_Simple_Cheat_Sheet.pdf --pdf-engine=xelatex
```
