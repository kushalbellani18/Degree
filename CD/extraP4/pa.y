%{
#include<stdio.h>
int flag=0;
%}

%token NUM

%left '+' '-'
%left '*' '/'

%%

ArithmeticExpression: E{
	printf("Result: %d\n\n", $$);
	return 0;
};

E: E'+'E {$$=$1+$3;}
| E'-'E {$$=$1-$3;}
| E'*'E {$$=$1*$3;}
| E'/'E {$$=$1/$3;}
| NUM {$$=$1;}
;

%%

int main() {
	yyparse();
}

void yyerror() {
	printf("INVALID!");
}
