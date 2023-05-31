#include<stdio.h>
#include<string.h> // For string
#include<stdlib.h> // For file

int getNumOfCharacters(char s[]);
int getNumOfWords(char s[]);
int getNumOfDigits(char s[]);
int getNumOfVowels(char s[]);
int getNumOfConstant(char s[]);
int getNumOfSpeChars(char s[]);
int getNumOfLines(char s[]);

int main(int *argv, char *argc[]) {
	char str[200];

	if(strcmp(argc[1], "-s") == 0) { // For Read String
		strcpy(str, argc[2]);

		printf(">> %s\n", str);

	} else if (strcmp(argc[1], "-f") == 0) { // For Read file

		FILE *file;
		char lol;

		if( (file = fopen(argc[2], "r") ) == NULL)
			printf(">> FILE is not found...\n");

		strcpy(str, "");

		lol = getc(file);
		while(lol != EOF) {
			strcat(str, (char[2]) {lol, '\0'});
			lol = getc(file);
		}

		printf(">> %s\n", str);
		fclose(file);

	} else { // Invalid tag

		printf("Please enter either \'-s\' for String input or \'-f\' for file input!");
		return 0;
	}

	printf("Number of Characters: %d\n", getNumOfCharacters(str));
	printf("Number of Words: %d\n", getNumOfWords(str));
	printf("Number of Digits: %d\n", getNumOfDigits(str));
	printf("Number of Vowels: %d\n", getNumOfVowels(str));
	printf("Number of Constants: %d\n", getNumOfConstant(str));
	printf("Number of Special Characters: %d\n", getNumOfSpeChars(str));
	printf("Number of Lines: %d\n", getNumOfLines(str));

	return 0;
}

int getNumOfCharacters(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++) {
		if( (s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z') )
			counter += 1;
	}

	return counter;
}

int getNumOfWords(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++)
		if(s[i] == ' ' || s[i] == '\n')
			counter += 1;

	counter += 1;
	return counter;
}

int getNumOfDigits(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++)
		if(s[i] >= '0' && s[i] <= '9')
			counter += 1;

	return counter;
}

int getNumOfVowels(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++)
		if(s[i] == 'a' || s[i] == 'e' || s[i] == 'u' || s[i] == 'i' || s[i] == 'o')
			counter += 1;

	return counter;
}

int getNumOfConstant(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++)
		if( !(s[i] == 'a' || s[i] == 'e' || s[i] == 'u' || s[i] == 'i' || s[i] == 'o')  && !(s[i] >= '0' && s[i] <= '9') && s[i] != ' ')
			counter += 1;

	return counter;
}

int getNumOfSpeChars(char s[]) {
	int counter = 0;
	char sp[] = "!@#$%^&*()_-+=*-/?;:.>,<|[]{}\\`~\'\"";

	for(int i=0; i<strlen(s); i++) {
		for(int j=0; j<strlen(sp); j++) {
			if(s[i] == sp[j]) {
				counter += 1;

				break;
			}
		}
	}

	return counter;
}

int getNumOfLines(char s[]) {
	int counter = 0;

	for(int i=0; i<strlen(s); i++)
		if(s[i] == '\n')
			counter += 1;

	counter += 1;
	return counter;
}
