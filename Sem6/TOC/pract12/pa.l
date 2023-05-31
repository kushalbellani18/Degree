%{
#include<stdio.h>
%}

%s B C DEAD

%%
<INITIAL>0 BEGIN INITIAL;
<INITIAL>1 BEGIN B;
<INITIAL>[^01\n] BEGIN DEAD;
<INITIAL>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<B>0 BEGIN C;
<B>1 BEGIN B;
<B>[^01\n] BEGIN DEAD;
<B>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<C>0 BEGIN C;
<C>1 BEGIN B;
<C>[^01\n] BEGIN DEAD;
<C>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("String is invalid!\n");}
%%

int yywrap() {}

int main() {
	yylex();

	return 0;
}
