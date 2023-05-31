%{
#include<stdio.h>
%}

%s A B DEAD

%%
<INITIAL>0 BEGIN A;
<INITIAL>1 BEGIN B;
<INITIAL>[^\n01] BEGIN DEAD;
<INITIAL>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<A>0 BEGIN B;
<A>1 BEGIN B;
<A>[^\n01] BEGIN DEAD;
<A>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<B>0 BEGIN A;
<B>1 BEGIN A;
<B>[^\n01] BEGIN DEAD;
<B>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("String is invalid!\n");}
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
