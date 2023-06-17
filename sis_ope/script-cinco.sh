#! /bin/bash

# funcion de ayuda
function ayuda() {

cat << DESCRIPCION_AYUDA
SYNOPSIS
      $0 NOMBRE_ [NOMBRE_2] ... [NOMBRE_N]

DESCRIPCION
   Muestra "hola NOMBRE_1, NOMBRE_2, ... NOMBRE_N!" por pantalla

CODIGOS DE RETORNO
      1 Si el numero de parametro es menor que 1

DESCRIPCION_AYUDA

}

# si numero de parametros <= 0
if test $# -le 0 ; then
  echo "Hay que introducir al menos un parametro"
  ayuda
  exit 1
fi

MENSAJE="Hola"
PRIMERO=1

# mientras haya parametros
while [ -n "$1" ]; do

      if [ $PRIMERO -eq 1 ]; then
            MENSAJE="$MENSAJE $1"
            PRIMERO=0
      else
            MENSAJE="$MENSAJE $1"
      fi

     # pasamos al siguiente parametro
     shift
done

# mostramos la salida por pantalla
echo $MENSAJE"!"

exit 0
