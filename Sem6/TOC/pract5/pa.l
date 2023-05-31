%{
#include<stdio.h>
%}

%%
[<][/]*[a-zA-Z]+[0-9]*[>] {printf("%s", yytext);}
. ;
%%

int yywrap() {}

int main() {
	yyin = fopen("file/basic.html", "r");
	yylex();
	fclose(yyin);

	return 0;
}
