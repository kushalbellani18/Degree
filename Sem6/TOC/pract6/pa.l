%{
#include<stdio.h>
%}

%%
((1|0)(1|0))+ {printf("1) Even length of string(0 & 1)");}
(1|0)*00(1|0)* {printf("2) Strings containing the substring 00");}
1?01? {printf("3) Strings not containing at most five one's");}
(0)*1(0)*1(0)*1(0)*1 {printf("4) Strings not containig at most five one's");}
0?11? {printf("5) Strings having odd number of zeroes and even number of one's");}
(1|0)(1|0)(1|0)(1|0)(1|0)(1|0) {printf("6) All possible strings of length 6 (0 & 1)");}
(0|1)[(1|0)(1|0)]* {printf("7) Odd number of string (0 & 1)");} 
%%

int yywrap() {}

int main() {
	yylex();

	return 0;
}
