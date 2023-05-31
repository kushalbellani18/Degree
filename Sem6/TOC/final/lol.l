%{
#include<stdio.h>
int cityCount = 0, dateCount = 0;
%}

%%
"Ahmedabad"|"AHMEDABAD"|"ahmedabad" {cityCount += 1;}
"20" {dateCount += 1;}
. ;
\n {}
%%

int yywrap() {}

int main(int argc, char* argv[]) {
	yyin = fopen(argv[1], "r");
	yyout = fopen(argv[2], "w");

	yylex();

	printf("Final City count: %d", cityCount);
	printf("\nFinal Date count: %d", dateCount);

	fprintf(yyout, "Final City count: %d", cityCount);
	fprintf(yyout, "\nFinal Date count: %d", dateCount);

	fclose(yyin);
	fclose(yyout);

	return 0;
}
