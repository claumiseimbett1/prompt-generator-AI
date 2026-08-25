# -*- coding: utf-8 -*-
from pathlib import Path
import re

path = Path(r"c:\Users\Unisinu\Desktop\Landing\Promp-Academicos\index.html")
text = path.read_text(encoding="utf-8")

# Unified label
ES = "Cómo usar esta herramienta"
EN = "How to use this tool"

# Unify i18n titles
text = text.replace('helpTitle: "Cómo Usar la App"', f'helpTitle: "{ES}"', 1)
text = text.replace('helpTitle: "How to Use the App"', f'helpTitle: "{EN}"', 1)
text = text.replace(
    'instructionsToggle: "Cómo usar esta herramienta", instructionsTitle: "INSTRUCCIONES: Cómo usar esta herramienta"',
    f'instructionsToggle: "{ES}", instructionsTitle: "{ES}"',
    1,
)
text = text.replace(
    'instructionsToggle: "How to use this tool", instructionsTitle: "INSTRUCTIONS: How to use this tool"',
    f'instructionsToggle: "{EN}", instructionsTitle: "{EN}"',
    1,
)

# Default HTML button text / panel title
text = text.replace(
    '<span id="instructions-toggle-text">Cómo usar esta herramienta</span>',
    f'<span id="instructions-toggle-text">{ES}</span>',
    1,
)
text = text.replace(
    '<h3 id="instructions-title" class="text-xl font-bold text-black dark:text-white mb-3">INSTRUCCIONES: Cómo usar esta herramienta</h3>',
    f'<h3 id="instructions-title" class="text-xl font-bold text-black dark:text-white mb-3">{ES}</h3>',
    1,
)

# Extract openInstructions helper and wire help + toggle
open_fn = '''
        function openInstructionsPanel(open) {
            const body = dom.instructionsPanelBody;
            const btn = dom.instructionsToggle;
            if (!body || !btn) return;
            const shouldOpen = open === undefined
                ? (body.classList.contains('hidden') || body.hasAttribute('hidden'))
                : !!open;
            if (shouldOpen) {
                body.classList.remove('hidden');
                body.removeAttribute('hidden');
                btn.setAttribute('aria-expanded', 'true');
                btn.classList.add('is-open');
                body.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            } else {
                body.classList.add('hidden');
                body.setAttribute('hidden', '');
                btn.setAttribute('aria-expanded', 'false');
                btn.classList.remove('is-open');
            }
        }

'''

if "function openInstructionsPanel" not in text:
    # insert before setupEventListeners
    text = text.replace(
        "        function setupEventListeners() {",
        open_fn + "        function setupEventListeners() {",
        1,
    )

# Replace instructions toggle listener
old_toggle = """dom.instructionsToggle?.addEventListener('click', () => {
                const body = dom.instructionsPanelBody;
                if (!body) return;
                const open = body.classList.contains('hidden') || body.hasAttribute('hidden');
                if (open) {
                    body.classList.remove('hidden');
                    body.removeAttribute('hidden');
                    dom.instructionsToggle.setAttribute('aria-expanded', 'true');
                    dom.instructionsToggle.classList.add('is-open');
                } else {
                    body.classList.add('hidden');
                    body.setAttribute('hidden', '');
                    dom.instructionsToggle.setAttribute('aria-expanded', 'false');
                    dom.instructionsToggle.classList.remove('is-open');
                }
            });
            """
new_toggle = """dom.instructionsToggle?.addEventListener('click', () => openInstructionsPanel());
            """
if old_toggle in text:
    text = text.replace(old_toggle, new_toggle, 1)
else:
    # try without optional chaining
    text = re.sub(
        r"dom\.instructionsToggle\?\.addEventListener\('click', \(\) => \{.*?\}\);\s*",
        new_toggle,
        text,
        count=1,
        flags=re.S,
    )

# Help button opens same panel instead of modal
text = text.replace(
    "dom.helpBtn.addEventListener('click', () => dom.helpModal.classList.remove('hidden'));",
    "dom.helpBtn.addEventListener('click', () => openInstructionsPanel(true));",
    1,
)

# setLanguage: use unified title for toggle and panel heading
text = text.replace(
    "if (dom.instructionsTitle) dom.instructionsTitle.textContent = t.instructionsTitle;",
    "if (dom.instructionsTitle) dom.instructionsTitle.textContent = t.instructionsTitle || t.instructionsToggle || t.helpTitle;",
    1,
)
text = text.replace(
    "if (dom.instructionsToggleText) dom.instructionsToggleText.textContent = t.instructionsToggle || t.instructionsTitle || 'Cómo usar esta herramienta';",
    "if (dom.instructionsToggleText) dom.instructionsToggleText.textContent = t.instructionsToggle || t.helpTitle || t.instructionsTitle;",
    1,
)
# help modal title still set but unused — keep in sync
text = text.replace(
    "dom.helpModalTitle.textContent = t.helpTitle;",
    "dom.helpModalTitle.textContent = t.helpTitle || t.instructionsToggle;",
    1,
)

path.write_text(text, encoding="utf-8", newline="\n")

t = path.read_text(encoding="utf-8")
print("helpTitle ES", f'helpTitle: "{ES}"' in t)
print("helpTitle EN", f'helpTitle: "{EN}"' in t)
print("instr title unified", f'instructionsTitle: "{ES}"' in t)
print("open fn", "function openInstructionsPanel" in t)
print("help opens panel", "openInstructionsPanel(true)" in t)
print("toggle uses helper", "openInstructionsPanel()" in t)
print("DONE")
