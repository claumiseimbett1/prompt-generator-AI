import re
from pathlib import Path

html = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos\index.html").read_text(encoding="utf-8")
css = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos\styles.css").read_text(encoding="utf-8")

# body+script class attrs (markup + JS templates)
body = html[html.find("<body"):]
classes = set()
for m in re.finditer(r'class\s*=\s*"([^"]+)"', body):
    classes.update(m.group(1).split())
for m in re.finditer(r"class\s*=\s*'([^']+)'", body):
    classes.update(m.group(1).split())
# template literals with class=
for m in re.finditer(r'class="([^"]+)"', body):
    classes.update(m.group(1).split())

# Also classList patterns less important

# Collect defined selectors from CSS (unescape)
defined = set()
for m in re.finditer(r"\.([a-zA-Z_][a-zA-Z0-9_\\:\-\[\]\/]*)", css):
    raw = m.group(1).replace("\\", "")
    defined.add(raw)

# Component/non-utility classes that are intentional
skip_prefixes = ()
componentish = {
    "app-card","app-hero","app-credits","hero-banner","hero-img","hero-logo","hero-copy",
    "credits-bar","credits-hint","credits-hint-chevron","credits-panel","credits-disclaimer","credits-attribution",
    "btn-primary","btn-secondary","btn-icon","filter-section","validation-box","validation-ok","validation-warn","validation-error",
    "instructions-box","instructions-icon","instructions-tip","instructions-panel","instructions-chevron","instructions-collapse",
    "choice-btn","lang-option","lang-cb","source-cb","doc-type-cb","suggest-cb","form-checkbox","form-radio",
    "loader","card-hover","suggestion-chip","is-open","is-active","is-selected",
}

missing = sorted(c for c in classes if c not in defined and c not in componentish)
# Filter out pure state that might be in attr selectors
print("MISSING UTILITIES (%d):" % len(missing))
for c in missing:
    print(" ", c)

# Specific checks
for c in ["md:mb-6","md:py-6","md:p-6","sm:w-auto","gap-2","opacity-80","block","mt-1"]:
    print(f"check {c}: defined={c in defined}")
