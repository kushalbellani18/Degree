%{
#include<stdio.h>
#include<string.h>
char status[100] = "False";
char str[100] = "";
%}

%%
(a(a|b)*b)|(b(a|b)*a) {strcpy(status, "True"); strcat(str, yytext);}
. {strcpy(status,"False"); strcat(str, yytext);}
\n {printf("%s ==> %s\n", str, status); strcpy(str, ""); strcpy(status, "False");}
%%

int yywrap() {}

int main(int argc, char* argv[]) {
	yyin = fopen(argv[1], "r");

	yylex();
}
