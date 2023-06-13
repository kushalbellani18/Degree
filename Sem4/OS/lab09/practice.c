#include<stdio.h>
#include<stdlib.h>
#include<signal.h>
#include<unistd.h>

void handlerSigStop(int signum);
void handlerSigCont(int signum);
void handlerSigInt(int signum);

int main() {
	pid_t pid;
	void (*sigStopReturn) (int);
	void (*sigContReturn) (int);
	void (*sigIntReturn) (int);

//	pid = fork();

//	printf("%d", pid);

//	if(pid == 0) {
		sigStopReturn = signal(SIGSTOP, handlerSigStop);
		sigContReturn = signal(SIGCONT, handlerSigCont);
		sigIntReturn = signal(SIGINT, handlerSigInt);

		if(sigStopReturn == SIG_ERR)
			printf("Not Caught in SIGSTOP!");
		if(sigIntReturn == SIG_ERR)
			printf("Not Caught in SIGINT!");
		if(sigContReturn == SIG_ERR)
			printf("Not Caught in SIGCONT!");

		for(int i=0; i<10; i++) {
			printf("%d\n", i);
			sleep(1);
		}
//	}


	kill(pid, SIGCONT);
	kill(pid, SIGINT);

	printf("\n");
	return 0;
}

void handlerSigStop(int signum) {
	if(signum == SIGSTOP) {
		printf("SIGSTOP is obtained!");
		exit(0);
	}
}

void handlerSigCont(int signum) {
	if(signum == SIGCONT) {
		printf("SIGCONT is obtained!");
		exit(0);
	}
}

void handlerSigInt(int signum) {
	if(signum == SIGINT) {
		printf("SIGINT is obtained!");
		exit(0);
	}
}
