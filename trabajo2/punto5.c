include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
	int i, fd,vector[10],dato,leidos;
	fd=creat("prueba", 0600);
	for(i=0;i<10;i++) vector[i]=i;
		write(fd, vector, sizeof(vector));
		close(0);
	fd= open("prueba", O_RDONLY);
	while ((leidos=read(fd,&dato,sizeof(int)))>0)
	{printf("leido el numero %d \n",dato);}
	close(fd);
	exit(0);
}
