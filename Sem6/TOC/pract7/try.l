%{
#include<stdio.h>
%}

%s A

%%
<INITIAL>1 BEGIN A;
<INITIAL>0 BEGIN INITIAL;
<INITIAL>\n BEGIN INITIAL; {printf("FAILED");}

<A>1 BEGIN A;
<A>0 BEGIN INITIAL;
<A>\n BEGIN INITIAL;  {printf("PASS");}

%%
int main() {
	yylex();

	return 0;
}

int yywrap() {
	return 1;
}
