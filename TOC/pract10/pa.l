%{
#include<stdio.h>
%}

%s GOAL ERROR DEAD

%%
<INITIAL>[a-zA-Z] BEGIN GOAL;
<INITIAL>[0-9] BEGIN ERROR;
<INITIAL>[^\n] BEGIN DEAD;
<INITIAL>\n BEGIN INITIAL; {printf("Enter a string!\n");}

<GOAL>[a-zA-Z] BEGIN GOAL;
<GOAL>[0-9] BEGIN GOAL;
<GOAL>[^\n] BEGIN DEAD;
<GOAL>\n BEGIN INITIAL; {printf("String accepted!\n");}

<ERROR>[a-zA-Z] BEGIN ERROR;
<ERROR>[0-9] BEGIN ERROR;
<ERROR>[^\n] BEGIN DEAD;
<ERROR>\n BEGIN INITIAL; {printf("String not accepted!\n");}

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("Invalid String!\n");}
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
