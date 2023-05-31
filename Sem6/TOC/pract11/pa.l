%{
#include<stdio.h>
%}

%%
b*a(a|b)* {printf("Found!\n");}
.;
%%

int yywrap() {}

int main() {
	yylex();

	return 0;
}
