# Where and How to Use Markdown

A beginner-friendly setup guide for students and researchers

Markdown is easy to start because **you usually do not need special installation or a compiler** (a program that turns source files into a finished document). A Markdown file is simply a plain-text file ending in `.md`.

If you can create a file called `notes.md`, type text into it, and open a preview, you can use Markdown.

---

## Quick choice: where should I write Markdown?

| Your situation | Recommended tool | Install anything? | Best for |
|---|---|---:|---|
| "I already use VS Code." | **VS Code** | VS Code only | Local notes, GitHub projects, research documentation |
| "I want nothing installed." | **GitHub web editor** | No | READMEs and repository documentation |
| "I want a Google-Docs-like collaborative Markdown editor." | **HackMD** | No | Shared notes, meetings, collaborative drafts |
| "I want a browser editor with a live preview." | **StackEdit** | No | Quick Markdown writing and previewing |
| "My notes live next to code and data analysis." | **Jupyter / Colab / Quarto** | Depends | Computational research notebooks and reproducible documents |
| "I want a personal library of linked notes." | **Obsidian** | Yes | One note per paper or idea, linked together |
| "I want formatted text as I type, with no preview pane." | **Typora / MarkText** | Yes | Writing that looks finished while you type |

**Beginner recommendation:**

- If you already downloaded this repository, use **VS Code**.
- If you do not want to install anything, use the **GitHub web editor**, **HackMD**, or **StackEdit**.
- If you work with R/Python notebooks, use Markdown cells in **Jupyter/Colab**, or move to **Quarto** later.

> Markdown is portable. The same `.md` file can usually be opened in VS Code, GitHub, HackMD, StackEdit, Obsidian, and many other tools. However, advanced features can differ because the tools use different Markdown "flavors."

---

# 1. Using Markdown in VS Code

VS Code has built-in Markdown support. For basic Markdown writing and previewing, **you do not need a Markdown extension**.

Official documentation: <https://code.visualstudio.com/Docs/languages/markdown>

## Step 1 - Install VS Code

Download VS Code from:

<https://code.visualstudio.com/>

If you already have VS Code, you are ready.

## Step 2 - Create a Markdown file

In VS Code:

1. choose **File -> New Text File**;
2. save it as something ending in `.md`, for example:

```text
paper_notes.md
```

3. type:

```markdown
# Paper Notes

## Main question

What is the mechanism behind the result?

## Tasks

- [ ] Re-read Section 3
- [ ] Check the appendix
- [ ] Reproduce Figure 2
```

That is already a valid Markdown document.

## Step 3 - Open the Markdown preview

VS Code can show the rendered document instead of the raw `#`, `**`, and backticks.

### macOS

Open preview:

```text
Shift + Command + V
```

Open preview beside the source:

```text
Command + K, then V
```

### Windows / Linux

Open preview:

```text
Ctrl + Shift + V
```

Open preview beside the source:

```text
Ctrl + K, then V
```

The side-by-side view is particularly good for beginners:

```text
Markdown source             Rendered preview
-------------------         ----------------
# Results                   Results
                            -------
**Finding:** ...            Finding: ...
```

You can also open the Command Palette and search for:

```text
Markdown: Open Preview
Markdown: Open Preview to the Side
```

## Step 4 - Edit source and watch the preview

A simple workflow is:

1. keep the `.md` file on the left;
2. keep the preview on the right;
3. make one change;
4. save;
5. check the preview.

Basic Markdown does **not** need a compile step: the preview simply updates as you edit.

## Step 5 - Add an image

Suppose your project looks like:

```text
project/
  notes.md
  figures/
    result.png
```

In `notes.md`, write:

```markdown
![Main result](figures/result.png)
```

Use **relative paths** like this when possible. They are much easier to move between VS Code and GitHub than paths such as `/Users/name/Desktop/...`.

## Step 6 - Add math when the renderer supports it

Many research-oriented Markdown tools support LaTeX-style math.

Inline:

```markdown
The parameter is $\beta$.
```

Display:

```markdown
$$
y_i = x_i'\beta + \varepsilon_i,
\qquad i=1,\ldots,n.
$$
```

Math support varies across Markdown tools, so always check the preview in the tool where the document will be read.

## Optional VS Code extensions

You do not need these to start. Add them only if you want the extra features.

- **markdownlint** - warns about inconsistent Markdown style.
- **Markdown All in One** - adds shortcuts and convenience features.

For a complete beginner, the built-in VS Code preview is enough.

---

# 2. Using Markdown directly on GitHub

