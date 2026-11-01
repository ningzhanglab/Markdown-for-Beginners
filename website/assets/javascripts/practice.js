// Live Markdown practice editor. Everything runs in the browser.
// Libraries are loaded from a pinned CDN version only on this page.
(function () {
  var source = document.getElementById("source");
  if (!source) return;

  var preview = document.getElementById("preview");
  var starter = document.getElementById("starter");
  var copyBtn = document.getElementById("copy");
  var base = new URL("../", document.currentScript.src);

  function load(src) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = src; s.onload = resolve; s.onerror = reject;
      document.head.appendChild(s);
    });
  }

  // Keep $...$ math out of the Markdown parser (underscores would become italics),
  // then put it back as KaTeX output.
  function render(md) {
    var math = [];
    function stash(display) {
      return function (_, tex) {
        var html;
        try { html = window.katex.renderToString(tex, { displayMode: display, throwOnError: false }); }
        catch (e) { html = "<code>" + tex + "</code>"; }
        math.push(html);
        return "MATHSLOT" + (math.length - 1) + "ENDSLOT";
      };
    }
    // Skip fenced code blocks and inline code when looking for math.
    var parts = md.split(/(```[\s\S]*?```|`[^`\n]*`)/g);
    for (var i = 0; i < parts.length; i += 2) {
      parts[i] = parts[i]
        .replace(/\$\$([\s\S]+?)\$\$/g, stash(true))
        .replace(/\$([^\s$](?:[^$\n]*?[^\s$])?)\$(?!\d)/g, stash(false));
    }
    var html = window.marked.parse(parts.join(""), { gfm: true, breaks: false });
    html = html.replace(/MATHSLOT(\d+)ENDSLOT/g, function (_, n) { return math[+n]; });
    return window.DOMPurify.sanitize(html, { ADD_ATTR: ["target"] });
  }

  var starters = [];
  var dirty = false;

  function update() { preview.innerHTML = render(source.value); }

  Promise.all([
    load("https://cdn.jsdelivr.net/npm/marked@12.0.2/marked.min.js"),
    load("https://cdn.jsdelivr.net/npm/dompurify@3.1.6/dist/purify.min.js"),
    fetch(new URL("starters.json", base)).then(function (r) { return r.json(); })
  ]).then(function (res) {
    starters = res[2];
    starters.forEach(function (s, i) {
      var o = document.createElement("option");
      o.value = i; o.textContent = s.label; starter.appendChild(o);
    });
    source.value = starters[0].text;
    dirty = false;
    update();
  }).catch(function () {
    preview.textContent = "The preview could not load. Check your internet connection and reload the page.";
  });

  source.addEventListener("input", function () { dirty = true; update(); });
  var current = 0;
  starter.addEventListener("change", function () {
    if (dirty && !window.confirm("Replace what you typed with this example?")) {
      starter.value = current;
      return;
    }
    current = +starter.value;
    source.value = starters[current].text;
    dirty = false;
    update();
  });
  copyBtn.addEventListener("click", function () {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(source.value).then(function () {
        copyBtn.textContent = "Copied";
        setTimeout(function () { copyBtn.textContent = "Copy my Markdown"; }, 1500);
      });
    } else { source.select(); }
  });
})();
