%{
#include<stdio.h>
#include<string.h>
%}

%%
[0-9]+ {fprintf(yyout, "Int = %d", atoi(yytext)); }
[0-9]*.[0-9]* {fprintf(yyout, "Float = %f", atof(yytext)); }
%%

int yywrap() {}

int main(int argc, char* argv[]) {
	yyin = fopen(argv[1], "r");
	yyout = fopen(argv[2], "w");
	yylex();

	fclose(yyin);
	fclose(yyout);
	
}
