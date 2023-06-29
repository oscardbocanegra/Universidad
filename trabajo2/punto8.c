#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>

int main(){
int i,j,fd;
int dato;
fd=open("prueba", O_RDONLY);
if (fork()!=0){
	while(read(fd,&dato,sizeof(int))>0){
		for(j=0;j<100000;j++); /*espera*/
			printf("Proceso padre. Dato =%d \n", dato);
		}
	}
else{
	while(read(fd, &dato,sizeof(int))>0){
		printf("Proceso hijo.Dato =%d\n", dato);
		}
	}
close(fd);
exit(0);
}
