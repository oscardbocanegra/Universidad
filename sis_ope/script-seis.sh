#! bin/bash

# funcion de ayuda
function ayuda() {

cat << DESCRIPCION_AYUDA
SYNOPSIS
	$0 NOMBRE_1 [NOMBRE_2] ... [NOMBRE_N]

DESCRIPCION
	Muestra "Hola NOMBRE_1, NOMBRE_2, ... NOMBRE_N!" por pantalla.

CODIGOS DE RETORNO
	1 Si el numero de parametro es menor que 1
	2 Si el usuario no esta conectado
DESCRIPCION_AYUDA

}

# si numero de parametro <= 0
if [ $# -le 0 ] ; then
	echo "Hay que introducir al menos un parametro"
	ayuda
	exit 1
fi

MENSAJE="Hola"
PRIMERO=1

# mientras haya parametros
while [ -n "$1" ]; do
	ESTA_CONECTADO=`who | grep $1`

	if [ -z "ESTA_CONECTADO" ]; then
		echo "El usuario $1 no esta conectado"
		ayuda
		exit 2
	fi

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
echo ${MENSAJE}"!"
