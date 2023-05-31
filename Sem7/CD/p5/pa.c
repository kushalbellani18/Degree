#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char symbolName[100][100];
char symbolType[100][100];
int indexS = 0;

void getArray(char []);
void dis();
int isAlpha(char);
void updateKeyword(int);

int main(int *argv, char *argc[]) {
	FILE *file;
	char lol;
	char str[200];

	file = fopen(argc[1], "r");

	if( file == NULL) {
		printf(">> FILE is not found... \n");

		exit(0);
	}

	strcpy(str, "");

	lol = getc(file);
	while(lol != EOF) {
		strcat(str, (char[2]) {lol, '\0'});
		lol = getc(file);
	}

	fclose(file);
	printf(">>> %s\n", str);

	getArray(str);
	dis();

	return 0;
}

void getArray(char str[]) {
	int isString(char);
	char s[100];
	int lock = 0;

	for(int i=0; i<strlen(str); i++) {
		if(lock == 0) {
			if(str[i] == '#') {
				strcpy(symbolName[indexS], (char []){str[i], '\0'});
				strcpy(symbolType[indexS], "Pre-processor");

				indexS += 1;
			} else if(str[i] == '<' || str[i] == '(' || str[i] == '{' || str[i] == '[') {
				strcpy(symbolName[indexS], (char []){str[i], '\0'});
				strcpy(symbolType[indexS], "Open Bracket");

				indexS += 1;
			} else if(str[i] == '>' || str[i] == ')' || str[i] == '}' || str[i] == ']') {
				strcpy(symbolName[indexS], (char []){str[i], '\0'});
				strcpy(symbolType[indexS], "Close Bracket");

				indexS += 1;
			} else if(str[i] == ',' | str[i] == ';') {
				strcpy(symbolName[indexS], (char []){str[i], '\0'});
				strcpy(symbolType[indexS], "Punctuation");

				indexS += 1;
			} else if(str[i] == '\"') {
				strcpy(symbolName[indexS], (char []){str[i], '\0'});
				strcpy(symbolType[indexS], "Quote");

				indexS += 1;
			} else if(isAlpha(str[i]) == 1 || str[i] == '.') {
				strcpy(s, "");
				strcat(s, (char []){str[i], '\0'});

				lock = 1;
			} else if(str[i] == '%') {
				strcpy(symbolName[indexS], strcat((char[]) {str[i], '\0'}, (char[]) {str[i+1], '\0'}));
				strcpy(symbolType[indexS], "Token");

				indexS += 1;
				i += 1;
			}
		} else {
			if(isAlpha(str[i]) == 1 || str[i] == '.')
				strcat(s, (char []){str[i], '\0'});
			else {
				lock = 0;

				strcpy(symbolName[indexS], s);
				strcpy(symbolType[indexS], "Identifier");

				indexS += 1;
				i -= 1;
			}
		}
	}
}

void dis() {
	printf("Size: %d\n", indexS);
	printf("Index\tName\tType\tAddress\n\n");
	for(int i=0; i<indexS; i++) {
		updateKeyword(i);

		printf("%d\t%s\t%s\t%d\n", i, symbolName[i], symbolType[i], &symbolName[i]);
	}
}

int isAlpha(char ch) {
	if( (ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z') )
		return 1;

	return 0;
}

void updateKeyword(int index) {
	char keyword[][100] = {
		"auto", "break", "case", "char",
		"const", "continue", "default", "do",
		"double", "else", "enum", "extern",
		"float", "for", "goto", "if",
		"int", "long", "register", "return",
		"short", "signed", "sizeof", "static",
		"struct", "switch", "typedef", "union",
		"unsigned", "void", "volatile", "while",
		"include"
	};

	for(int i=0; i<34; i++) {
		if(strcmp(keyword[i], symbolName[index]) == 0 || (symbolName[index][strlen(symbolName[index]) - 2] == '.' && symbolName[index][strlen(symbolName[index]) - 1] == 'h')) {
			strcpy(symbolType[index], "Keywords");
			break;
		}
	}
}
