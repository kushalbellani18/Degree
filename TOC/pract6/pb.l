%{
#include<stdio.h>
%}

%%
a(a|b)*a {printf("1) Strings start and end with a");}
(a(a|b)*a) | (b(a|b)*b) {printf("2) Strings start and end with same symbol");}
(a(a|b)*b) | (b(a|b)*a) {printf("3) Strings start and end with different symbol");}
(a|b)(a|b)a(a|b)* {printf("4) The 3rd symbol from left end is a");}
(a|b)*b(a|b) {printf("5) The 2nd symbol from right end is b");}
a(a|b)((a|b)(a|b))* {printf("6) Strings start with a and length is even");}
a(ba|ab|a)* {printf("7) Strings start with a and does not contain 2 consecutive b");}
(ab|ba|aa|bb)+ {printf("8) L={a^m b^n | m+n = even}");}
(a|b)(ab|ba|aa|bb)* {printf("9) L={a^m b^n | m+n odd}");}
%%

int yywrap() {}

int main() {
	yylex();

	return 0;
}
