%{
#include<stdio.h>
%}

%s A B C D E G F Z DEAD

%%
<INITIAL>0 BEGIN A;
<INITIAL>1 BEGIN D;
<INITIAL>[^01\n] BEGIN DEAD;
<INITIAL>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<A>0 BEGIN B;
<A>1 BEGIN G;
<A>[^01\n] BEGIN DEAD;
<A>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<B>0 BEGIN B;
<B>1 BEGIN C;
<B>[^01\n] BEGIN DEAD;
<B>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<C>0 BEGIN C;
<C>1 BEGIN Z;
<C>[^01\n] BEGIN DEAD;
<C>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<D>0 BEGIN G;
<D>1 BEGIN E;
<D>[^01\n] BEGIN DEAD;
<D>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<E>0 BEGIN F;
<E>1 BEGIN E;
<E>[^01\n] BEGIN DEAD;
<E>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<F>0 BEGIN Z;
<F>1 BEGIN F;
<F>[^01\n] BEGIN DEAD;
<F>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<G>0 BEGIN C;
<G>1 BEGIN F;
<G>[^01\n] BEGIN DEAD;
<G>\n BEGIN INITIAL; {printf("String is not accepted!\n");}

<Z>0 BEGIN Z;
<Z>1 BEGIN Z;
<Z>[^01\n] BEGIN DEAD;
<Z>\n BEGIN INITIAL; {printf("String is accepted!\n");}

<DEAD>[^\n] BEGIN DEAD;
<DEAD>\n BEGIN INITIAL; {printf("String is invalid!\n");}
%%

int yywrap() {}

int main() {
	yylex();
	return 0;
}
