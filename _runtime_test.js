const fs = require("fs");
const { parseHTML } = require("linkedom");
const html = fs.readFileSync("index.html", "utf8");
const { document, window } = parseHTML(html);
global.document = document;
global.window = window;
global.alert = () => {};
global.requestAnimationFrame = (cb) => setTimeout(cb, 0);

const m = html.match(/<script>([\s\S]*?)<\/script>/);
let script = m[1];
// Trigger DOMContentLoaded handlers immediately by replacing listener
script = script.replace(
  /document\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{/,
  "(() => {"
);
// close: find last matching for DOMContentLoaded - the init ends with });
script = script.replace(/\}\);\s*$/, "})();");

try {
  eval(script);
} catch (e) {
  console.error("RUNTIME", e.message);
  console.error(e.stack.split("\n").slice(0, 8).join("\n"));
  process.exit(1);
}

const ids = [
  "advanced-filters-label",
  "doc-type-label",
  "doc-type-container",
  "quality-label",
  "quality-container",
  "output-format-label",
  "output-format-container",
  "output-detailed-label",
  "peer-reviewed-label",
];
for (const id of ids) {
  const el = document.getElementById(id);
  const text = el ? el.textContent.trim().replace(/\s+/g, " ").slice(0, 100) : null;
  console.log(
    id,
    "| exists:",
    !!el,
    "| children:",
    el ? el.children.length : 0,
    "| text:",
    JSON.stringify(text)
  );
}
