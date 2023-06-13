#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/stat.h>
#include<fcntl.h>

struct passportApplication {
	char name[90];
	char address[100];
	int aadharNumber;
	char email[100];
	char timeIn[30];
};

struct passportApplication *ptr;
int count = -1;
int setDay, setMonth, setYear;
void enterNewData();
void display();
void initailize();
void writeData();

int main() {
	int choice;

	ptr = (struct passportApplication *) malloc(count * sizeof(struct passportApplication));
	initailize();

	while(1) {
		printf("----------------------> Welcome International Airport <---------------------\n\n");
		printf("\t\t\t Press 1 to enter detail: ");
		scanf("%d", &choice);

		if(choice == 1) {
			enterNewData();
		} else if(choice == 5) {
			display();
		} else
			break;
	}

	writeData();
	free(ptr);

	printf("EXIT!!!!");
	printf("\n");
	return 0;
}

void initailize() {
	time_t t = time(NULL);
	struct tm now = *localtime(&t);

	setDay = now.tm_mday;
	setMonth = now.tm_mon+1;
	setYear = now.tm_year+1900;
}

void enterNewData() {
	time_t t = time(NULL);		//create time struct
	struct tm now = *localtime(&t);	//getTime value automatically to store in now variable

	if(setDay == now.tm_mday && setMonth == now.tm_mon+1 && setYear == now.tm_year+1900) {
		count += 1;
		ptr = realloc(ptr, (count+1) * sizeof(struct passportApplication));

		printf("\n");
		printf("Enter Name: ");
		scanf("%s", ptr[count].name);
		printf("Enter Address: ");
		scanf("%s", ptr[count].address);
		printf("Enter Aadhar Number: ");
		scanf("%d", &ptr[count].aadharNumber);
		printf("Enter Email: ");
		scanf("%s", ptr[count].email);

		char s[5];
		strcpy(ptr[count].timeIn, "");
		sprintf(s, "%d", now.tm_hour);
		strcat(ptr[count].timeIn, s);
		strcat(ptr[count].timeIn, ":");
		sprintf(s, "%d", now.tm_min);
		strcat(ptr[count].timeIn, s);
		strcat(ptr[count].timeIn, ":");
		sprintf(s, "%d", now.tm_sec);
		strcat(ptr[count].timeIn, s);

		//printf("%d ---> %s \t %d \t %s\n", count, ptr[count].name, ptr[count].aadharNumber, ptr[count].timeIn);
	} else {
		writeData();
		free(ptr);
		ptr = (struct passportApplication *) malloc(count * sizeof(struct passportApplication));
		initailize();
	}
}

void writeData() {
	int fd;
	char loc[100];
	char s[5];

	strcpy(loc, "file/");
	sprintf(s, "%d", setDay);
	strcat(loc, s);
	sprintf(s, "%d", setMonth);
	strcat(loc, s);
	sprintf(s, "%d", setYear);
	strcat(loc, s);
	strcat(loc, ".txt");

	fd = open(loc, O_WRONLY | O_APPEND);

	if(fd < 0) {
		printf("=====>CREAT\n");
		int f;
		f = creat(loc, O_RDWR | O_APPEND);

		//writeData();

		char s[10];

		for(int i=0; i<=count; i++) {
			sprintf(s, "%d", ptr[i].aadharNumber);

			write(f, ptr[i].name, strlen(ptr[i].name));
			write(f, "\n", 1);
			write(f, ptr[i].address, strlen(ptr[i].address));
			write(f, "\n", 1);
			write(f, s, strlen(s));
			write(f, "\n", 1);
			write(f, ptr[i].email, strlen(ptr[i].email));
			write(f, "\n", 1);
			write(f, ptr[i].timeIn, strlen(ptr[i].timeIn));
			write(f, "\n---------------\n", strlen("\n---------------\n"));
		}
	}
	else {
		printf("=====>OPEN\n");
		char s[10];

		for(int i=0; i<=count; i++) {
			sprintf(s, "%d", ptr[i].aadharNumber);

			write(fd, ptr[i].name, strlen(ptr[i].name));
			write(fd, "\n", 1);
			write(fd, ptr[i].address, strlen(ptr[i].address));
			write(fd, "\n", 1);
			write(fd, s, strlen(s));
			write(fd, "\n", 1);
			write(fd, ptr[i].email, strlen(ptr[i].email));
			write(fd, "\n", 1);
			write(fd, ptr[i].timeIn, strlen(ptr[i].timeIn));
			write(fd, "\n---------------\n", strlen("\n---------------\n"));
		}
	}
}

void display() {
	for(int i=0; i<=count; i++) {
		printf("\n\n-----------------------\n\n");
        printf("%d-->", i);
		printf("%s \t %d \t %s", ptr[i].name, ptr[i].aadharNumber, ptr[i].timeIn);
	}
}
