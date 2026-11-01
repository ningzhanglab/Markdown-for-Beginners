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

!!! tip "Things to try"
    - Change `#` to `##` and watch the heading get smaller.
    - Turn a word bold with `**double asterisks**`.
    - Add a line starting with `- [ ]` to make a checkbox.
    - Write `$x^2$` for inline math.
    - Put a filename in `backticks`.

<script src="../../assets/javascripts/practice.js"></script>
