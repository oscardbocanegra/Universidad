[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Programación Avanzada Java / Advanced Java Programming

Este directorio contiene proyectos y recursos para la asignatura de Programación Avanzada Java.

This directory contains projects and resources for the subject of Advanced Java Programming.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `farmacy.zip`, `poo_banck_project.zip` — Proyectos comprimidos / Compressed projects
- **farmacy/**
  - `programacion.pdf` — Documentación / Documentation
  - **PharmacyOrderApp/** — Aplicación de farmacia / Pharmacy application
- **poo_banck_project/** — Proyecto de banco en Java / Java bank project

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
