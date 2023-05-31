%{
#include<stdio.h>
#include<string.h>
char msg[100];
int charCount = 0, wordCount = 0, lineCount = 0;
%}

%%
[ ] {wordCount++;}
. {charCount++;}
\n {lineCount++;}
%%

int yywrap() {}

int main(int argc, char *argv[]) {

 yyin = fopen(argv[1], "r");

 yylex();

 printf("Char: %d\n", charCount);
 printf("Word: %d\n", wordCount + lineCount);
 printf("Line: %d\n", lineCount);

 return 0;
}
