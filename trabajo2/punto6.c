#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
printf("Inicio de test\n");
if (fork() == 0)
printf("Yo soy el hijo\n");
else
printf("Yo soy el padre\n");
exit(0);
}
