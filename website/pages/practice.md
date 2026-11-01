---
title: Practice editor
---

# Practice editor

Type Markdown on the left. The rendered result appears on the right as you type. Nothing you write leaves your browser, and nothing is saved when you close the page.

<div class="practice-toolbar">
  <label for="starter">Start from:</label>
  <select id="starter" aria-label="Choose a starter example"></select>
  <button type="button" id="copy">Copy my Markdown</button>
</div>

<details class="cheat" markdown="1">
<summary>Syntax reminder</summary>

| You type | You get |
|---|---|
| `# Title` | A big heading |
| `## Section` | A smaller heading |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `- item` | A bullet |
| `1. item` | A numbered item |
| `- [ ] task` | A checkbox |
| `[text](https://example.com)` | A link |
| `` `code` `` | Code style |
| `> quote` | A quotation |
| `$x^2$` | Math (if your tool supports it) |

More in the [Simple Cheat Sheet](../cheat-sheets/simple.md).

</details>

<div class="practice" id="practice">
  <div>
    <h3>Type here</h3>
    <textarea id="source" spellcheck="false" aria-label="Markdown source"></textarea>
  </div>
  <div>
    <h3>You will see</h3>
    <div id="preview" class="preview" aria-live="polite"></div>
  </div>
</div>

Ready for more? Try the [practice exercises](exercises.md).

!!! tip "Things to try"
    - Change `#` to `##` and watch the heading get smaller.
    - Turn a word bold with `**double asterisks**`.
    - Add a line starting with `- [ ]` to make a checkbox.
    - Write `$x^2$` for inline math.
    - Put a filename in `backticks`.

<script src="../../assets/javascripts/practice.js"></script>
