%{
#include<stdio.h>
#include<string.h>
char status[100] = "False";
char str[100] = "";
%}

%%
(1|0)(1|0) {printf("True");}
\n {printf("False");}
%%

int yywrap() {}

int main() {
	//yyin = fopen(argv[1], "r");

	yylex();

	return 0;
}
