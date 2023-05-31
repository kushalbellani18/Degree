%{
#include<stdio.h>
%}

%%
"<!"-[-]+.*[-]+-">" {printf("%s", yytext);}
. ;
%%

int yywrap() {}

int main() {
	yyin = fopen("file/basic.html", "r");
	yylex();
	fclose(yyin);

	return 0;
}
