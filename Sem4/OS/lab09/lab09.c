#include<stdio.h>
#include<signal.h>
#include<unistd.h>
#include<stdlib.h>

void handlerSigStop(int signum);
void handlerSigCont(int signum);
void handlerSigInt(int signum);

int main() {
	pid_t pid;
	void (*sigStopReturn) (int);
	void (*sigContReturn) (int);
	void (*sigIntReturn) (int);

	pid = fork();

	if(pid == 0) {
		//Check for SIGSTOP HANDLER
		sigStopReturn = signal(SIGSTOP, handlerSigStop);
		if(sigStopReturn == SIG_ERR) {
			printf("\nNot Caught in SIGSTOP\n");
//			return 1;
		}

		//Check for SIGCONT Handler
		sigContReturn = signal(SIGCONT, handlerSigCont);
		if(sigContReturn == SIG_ERR) {
			printf("\nCaught in SIGCONT\n");
//			return 1;
		}

		//Check for SIGINT Handler
		sigIntReturn = signal(SIGINT, handlerSigInt);
		if(sigIntReturn == SIG_ERR) {
			printf("\nCaught in SIGINT\n");
//			return 1;
		}


		while(1) {
			printf("PID - %d is Alive!\n",pid);
			sleep(1);
		}
	}

	sleep(5);

//	kill(pid, SIGSTOP); //Suspend
	kill(pid, SIGCONT); //Resume
	kill(pid, SIGINT);  //Interrupt
	printf("\n");
	return 0;
}

void handlerSigStop(int signum) {
	if(signum == SIGSTOP) {
		printf("SIGSTOP is obtained!!!\n\n");
		exit(0);
	} else {
		printf("Received %d Signal\n", signum);
	}
}

void handlerSigCont(int signum) {
	if(signum == SIGCONT) {
		printf("SIGCONT is obtained!!!\n\n");
		exit(0);
	} else {
		printf("Received %d Signal\n", signum);
	}
}

void handlerSigInt(int signum) {
	if(signum == SIGINT) {
		printf("SIGINT is obtained!!!\n\n");
		exit(0);
	} else {
		printf("Received %d Signal\n", signum);
	}
}
