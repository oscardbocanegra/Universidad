[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Teoría de Autómatas / Automata Theory

Este directorio contiene recursos y trabajos para la asignatura de Teoría de Autómatas.

This directory contains resources and assignments for the subject of Automata Theory.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `Autómatas_finitos_y_lenguajes_regulares_JFLAP.pdf`, `trabajo1.jff` — Recursos y trabajos / Resources and assignments

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
