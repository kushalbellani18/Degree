%{
#include<stdio.h>
%}

%s S1 S2 S3 GOAL ERROR

%%
<INITIAL>[a-zA-Z] BEGIN S1;
<INITIAL>[^a-zA-Z] BEGIN ERROR;

<S1>[a-zA-Z] BEGIN S1;
<S1>[0-9] BEGIN S1;
<S1>@ BEGIN S2;
<S1>[
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
