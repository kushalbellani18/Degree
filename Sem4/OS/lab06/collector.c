#include<stdio.h>
#include<sys/ipc.h>
#include<sys/types.h>
#include<sys/msg.h>
#include<string.h>
#include<stdlib.h>
#include<sys/stat.h>
#include<fcntl.h>
#include<unistd.h>

struct msgQueue {
	long msgType;	//msgType would be set to 1 after msgget(), otherwise common error!!!
	char name[100];
};

void updateData(char str[]);

int main() {
	struct msgQueue voterName;
	key_t key1, key2;

	key1 = ftok("lab06_1", 45);
	key2 = ftok("lab06_2", 46);

	int msgid1 = msgget(key1, 0666 | IPC_CREAT);
	int msgid2 = msgget(key2, 0666 | IPC_CREAT);
	voterName.msgType = 1;

	int choice = -1;

	while(1) {
		msgrcv(msgid1, &voterName, 100, 0, 0);

		if(strcmp(voterName.name, "quit") == 0)
			break;

		printf("\t\t\tHi, %s! \n\t\tWelcome to vote...\n\n", voterName.name);
		printf("\t\t\t 1) Vote A or 2) Vote B\n\n");
		printf("Enter your choice: ");
		scanf("%d",&choice);

		if(choice == 1)
			updateData("voteA");
		else if(choice == 2)
			updateData("voteB");

		msgsnd(msgid2, &voterName, 100, 0);

		printf("\t\t\tKindly Please exit. Thanks for vote!!\n\n");

		choice = -1;
	}

	voterName.msgType = 0;

	return 0;
}

void updateData(char str[]) {
	char loc[50];
	int score, fd;

	strcpy(loc, "file/");
	strcat(loc, str);
	strcat(loc, ".txt");

	char *c = (char *) calloc(100, sizeof(char));
	char num[50];
	fd = open(loc, O_RDONLY);

	strcpy(num, "");

	while(read(fd, c, 1)) {
		if(strcmp(c, "\n") == 0)
			break;

		strcat(num, c);
	}

	score = atoi(num);
	score += 1;

	sprintf(num, "%d", score); //convert int to string

	close(fd);
	free(c);

	fd = open(loc, O_WRONLY);

	write(fd, num, sizeof(score));

	close(fd);
}
