%{
#include<stdio.h>
#include<string.h>
char gStr[100];
%}

%%
[A-Z]* {strcat(gStr, yytext); printf("%s\t", yytext);}

[a-z]+ { char str[100], str2[100];
	 strcpy(str, yytext);
	 strcpy(str2, yytext);

	int i = -1;
	int min, max;

	min = (int)'a';
	max = (int)'z';
	
	for(int x=0; x<strlen(str); x++){
		i = (int) str[x];

		if(i >= min && i <= max) {
			str2[x] = (char) (i - 32);
		}
	}
	strcat(gStr, str2);

	}

\n {printf(">> %s\n", gStr); return 0;}
%%

int yywrap(void) {}

int main() {
	yylex();

	return 0;
}
