# Before you start

This sheet is **not the place to begin**.

Start with `Markdown_Simple_Cheat_Sheet.pdf`. Come back here when you need more control over links, paths, tables, code, math, GitHub, or research documentation.

A useful mental model is:

```text
Basic Markdown = portable writing syntax
Advanced Markdown = features that may depend on the renderer
```

Different tools can add different features. GitHub, Pandoc, Quarto, Jupyter, Obsidian, and HackMD are not identical.

---

# 1. Hard line breaks and horizontal rules

Markdown normally uses blank lines for new paragraphs.

If you truly need a hard line break, two spaces at the end of a line often work:

```markdown
Author: Jane Doe  
Department: Economics
```

Rendered:

Author: Jane Doe  
Department: Economics

A horizontal rule can be written as:

```markdown
---
```

Use these sparingly in ordinary academic prose.

---

# 2. Strikethrough, nested lists, and blockquotes

## Strikethrough

```markdown
~~old wording~~
```

Rendered:

~~old wording~~

## Nested list

```markdown
- Data
  - Raw files
  - Clean files
- Output
  - Tables
  - Figures
```

Rendered:

- Data
  - Raw files
  - Clean files
- Output
  - Tables
  - Figures

## Blockquote

```markdown
> The author argues that the policy changed incentives.
```

Rendered:

> The author argues that the policy changed incentives.

---

# 3. Escaping Markdown punctuation

Markdown punctuation can have special meaning. A backslash can show a symbol literally.

```markdown
\*literal asterisk\*
\# not a heading
\_underscore\_
```

For filenames, variables, and commands, inline code is usually easier:

```markdown
`income_after_tax`
`README.md`
`\qquad`
```

---

# 4. Links beyond the basics

## Direct URL

```markdown
<https://www.example.com/>
```

## Link to another file

Suppose:

```text
project/
  README.md
  notes/
    literature.md
```

Inside `README.md`:

```markdown
See the [literature notes](notes/literature.md).
```

## Link to a heading

A heading such as:

```markdown
## Main Results
```

usually has an anchor similar to:

```markdown
[Jump to results](#main-results)
```

Exact anchor rules can vary by renderer.

## Reference-style links

```markdown
Read the [project website][site].

[site]: https://example.com/project
```

This keeps long URLs out of the middle of prose.

---

# 5. Relative paths and `../`

Relative paths make a project portable.

Suppose:

```text
project/
  figures/
    result.png
  notes/
    meeting.md
```

From `notes/meeting.md`, this path:

```markdown
![Result](../figures/result.png)
```

means:

```text
..          go up one folder
figures/    enter figures
result.png  open the file
```

Avoid absolute paths such as:

```text
/Users/name/Desktop/project/figures/result.png
```

because they usually work only on your computer.

---

# 6. Images and size control

Basic Markdown:

```markdown
![Main result](figures/main_result.png)
```

Basic Markdown intentionally offers little layout control.

Some tools accept HTML:

```html
<img src="figures/main_result.png" width="500" alt="Main result">
```

Pandoc and Quarto have additional image-size syntax. Use tool-specific syntax only when you know where the document will be rendered.

If an image is missing, check spelling, capitalization, extension, relative path, and whether the image file was actually uploaded or committed.

---

# 7. Tables: alignment and pipe characters

## Alignment

```markdown
| Left | Center | Right |
|:---|:---:|---:|
| text | text | 12.5 |
```

Rendered:

| Left | Center | Right |
|:---|:---:|---:|
| text | text | 12.5 |

Memory trick:

```text
:---     left
:---:    center
---:     right
```

## A literal pipe inside a table

The `|` character normally separates columns. Escape it when needed:

```markdown
| Item | Meaning |
|---|---|
| `A \| B` | A or B |
```

If a table becomes wide or highly formatted, use LaTeX, Quarto, HTML, or generated table output instead.

---

# 8. Code blocks and language labels

A fenced code block uses triple backticks:

````markdown
```python
print("hello")
```
````

Rendered:

```python
print("hello")
```

Common language labels include:

```text
r
python
stata
bash
latex
json
yaml
```

The label mainly helps syntax highlighting.

## Showing backticks inside code examples

If you are documenting Markdown itself, use a longer outer fence:

`````markdown
````markdown
```python
print("hello")
```
````
`````

The outer fence must be longer than the inner one.

---

# 9. Inline code containing a backtick

Ordinary inline code uses one backtick:

```markdown
`code`
```

To show text that itself contains a backtick, use two backticks outside:

```markdown
Use `` `code` `` when explaining inline code syntax.
```

Rendered:

Use `` `code` `` when explaining inline code syntax.

---

# 10. Math in Markdown

Math support is common in academic Markdown tools, but it is not identical everywhere.

## Inline math

```markdown
The parameter is $\beta$ and the estimate is $\hat{\beta}$.
```

Rendered:

The parameter is $\beta$ and the estimate is $\hat{\beta}$.

## Display math

```markdown
$$
y_i = x_i'\beta + \varepsilon_i,
\qquad i=1,\ldots,n.
$$
```

Rendered:

$$
y_i = x_i'\beta + \varepsilon_i,
\qquad i=1,\ldots,n.
$$

Here Markdown marks the math region, while commands such as `\beta`, `\varepsilon`, `\qquad`, and `\ldots` are LaTeX-style math commands.

Another example:

