# Building the PDFs

Each `.pdf` in the repository is built from the `.md` file next to it.

```bash
bash build/build_pdfs.sh            # rebuild every PDF
bash build/build_pdfs.sh Simple     # rebuild only files with "Simple" in the name
```

You need [Pandoc](https://pandoc.org/) and a LaTeX engine such as TeX Live or TinyTeX. The script uses XeLaTeX; set `PDF_ENGINE` to change it.

## Why are there `.yaml` files here?

Title, margins, and font size for a PDF are Pandoc settings. They used to sit at the top of each `.md` file, where GitHub showed them as a table above the page. They now live in `build/<file name>.yaml`, so the Markdown stays clean. A file with no `.yaml` here builds with Pandoc's defaults.

## After editing a Markdown file

Rebuild its PDF with the command above and commit both files together, so the PDF never falls behind the source.
