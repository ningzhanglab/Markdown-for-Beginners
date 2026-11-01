// Render the $...$ and $$...$$ math that pymdownx.arithmatex wraps in
// <span class="arithmatex"> elements. KaTeX is loaded just before auto-render.
document.addEventListener("DOMContentLoaded", function () {
  if (!window.renderMathInElement) return;
  renderMathInElement(document.body, {
    delimiters: [
      { left: "\\[", right: "\\]", display: true },
      { left: "\\(", right: "\\)", display: false },
    ],
    ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    ignoredClasses: ["no-math"],
    throwOnError: false,
  });
});
