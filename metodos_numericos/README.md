[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Métodos Numéricos / Numerical Methods

Este directorio contiene trabajos y recursos para la asignatura de Métodos Numéricos.

This directory contains assignments and resources for the subject of Numerical Methods.

## Estructura de Carpetas y Archivos / Folder and File Structure

- **trabajo1/**
  - `colgii29_t2_lab/` — Laboratorio / Lab
- **trabajo2/**
  - `metodos de las multiplicaciones sucesivas.docx`, `newton_raphson.py` — Métodos numéricos / Numerical methods

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
