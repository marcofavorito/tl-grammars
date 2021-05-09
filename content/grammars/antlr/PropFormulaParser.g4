grammar PropFormulaParser;

@header{
	package generatedParsers;
}

propositionalFormula
	: 	doubleImplicationProp
	;

doubleImplicationProp
    :   implicationProp (DOUBLEIMPLY implicationProp)*
    ;

implicationProp
    :   xorProp (IMPLY xorProp)*
    ;

xorProp
    :   orProp (XOR orProp)*
    ;

orProp
    :   andProp (OR andProp)*
    ;

andProp
    :   notProp (AND notProp)*
    ;

notProp
    :   NOT? atom
    |   NOT? LPAREN propositionalFormula RPAREN
    ;

atom
	:   NAME*
	|	TRUE
	|	FALSE
    ;


    NAME : [a-zA-Z_][a-zA-Z0-9_]*;
    TRUE : ('true');
    FALSE : ('false');

    DOUBLEIMPLY : ('<->');
    IMPLY : ('->');
    XOR : ('^');
    OR  : ('||'|'|');
    AND : ('&&'|'&');
    NOT : ('!');

    LPAREN : ('(');
    RPAREN : (')');

    WS : (' ' | '\t' | '\r' | '\n')+ -> skip;

