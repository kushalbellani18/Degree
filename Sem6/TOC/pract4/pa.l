%{
#include<stdio.h>
#include<string.h>
int count = 0;
%}

%%
.*\n {
	count++;
	fprintf(yyout, "%d) %s", count, yytext);
}
%%

int yywrap() {}

int main(int argc, char* argv[]) {
	yyin = fopen(argv[1], "r");
	yyout = fopen(argv[2], "w");
	yylex();

	fclose(yyin);
	fclose(yyout);
	
}
