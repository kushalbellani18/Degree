%{
#include<stdio.h>
%}

%%
[a-z]*[A-Z]+[a-z]* {printf("Found!\n");}
%%

int yywrap(void) {}

int main() {
 yylex();

 return 0;
}
