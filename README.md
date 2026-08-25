# Generador de Prompts Académicos

Aplicación web para crear prompts JSON estructurados y realizar búsquedas académicas profundas con IA. Optimizada para móvil y compatible con Chrome, Edge, Firefox y Safari.

🌐 **Demo en vivo**: [https://cmsipage.netlify.app/](https://cmsipage.netlify.app/)  
📦 **Repositorio**: [https://github.com/claumiseimbett1/prompt-generator-AI](https://github.com/claumiseimbett1/prompt-generator-AI)

## Descripción

Esta herramienta permite a investigadores, estudiantes y académicos generar prompts especializados para búsquedas profundas y estructuradas con inteligencia artificial. Incluye plantillas por área de estudio, validación BibTeX y un modo demostración que funciona sin API keys.

## Características

### Generación de prompts
- Creación automática de prompts JSON estructurados
- **Reformular** y **Sugerir Conceptos** con respuestas contextuales (modo demo)
- Sugerencias bilingües (español / inglés) por dominio de investigación
- Copia al portapapeles con fallback para distintos navegadores

### Plantillas por área (nuevo)
Precargan fuentes, tipos de documento, criterios de calidad, rango de fechas y formato de salida:

| Plantilla | Fuentes destacadas | Formato sugerido |
|-----------|-------------------|------------------|
| Medicina y salud | PubMed, Semantic Scholar, DOAJ, Crossref | BibTeX + APA |
| Educación | ERIC, Scielo, Redalyc, Google Scholar | BibTeX + APA |
| Ingeniería | arXiv, Semantic Scholar, CORE, Crossref | BibTeX + IEEE |
| Ciencias sociales | Scielo, Redalyc, Dialnet, JSTOR | BibTeX + APA |
| Ciencias ambientales | DOAJ, BASE, CORE, Semantic Scholar | Lienzo IA |
| Derecho | JSTOR, Dialnet, BASE, Google Scholar | BibTeX + APA |
| Tecnología e IA | arXiv, Semantic Scholar, Crossref, CORE | BibTeX + IEEE |
| Revisión sistemática | PubMed, Cochrane, Semantic Scholar, DOAJ, Scielo | Lienzo PRISMA |
| Revisión de alcance | PubMed, ERIC, Semantic Scholar, DOAJ, Scielo | Lienzo PRISMA-ScR |
| Meta-análisis | PubMed, Cochrane, Semantic Scholar, Crossref | Lienzo meta-análisis |
| Estado del arte | Scholar, Semantic Scholar, Scielo, Redalyc, JSTOR | Lienzo estado del arte |

### Validación BibTeX (nuevo)
Al elegir **BibTeX + APA** o **BibTeX + IEEE**, la app:
- Verifica que el prompt incluya campos clave (`author`, `title`, `year`, `doi`, `url`)
- Advierte si no hay fuentes seleccionadas o si falta «Revisado por pares»
- Muestra un panel de estado (ok / advertencia / error) antes de copiar
- Pide confirmación al copiar si hay advertencias pendientes

### Interfaz
- Diseño responsive con paleta beige profesional
- Logo CMSI integrado
- Tema claro / oscuro
- CSS local autocontenido (sin depender del CDN de Tailwind)
- Compatible con Chrome, Edge, Firefox y Safari

### Filtros avanzados
- **Generales**: área geográfica, idiomas, fechas de publicación
- **Fuentes**: 16 bases de datos académicas de acceso abierto
- **Documentos**: artículos, libros, tesis, revisiones, conferencias, informes, patentes
- **Calidad**: revisión por pares, solo texto completo (PDF)
- **Sitios personalizados**: dominios adicionales con sintaxis `site:`

### Formatos de salida
1. **Lienzo IA (Detallado)** — lista bibliográfica completa en APA 7
2. **Lienzo IA — Revisión sistemática (PRISMA)** — protocolo PICO, flujo PRISMA, extracción, calidad y síntesis
3. **Lienzo IA — Revisión de alcance (PRISMA-ScR)** — pregunta PCC, mapa de evidencia y vacíos
4. **Lienzo IA — Meta-análisis** — medida de efecto, tabla cuantitativa, heterogeneidad y GRADE
5. **Lienzo IA — Estado del arte** — mapa teórico, debates, tendencias, vacíos y posicionamiento
6. **BibTeX + APA** — para Zotero, Mendeley, etc.
7. **BibTeX + IEEE** — para ingeniería y ciencias exactas

## Uso rápido

1. Escribe tu **tema de investigación**
2. (Opcional) Elige una **plantilla** por área o tipo de revisión
3. Usa **Reformular** o **Sugerir Conceptos** para refinar
4. Ajusta filtros, fuentes y criterios de calidad
5. Escoge el **formato de salida** (lienzo, PRISMA, alcance, meta-análisis, estado del arte o BibTeX)
6. Genera el prompt, revisa avisos BibTeX si aplica, y **Copia** para pegarlo en tu IA

### IAs sugeridas
ChatGPT, Claude, Perplexity, Llama, Gemini, Copilot, Groq, Mistral, DeepSeek, etc.

## Instalación

### Acceso directo
Abre [https://cmsipage.netlify.app/](https://cmsipage.netlify.app/) en tu navegador.

### Local
```bash
git clone https://github.com/claumiseimbett1/prompt-generator-AI.git
cd prompt-generator-AI
# Abre index.html en el navegador, o usa un servidor local:
python -m http.server 8000
```

> **Importante al publicar**: sube `index.html`, `styles.css` y la carpeta `logo/` juntos. El CSS está incrustado en `index.html`, pero `styles.css` sirve como referencia para edición.

## Estructura del proyecto

```
prompt-generator-AI/
├── index.html      # Aplicación principal (HTML + CSS inline + JS)
├── styles.css      # Hoja de estilos de referencia (sincronizada con index.html)
├── logo/
│   └── logo-CMSI.png
└── README.md
```

## Bases de datos incluidas

### Regionales
- **Scielo** — América Latina, España y Portugal
- **Redalyc** — Revistas científicas de ALC
- **Latindex** — Directorio regional de revistas
- **Dialnet** — Producción científica hispana

### Internacionales
- **Google Scholar**
- **Semantic Scholar** — [semanticscholar.org](https://www.semanticscholar.org/)
- **PubMed Central**
- **ERIC**
- **arXiv**
- **DOAJ**
- **CORE**

### Agregadores y repositorios (nuevo)
- **Cochrane Library** — revisiones sistemáticas y evidencia clínica
- **ResearchGate**
- **JSTOR (OA)**
- **BASE** — [base-search.net](https://www.base-search.net/)
- **Crossref** — [crossref.org](https://www.crossref.org/)

Además: **Dominios confiables** (`.edu`, `.gov`, `.org`, `.int`, `.gob`, `.ac.uk`).

## Configuración de APIs (opcional)

La app funciona en **modo demostración** sin API keys. Para conectar Gemini u otra IA en producción, configura la clave en la sección `aiConfig` de `index.html`.

- [Google AI Studio](https://makersuite.google.com/app/apikey) — Gemini
- [Anthropic Console](https://console.anthropic.com/) — Claude

## Personalización

### Logo
Reemplaza `logo/logo-CMSI.png`. El tamaño es responsive (192×96 px en móvil, 224×112 px en desktop).

### Colores (variables CSS)
| Variable | Valor | Uso |
|----------|-------|-----|
| `--beige-light` | `#f3ede0` | Fondos |
| `--beige-dark` | `#d5b690` | Botones y acentos |
| `--beige-muted` | `#d6ccc2` | Bordes |
| `--yellow` | `#fffc00` | Destacados |

## Changelog reciente

### v2025.08 — Compatibilidad y nuevas funciones
- CSS local sin CDN de Tailwind (fix Chrome / Edge)
- Plantillas por área de estudio (7 disciplinas)
- Validación BibTeX al generar y copiar
- Nuevas fuentes: Semantic Scholar, ResearchGate, JSTOR (OA), BASE, Crossref
- SVG e inputs con tamaños fijos para evitar roturas visuales
- Mejoras de layout responsive en fila de botones

## Contribuir

1. Haz fork del repositorio
2. Crea una rama (`git checkout -b feature/mi-mejora`)
3. Commit y push
4. Abre un Pull Request

## Licencia

Creative Commons Attribution 4.0 International ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)).

Esta obra se basa en el proyecto original de Pablo G. Guízar. Se mantiene la atribución al autor, se indican las modificaciones y se conserva la misma licencia, conforme a CC BY 4.0.

## Autoría y atribución

**Desarrollo original** — Pablo G. Guízar, con asistencia de Gemini  
Proyecto original: [Generador de Prompts Académicos Avanzado](https://gemini.google.com/share/4af4639b6049)

**Modificado y ampliado** — Claudia Serpa Imbett, con asistencia de Claude Code / Cursor  

Entre otras mejoras:
- Optimización móvil y logo CMSI
- Plantillas por área y por tipo de revisión
- Lienzos de **revisión sistemática (PRISMA)**, **revisión de alcance (PRISMA-ScR)**, **meta-análisis** y **estado del arte**
- Validación BibTeX al generar y copiar
- Compatibilidad cross-browser (CSS local, sin dependencia del CDN de Tailwind)
- Nuevas fuentes académicas (Semantic Scholar, Cochrane, ResearchGate, JSTOR OA, BASE, Crossref, etc.)
- Formatos BibTeX APA / IEEE e instrucciones actualizadas (ES/EN)

### Cumplimiento CC BY 4.0
- Atribución al autor original
- Enlace al trabajo original
- Indicación de cambios / ampliaciones
- Misma licencia CC BY 4.0
- Aviso de licencia en la aplicación y en este README

## Soporte

- Demo: [cmsipage.netlify.app](https://cmsipage.netlify.app/)
- Ayuda integrada: botón **?** en la app
- Issues: [GitHub Issues](https://github.com/claumiseimbett1/prompt-generator-AI/issues)

> ⚠️ Esta herramienta puede cometer errores. Comprueba siempre la información después de usar el prompt en tu IA.

---

**¡Feliz investigación!**
