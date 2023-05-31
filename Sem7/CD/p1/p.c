#include<stdio.h>
#include<string.h>

int checkInitialValid(char []);
int checkIdentifier(char[]);
int isSameAsKeyword(char []);

int main() {
	char lol[100];

	printf("Enter a string: ");
	fgets(lol, sizeof(lol), stdin);

	printf("\n");
//	printf("ANS: %d\n", isSameAsKeyword(lol));

	if(checkInitialValid(lol) == 1 && checkIdentifier(lol) && isSameAsKeyword(lol) != 1)
		printf("VALID IDENTIFIER!!!");
	else
		printf("INVALID IDENTIFIER!!!");

	return 0;
}

int checkInitialValid(char s[]) {
	char num[] = "0123456789";
	char special[] = "!@#$%^&*()-+=*/.,?:; ";

	//Check numerical
	for(int ni=0; ni<strlen(num); ni++) {
		if(s[0] == num[ni])
			return 0; //Return False
	}

	//Check special char
	for(int si=0; si<strlen(special); si++) {
		if(s[0] == special[si])
			return 0; //Return False
	}

	return 1; //Return True
}

int checkIdentifier(char s[]) {
	char special[] = "!@#$%^&*()-+=*/.,?:; ";

	for(int si=0; si<strlen(s); si++) {
		for(int spi=0; spi<strlen(special); spi++) {
			//Check special char
			if(s[si] == special[spi])
				return 0; //Return False
		}
	}

	return 1; // Return True
}

int isSameAsKeyword(char s[]) {
	char keyword[][100] = {
		"auto", "break", "case", "char",
		"const", "continue", "default", "do",
		"double", "else", "enum", "extern",
		"float", "for", "goto", "if",
		"int", "long", "register", "return",
		"short", "signed", "sizeof", "static",
		"struct", "switch", "typedef", "union",
		"unsigned", "void", "volatile", "while"
	};

	int maxSize = sizeof(keyword) / sizeof(keyword[0]);

	for(int ki=0; ki<maxSize; ki++) {
		if(strcmp(s, strcat(keyword[ki], "\n")) == 0)
			return 1; //Return True
	}

	return 0; //Return False
}
