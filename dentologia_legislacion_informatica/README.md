[![Projects](https://img.shields.io/badge/Projects-1-blue.svg)](#-proyectos)
# Dentología, Legislación e Informática

This directory contains resources and activities for the subject of Dentistry, Legislation, and Informatics.

Este directorio contiene recursos y actividades para la asignatura de Dentología, Legislación e Informática.

## Folder and File Structure / Estructura de Carpetas y Archivos

- **act1/**
  - `act1.pdf` — Activity 1 statement / Enunciado de la actividad 1

## How to keep this README dynamic? / ¿Cómo mantener este README dinámico?

You can update this README automatically by running a script that lists the folder contents and formats them in Markdown. For example, in PowerShell:

Puedes actualizar automáticamente este README ejecutando un script que liste el contenido de la carpeta y lo formatee en Markdown. Por ejemplo, en PowerShell:

```powershell
Get-ChildItem -Recurse | ForEach-Object {
    if ($_.PSIsContainer) {
        "- **$($_.Name)/**"
    } else {
        "  - `$($_.Name)`"
    }
}
```

Copy the output and paste it into the structure section. / Copia la salida y pégala en la sección de estructura.

---

_Add brief descriptions for each file or folder as needed. / Agrega descripciones breves para cada archivo o carpeta según corresponda._
