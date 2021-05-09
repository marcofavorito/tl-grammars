# Generated from PropFormulaParser.g4 by ANTLR 4.9
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("M\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\7\2\36\n\2\f\2\16\2!\13\2\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\3\b\3\b\5\b:\n\b\3\t\3\t\3\t\5\t?\n\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\3\f\3\r\6\rH\n\r\r\r\16\rI\3\r\3\r\2\2\16")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\3\2\5\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"")
        buf.write("\2P\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\3\33\3")
        buf.write("\2\2\2\5\"\3\2\2\2\7\'\3\2\2\2\t-\3\2\2\2\13\61\3\2\2")
        buf.write("\2\r\64\3\2\2\2\179\3\2\2\2\21>\3\2\2\2\23@\3\2\2\2\25")
        buf.write("B\3\2\2\2\27D\3\2\2\2\31G\3\2\2\2\33\37\t\2\2\2\34\36")
        buf.write("\t\3\2\2\35\34\3\2\2\2\36!\3\2\2\2\37\35\3\2\2\2\37 \3")
        buf.write("\2\2\2 \4\3\2\2\2!\37\3\2\2\2\"#\7v\2\2#$\7t\2\2$%\7w")
        buf.write("\2\2%&\7g\2\2&\6\3\2\2\2\'(\7h\2\2()\7c\2\2)*\7n\2\2*")
        buf.write("+\7u\2\2+,\7g\2\2,\b\3\2\2\2-.\7>\2\2./\7/\2\2/\60\7@")
        buf.write("\2\2\60\n\3\2\2\2\61\62\7/\2\2\62\63\7@\2\2\63\f\3\2\2")
        buf.write("\2\64\65\7`\2\2\65\16\3\2\2\2\66\67\7~\2\2\67:\7~\2\2")
        buf.write("8:\7~\2\29\66\3\2\2\298\3\2\2\2:\20\3\2\2\2;<\7(\2\2<")
        buf.write("?\7(\2\2=?\7(\2\2>;\3\2\2\2>=\3\2\2\2?\22\3\2\2\2@A\7")
        buf.write("#\2\2A\24\3\2\2\2BC\7*\2\2C\26\3\2\2\2DE\7+\2\2E\30\3")
        buf.write("\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2")
        buf.write("\2JK\3\2\2\2KL\b\r\2\2L\32\3\2\2\2\7\2\379>I\3\b\2\2")
        return buf.getvalue()


class PropFormulaParserLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NAME = 1
    TRUE = 2
    FALSE = 3
    DOUBLEIMPLY = 4
    IMPLY = 5
    XOR = 6
    OR = 7
    AND = 8
    NOT = 9
    LPAREN = 10
    RPAREN = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NAME", "TRUE", "FALSE", "DOUBLEIMPLY", "IMPLY", "XOR", "OR", 
            "AND", "NOT", "LPAREN", "RPAREN", "WS" ]

    ruleNames = [ "NAME", "TRUE", "FALSE", "DOUBLEIMPLY", "IMPLY", "XOR", 
                  "OR", "AND", "NOT", "LPAREN", "RPAREN", "WS" ]

    grammarFileName = "PropFormulaParser.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


