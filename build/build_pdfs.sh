#!/usr/bin/env bash
# Rebuild every PDF from its Markdown source.
#
#   bash build/build_pdfs.sh              rebuild all PDFs
#   bash build/build_pdfs.sh Handbook     rebuild only files whose name contains "Handbook"
#
# Needs Pandoc and a LaTeX engine (XeLaTeX by default; e.g. TeX Live or TinyTeX).
# Set PDF_ENGINE to use another engine. PDF settings (title, margins, fonts) live
# in build/<file name>.yaml; a file without a .yaml builds with Pandoc's defaults.
set -euo pipefail
cd "$(dirname "$0")/.."

ENGINE="${PDF_ENGINE:-xelatex}"
FILTER="${1:-}"

SOURCES=(
  00_Start_Here/Markdown_Troubleshooting.md
  00_Start_Here/Markdown_Glossary.md
  01_Markdown_Handbooks/Markdown_Beginner_Handbook.md
  01_Markdown_Handbooks/Markdown_Setup_and_Editors_Guide.md
  02_Markdown_Cheat_Sheets/Markdown_Simple_Cheat_Sheet.md
  02_Markdown_Cheat_Sheets/Markdown_Advanced_Cheat_Sheet.md
  03_Markdown_Templates/Markdown_Template_01_Minimal_Note.md
  03_Markdown_Templates/Markdown_Template_02_Research_Notes.md
  03_Markdown_Templates/Markdown_Template_03_Project_README.md
  03_Markdown_Templates/Markdown_Template_04_Class_Notes.md
  03_Markdown_Templates/Markdown_Template_05_Weekly_Plan.md
  03_Markdown_Templates/Markdown_Template_06_Meeting_Notes.md
)

for src in "${SOURCES[@]}"; do
  name="$(basename "$src" .md)"
  [[ -n "$FILTER" && "$name" != *"$FILTER"* ]] && continue
  args=(--pdf-engine="$ENGINE")
  [[ -f "build/$name.yaml" ]] && args+=(--metadata-file="build/$name.yaml")
  echo "Building ${src%.md}.pdf"
  pandoc "$src" -o "${src%.md}.pdf" "${args[@]}"
done
echo "Done."