GitHub renders Markdown in repository `README.md` files and throughout its web interface. GitHub uses **GitHub Flavored Markdown (GFM)**, which includes features such as tables, task lists, and strikethrough.

Official guide: <https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax>

## Edit a README without Git or VS Code

You can edit Markdown entirely in the browser.

1. Open a repository on GitHub.
2. Open `README.md` or another `.md` file.
3. Click the edit/pencil control.
4. Edit the Markdown source.
5. Use the preview option to inspect the rendered result.
6. Commit/save the change.

For a new repository, a simple README can begin with:

```markdown
# Replication Files

This repository contains the code and documentation for the project.

## Folder structure

- `data/` - input data
- `code/` - analysis code
- `output/` - generated tables and figures

## Reproduction

1. Run `01_clean.R`.
2. Run `02_analysis.R`.
3. Check `output/`.
```

## Good uses of GitHub Markdown

- repository `README.md` files;
- replication instructions;
- project documentation;
- issue descriptions;
- pull-request descriptions;
- public teaching materials.

## A privacy reminder

Do not put restricted data, confidential participant information, private API keys, or material prohibited by a data-use agreement into a public GitHub repository.

---

# 3. Using HackMD in the browser

HackMD is a browser-based Markdown workspace designed around writing, sharing, and real-time collaboration.

Website: <https://hackmd.io/>

It is useful when you want something closer to a collaborative shared document while still keeping the underlying content in Markdown.

## Beginner workflow

1. Open HackMD and create/sign in to an account.
2. Create a new note.
3. Type Markdown in the editor.
4. Use the rendered view/preview to check formatting.
5. Share the note with collaborators if needed.
6. Check sharing permissions before adding unpublished or sensitive material.

A coauthor-meeting note could look like:

```markdown
# Coauthor Meeting - 2026-09-26

## Decisions

- Keep the main sample definition.
- Move robustness results to the appendix.

## Questions

- Why does the estimate change in the rural subsample?

## Next actions

- [ ] Update Table 2
- [ ] Re-run robustness checks
- [ ] Draft response to referee comment 4
```

HackMD is especially convenient for:

- meeting notes;
- shared research notes;
- reading groups;
- collaborative outlines;
- lightweight documentation.

---

# 4. Using StackEdit in the browser

StackEdit is an in-browser Markdown editor with a live preview.

Website: <https://stackedit.io/>

Its official site describes support for Markdown flavors including GitHub Flavored Markdown and CommonMark, live preview, LaTeX-style mathematical expressions, and synchronization options with services such as Google Drive, Dropbox, and GitHub.

## Beginner workflow

1. Open StackEdit.
2. Start a new document.
3. Type Markdown in the source/editor pane.
4. Watch the rendered preview.
5. Export or synchronize the document if needed.

StackEdit is useful when you want to practice Markdown in a browser without setting up a local project.

Example:

```markdown
# Seminar Notes

**Speaker:** Jane Doe  
**Topic:** Labor market adjustment

## Main contribution

The paper studies ...

## Equation I want to revisit

$$
y_i = \alpha + \beta x_i + \varepsilon_i.
$$

## Questions

1. How is the sample selected?
2. What is the identifying variation?
```

---

# 5. Markdown in Jupyter Notebook or Google Colab

If you analyze data in Python, Julia, or R notebooks, you can combine **code cells** with **Markdown cells**.

A Markdown cell can contain:

```markdown
## Results

The coefficient is positive in the baseline sample.

$$
\hat{\beta} = 0.12.
$$

The next cell reproduces the figure.
```

Then the next notebook cell can contain the actual Python/R code.

This is useful for:

- exploratory analysis;
- computational notes;
- teaching notebooks;
- documenting why a code block exists;
- keeping equations and interpretation next to results.

A notebook is not the same as a plain `.md` file, but Markdown syntax is used inside its text cells.

---

# 6. Markdown with Quarto

Quarto is useful when you eventually want Markdown-like source plus:

- citations;
- cross-references;
- equations;
- executable R/Python/Julia code;
- HTML, PDF, or Word output.

A Quarto source file usually ends in `.qmd` rather than `.md`.

Example:

```markdown
---
title: "Research Note"
format: html
---

# Results

The analysis is summarized below.
```

You can edit Quarto in VS Code or RStudio. It is a good next step after ordinary Markdown, but you do not need it to learn Markdown.

---

# 7. Obsidian and live-preview editors

These are good once you know the basic syntax. They are not required.

## Obsidian

Obsidian is a note-taking app that stores every note as an ordinary `.md` file inside a folder called a **vault**. It adds features such as `[[wiki links]]` between notes and a Live Preview mode where formatting appears as you type.

