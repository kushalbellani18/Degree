%{
#include<stdio.h>
#include<string.h>

YYSTYPE yylval;
%}

%union {
	int v;
	char t;
}

%start hi

%token NUM

%left '+' '-'

%type<v> expr

%%

hi: expr{
	return 0;
};

expr: 
	NUM {
		printf("d-> Ans: %d\n", $$);
		printf("c-> Ans: %c\n", $$);
		printf("s-> Ans: %s\n", $$);
	}
	;

%%

void main() {
	yyparse();
}

void yyerror() {
	printf("Error...");
}
