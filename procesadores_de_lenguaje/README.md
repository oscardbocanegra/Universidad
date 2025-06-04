[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Procesadores de Lenguaje / Language Processors

Este directorio contiene recursos y soluciones para la asignatura de Procesadores de Lenguaje.

This directory contains resources and solutions for the subject of Language Processors.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `informe.pdf`, `laboratorio_solucion.R` — Informes y soluciones de laboratorio / Reports and lab solutions
- **trabajo2/**
  - `lexer.py`, `procesadores_de_lenguajes_2.docx`, `procesadores_de_lenguajes_2.pdf` — Ejercicios y documentación / Exercises and documentation

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
