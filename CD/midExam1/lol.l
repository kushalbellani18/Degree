%{
#include<stdio.h>

int validTokens = 0;
%}

%%

\#[a-z]*<[a-z]*\.h> {/*printf("%s -> PREPROCESSOR DEFINED\n", yytext);*/ validTokens += 1;}
[a-z]*\( {/*printf("%s -> FUNCTION\n", yytext);*/ validTokens += 1;}
"int main"\(\) {/*printf("%s -> MAIN FUNCTION\n", yytext);*/ validTokens += 2;}
"="|"+"|"*"|"-"|"/" {/*printf("%s -> ASSIGNMENT\n", yytext);*/ validTokens += 1;}
"int"|"return"|"float" {/*printf("%s -> KEYWORD\n", yytext);*/ validTokens += 1;}
[a-z]+ {/*printf("%s -> IDENTIFIER\n", yytext);*/ validTokens += 1;}
[!@#$%^&*=+<>/?] {/*printf("ERRoR");*/ validTokens -= 1;}
"include"|"#include" {/*printf("noWay");*/ validTokens -= 1;}
[)\{,,,;\}0-9] {}

%%

int yywrap() {}
int main(int *argv, char *argc[]) {
	yyin = fopen(argc[1], "r");
	yylex();

	printf("Answer: %d\n\n", validTokens);

	fclose(yyin);

	return 0;
}
