%{
#include<stdio.h>
#include<string.h>
char status[100] = "False";
char str[100] = "";
int count = 0;
%}

%%
(a|b)a((a|b)(a|b))* {strcpy(status, "True"); strcat(str, yytext);}
. {strcat(str, yytext);}
^[ab\n] {printf("Invalid");}
[\n] {printf("%s ==> %s\n", str, status); strcpy(str, ""); strcpy(status, "False");}
%%

int yywrap() {}

int main(int argc, char* argv[]) {
	yyin = fopen(argv[1], "r");

	yylex();

	return 0;
}
