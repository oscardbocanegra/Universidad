[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Investigación de Operaciones / Operations Research

Este directorio contiene actividades y recursos para la asignatura de Investigación de Operaciones.

This directory contains activities and resources for the subject of Operations Research.

## Estructura de Carpetas y Archivos / Folder and File Structure

- **act1/**
  - `glpk.py`, `por_si_aca.ggb`, `sol_act.docx`, `sol_act1.pdf`, `__pycache__/` — Actividad 1 y recursos / Activity 1 and resources
- **act2/**
  - `colgii36tema6actgrup.docx`, `sol_act.ipynb`, `sol_act2.pdf` — Actividad 2 y recursos / Activity 2 and resources

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
