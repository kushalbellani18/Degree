%{
#include<stdio.h>
#include<string.h>
#include"y.tab.h"

#define YYSTYPE *char

extern YYSTYPE yylval;

%}

%%

[0-9]+|[0-9]*\.[0-9]+ {

	strcpy(yylval, yytext);
	
	return NUM;
}

[\t] ;
[\n] return 0;

. return yytext[0];

%%

int yywrap() { return 1; }
