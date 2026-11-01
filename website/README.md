# Website source

The site is built from the Markdown files in the numbered folders at the top of
this repository. **Edit those originals**, not anything in `website/_docs/`.

| Path | What it is |
|---|---|
| `prepare.py` | Copies the originals into `_docs/`, makes the `<details>` solution blocks work, links file names such as `Markdown_Glossary.md` to their pages, and generates the templates page and the practice editor's examples |
| `check_links.py` | Weekly check of external links |
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

The PDFs are copied into the site as they are. Rebuild them with `bash build/build_pdfs.sh`; see [build/README.md](../build/README.md).

## Checking links

```bash
python website/check_links.py
```

Checks the external links written in the Markdown files and lists any that are broken. Links inside code examples are skipped. A weekly workflow (`.github/workflows/links.yml`) runs the same check. Site-internal links are checked on every build, because a broken one stops the build.
