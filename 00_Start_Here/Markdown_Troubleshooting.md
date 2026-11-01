# Why Doesn't Mine Look Right?

Most Markdown problems come from a few small slips. Find the symptom, compare what you typed with the fix, and try again.

## My heading shows `##Results` instead of a heading

A heading needs a **space** after the `#` signs.

```text
##Results       wrong
## Results      right
```

## Two paragraphs run together

Markdown starts a new paragraph only after a **blank line**. A single line break is usually ignored.

````markdown
This is the first paragraph.
This is the second paragraph.   <- joins the first one

This is the first paragraph.

This is the second paragraph.   <- separate paragraph
````

## Everything after one point turns into a grey code box

A code block was opened with three backticks but never closed. Every opening fence needs a closing fence.

````markdown
```r
summary(df)

Next paragraph...        <- still inside the code block
````

Add three backticks on a line by themselves after the last line of code.

## My bold text did not turn bold

There must be **no spaces** just inside the stars.

```text
** Important **     wrong
**Important**       right
```

## My list did not appear as a list

Each item needs a dash (or number) **followed by a space**. It is also safest to leave a blank line before the list.

```text
-item one           wrong
- item one          right
```

## Part of my text turned italic or bold by accident

The signs `*` and `_` mean emphasis. A name written between underscores, or text between stars, is treated as formatting. Put names, file names, and symbols in backticks so they show exactly as typed.

```text
The file _draft_ is ready.       "draft" turns italic
The file `_draft_` is ready.     shows _draft_ exactly
```

## My image does not show

Check these in order:

1. The file name, including capital letters and the extension.
2. The path is **relative to the Markdown file**, not an address on your own computer.
3. The image file was actually saved or uploaded with the project.

```text
![Chart](/Users/me/Desktop/chart.png)    wrong: only works on your computer
![Chart](figures/chart.png)              right
```

## A link does not work

Spaces inside the address break a link. Rename the file without spaces (best), or write `%20` for each space.

```text
[Notes](my notes.md)     wrong
[Notes](my_notes.md)     right
```

## My table shows as plain text

A table needs a separator row (dashes) under the header row, and a blank line before it.

```markdown
| Name | Score |
|---|---:|
| Ana | 12 |
```

## A table has an extra column

A literal vertical bar inside a cell is read as a column break. Write a backslash before it, or reword the cell.

## Math prints as `$x^2$`

The tool you are using may not support math. GitHub and the VS Code preview do; some simple viewers do not. Check where the file will be read.

## `[@smith2024]` or `[^1]` appears literally

Citations like `[@smith2024]` need Pandoc or Quarto with a bibliography file. Footnotes like `[^1]` need a viewer that supports footnotes. In a simpler viewer they show as typed.

## A small table appears at the top of my file on GitHub

That is **front matter**: settings between two lines of `---` at the very top of the file. GitHub shows it as a table. It is not a mistake.

## Still stuck?

Paste your text into the practice editor on the website, or into a different Markdown viewer. If it looks right there, the problem is the tool you were using, not your Markdown. See the glossary in `Markdown_Glossary.md` for unfamiliar words.
