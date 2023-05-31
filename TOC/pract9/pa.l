%{
#include<stdio.h>
%}

%s GOAL1 GOAL2 ERROR DEAD

%%
<INITIAL>"GNU" BEGIN GOAL1;
<INITIAL>"BDA"|"CBA"|"CS" BEGIN ERROR;
<INITIAL>[^\n] BEGIN DEAD;
<INITIAL>\n BEGIN INITIAL; {printf("Enter a string!\n");} 

<GOAL1>"GNU" BEGIN ERROR;
<GOAL1>"BDA"|"CBA"|"CS" BEGIN GOAL2;
<GOAL1>[^\n] BEGIN DEAD;
<GOAL1>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<GOAL2>"GNU" BEGIN GOAL1;
<GOAL2>"BDA"|"CBA"|"CS" BEGIN GOAL2;
<GOAL2>[^\n] BEGIN DEAD;
<GOAL2>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<ERROR>"GNU"|"BDA"|"CBA"|"CS" BEGIN ERROR;
<ERROR>[^\n] BEGIN DEAD;
<ERROR>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("Invalid!\n");}
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
