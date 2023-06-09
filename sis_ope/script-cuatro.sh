#! /bin/bash

# si el numero de parametros menor o igual que 0
if [ $# -le 0 ]; then
   echo "Hay que introducir al menos un parametro"
   exit 1
fi

MENSAJE="Hola"
PRIMERO=1

# mientras haya parametro
while [ -n "$1" ]; do

     if [ $PRIMERO -eq 1 ]; then
           MENSAJE="$MENSAJE $1"
           PRIMERO=0
     else
           MENSAJE="$MENSAJE, $1"
     fi

     # pasamos al siguiente parametro
     shift
done

# mostramos la salida por pantalla
echo $MENSAJE"!"
