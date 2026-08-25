# -*- coding: utf-8 -*-
from pathlib import Path
import re

t = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos\index.html").read_text(encoding="utf-8")

# Extract translations object roughly and eval with node
js = re.search(r"<script>(.*?)</script>\s*</body>", t, re.S).group(1)

# Pull just the keys we care about via regex from es block
es_start = js.find("es: {")
en_start = js.find("en: {")
es = js[es_start:en_start]

keys = [
    "outputFormatDetailed", "outputFormatSystematic", "outputFormatScoping",
    "outputFormatMeta", "outputFormatStateOfArt", "outputFormatBibtexApa", "outputFormatBibtexIeee",
    "outputFormatHint", "outputDescDetailed", "areaTemplates", "instructionsTitle", "instructionsFormats"
]
print("=== ES keys ===")
for k in keys:
    print(k, "YES" if re.search(rf'{k}\s*:', es) else "NO")

en = js[en_start:js.find("};", en_start)+2]
print("\n=== EN keys ===")
for k in keys:
    print(k, "YES" if re.search(rf'{k}\s*:', en) else "NO")

# Check areaTemplates content in staticData
m = re.search(r"areaTemplates:\s*\{([^}]+(?:\{[^}]*\}[^}]*)*)\}", js)
# simpler
idx = js.find("areaTemplates: {")
# find staticData areaTemplates (second occurrence might be in translations)
print("\nareaTemplates occurrences", js.count("areaTemplates:"))
# staticData one should have none:, medicine:
sd = js.find("const staticData")
print("static has stateofart", "stateofart:" in js[sd:sd+5000])
print("static snippet around templates:")
i = js.find("areaTemplates:", sd)
print(js[i:i+800])

# Check CSS utilities in styles.css and index style
css = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos\styles.css").read_text(encoding="utf-8")
for u in [r".bg-\[\#f3ede0\]", r".bg-\[\#d5b690\]", r".text-\[\#333\]", r".hover\:bg-\[\#d5b690\]", r".hover\:bg-\[\#b8a082\]", r".border-\[\#d5b690\]"]:
    print(u, u in css)

style = re.search(r"<style>(.*?)</style>", t, re.S).group(1)
print("\nInlined style has beige utils:", ".bg-\\[#f3ede0\\]" in style or ".bg-[#f3ede0]" in style)
print("search escaped:", "bg-\\[#f3ede0\\]" in style)
print("search raw file for f3ede0 class:", "f3ede0" in style)
