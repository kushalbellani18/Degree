%{
#include<stdio.h>
%}

%%
\#[a-z]*<[a-z]*\.h> {printf("%s is PREPROCESSOR DIRECTIVE! \n", yytext);}

"auto"|"break"|"case"|"char"|"const"|"continue"|"default"|"do"|"double"|"else"|"enum"|"extern"|"float"|"for"|"goto"|"if"|"int"|"long"|"register"|"return"|"short"|"signed"|"sizeof"|"static"|"struct"|"switch"|"typedef"|"union"|"unsigned"|"void"|"volatile"|"while" {printf("%s is KEYWORD!\n", yytext); }

[a-z]+\( {printf("%s is FUNCTION!\n", yytext); }

\".+\" {printf("%s is STRING!\n", yytext); }

[a-zA-Z0-9]+ {printf("%s is IDENTIFIER! \n", yytext); }

"+"|"-"|"*"|"="|"/" {printf("%s is ASSIGNMENT!\n", yytext); }

%%

int yywrap() {}

int main() {
	yyin = fopen("file/blah.c", "r");
	yylex();
	fclose(yyin);

	return 0;
}
