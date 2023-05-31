#include<stdio.h>
#include<string.h>

char symName[180][180];
char symType[180][180];
int indexS = 0;

void getArray(char s[]);
void dis();

int main(int *argv, char *argc[]) {
	FILE *file;
	file = fopen(argc[1], "r");

	char str[200];
	char lol;

	strcpy(str, "");

	lol = getc(file);
	while(lol != EOF) {
		strcat(
			str, (char []){lol, '\0'}
		);

		lol = getc(file);
	}

	//printf("%s \n", str);

	getArray(str);
	dis();

	return 0;
}

void getArray(char s[]) {
	int lock=0;
	char token[3];

	for(int i=0; i<strlen(s); i++) {
		if(s[i] == '#') {
			strcpy(symName[indexS], (char[]) {s[i], '\0'});

			indexS += 1;
		} else if(s[i] == '<' || s[i] == '(' || s[i] == '{') {
			strcpy(symName[indexS], (char[]) {s[i], '\0'});

			indexS += 1;
		} else if(s[i] == '>' || s[i] == ')' || s[i] == '}') {
			strcpy(symName[indexS], (char[]) {s[i], '\0'});

			indexS += 1;
		} else if(s[i] == '%') {
			strcpy(symName[indexS], (char []) {s[i], s[i+1], '\0'});

			i += 1;
			indexS += 1;
		}
	}
}

void dis() {
	int length;

	length = sizeof(symName) / sizeof(symName[0]);

	printf("symName\n\n");
	for(int i=0; i<indexS; i++)
		printf("%s\n", symName[i]);
}

