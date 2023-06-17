#!/bin/bash
echo "Ingrese el nombre del directorio:"
read directorio
if [ ! -d "$directorio" ]; then
  mkdir "$directorio"
  echo "Directorio creado."
else
  echo "El directorio ya existe."
fi

