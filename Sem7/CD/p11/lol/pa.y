%{
#include<stdio.h>
%}

%token NUM

%left '+' '-'
%left '*' '/'

%%

A: E{
	printf("Ans: %d\n", $$);
	return 0;
};

E:E'+'E{$$=$1+$3;}|
E'-'E{$$=$1-$3;}|
E'*'E{$$=$1*$3;}|
E'/'E{$$=$1/$3;}|
NUM{$$=$1;};

%%

void main() {
	yyparse();
}

void yyerror() {
	printf("BYE\n");
}
