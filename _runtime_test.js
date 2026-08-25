
const fs = require(fs);
const { parseHTML } = require(linkedom);
const html = fs.readFileSync(String.rawc:\Users\Unisinu\Desktop\Landing\Promp-Academicos\index.html, utf8);
const { document, window } = parseHTML(html);
global.document = document;
global.window = window;
global.HTMLElement = window.HTMLElement;
// strip and eval script
const m = html.match(/<script>([\s\S]*?)<\/script>/);
const script = m[1]
  .replace(/document\.addEventListener\('DOMContentLoaded',\s*\(\)\s*=>\s*\{/, '(() => {')
  .replace(/\}\);\s*$/, '})();');
try {
  eval(script);
} catch (e) {
  console.error(RUNTIME, e.message);
  console.error(e.stack.split(\n).slice(0,5).join(\n));
  process.exit(1);
}
const ids = [doc-type-container,quality-container,output-format-container,advanced-filters-label];
for (const id of ids) {
  const el = document.getElementById(id);
  console.log(id, exists, !!el, htmlLen, el ? el.innerHTML.length : 0, text, el ? JSON.stringify(el.textContent.trim().slice(0,80)) : null);
}
