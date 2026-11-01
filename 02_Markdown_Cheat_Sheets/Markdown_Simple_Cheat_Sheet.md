# Start here

Markdown is **normal text with a few simple symbols for formatting**.

A Markdown file usually ends in:

```text
.md
```

For example:

```text
notes.md
```

You can write Markdown in **VS Code, GitHub, HackMD, StackEdit, Obsidian, Jupyter, or Quarto**.

> **Beginner rule:** type first, preview second. You do not need to memorize everything.

A good beginner workflow in VS Code is:

```text
left: what you type        right: rendered preview
```

Open preview with:

```text
macOS:          Shift + Command + V
Windows/Linux: Ctrl + Shift + V
```

---

# 1. Headings

## Type this

```markdown
# Main title
## Section
### Smaller section
```

## It looks like this

# Main title

## Section

### Smaller section

**Simple rule:** more `#` signs = smaller heading.

Always put a space after `#`.

```text
## Results     good
##Results      avoid
```

---

# 2. Paragraphs

## Type this

```markdown
This is the first paragraph.

This is the second paragraph.
```

## It looks like this

This is the first paragraph.

This is the second paragraph.

**Simple rule:** leave one blank line between paragraphs.

---

# 3. Bold and italic

## Type this

```markdown
**important result**
*paper title or emphasis*
***very important***
```

## It looks like this

**important result**

*paper title or emphasis*

***very important***

A useful research-note pattern is:

```markdown
**Finding:** The estimate is stable.

**Question:** Why does the result change?

**TODO:** Check Table 3.
```

---

# 4. Bullet and numbered lists

## Bullets - type this

```markdown
- Read the paper
- Check the appendix
- Reproduce Figure 2
```

## It looks like this

- Read the paper
- Check the appendix
- Reproduce Figure 2

## Numbered list - type this

```markdown
1. Download the data
2. Clean the data
3. Run the analysis
```

## It looks like this

1. Download the data
2. Clean the data
3. Run the analysis

---

# 5. Checkboxes

Checkboxes are useful for research tasks.

## Type this

```markdown
- [x] Read the introduction
- [ ] Check the data section
- [ ] Prepare seminar questions
```

## It looks like this

- [x] Read the introduction
- [ ] Check the data section
- [ ] Prepare seminar questions

> Checkboxes work especially well on GitHub and many Markdown editors.

---

# 6. Links

The pattern is:

```text
[text people see](web address)
```

## Type this

```markdown
[Google Scholar](https://scholar.google.com/)
```

## It looks like this

[Google Scholar](https://scholar.google.com/)

You can also link to another file in the same project:

```markdown
[Open my notes](notes.md)
```

**Simple rule:** square brackets contain the label; parentheses contain the destination.

---

# 7. Images

An image looks like a link with `!` at the beginning.

```text
![description](path-to-image)
```

Suppose your folder is:

```text
project/
  notes.md
  figures/
    result.png
```

Type:

```markdown
![Main result](figures/result.png)
```

**Simple rule:** use a path relative to the Markdown file. Avoid paths such as `/Users/name/Desktop/...`.

If an image does not appear, check the filename and folder path first.

---

# 8. Inline code

Use one backtick when you want to show a filename, variable name, command, or code literally.

## Type this

```markdown
Open `analysis.R` and check the variable `income`.
```

## It looks like this

Open `analysis.R` and check the variable `income`.

This is also useful for showing a LaTeX command such as `\qquad` without running it.

---

# 9. Code blocks

Use three backticks before and after a larger block of code.

## Type this

````markdown
```r
model <- lm(y ~ x, data = df)
summary(model)
```
````

## It looks like this

```r
model <- lm(y ~ x, data = df)
summary(model)
```

You may replace `r` with `python`, `stata`, `bash`, or another language name.

**Simple rule:** every opening set of three backticks needs a closing set.

---

# 10. A small table

Tables are optional. Learn them only when you need them.

## Type this

```markdown
| Variable | Mean |
|---|---:|
| Income | 52.4 |
| Age | 34.1 |
```

## It looks like this

| Variable | Mean |
|---|---:|
| Income | 52.4 |
| Age | 34.1 |

The second row tells Markdown that this is a table.

For complicated publication tables, use LaTeX, Quarto, or generated output instead of forcing everything into Markdown.

---

# 11. Simple math - optional

Some Markdown tools support LaTeX-style math (the notation many papers use for equations; you can just copy the examples).

## Inline math

Type:

```markdown
The parameter is $\beta$.
```

Rendered idea:

The parameter is $\beta$.

## Display math

Type:

```markdown
$$
y_i = \alpha + \beta x_i + \varepsilon_i
$$
```

Rendered idea:

$$
y_i = \alpha + \beta x_i + \varepsilon_i
$$

Inside the math, `\alpha`, `\beta`, and `\varepsilon` are LaTeX math commands.

If you see the dollar signs and backslashes literally, your current Markdown viewer may not support math in that context.

---

# 12. Five beginner mistakes

## No space after a heading marker

```text
##Results      wrong
## Results     better
```

## No blank line between paragraphs

Use a blank line when you want a new paragraph.

## Missing closing code fence

Every opening triple-backtick fence needs a closing fence.

## Image path points to your own computer

Prefer:

```markdown
![Result](figures/result.png)
```

instead of an absolute path from your desktop.

## Assuming every Markdown viewer is identical

Basic syntax is very portable, but math, citations, footnotes, and some other features vary by tool.

For more fixes with examples, see `Markdown_Troubleshooting.pdf`.

---

# Quick lookup

| I want to... | Type |
|---|---|
| Heading | `# Heading` |
| Smaller heading | `## Heading` |
| Bold | `**text**` |
| Italic | `*text*` |
| Bullet | `- item` |
| Numbered item | `1. item` |
| Checkbox | `- [ ] task` |
| Link | `[name](https://...)` |
| Image | `![description](image.png)` |
| Inline code | `` `code` `` |
| Code block | three backticks before and after |
| Small table | cells separated by vertical bars, plus a separator row |
| Inline math | `$...$` |
| Display math | `$$...$$` |

# A complete first note

Copy this into a file called `paper_notes.md`:

```markdown
# Paper Notes

**Paper:** Example Paper

## Main question

What question does the paper answer?

## Main finding

The main result is ...

## My questions

- Why is this sample used?
- What is the main mechanism?
- What should I check in the appendix?

## Tasks

- [ ] Read the data section
- [ ] Check Table 2
- [ ] Write a one-paragraph summary
```

Markdown is just as useful outside research. For example, a plan for the week:

```markdown
# Plan for This Week

**Goal:** Finish the report.

## Monday

- [x] Outline the report
- [ ] Email the team

## Tuesday

- [ ] Write the first draft
```

That is already a useful Markdown document. Learn the advanced sheet only when you actually need more.
