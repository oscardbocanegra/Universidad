[![Projects](https://img.shields.io/badge/Projects-2-yellow.svg)](#-proyectos)
# Diseño Avanzado / Advanced Design

Este directorio contiene archivos y proyectos para la asignatura de Diseño Avanzado.

This directory contains files and projects for the subject of Advanced Design.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `datos_100.txt`, `datos_1000.txt`, `datos_10000.txt` — Datos de ejemplo / Example data
- `laboratorio1.py` — Laboratorio 1 / Lab 1
- **trabajo_2/**
  - `puzle.py` — Ejercicio de puzzle / Puzzle exercise

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
