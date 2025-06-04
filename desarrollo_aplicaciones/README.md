[![Projects](https://img.shields.io/badge/Projects-4-orange.svg)](#-proyectos)
# Desarrollo de Aplicaciones / Application Development

Este directorio contiene proyectos, recursos y ejemplos para la asignatura de Desarrollo de Aplicaciones.

This directory contains projects, resources, and examples for the subject of Application Development.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `principal.html` — Página principal / Main page
- `styles.css` — Estilos globales / Global styles
- **2nd_project/**
  - `app.js` — Lógica principal / Main logic
  - `index.html` — Página de inicio / Home page
  - `styles.css` — Estilos / Styles
- **imagenes/**
  - `cer1.png`, `cer2.png`, `cer3.png`, `cer4.png`, `ingles.png`, `perfiles.jpg` — Imágenes de recursos / Resource images
- **project/**
  - `package.json`, `package-lock.json` — Configuración de Node.js / Node.js configuration
  - `node_modules/` — Dependencias / Dependencies
- **testapp/**
  - `firebase-config.js` — Configuración de Firebase / Firebase config
  - `index.html`, `main.js`, `style.css` — Archivos principales / Main files
  - **assets/**, **components/** — Recursos y componentes / Assets and components

## ¿Cómo mantener este README dinámico? / How to keep this README dynamic?

Puedes actualizar automáticamente este README ejecutando un script que liste el contenido de la carpeta y lo formatee en Markdown. For example, in PowerShell:

```powershell
Get-ChildItem -Recurse | ForEach-Object {
    if ($_.PSIsContainer) {
        "- **$($_.Name)/**"
    } else {
        "  - `$($_.Name)`"
    }
}
```

Luego, puedes copiar la salida y pegarla en la sección de estructura. / Then, you can copy the output and paste it into the structure section.

---

_Agrega descripciones breves para cada archivo o carpeta según corresponda. / Add brief descriptions for each file or folder as needed._
