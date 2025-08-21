# Generador de Prompts Académicos

Una aplicación web moderna y completamente optimizada para móviles que permite crear prompts estructurados para búsquedas de investigación académica con IA.

🌐 **Demo en vivo**: [https://cmsipages.netlify.app](https://cmsipages.netlify.app)

## 🎯 Descripción

Esta herramienta permite a investigadores, estudiantes y académicos generar prompts especializados para realizar búsquedas profundas y estructuradas utilizando inteligencia artificial. Incluye funcionalidades de demostración que funcionan sin necesidad de configurar API keys.

## ✨ Características

### 🔍 **Generación Inteligente de Prompts**
- Creación automática de prompts JSON estructurados
- **Funciones de IA integradas**: Reformulación y sugerencias de conceptos
- Generación contextual de términos clave relevantes por dominio
- Sugerencias bilingües (español/inglés) inteligentes
- Interfaz de demostración funcional sin API keys

### 🎨 **Interfaz Moderna y Móvil**
- **Diseño completamente responsive** con optimización específica para móviles
- **Logo CMSI integrado** con tamaño adaptativo
- Tema oscuro/claro adaptativo
- **Paleta de colores beige profesional** inspirada en cmsipage.netlify.app
- Botones táctiles optimizados para dispositivos móviles
- Espaciado y tipografía adaptativa
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
1. **Lienzo IA (Detallado)**: Lista bibliográfica completa
2. **BibTeX + APA**: Para gestores de referencias en formato APA
3. **BibTeX + IEEE**: Para gestores de referencias en formato IEEE

## 🚀 Uso

### Pasos Básicos
1. **✨ Paso 1:** Escribe tu tema de investigación en el campo principal
2. **🔄 Paso 2:** Usa "Reformular" o "Sugerir Conceptos" para mejorar tu búsqueda con IA
3. **⚙️ Paso 3:** Ajusta los filtros según tus necesidades (idiomas, fechas, bases de datos)
4. **📊 Paso 4:** Escoge el formato de salida: BibTeX + APA o BibTeX + IEEE según prefieras
5. **🎯 Paso 5:** Genera el prompt y cópialo para usarlo con tu IA de investigación favorita

### 🤖 **IAs Sugeridas**
ChatGPT, Claude, Perplexity, Llama, Gemini, Copilot, Groq, Mistral, DeepSeek, etc.

### Características de IA Inteligentes
- **Reformular**: Obtén enfoques alternativos contextuales para tu tema
- **Sugerir Conceptos**: Términos específicos por dominio (energía, óptica, agricultura, medicina, etc.)
- **Generación contextual**: La IA reconoce el área de investigación y sugiere conceptos relevantes
- **Funciona sin configuración**: Modo demostración completamente funcional

## 🛠️ Instalación

### Acceso Directo
🌐 **Visita**: [https://cmsipages.netlify.app](https://cmsipages.netlify.app)

### Instalación Local
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

### ✅ **Funciona sin configuración**
La aplicación incluye un **modo demostración completamente funcional** que no requiere API keys. Las funciones "Reformular" y "Sugerir Conceptos" funcionan inmediatamente con respuestas inteligentes simuladas.

### 🚀 **Funciones de IA incluidas**
- **Reformulación contextual**: Genera enfoques alternativos basados en tu tema específico
- **Conceptos por dominio**: Reconoce automáticamente el área (energía, medicina, educación, etc.) y sugiere términos relevantes
- **Términos bilingües**: Conceptos en español e inglés según el dominio de investigación
- **Sin autenticación**: Funciona directamente sin necesidad de configurar APIs externas

### 🔧 **APIs Opcionales (Para producción)**
Si deseas conectar APIs reales de IA:

#### **Gemini AI**
1. Obtén tu API key en [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Reemplaza la función `callGemini` en `index.html` con llamadas reales a la API

> **Nota**: El modo demostración actual es completamente funcional para uso educativo y pruebas. Para implementaciones en producción con volúmenes altos, considera configurar APIs reales.

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
- **Logo CMSI integrado**: Ya incluido en `logo/logo-CMSI.png`
- **Responsive**: Tamaño adaptativo (32x16 en móvil, 56x28 en desktop)
- **Posición**: Alineado a la izquierda para mejor composición
- Para cambiar el logo, reemplaza el archivo en `logo/logo-CMSI.png`

### Colores
La aplicación utiliza una **paleta de colores beige profesional** inspirada en cmsipage.netlify.app:
- **Beige claro**: #f3ede0 (fondos principales)
- **Beige oscuro**: #d5b690 (acentos y botones)
- **Beige sutil**: #d6ccc2 (bordes y detalles)
- **Amarillo**: #fffc00 (elementos destacados)
- **Gradientes**: Combinaciones beige-amarillo para elementos especiales
- **Variables CSS**: Implementadas para fácil personalización

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
- **Optimización completa para móviles** con diseño responsive
- **Logo CMSI integrado** con tamaño adaptativo
- **Esquema de colores beige profesional** inspirado en cmsipage.netlify.app
- **Funciones de IA inteligentes** sin necesidad de API keys
- **Generación contextual de conceptos** por dominio de investigación
- **Formatos BibTeX mejorados** (APA e IEEE)
- **Simplificación a español e inglés** únicamente
- **Interfaz táctil optimizada** para dispositivos móviles
- **Espaciado y tipografía adaptativa**
- **Mensaje de advertencia** sobre verificación de información

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

1. **Demo en vivo**: [https://cmsipages.netlify.app](https://cmsipages.netlify.app)
2. Revisa la sección de ayuda en la aplicación (botón ❓)
3. Abre un issue en el repositorio
4. Contacta al desarrollador

### ⚠️ **Nota Importante**
Esta herramienta puede cometer errores. Siempre comprueba la información arrojada luego de copiar el prompt en tu IA escogida.

## 🔗 Enlaces Útiles

- [Google AI Studio](https://makersuite.google.com/) - Para obtener API keys de Gemini
- [Anthropic Console](https://console.anthropic.com/) - Para obtener API keys de Claude
- [TailwindCSS](https://tailwindcss.com/) - Framework CSS utilizado
- [Creative Commons](https://creativecommons.org/licenses/by/4.0/) - Información sobre la licencia

## 🤖 Funciones de IA Integradas

### **Reformulación Inteligente**
- ✅ Genera enfoques alternativos contextuales
- ✅ Perspectivas complementarias automáticas
- ✅ Adaptación al tema específico del usuario
- 💡 Ejemplo: "energías renovables" → "Análisis comparativo de energías renovables"

### **Sugerencias de Conceptos por Dominio**
- ✅ **Energía**: sostenibilidad, eficiencia energética, biomasa, solar power
- ✅ **Medicina**: biomedicina, diagnóstico, epidemiología, clinical research
- ✅ **Educación**: pedagogía, metodología, educational technology
- ✅ **IA**: machine learning, deep learning, redes neuronales
- ✅ **Agricultura**: agricultura digital, IoT agrícola, precision agriculture
- 💡 **Reconocimiento automático** del dominio de investigación

### **Términos Bilingües Inteligentes**
- ✅ Conceptos en español e inglés relevantes
- ✅ Terminología académica especializada
- ✅ Sinónimos y variaciones de búsqueda

> **Ventaja**: Funciona inmediatamente sin configuración, ideal para demostraciones y uso educativo.

---

---

**🌐 Demo en vivo**: [https://cmsipages.netlify.app](https://cmsipages.netlify.app)

**¡Feliz investigación! 🎓📚**