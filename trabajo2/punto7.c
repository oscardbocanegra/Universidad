#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){

int i,j;

if (fork()!=0){
	for (i=0;i<100;i++){
		for (j=0;j<100000;i++){
			printf("Proceso padre. Indicate i=%d \n", i);
		}
	}
}else {
	for (i=0;1<100;i++){
		for(j=0;j<100000;j++){
			printf("Proceso hijo. Indicate i=%d \n", i);
		}
	}
}

exit(0);

}
