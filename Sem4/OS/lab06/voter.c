#include<stdio.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<sys/msg.h>
#include<string.h>

struct msgQueue {
	long msgType;	//msgType would be set to 1 after msgget(), otherwise common error!!!
	char name[100];
};

int main() {
	struct msgQueue voterName;
	key_t key1, key2;

	key1 = ftok("lab06_1", 45);
	key2 = ftok("lab06_2", 46);

	int msgid1 = msgget(key1, 0666 | IPC_CREAT);
	int msgid2 = msgget(key2, 0666 | IPC_CREAT);
	voterName.msgType = 1;

	while(1) {
		printf("\n---------------------------------------");
		printf("\nEnter your name: ");
		scanf("%s", voterName.name);
		//fgets(voterName.name, 100, stdin);

		if(strcmp(voterName.name, "quit") == 0) {
			msgsnd(msgid1, &voterName, 100, 0);
			break;
		}

		msgsnd(msgid1, &voterName, 100, 0);
		printf("Please wait! %s is processing...",voterName.name);
		msgrcv(msgid2, &voterName, 100, 0, 0);

		printf("\n%s is done!!!", voterName.name);
		printf("\nPlease next!!");
	}

	voterName.msgType = 0;
	printf("\tExit!!\n");

	return 0;
}
