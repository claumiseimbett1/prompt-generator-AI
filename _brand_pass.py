# -*- coding: utf-8 -*-
from pathlib import Path
import re

root = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos")
css_path = root / "styles.css"
html_path = root / "index.html"
css = css_path.read_text(encoding="utf-8")
html = html_path.read_text(encoding="utf-8")

replacements = [
    (".border { border-width: 1px; border-style: solid; border-color: var(--gray-300); }",
     ".border { border-width: 1px; border-style: solid; border-color: var(--beige-muted); }"),
    (".border-t { border-top: 1px solid var(--gray-200); }",
     ".border-t { border-top: 1px solid var(--beige-muted); }"),
    (".border-b { border-bottom: 1px solid var(--gray-200); }",
     ".border-b { border-bottom: 1px solid var(--beige-muted); }"),
    (".border-gray-200 { border-color: var(--gray-200); }",
     ".border-gray-200 { border-color: var(--beige-muted); }"),
    (".hover\\:bg-gray-50:hover { background-color: #f9fafb; }",
     ".hover\\:bg-gray-50:hover { background-color: var(--beige-light); }"),
    (".hover\\:bg-gray-100:hover { background-color: var(--gray-100); }",
     ".hover\\:bg-gray-100:hover { background-color: var(--beige-light); }"),
    (".text-gray-500 { color: var(--gray-500); }",
     ".text-gray-500 { color: var(--beige-hover); }"),
    (".text-gray-600 { color: var(--gray-600); }",
     ".text-gray-600 { color: var(--text-secondary); }"),
    (".text-gray-700 { color: var(--gray-700); }",
     ".text-gray-700 { color: var(--text-secondary); }"),
    (".text-gray-800 { color: var(--gray-800); }",
     ".text-gray-800 { color: var(--text-secondary); }"),
    ("background-color: #efe6d6;",
     "background-color: var(--beige-light);"),
    ("#instructions-toggle.is-open {\n  background-color: var(--yellow);\n  color: #000;\n  border-color: #111;\n}",
     "#instructions-toggle.is-open {\n  background-color: var(--yellow);\n  color: var(--black);\n  border-color: var(--beige-dark);\n}"),
]

for a, b in replacements:
    css = css.replace(a, b, 1)

css = css.replace(
    """.app-card {
  border: 2px solid var(--beige-muted);
  background: #fff;
}""",
    """.app-card {
  border: 2px solid var(--beige-dark);
  background: #ffffff;
  box-shadow: 0 12px 40px rgba(213, 182, 144, 0.25);
}""",
)

css = css.replace(
    """body {
  font-family: Inter, "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  background: #ffffff;
  margin: 0;
  min-height: 100vh;
  line-height: 1.5;
  color: var(--gray-800);""",
    """body {
  font-family: Inter, "Segoe UI", system-ui, -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
  background: linear-gradient(180deg, #fffef5 0%, var(--beige-light) 100%);
  margin: 0;
  min-height: 100vh;
  line-height: 1.5;
  color: var(--text-secondary);""",
)

css = css.replace(
    """  background-color: #fff;
  border: 2px solid var(--beige-muted);
  cursor: pointer;
  accent-color: var(--beige-dark);""",
    """  background-color: var(--white);
  border: 2px solid var(--beige-dark);
  cursor: pointer;
  accent-color: var(--beige-dark);""",
)

css_path.write_text(css, encoding="utf-8", newline="\n")

html = html.replace(
    "border border-gray-300 dark:border-gray-600 bg-white dark:bg-gray-700",
    "border border-[#d5b690] dark:border-gray-600 bg-white dark:bg-gray-700",
)
html = html.replace(
    'class="mt-3 p-3 bg-white dark:bg-gray-800 rounded instructions-tip"',
    'class="mt-3 p-3 rounded instructions-tip"',
)
html = html.replace(
    'label class="flex items-center p-2 border border-gray-200 dark:border-gray-600 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 cursor-pointer transition-colors"',
    'label class="choice-btn flex items-center p-2 cursor-pointer"',
)
html = html.replace(
    'id="close-modal-btn" class="text-3xl md:text-2xl font-bold text-gray-500 hover:text-gray-800 dark:hover:text-white p-1 hover:bg-gray-100 dark:hover:bg-gray-700 rounded transition-colors"',
    'id="close-modal-btn" class="btn-icon text-3xl md:text-2xl font-bold p-1 rounded"',
)

css = css_path.read_text(encoding="utf-8").strip()
html2, n = re.subn(
    r"(?s)(<style>\r?\n).*?(\r?\n\s*</style>)",
    lambda m: m.group(1) + css + m.group(2),
    html,
    count=1,
)
assert n == 1
html_path.write_text(html2, encoding="utf-8", newline="\n")
print("OK")
