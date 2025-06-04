[![Projects](https://img.shields.io/badge/Projects-2-green.svg)](#-proyectos)
# Informática Teórica / Theoretical Computer Science

Este directorio contiene trabajos y recursos para la asignatura de Informática Teórica.

This directory contains assignments and resources for the subject of Theoretical Computer Science.

## Estructura de Carpetas y Archivos / Folder and File Structure

- **trabajo1/**
  - `Ejercicio 1.jff.resx.jff`, `ejercicio2.jff`, `Laboratorio_Máquinas_Turing_JFLAP.pdf` — Ejercicios y laboratorio de máquinas de Turing / Turing machine exercises and lab
- **trabajo2/**
  - `punto1.jff`, `punto2.jff`, `trabajo_info_teorica.pdf` — Ejercicios y trabajo teórico / Exercises and theoretical work

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
