[![Projects](https://img.shields.io/badge/Projects-6-green.svg)](#-proyectos)
# Aprendizaje Automático y Minería de Datos

Este directorio contiene actividades, datasets y soluciones relacionadas con la asignatura de Aprendizaje Automático y Minería de Datos.

## Estructura de Carpetas y Archivos

- **act1/**
  - `act1.docx` — Enunciado de la actividad 1 (Word)
  - `act1.pdf` — Enunciado de la actividad 1 (PDF)
  - `solve_act.ipynb` — Notebook con la solución de la actividad 1
  - `dataset/` — Conjunto de datos utilizado en la actividad 1
- **act2/**
  - `act2.pdf` — Enunciado de la actividad 2 (PDF)
  - `actividad2.ipynb` — Notebook con la solución de la actividad 2
  - `gii32_t4_trab.docx` — Documento adicional relacionado
  - `file/` — Carpeta para archivos auxiliares

## ¿Cómo mantener este README dinámico?

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

Luego, puedes copiar la salida y pegarla en la sección de estructura.

---

_Agrega descripciones breves para cada archivo o carpeta según corresponda._
