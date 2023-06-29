#include <stdio.h>

int main() {
    FILE *archivo;
    archivo = fopen("numeros.txt", "w");

    if (archivo == NULL) {
        printf("No se pudo crear el fichero.");
        return 1;
    }


    for (int i = 0; i < 10; i++) {
        fprintf(archivo, "%d\n", i);
    }

    fclose(archivo);

    printf("Se han escrito los números del 0 al 9 en el fichero.\n");

    return 0;
}
