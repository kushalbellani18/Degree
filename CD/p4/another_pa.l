%{
#include<stdio.h>
#include<string.h>

float p, flag, answer;
char cc;
%}

digit [0-9]+|[0-9]*"."[0-9]+
op "+"|"-"|"*"|"/"

%%

{digit} {
	p=atof(yytext);

	if(flag == 0) {
		answer = p;
		flag = 1;
	} else {
		switch(cc) {
			case '+': answer += p; break;
			case '-': answer -= p; break;
			case '*': answer *= p; break;
			case '/': answer /= p; break;
		}
	}
}

{op} {
	if(strcmp(yytext, "+") == 0)
		cc = '+';
	
	if(strcmp(yytext, "-") == 0)
		cc = '-';
	
	if(strcmp(yytext, "*") == 0)
		cc = '*';
	
	if(strcmp(yytext, "/") == 0)
		cc = '/';
}

\n {printf("Final Answer: %f\n\n", answer); flag=answer=0;}

%%

int yywrap() {}

int main() {
	yylex();

	return 0;
}
