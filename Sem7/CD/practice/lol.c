#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char symName[100][100];
char symType[100][100];
int indexS = 0;

void storeArray(char str[]);
int isAlpha(char c);
void dis();
void isSameAsKeyword();

int main(int *argv, char *argc[]) {
	FILE *file;
	char str[100];
	char s;

	if( (file=fopen(argc[1], "r")) == NULL ) {
		printf("QUITING\n");
		exit(0);
	}

	strcpy(str, "");
	s = getc(file);

	while(s != EOF) {
		strcat(str, (char[2]) {s, '\0'});
		s = getc(file);
	}

	storeArray(str);
	dis();

	return 0;
}

void storeArray(char str[]) {
	int lock=0;
	char lol[100];

	for(int i=0; i<strlen(str); i++) {
		if(lock == 0) {
			if(str[i] == '#') {
				strcpy(symName[indexS], (char[2]) {str[i], '\0'});
				strcpy(symType[indexS], "Pre-processor");

				indexS += 1;
			}
			else if(str[i] == '(' || str[i] == '{' | str[i] == '[' | str[i] == '<') {
				strcpy(symName[indexS], (char[2]) {str[i], '\0'});
				strcpy(symType[indexS], "Open Bracket");

				indexS += 1;
			}
			else if(str[i] == ')' || str[i] == '}' | str[i] == ']' | str[i] == '>') {
				strcpy(symName[indexS], (char[2]) {str[i], '\0'});
				strcpy(symType[indexS], "Close Bracket");

				indexS += 1;
			}
			else if(str[i] == '%') {
				strcpy(symName[indexS], (char[2]) {str[i], '\0'});
				strcat(symName[indexS], (char[2]) {str[i+1], '\0'});
				strcpy(symType[indexS], "Tokens");

				indexS += 1;
				i += 1;
			}
			else if(isAlpha(str[i]) == 1 || str[i] == '.') {
				strcpy(lol, "");
				strcat(lol, (char[2]) {str[i], '\0'});

				lock = 1;
			}
			else if(str[i] == ',' || str[i] == ';') {
				strcpy(symName[indexS], (char[2]) {str[i], '\0'});
				strcpy(symType[indexS], "Puncutations");

				indexS += 1;
			}
		} else {
			if(isAlpha(str[i]) == 1 || str[i] == '.')
				strcat(lol, (char[2]) {str[i], '\0'});
			else {
				strcpy(symName[indexS], lol);
				strcpy(symType[indexS], "Identifier");

				indexS += 1;
				i -= 1;
				lock = 0;
			}
		}
	}
}

int isAlpha(char c) {
	if( (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') )
		return 1;

	return 0;
}

void isSameAsKeyword() {
	/*
		a-1, b-1, c-4, d-3, e-3,
		f-2, g-1, i-2, l-1, r-2,
		s-6, t-1, u-2, v-2, w-1
	*/
	char keyword[][100] = {
		"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern",
		"float", "for", "goto", "int", "if", "long", "register", "return",
		"sizeof", "signed", "struct", "static", "switch", "short", "typedef", "unsigned", "union", "void", "volatile", "while"
	};

}

void dis() {
	printf("\n");
	printf("SymName\tSymType\tAddress\n\n");
	for(int i=0; i<indexS; i++) {
		printf("%s\t%s\t%d\n", symName[i], symType[i], &symName[i]);
	}

	printf("\n");
}
