%{
#include<stdio.h>
%}

%s S1 S2 S3 GOAL ERROR DEAD

%%
<INITIAL>[a-zA-Z] BEGIN S1;
<INITIAL>[0-9] BEGIN ERROR;
<INITIAL>@ BEGIN ERROR;
<INITIAL>\. BEGIN ERROR;
<INITIAL>[^\n] BEGIN DEAD;

<S1>[a-zA-Z] BEGIN S1;
<S1>[0-9] BEGIN S1;
<S1>@ BEGIN S2;
<S1>\. BEGIN ERROR;
<S1>[^\n] BEGIN DEAD;
<S1>\n BEGIN INITIAL; {printf("Invalid!\n");}

<S2>"gmail" BEGIN S3;
<S2>"yahoo" BEGIN ERROR;
<S2>"hotmail" BEGIN ERROR;
<S2>[a-zA-Z] BEGIN DEAD;
<S2>[0-9] BEGIN DEAD;
<S2>\. BEGIN ERROR;
<S2>[^\n] BEGIN DEAD;
<S2>\n BEGIN INITIAL; {printf("Invalid!\n");}

<S3>".com" BEGIN GOAL;
<S3>[a-zA-Z] BEGIN ERROR;
<S3>[0-9] BEGIN ERROR;
<S3>\. BEGIN ERROR;
<S3>[^\n] BEGIN DEAD;
<S3>\n BEGIN INITIAL; {printf("Invalid!\n");}

<GOAL>\n BEGIN INITIAL; {printf("String accepted!\n");}
<GOAL>[a-zA-Z] BEGIN ERROR;
<GOAL>[0-9] BEGIN ERROR;
<GOAL>\. BEGIN ERROR;
<GOAL>[^\n] BEGIN DEAD;

<ERROR>".com" BEGIN ERROR;
<ERROR>".in" BEGIN ERROR;
<ERROR>\n BEGIN INITIAL; {printf("String not accepted!\n");}
<ERROR>[^\n] BEGIN DEAD;

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("Invalid!\n");}
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
