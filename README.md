# Generador de Prompts Académicos

Una aplicación web moderna para crear prompts estructurados que optimizan las búsquedas de investigación académica con IA.

## 🎯 Descripción

Esta herramienta permite a investigadores, estudiantes y académicos generar prompts especializados para realizar búsquedas profundas y estructuradas utilizando inteligencia artificial como **Gemini AI** o **Claude AI**.

## ✨ Características

### 🔍 **Generación Inteligente de Prompts**
- Creación automática de prompts JSON estructurados
- **Dual AI Integration**: Soporte para Google Gemini y Anthropic Claude
- Reformulación inteligente de temas de investigación
- Sugerencias de conceptos clave multiidioma
- Selector de proveedor de IA en tiempo real

### 🎨 **Interfaz Moderna**
- Diseño responsive optimizado para móvil y desktop
- Tema oscuro/claro adaptativo
- Paleta de colores profesional inspirada en diseño académico
- Animaciones suaves y experiencia de usuario fluida

### 🌐 **Soporte Multiidioma**
- Español e inglés completamente soportados
- Interfaz que se adapta dinámicamente al idioma seleccionado

### ⚙️ **Filtros Avanzados**
- **Filtros Generales**: Área geográfica, idiomas, fechas de publicación
- **Fuentes Académicas**: Bases de datos confiables (Google Scholar, Scielo, Redalyc, Latindex, Dialnet, PubMed, etc.)
- **Tipos de Documento**: Artículos, libros, tesis, revisiones, conferencias
- **Criterios de Calidad**: Revisión por pares, texto completo

### 📊 **Formatos de Salida**
1. **Lienzo IA (Detallado)**: Lista bibliográfica completa en formato APA
2. **BibTeX**: Para importar directamente a gestores de referencias

## 🚀 Uso

### Método Básico
1. **Selecciona tu proveedor de IA** (Gemini AI o Claude AI)
2. **Ingresa tu tema** de investigación en el campo principal
3. **Configura los filtros** según tus necesidades específicas
4. **Selecciona el formato** de salida deseado
5. **Genera el prompt** y cópialo
6. **Pégalo en tu IA** de investigación favorita

### Características de IA (Opcional)
- **Reformular**: Obtén nuevos enfoques para tu tema usando la IA seleccionada
- **Sugerir Conceptos**: Encuentra términos de búsqueda relevantes en múltiples idiomas
- **Cambio dinámico**: Alterna entre Gemini y Claude según tus preferencias

## 🛠️ Instalación

### Método Simple
```bash
# Clona el repositorio
git clone [URL_DEL_REPOSITORIO]

# Navega al directorio
cd Promp-Academicos

# Abre index.html en tu navegador favorito
```

### Servidor Local (Recomendado)
```bash
# Con Python 3
python -m http.server 8000

# Con Node.js (si tienes live-server instalado)
npx live-server

# Con PHP
php -S localhost:8000
```

## 🔧 Configuración

### APIs de IA (Opcional)
Para habilitar las funciones de IA, puedes configurar una o ambas API keys:

