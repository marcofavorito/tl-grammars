grammar LDLfFormulaParser;

import PropFormulaParser;

/*@parser::members{
	
}*/

start
    :   expression EOF
    ;

expression
	:   doubleImplicationTemp
    ;

doubleImplicationTemp
    :   implicationTemp (DOUBLEIMPLY implicationTemp)*
    ;

implicationTemp
	:   orTemp (IMPLY orTemp)*
    ;

orTemp
    :   andTemp (OR andTemp)*
    ;

andTemp
    :   ldlfBox (AND ldlfBox)*
    ;

ldlfBox
	:   (BOXLPAREN regularExpression BOXRPAREN)? ldlfDiamond
    ;

ldlfDiamond
    :   (DIAMONDLPAREN regularExpression DIAMONDRPAREN)? notTemp
    ;  

notTemp
	:   ldlfAtom
    |   NOT? LPAREN expression RPAREN 
    ;

ldlfAtom
    :   TT
    |	FF
    ;

    regularExpression
    	:	alternation
    	;

    alternation
    	: 	concatenation (ALTERNATION concatenation)*
    	;

    concatenation
        :	star (CONCATENATION star)*
    	;

    star
    	: 	test STAR?
    	|	LPAREN regularExpression RPAREN STAR?
    	;

    test
    	: 	LPAREN expression RPAREN TEST
    	|	atom TEST
    	| 	propositionalFormula
    	;


    TT : ('tt');
    FF : ('ff');
    END : ('end');

    BOXLPAREN : ('[');
    BOXRPAREN : (']');
    DIAMONDLPAREN : ('<');
    DIAMONDRPAREN : ('>');

    STAR : ('*');
    TEST : ('?');
    ALTERNATION : ('+');
    CONCATENATION : (';');
