%{
#include<stdio.h>
%}

%%
is |
am |
were |
was |
be |
being |
been |
do |
does |
did |
will |
would |
should |
can |
could |
has |
have |
had |
go {printf("%s is a verb\n", yytext);}

[a-zA-Z]+ {printf("%s might Noun\n", yytext);}
%%

int main() {
 yylex();
}
