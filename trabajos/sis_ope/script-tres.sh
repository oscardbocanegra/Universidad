#! /bin/bash
echo "numero de parametros = $#"
# si numero de parametros menor o igual que 0
if [ $# -le 0 ]; then
   echo "Hay que introducir al menos un parametro"
   exit 1
fi
echo "Hola $@!"
