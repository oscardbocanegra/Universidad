[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Informática Gráfica y Visualización / Computer Graphics and Visualization

Este directorio contiene actividades y recursos para la asignatura de Informática Gráfica y Visualización.

This directory contains activities and resources for the subject of Computer Graphics and Visualization.

## Estructura de Carpetas y Archivos / Folder and File Structure

- **act1/**
  - `actividad_reloj.doc`, `actividad_reloj.pdf`, `reloj.py` — Actividad de reloj / Clock activity
- **act2/**
  - `colgii52t7trab.doc`, `colgii52t7trab.pdf`, `cuatro_vistas_cubo.py`, `main.py` — Actividad de cubo y vistas / Cube and views activity
  - `venv/` — Entorno virtual / Virtual environment

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
