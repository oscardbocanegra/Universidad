[![Projects](https://img.shields.io/badge/Projects-1-blue.svg)](#-proyectos)
# Sistemas Inteligentes / Intelligent Systems

Este directorio contiene recursos y ejercicios para la asignatura de Sistemas Inteligentes.

This directory contains resources and exercises for the subject of Intelligent Systems.

## Estructura de Carpetas y Archivos / Folder and File Structure

- `agente_maquina_expendedora.py`, `agente_reactivo_simple.py` — Ejercicios de agentes / Agent exercises

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