#### **Gemini AI**
1. Obtén tu API key en [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Abre `index.html` y busca la configuración (alrededor de la línea 245):
```javascript
const aiConfig = {
    gemini: {
        apiKey: "TU_GEMINI_API_KEY_AQUÍ", // Añade tu clave de Gemini
        endpoint: "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent"
    },
    //...
};
```

#### **Claude AI**
1. Obtén tu API key en [Anthropic Console](https://console.anthropic.com/)
2. En la misma sección de configuración:
```javascript
const aiConfig = {
    //...
    claude: {
        apiKey: "TU_CLAUDE_API_KEY_AQUÍ", // Añade tu clave de Claude
        endpoint: "https://api.anthropic.com/v1/messages"
    }
};
```

> **Nota**: Sin API keys, la aplicación funciona perfectamente para generar prompts, pero sin las funciones de reformulación y sugerencias automáticas. Puedes configurar solo una de las dos APIs si prefieres.

## 📁 Estructura del Proyecto

```
Promp-Academicos/
│
├── index.html          # Aplicación principal
├── README.md           # Este archivo
└── [espacio para logo] # Coloca tu logo en el directorio raíz
```

## 🎨 Personalización

### Logo
- Coloca tu logo en el directorio raíz
- Modifica las líneas 66-70 en `index.html` para referenciar tu imagen:
```html
<img src="logo-CMSI.png" alt="Logo" class="w-32 h-16 object-contain">
```

### Colores
La aplicación utiliza una paleta de colores profesional:
- **Fondo**: #f3ede0 (beige claro)
- **Acentos**: #d5b690 (beige oscuro)
- **Hover**: #b8a082 (beige más oscuro)

## 📚 Bases de Datos Académicas Incluidas

La herramienta incluye acceso a las principales bases de datos académicas de acceso abierto:

### **Bases de Datos Regionales**
- **Scielo** - Red de revistas científicas de América Latina, España y Portugal
- **Redalyc** - Red de Revistas Científicas de América Latina y el Caribe
- **Latindex** - Sistema Regional de Información en Línea para Revistas Científicas de América Latina, el Caribe, España y Portugal
- **Dialnet** - Portal de difusión de la producción científica hispana

### **Bases de Datos Internacionales**
- **Google Scholar** - Motor de búsqueda de literatura académica
- **PubMed Central** - Archivo digital de literatura biomédica y de ciencias de la vida
- **ERIC** - Base de datos de literatura educativa
- **arXiv** - Repositorio de preprints en física, matemáticas, ciencias de la computación
- **DOAJ** - Directory of Open Access Journals
- **CORE** - Agregador de papers de investigación de acceso abierto

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Haz fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia Creative Commons Attribution 4.0 International (CC BY 4.0).

## 👥 Autoría y Atribución

### Desarrollo Inicial
**Pablo G. Guízar** con la asistencia de Gemini  
📂 **Proyecto original**: [Generador de Prompts Académicos Avanzado](https://gemini.google.com/share/4af4639b6049)  
🗓️ **Desarrollo inicial**: 2024

### Modificaciones y Mejoras
**Claudia Serpa Imbett** con la asistencia de Claude Code  
✨ **Mejoras incluidas**:
- Integración dual de IA (Gemini + Claude)
- Nuevo esquema de colores profesional
- Simplificación a español e inglés únicamente
- Optimizaciones de interfaz y experiencia de usuario

---

### ✅ **Cumplimiento CC BY 4.0**
Este README cumple con los requisitos de la licencia Creative Commons Attribution 4.0:

- ✅ **Atribución completa**: Autor original claramente identificado
- ✅ **Enlace al trabajo original**: Proporcionado arriba
- ✅ **Indicación de cambios**: Modificaciones documentadas
- ✅ **Misma licencia**: Mantenida CC BY 4.0
- ✅ **Aviso de licencia**: Incluido en el código y documentación

## 🆘 Soporte

Si encuentras algún problema o tienes sugerencias:

1. Revisa la sección de ayuda en la aplicación (botón ❓)
2. Abre un issue en el repositorio
3. Contacta al desarrollador

## 🔗 Enlaces Útiles

- [Google AI Studio](https://makersuite.google.com/) - Para obtener API keys de Gemini
- [Anthropic Console](https://console.anthropic.com/) - Para obtener API keys de Claude
- [TailwindCSS](https://tailwindcss.com/) - Framework CSS utilizado
- [Creative Commons](https://creativecommons.org/licenses/by/4.0/) - Información sobre la licencia

## 🤖 Comparación de Proveedores de IA

### **Gemini AI**
- ✅ Excelente para análisis multiidioma
- ✅ Respuestas rápidas y precisas
- ✅ Formato JSON nativo
- 💡 Ideal para sugerencias de conceptos académicos

### **Claude AI**
- ✅ Comprensión profunda del contexto
- ✅ Reformulaciones muy naturales
- ✅ Excelente para temas complejos
- 💡 Ideal para investigación avanzada

> **Recomendación**: Prueba ambos proveedores para ver cuál se adapta mejor a tu estilo de investigación. Puedes alternar entre ellos según el tipo de consulta.

---

**¡Feliz investigación! 🎓📚**