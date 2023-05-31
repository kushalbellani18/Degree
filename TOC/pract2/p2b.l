%{
#include<stdio.h>
int vowelCount=0, constantCount=0;
%}

%%
[aioue] {vowelCount++;}
. {constantCount++;}
\n {printf("Vowel: %d\n", vowelCount); printf("Constant: %d\n", constantCount); vowelCount=0; constantCount=0;}
%%

int yywrap() {}

int main() {
 yylex();
}
