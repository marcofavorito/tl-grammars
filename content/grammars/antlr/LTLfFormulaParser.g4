grammar LTLfFormulaParser;

import PropFormulaParser;

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
    :   xorTemp (IMPLY xorTemp)*
    ;

xorTemp
    :   orTemp (XOR orTemp)*
    ;


orTemp
    :   andTemp (OR andTemp)*
    ;

andTemp
    :   release (AND release)*
    ;


release
    :   weakUntil (WEAKUNTIL weakUntil)*
    ;


weakUntil
    :   strongRelease (RELEASE strongRelease)*
    ;


strongRelease
    :   until (STRONGRELEASE until)*
    ;


until
    :   globally(UNTIL globally)*
    ;

globally
    :   GLOBALLY? eventually
    ;

eventually
    :   EVENTUALLY? weakNext		
    ;

weakNext
    :   WEAKNEXT? next_
    ;

next_
    :   NEXT? notTemp
    ;  

notTemp
    :   ltlfAtom
    |   NOT? LPAREN expression RPAREN
    ;

ltlfAtom
    :   NAME
    |   propositionalFormula
    ;

    WEAKUNTIL : ('W');
    UNTIL : ('U');
    RELEASE : ('R'|'V');
    STRONGRELEASE : ('M');
    GLOBALLY : ('G');
    EVENTUALLY : ('F');
    WEAKNEXT : ('X');
    NEXT : ('X[!]');