```markdown
$$
\frac{1}{n}\sum_{i=1}^{n} x_i
$$
```

Rendered:

$$
\frac{1}{n}\sum_{i=1}^{n} x_i
$$

If math works in one viewer but not another, it may be a renderer difference rather than a syntax error.

---

# 11. Footnotes

Many extended Markdown systems support footnotes:

```markdown
This result uses the restricted sample.[^1]

[^1]: The restriction removes observations with missing baseline values.
```

Footnotes are common in Pandoc and similar systems, but check your renderer.

---

# 12. YAML front matter

Pandoc and Quarto often use a metadata block at the top of a file:

```yaml
---
title: "Research Note"
author: "Jane Doe"
date: "2026-09-27"
---
```

Think of YAML front matter as **document settings**, not ordinary body text.

A Quarto file might add:

```yaml
---
title: "Research Note"
format: html
---
```

---

# 13. Academic citations

Plain Markdown does not define one universal citation system.

For simple notes, ordinary prose is fine:

```markdown
See Smith (2024), especially Section 3.
```

Pandoc or Quarto can support bibliography-based syntax such as:

```markdown
Recent work reaches a similar conclusion [@smith2024].
```

If `[@smith2024]` appears literally, your current viewer is probably treating the file as ordinary Markdown. Bibliography citations need an academic renderer plus bibliography configuration.

---

# 14. A minimal research README

A README should answer:

1. What is this project?
2. What is inside the folders?
3. How do I reproduce or use it?
4. What should I read or run first?

Example:

```markdown
# Project Title

One paragraph describing the project.

## Files

- `data/` - input data
- `code/` - scripts
- `output/` - tables and figures

## Reproduction

1. Run `01_clean.R`.
2. Run `02_analysis.R`.
3. Check `output/`.
```

---

# 15. A useful research folder

```text
project/
  README.md
  data/
    raw/
    clean/
  code/
    01_clean.R
    02_analysis.R
  figures/
  tables/
  notes/
    literature.md
    meetings.md
```

Markdown is useful for documenting what these folders contain and recording decisions that would otherwise be lost.

---

# 16. Paper-reading note template

```markdown
# Author (Year) - Short Title

## One-sentence summary

## Research question

## Data

## Method / design

## Main result

## Mechanism / interpretation

## What I learned

## Questions

- 

## Useful pages / figures

- p. 
```

---

# 17. Research log template

```markdown
# Research Log - 2026-09-27

## What I did

- Cleaned the main sample.
- Re-ran Figure 2.

## What changed

- Dropped duplicate observations.

## Problem

The coefficient changes after the merge.

## Next

- [ ] Check merge keys.
- [ ] Compare dropped observations.
```

A log records **why** you made changes, not just the final code.

---

# 18. Meeting-note template

```markdown
# Advisor Meeting - 2026-09-27

## Decisions

- Keep the main specification.
- Move robustness checks to the appendix.

## Questions

- Why does the rural subsample differ?

## Actions

- [ ] Update Table 2
- [ ] Draft two paragraphs on mechanism
- [ ] Send revised figure by Friday
```

---

# 19. GitHub README habits

Good habits:

- use relative links;
- keep filenames simple;
- explain what a new user should do first;
- show commands as code;
- keep instructions in the order they should be run;
- use headings so the page is easy to scan.

Avoid:

- giant unbroken paragraphs;
- absolute paths from your own computer;
- undocumented folder names;
- instructions that assume the reader knows Git;
- private data, passwords, tokens, or API keys.

---

# 20. Common mistakes

## Heading does not render

```text
##Results      wrong
## Results     better
```

## Two paragraphs appear as one

Use a blank line between paragraphs.

## The rest of the document becomes one giant code block

You probably forgot to close a fenced code block.

## Image works locally but not on GitHub

Use a relative path and make sure the image itself is uploaded.

## Table does not render

A table needs a separator row:

```markdown
| Variable | Mean |
|---|---:|
| Income | 52.4 |
```

## Citation syntax appears literally

`[@smith2024]` needs a renderer such as Pandoc or Quarto plus bibliography setup.

## Too many heading levels

For most notes, `#`, `##`, and `###` are enough.

## Treating Markdown like Word

Markdown is strongest when you think about **structure**, not exact page layout.

---

# Advanced quick lookup

| Need | Syntax / idea |
|---|---|
| Hard line break | two spaces at end of line |
| Strikethrough | `~~text~~` |
| Nested list | indent child items |
| Blockquote | `> quote` |
| Direct URL | `<https://...>` |
| Relative file link | `[notes](notes/file.md)` |
| Go up one folder | `../` |
| Heading link | `[results](#results)` |
| Reference-style link | `[text][id]` plus `[id]: URL` |
| Table alignment | `:---`, `:---:`, `---:` |
| Language code block | triple backticks + language |
| Inline math | `$...$` |
| Display math | `$$...$$` |
| Footnote | `[^1]` plus definition |
| YAML metadata | `---` block at top |
| Pandoc/Quarto citation | `[@key]` |

# Which file should you read next?

- If this sheet already feels like too much, return to **Markdown_Simple_Cheat_Sheet.pdf**.
- If you want a slower tutorial, read **../01_Markdown_Handbooks/Markdown_Beginner_Handbook.pdf**.
- If you need editor instructions, read **../01_Markdown_Handbooks/Markdown_Setup_and_Editors_Guide.pdf**.
