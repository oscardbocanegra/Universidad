[![Projects](https://img.shields.io/badge/Projects-1-blue.svg)](#-proyectos)
# Estructura de Computadores / Computer Structure

Este directorio contiene ejercicios y recursos para la asignatura de Estructura de Computadores.

This directory contains exercises and resources for the subject of Computer Structure.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `ejercicio1.asm`, `ejercicio2.asm`, `ejercicio3.asm` — Ejercicios en ensamblador / Assembly exercises
- `estructura.pdf` — Apuntes o teoría / Notes or theory

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