It is a good fit for a personal library of linked notes, for example one note per paper or per idea.

**Portability warning:** `[[wiki links]]`, callouts, and embeds are Obsidian features. GitHub and most other tools do not understand them. If you plan to publish a note, use ordinary links such as `[text](other_note.md)` instead.

Download: <https://obsidian.md/>

## Typora and MarkText

Typora and MarkText are editors that show formatted text as you type, so there is no separate preview pane. The file on disk is still plain Markdown.

Check each tool's website for its current price and availability before installing.

## Advice for beginners

Learn the syntax first in a simple editor such as VS Code or the [practice editor on the website](https://ningzhanglab.github.io/Markdown-for-Beginners/start-here/practice/). Because the file is plain text, you can move to any of these editors later without converting anything.

---

# 8. Which tool should a non-technical beginner choose?

## Use VS Code if ...

- you already use it for other writing or coding;
- you want your notes stored as local files;
- you want one folder containing code, Markdown, figures, and other project files;
- you plan to use GitHub later.

## Use GitHub's web editor if ...

- you mainly need to edit a README;
- you want to contribute a small documentation change;
- you do not want to install an editor.

## Use HackMD if ...

- several people need to edit a note together;
- you want browser-based collaboration;
- you want a shared seminar/coauthor document.

## Use StackEdit if ...

- you want a browser editor with a live preview;
- you are practicing Markdown;
- you want to work without configuring VS Code.

## Use Jupyter / Colab if ...

- prose belongs directly beside executable code;
- the document is part of data analysis rather than a standalone note.

## Use Quarto if ...

- you want reproducible academic documents from Markdown-like source;
- you need citations, cross-references, code execution, and multiple output formats.

## Use Obsidian if ...

- you want a personal library of notes that link to each other;
- you are happy keeping the notes on your own computer;
- you will not need to publish them on GitHub exactly as written.

## Use Typora or MarkText if ...

- you find a separate preview pane distracting;
- you want the page to look finished while you type.

---

# 9. Important: Markdown looks slightly different across tools

Do not assume every feature works everywhere.

The following are broadly portable:

```markdown
# Heading

**bold**

*italic*

- bullet

1. numbered item

[link](https://example.com)

`inline code`
```

These may vary by renderer:

- mathematical expressions;
- footnotes;
- task lists;
- callouts/admonitions;
- citations;
- automatic cross-references;
- diagrams;
- YAML metadata.

**Rule:** write using the common Markdown core when portability matters, and use advanced features only when you know which renderer will display the file.

---

# 10. Moving the same file between VS Code, GitHub, and web editors

Because Markdown is plain text, the basic workflow is simple:

```text
notes.md
   |
   +--> edit locally in VS Code
   +--> upload/commit to GitHub
   +--> open/copy into HackMD
   +--> open/copy into StackEdit
```

For maximum portability:

1. keep images in the project folder;
2. use relative image links;
3. avoid tool-specific syntax unless necessary;
4. keep filenames simple;
5. save the source as UTF-8;
6. preview the file on the platform where readers will view it.

---

# 11. Exporting Markdown to PDF

Markdown itself is only source text. PDF export depends on the tool.

## Simplest option

If your editor provides a print/export view, use it for a quick PDF.

## Reproducible academic option: Pandoc

If Pandoc and a LaTeX distribution such as TinyTeX are installed:

```bash
pandoc notes.md -o notes.pdf
```

This is useful when you want the same Markdown source to generate a repeatable PDF.

## Quarto

For a Quarto file:

```bash
quarto render notes.qmd --to pdf
```

For beginners, PDF export is optional. Learn ordinary Markdown writing and previewing first.

---

# 12. Five-minute practice exercise

Create a file named:

```text
my_first_markdown_note.md
```

Paste:

```markdown
# My First Research Note

## Question

What am I trying to understand?

## Notes

**Main idea:** Write one sentence here.

- Evidence 1
- Evidence 2
- Evidence 3

## Tasks

- [x] Create this file
- [ ] Add one paper citation/link
- [ ] Add one equation
- [ ] Add one image

## Code or command

Run `python analysis.py` after cleaning the data.

## Equation

$$
y_i = x_i'\beta + \varepsilon_i,
\qquad i=1,\ldots,n.
$$
```

Then open the preview in VS Code or paste the same source into a browser Markdown editor.

You now know enough Markdown to create useful research notes.

---

# 13. Recommended next file in this repository

After completing this guide, read:

```text
01_Markdown_Handbooks/Markdown_Beginner_Handbook.md
```

Use its PDF version if you want to read the guide without editing the source.

