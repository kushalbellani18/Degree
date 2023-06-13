#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/wait.h>

int main() {
	pid_t pid;
	int *ptr;
	float avg = 0;

	pid = fork();
	ptr = (int *)malloc(3 * sizeof(*ptr));

	printf("Enter 3 different employee salayees:\n");
	for(int i=0; i<3; i++) {
		scanf("%d", &ptr[i]);
	}

	for(int i=0; i<3; i++) {
		printf("pid - %d ---> %d\n", pid, ptr[i]);
		avg += (float)ptr[i];
	}
	avg /= 3;

	free(ptr);
//	printf("\t\tAVG: %f\n", avg);

	if(pid == 0) {
		printf("\nThis is Child Process\n");
		printf("\t\tAVG: %f\n", avg);

	} else {
		printf("\nThis is Parent Process\n");
		printf("\t\tAVG: %f\n", avg);
	}

	return 0;
}
