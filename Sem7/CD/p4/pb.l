%{
#include<stdio.h>
#include<string.h>

int top = -1;
char arr[1][100];

void push(char s[]);
void pop(char s[]);
void dis();
%}

open "("|"{"|"["
close ")"|"}"|"]"

%%

{open} {push(yytext);}
{close} {pop(yytext);}
\n {dis();}

%%

void push(char s[]) {
	top += 1;

	strcpy(arr[top], s);
}

void pop(char s[]) {
	if(strcmp(")", s) == 0) {

		if(strcmp("(", arr[top]) == 0) {
			top -= 1;
		}

	} else if(strcmp("}", s) == 0) {

		if(strcmp("{", arr[top]) == 0) {
			top -= 1;
		}
		
	} else if(strcmp("]", s) == 0) {

		if(strcmp("[", arr[top]) == 0) {
			top -= 1;
		}
		
	}
}

void dis() {
	if(top == -1)
		printf("VALID\n\n");
	else
		printf("INVALID\n\n");

	top = -1;
}

int yywrap() {}

int main() {
	yylex();

	return 0;
}
