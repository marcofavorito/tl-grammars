# Generated from LDLfFormulaParser.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31")
        buf.write("\u00dc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\7\49\n\4\f\4\16\4<\13\4\3")
        buf.write("\5\3\5\3\5\7\5A\n\5\f\5\16\5D\13\5\3\6\3\6\3\6\7\6I\n")
        buf.write("\6\f\6\16\6L\13\6\3\7\3\7\3\7\7\7Q\n\7\f\7\16\7T\13\7")
        buf.write("\3\b\3\b\3\b\3\b\5\bZ\n\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t")
        buf.write("b\n\t\3\t\3\t\3\n\3\n\5\nh\n\n\3\n\3\n\3\n\3\n\5\nn\n")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\r\7\rw\n\r\f\r\16\rz\13")
        buf.write("\r\3\16\3\16\3\16\7\16\177\n\16\f\16\16\16\u0082\13\16")
        buf.write("\3\17\3\17\5\17\u0086\n\17\3\17\3\17\3\17\3\17\5\17\u008c")
        buf.write("\n\17\5\17\u008e\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u0099\n\20\3\21\3\21\3\22\3\22\3\22")
        buf.write("\7\22\u00a0\n\22\f\22\16\22\u00a3\13\22\3\23\3\23\3\23")
        buf.write("\7\23\u00a8\n\23\f\23\16\23\u00ab\13\23\3\24\3\24\3\24")
        buf.write("\7\24\u00b0\n\24\f\24\16\24\u00b3\13\24\3\25\3\25\3\25")
        buf.write("\7\25\u00b8\n\25\f\25\16\25\u00bb\13\25\3\26\3\26\3\26")
        buf.write("\7\26\u00c0\n\26\f\26\16\26\u00c3\13\26\3\27\5\27\u00c6")
        buf.write("\n\27\3\27\3\27\5\27\u00ca\n\27\3\27\3\27\3\27\3\27\5")
        buf.write("\27\u00d0\n\27\3\30\7\30\u00d3\n\30\f\30\16\30\u00d6\13")
        buf.write("\30\3\30\3\30\5\30\u00da\n\30\3\30\2\2\31\2\4\6\b\n\f")
        buf.write("\16\20\22\24\26\30\32\34\36 \"$&(*,.\2\3\3\2\3\4\2\u00de")
        buf.write("\2\60\3\2\2\2\4\63\3\2\2\2\6\65\3\2\2\2\b=\3\2\2\2\nE")
        buf.write("\3\2\2\2\fM\3\2\2\2\16Y\3\2\2\2\20a\3\2\2\2\22m\3\2\2")
        buf.write("\2\24o\3\2\2\2\26q\3\2\2\2\30s\3\2\2\2\32{\3\2\2\2\34")
        buf.write("\u008d\3\2\2\2\36\u0098\3\2\2\2 \u009a\3\2\2\2\"\u009c")
        buf.write("\3\2\2\2$\u00a4\3\2\2\2&\u00ac\3\2\2\2(\u00b4\3\2\2\2")
        buf.write("*\u00bc\3\2\2\2,\u00cf\3\2\2\2.\u00d9\3\2\2\2\60\61\5")
        buf.write("\4\3\2\61\62\7\2\2\3\62\3\3\2\2\2\63\64\5\6\4\2\64\5\3")
        buf.write("\2\2\2\65:\5\b\5\2\66\67\7\21\2\2\679\5\b\5\28\66\3\2")
        buf.write("\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;\7\3\2\2\2<:\3\2\2")
        buf.write("\2=B\5\n\6\2>?\7\22\2\2?A\5\n\6\2@>\3\2\2\2AD\3\2\2\2")
        buf.write("B@\3\2\2\2BC\3\2\2\2C\t\3\2\2\2DB\3\2\2\2EJ\5\f\7\2FG")
        buf.write("\7\24\2\2GI\5\f\7\2HF\3\2\2\2IL\3\2\2\2JH\3\2\2\2JK\3")
        buf.write("\2\2\2K\13\3\2\2\2LJ\3\2\2\2MR\5\16\b\2NO\7\25\2\2OQ\5")
        buf.write("\16\b\2PN\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2S\r\3\2")
        buf.write("\2\2TR\3\2\2\2UV\7\6\2\2VW\5\26\f\2WX\7\7\2\2XZ\3\2\2")
        buf.write("\2YU\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\5\20\t\2\\\17\3\2")
        buf.write("\2\2]^\7\b\2\2^_\5\26\f\2_`\7\t\2\2`b\3\2\2\2a]\3\2\2")
        buf.write("\2ab\3\2\2\2bc\3\2\2\2cd\5\22\n\2d\21\3\2\2\2en\5\24\13")
        buf.write("\2fh\7\26\2\2gf\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\27\2\2")
        buf.write("jk\5\4\3\2kl\7\30\2\2ln\3\2\2\2me\3\2\2\2mg\3\2\2\2n\23")
        buf.write("\3\2\2\2op\t\2\2\2p\25\3\2\2\2qr\5\30\r\2r\27\3\2\2\2")
        buf.write("sx\5\32\16\2tu\7\f\2\2uw\5\32\16\2vt\3\2\2\2wz\3\2\2\2")
        buf.write("xv\3\2\2\2xy\3\2\2\2y\31\3\2\2\2zx\3\2\2\2{\u0080\5\34")
        buf.write("\17\2|}\7\r\2\2}\177\5\34\17\2~|\3\2\2\2\177\u0082\3\2")
        buf.write("\2\2\u0080~\3\2\2\2\u0080\u0081\3\2\2\2\u0081\33\3\2\2")
        buf.write("\2\u0082\u0080\3\2\2\2\u0083\u0085\5\36\20\2\u0084\u0086")
        buf.write("\7\n\2\2\u0085\u0084\3\2\2\2\u0085\u0086\3\2\2\2\u0086")
        buf.write("\u008e\3\2\2\2\u0087\u0088\7\27\2\2\u0088\u0089\5\26\f")
        buf.write("\2\u0089\u008b\7\30\2\2\u008a\u008c\7\n\2\2\u008b\u008a")
        buf.write("\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u008e\3\2\2\2\u008d")
        buf.write("\u0083\3\2\2\2\u008d\u0087\3\2\2\2\u008e\35\3\2\2\2\u008f")
        buf.write("\u0090\7\27\2\2\u0090\u0091\5\4\3\2\u0091\u0092\7\30\2")
        buf.write("\2\u0092\u0093\7\13\2\2\u0093\u0099\3\2\2\2\u0094\u0095")
        buf.write("\5.\30\2\u0095\u0096\7\13\2\2\u0096\u0099\3\2\2\2\u0097")
        buf.write("\u0099\5 \21\2\u0098\u008f\3\2\2\2\u0098\u0094\3\2\2\2")
        buf.write("\u0098\u0097\3\2\2\2\u0099\37\3\2\2\2\u009a\u009b\5\"")
        buf.write("\22\2\u009b!\3\2\2\2\u009c\u00a1\5$\23\2\u009d\u009e\7")
        buf.write("\21\2\2\u009e\u00a0\5$\23\2\u009f\u009d\3\2\2\2\u00a0")
        buf.write("\u00a3\3\2\2\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2")
        buf.write("\u00a2#\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a4\u00a9\5&\24")
        buf.write("\2\u00a5\u00a6\7\22\2\2\u00a6\u00a8\5&\24\2\u00a7\u00a5")
        buf.write("\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9")
        buf.write("\u00aa\3\2\2\2\u00aa%\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ac")
        buf.write("\u00b1\5(\25\2\u00ad\u00ae\7\23\2\2\u00ae\u00b0\5(\25")
        buf.write("\2\u00af\u00ad\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1\u00af")
        buf.write("\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\'\3\2\2\2\u00b3\u00b1")
        buf.write("\3\2\2\2\u00b4\u00b9\5*\26\2\u00b5\u00b6\7\24\2\2\u00b6")
        buf.write("\u00b8\5*\26\2\u00b7\u00b5\3\2\2\2\u00b8\u00bb\3\2\2\2")
        buf.write("\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba)\3\2\2")
        buf.write("\2\u00bb\u00b9\3\2\2\2\u00bc\u00c1\5,\27\2\u00bd\u00be")
        buf.write("\7\25\2\2\u00be\u00c0\5,\27\2\u00bf\u00bd\3\2\2\2\u00c0")
        buf.write("\u00c3\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c2+\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4\u00c6\7\26\2")
        buf.write("\2\u00c5\u00c4\3\2\2\2\u00c5\u00c6\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00d0\5.\30\2\u00c8\u00ca\7\26\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cb\3\2\2\2")
        buf.write("\u00cb\u00cc\7\27\2\2\u00cc\u00cd\5 \21\2\u00cd\u00ce")
        buf.write("\7\30\2\2\u00ce\u00d0\3\2\2\2\u00cf\u00c5\3\2\2\2\u00cf")
        buf.write("\u00c9\3\2\2\2\u00d0-\3\2\2\2\u00d1\u00d3\7\16\2\2\u00d2")
        buf.write("\u00d1\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5\u00da\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d7\u00da\7\17\2\2\u00d8\u00da\7\20\2\2\u00d9")
        buf.write("\u00d4\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3\2\2\2")
        buf.write("\u00da/\3\2\2\2\32:BJRYagmx\u0080\u0085\u008b\u008d\u0098")
        buf.write("\u00a1\u00a9\u00b1\u00b9\u00c1\u00c5\u00c9\u00cf\u00d4")
        buf.write("\u00d9")
        return buf.getvalue()


class LDLfFormulaParserParser ( Parser ):

    grammarFileName = "LDLfFormulaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "TT", "FF", "END", "BOXLPAREN", "BOXRPAREN", 
                      "DIAMONDLPAREN", "DIAMONDRPAREN", "STAR", "TEST", 
                      "ALTERNATION", "CONCATENATION", "NAME", "TRUE", "FALSE", 
                      "DOUBLEIMPLY", "IMPLY", "XOR", "OR", "AND", "NOT", 
                      "LPAREN", "RPAREN", "WS" ]

    RULE_start = 0
    RULE_expression = 1
    RULE_doubleImplicationTemp = 2
    RULE_implicationTemp = 3
    RULE_orTemp = 4
    RULE_andTemp = 5
    RULE_ldlfBox = 6
    RULE_ldlfDiamond = 7
    RULE_notTemp = 8
    RULE_ldlfAtom = 9
    RULE_regularExpression = 10
    RULE_alternation = 11
    RULE_concatenation = 12
    RULE_star = 13
    RULE_test = 14
    RULE_propositionalFormula = 15
    RULE_doubleImplicationProp = 16
    RULE_implicationProp = 17
    RULE_xorProp = 18
    RULE_orProp = 19
    RULE_andProp = 20
    RULE_notProp = 21
    RULE_atom = 22

    ruleNames =  [ "start", "expression", "doubleImplicationTemp", "implicationTemp", 
                   "orTemp", "andTemp", "ldlfBox", "ldlfDiamond", "notTemp", 
                   "ldlfAtom", "regularExpression", "alternation", "concatenation", 
                   "star", "test", "propositionalFormula", "doubleImplicationProp", 
                   "implicationProp", "xorProp", "orProp", "andProp", "notProp", 
                   "atom" ]

    EOF = Token.EOF
    TT=1
    FF=2
    END=3
    BOXLPAREN=4
    BOXRPAREN=5
    DIAMONDLPAREN=6
    DIAMONDRPAREN=7
    STAR=8
    TEST=9
    ALTERNATION=10
    CONCATENATION=11
    NAME=12
    TRUE=13
    FALSE=14
    DOUBLEIMPLY=15
    IMPLY=16
    XOR=17
    OR=18
    AND=19
    NOT=20
    LPAREN=21
    RPAREN=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(LDLfFormulaParserParser.EOF, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = LDLfFormulaParserParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.expression()
            self.state = 47
            self.match(LDLfFormulaParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def doubleImplicationTemp(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.DoubleImplicationTempContext,0)


        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = LDLfFormulaParserParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.doubleImplicationTemp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleImplicationTempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicationTemp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.ImplicationTempContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.ImplicationTempContext,i)


        def DOUBLEIMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.DOUBLEIMPLY)
            else:
                return self.getToken(LDLfFormulaParserParser.DOUBLEIMPLY, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_doubleImplicationTemp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleImplicationTemp" ):
                listener.enterDoubleImplicationTemp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleImplicationTemp" ):
                listener.exitDoubleImplicationTemp(self)




    def doubleImplicationTemp(self):

        localctx = LDLfFormulaParserParser.DoubleImplicationTempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_doubleImplicationTemp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.implicationTemp()
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.DOUBLEIMPLY:
                self.state = 52
                self.match(LDLfFormulaParserParser.DOUBLEIMPLY)
                self.state = 53
                self.implicationTemp()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicationTempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orTemp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.OrTempContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.OrTempContext,i)


        def IMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.IMPLY)
            else:
                return self.getToken(LDLfFormulaParserParser.IMPLY, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_implicationTemp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicationTemp" ):
                listener.enterImplicationTemp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicationTemp" ):
                listener.exitImplicationTemp(self)




    def implicationTemp(self):

        localctx = LDLfFormulaParserParser.ImplicationTempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_implicationTemp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.orTemp()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.IMPLY:
                self.state = 60
                self.match(LDLfFormulaParserParser.IMPLY)
                self.state = 61
                self.orTemp()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrTempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andTemp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.AndTempContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.AndTempContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.OR)
            else:
                return self.getToken(LDLfFormulaParserParser.OR, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_orTemp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrTemp" ):
                listener.enterOrTemp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrTemp" ):
                listener.exitOrTemp(self)




    def orTemp(self):

        localctx = LDLfFormulaParserParser.OrTempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_orTemp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.andTemp()
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.OR:
                self.state = 68
                self.match(LDLfFormulaParserParser.OR)
                self.state = 69
                self.andTemp()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndTempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ldlfBox(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.LdlfBoxContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.LdlfBoxContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.AND)
            else:
                return self.getToken(LDLfFormulaParserParser.AND, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_andTemp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndTemp" ):
                listener.enterAndTemp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndTemp" ):
                listener.exitAndTemp(self)




    def andTemp(self):

        localctx = LDLfFormulaParserParser.AndTempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_andTemp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.ldlfBox()
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.AND:
                self.state = 76
                self.match(LDLfFormulaParserParser.AND)
                self.state = 77
                self.ldlfBox()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LdlfBoxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ldlfDiamond(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.LdlfDiamondContext,0)


        def BOXLPAREN(self):
            return self.getToken(LDLfFormulaParserParser.BOXLPAREN, 0)

        def regularExpression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.RegularExpressionContext,0)


        def BOXRPAREN(self):
            return self.getToken(LDLfFormulaParserParser.BOXRPAREN, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_ldlfBox

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLdlfBox" ):
                listener.enterLdlfBox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLdlfBox" ):
                listener.exitLdlfBox(self)




    def ldlfBox(self):

        localctx = LDLfFormulaParserParser.LdlfBoxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ldlfBox)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LDLfFormulaParserParser.BOXLPAREN:
                self.state = 83
                self.match(LDLfFormulaParserParser.BOXLPAREN)
                self.state = 84
                self.regularExpression()
                self.state = 85
                self.match(LDLfFormulaParserParser.BOXRPAREN)


            self.state = 89
            self.ldlfDiamond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LdlfDiamondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notTemp(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.NotTempContext,0)


        def DIAMONDLPAREN(self):
            return self.getToken(LDLfFormulaParserParser.DIAMONDLPAREN, 0)

        def regularExpression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.RegularExpressionContext,0)


        def DIAMONDRPAREN(self):
            return self.getToken(LDLfFormulaParserParser.DIAMONDRPAREN, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_ldlfDiamond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLdlfDiamond" ):
                listener.enterLdlfDiamond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLdlfDiamond" ):
                listener.exitLdlfDiamond(self)




    def ldlfDiamond(self):

        localctx = LDLfFormulaParserParser.LdlfDiamondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ldlfDiamond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LDLfFormulaParserParser.DIAMONDLPAREN:
                self.state = 91
                self.match(LDLfFormulaParserParser.DIAMONDLPAREN)
                self.state = 92
                self.regularExpression()
                self.state = 93
                self.match(LDLfFormulaParserParser.DIAMONDRPAREN)


            self.state = 97
            self.notTemp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotTempContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ldlfAtom(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.LdlfAtomContext,0)


        def LPAREN(self):
            return self.getToken(LDLfFormulaParserParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LDLfFormulaParserParser.RPAREN, 0)

        def NOT(self):
            return self.getToken(LDLfFormulaParserParser.NOT, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_notTemp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotTemp" ):
                listener.enterNotTemp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotTemp" ):
                listener.exitNotTemp(self)




    def notTemp(self):

        localctx = LDLfFormulaParserParser.NotTempContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_notTemp)
        self._la = 0 # Token type
        try:
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LDLfFormulaParserParser.TT, LDLfFormulaParserParser.FF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 99
                self.ldlfAtom()
                pass
            elif token in [LDLfFormulaParserParser.NOT, LDLfFormulaParserParser.LPAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LDLfFormulaParserParser.NOT:
                    self.state = 100
                    self.match(LDLfFormulaParserParser.NOT)


                self.state = 103
                self.match(LDLfFormulaParserParser.LPAREN)
                self.state = 104
                self.expression()
                self.state = 105
                self.match(LDLfFormulaParserParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LdlfAtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TT(self):
            return self.getToken(LDLfFormulaParserParser.TT, 0)

        def FF(self):
            return self.getToken(LDLfFormulaParserParser.FF, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_ldlfAtom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLdlfAtom" ):
                listener.enterLdlfAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLdlfAtom" ):
                listener.exitLdlfAtom(self)




    def ldlfAtom(self):

        localctx = LDLfFormulaParserParser.LdlfAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ldlfAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            _la = self._input.LA(1)
            if not(_la==LDLfFormulaParserParser.TT or _la==LDLfFormulaParserParser.FF):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegularExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternation(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.AlternationContext,0)


        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_regularExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegularExpression" ):
                listener.enterRegularExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegularExpression" ):
                listener.exitRegularExpression(self)




    def regularExpression(self):

        localctx = LDLfFormulaParserParser.RegularExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_regularExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.alternation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatenation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.ConcatenationContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.ConcatenationContext,i)


        def ALTERNATION(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.ALTERNATION)
            else:
                return self.getToken(LDLfFormulaParserParser.ALTERNATION, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_alternation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlternation" ):
                listener.enterAlternation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlternation" ):
                listener.exitAlternation(self)




    def alternation(self):

        localctx = LDLfFormulaParserParser.AlternationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alternation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.concatenation()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.ALTERNATION:
                self.state = 114
                self.match(LDLfFormulaParserParser.ALTERNATION)
                self.state = 115
                self.concatenation()
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatenationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def star(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.StarContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.StarContext,i)


        def CONCATENATION(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.CONCATENATION)
            else:
                return self.getToken(LDLfFormulaParserParser.CONCATENATION, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_concatenation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatenation" ):
                listener.enterConcatenation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatenation" ):
                listener.exitConcatenation(self)




    def concatenation(self):

        localctx = LDLfFormulaParserParser.ConcatenationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_concatenation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.star()
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.CONCATENATION:
                self.state = 122
                self.match(LDLfFormulaParserParser.CONCATENATION)
                self.state = 123
                self.star()
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def test(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.TestContext,0)


        def STAR(self):
            return self.getToken(LDLfFormulaParserParser.STAR, 0)

        def LPAREN(self):
            return self.getToken(LDLfFormulaParserParser.LPAREN, 0)

        def regularExpression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.RegularExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LDLfFormulaParserParser.RPAREN, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_star

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStar" ):
                listener.enterStar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStar" ):
                listener.exitStar(self)




    def star(self):

        localctx = LDLfFormulaParserParser.StarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_star)
        self._la = 0 # Token type
        try:
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.test()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LDLfFormulaParserParser.STAR:
                    self.state = 130
                    self.match(LDLfFormulaParserParser.STAR)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(LDLfFormulaParserParser.LPAREN)
                self.state = 134
                self.regularExpression()
                self.state = 135
                self.match(LDLfFormulaParserParser.RPAREN)
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LDLfFormulaParserParser.STAR:
                    self.state = 136
                    self.match(LDLfFormulaParserParser.STAR)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LDLfFormulaParserParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(LDLfFormulaParserParser.RPAREN, 0)

        def TEST(self):
            return self.getToken(LDLfFormulaParserParser.TEST, 0)

        def atom(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.AtomContext,0)


        def propositionalFormula(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.PropositionalFormulaContext,0)


        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_test

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTest" ):
                listener.enterTest(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTest" ):
                listener.exitTest(self)




    def test(self):

        localctx = LDLfFormulaParserParser.TestContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_test)
        try:
            self.state = 150
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 141
                self.match(LDLfFormulaParserParser.LPAREN)
                self.state = 142
                self.expression()
                self.state = 143
                self.match(LDLfFormulaParserParser.RPAREN)
                self.state = 144
                self.match(LDLfFormulaParserParser.TEST)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.atom()
                self.state = 147
                self.match(LDLfFormulaParserParser.TEST)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.propositionalFormula()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropositionalFormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def doubleImplicationProp(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.DoubleImplicationPropContext,0)


        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_propositionalFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropositionalFormula" ):
                listener.enterPropositionalFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropositionalFormula" ):
                listener.exitPropositionalFormula(self)




    def propositionalFormula(self):

        localctx = LDLfFormulaParserParser.PropositionalFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_propositionalFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.doubleImplicationProp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoubleImplicationPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def implicationProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.ImplicationPropContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.ImplicationPropContext,i)


        def DOUBLEIMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.DOUBLEIMPLY)
            else:
                return self.getToken(LDLfFormulaParserParser.DOUBLEIMPLY, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_doubleImplicationProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleImplicationProp" ):
                listener.enterDoubleImplicationProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleImplicationProp" ):
                listener.exitDoubleImplicationProp(self)




    def doubleImplicationProp(self):

        localctx = LDLfFormulaParserParser.DoubleImplicationPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_doubleImplicationProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.implicationProp()
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.DOUBLEIMPLY:
                self.state = 155
                self.match(LDLfFormulaParserParser.DOUBLEIMPLY)
                self.state = 156
                self.implicationProp()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImplicationPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def xorProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.XorPropContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.XorPropContext,i)


        def IMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.IMPLY)
            else:
                return self.getToken(LDLfFormulaParserParser.IMPLY, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_implicationProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicationProp" ):
                listener.enterImplicationProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicationProp" ):
                listener.exitImplicationProp(self)




    def implicationProp(self):

        localctx = LDLfFormulaParserParser.ImplicationPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_implicationProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.xorProp()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.IMPLY:
                self.state = 163
                self.match(LDLfFormulaParserParser.IMPLY)
                self.state = 164
                self.xorProp()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XorPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.OrPropContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.OrPropContext,i)


        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.XOR)
            else:
                return self.getToken(LDLfFormulaParserParser.XOR, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_xorProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorProp" ):
                listener.enterXorProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorProp" ):
                listener.exitXorProp(self)




    def xorProp(self):

        localctx = LDLfFormulaParserParser.XorPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_xorProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.orProp()
            self.state = 175
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.XOR:
                self.state = 171
                self.match(LDLfFormulaParserParser.XOR)
                self.state = 172
                self.orProp()
                self.state = 177
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def andProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.AndPropContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.AndPropContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.OR)
            else:
                return self.getToken(LDLfFormulaParserParser.OR, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_orProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrProp" ):
                listener.enterOrProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrProp" ):
                listener.exitOrProp(self)




    def orProp(self):

        localctx = LDLfFormulaParserParser.OrPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_orProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            self.andProp()
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.OR:
                self.state = 179
                self.match(LDLfFormulaParserParser.OR)
                self.state = 180
                self.andProp()
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AndPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def notProp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LDLfFormulaParserParser.NotPropContext)
            else:
                return self.getTypedRuleContext(LDLfFormulaParserParser.NotPropContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.AND)
            else:
                return self.getToken(LDLfFormulaParserParser.AND, i)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_andProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndProp" ):
                listener.enterAndProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndProp" ):
                listener.exitAndProp(self)




    def andProp(self):

        localctx = LDLfFormulaParserParser.AndPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_andProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.notProp()
            self.state = 191
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LDLfFormulaParserParser.AND:
                self.state = 187
                self.match(LDLfFormulaParserParser.AND)
                self.state = 188
                self.notProp()
                self.state = 193
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotPropContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.AtomContext,0)


        def NOT(self):
            return self.getToken(LDLfFormulaParserParser.NOT, 0)

        def LPAREN(self):
            return self.getToken(LDLfFormulaParserParser.LPAREN, 0)

        def propositionalFormula(self):
            return self.getTypedRuleContext(LDLfFormulaParserParser.PropositionalFormulaContext,0)


        def RPAREN(self):
            return self.getToken(LDLfFormulaParserParser.RPAREN, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_notProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotProp" ):
                listener.enterNotProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotProp" ):
                listener.exitNotProp(self)




    def notProp(self):

        localctx = LDLfFormulaParserParser.NotPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_notProp)
        self._la = 0 # Token type
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LDLfFormulaParserParser.NOT:
                    self.state = 194
                    self.match(LDLfFormulaParserParser.NOT)


                self.state = 197
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==LDLfFormulaParserParser.NOT:
                    self.state = 198
                    self.match(LDLfFormulaParserParser.NOT)


                self.state = 201
                self.match(LDLfFormulaParserParser.LPAREN)
                self.state = 202
                self.propositionalFormula()
                self.state = 203
                self.match(LDLfFormulaParserParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(LDLfFormulaParserParser.NAME)
            else:
                return self.getToken(LDLfFormulaParserParser.NAME, i)

        def TRUE(self):
            return self.getToken(LDLfFormulaParserParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LDLfFormulaParserParser.FALSE, 0)

        def getRuleIndex(self):
            return LDLfFormulaParserParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = LDLfFormulaParserParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LDLfFormulaParserParser.BOXRPAREN, LDLfFormulaParserParser.DIAMONDRPAREN, LDLfFormulaParserParser.STAR, LDLfFormulaParserParser.TEST, LDLfFormulaParserParser.ALTERNATION, LDLfFormulaParserParser.CONCATENATION, LDLfFormulaParserParser.NAME, LDLfFormulaParserParser.DOUBLEIMPLY, LDLfFormulaParserParser.IMPLY, LDLfFormulaParserParser.XOR, LDLfFormulaParserParser.OR, LDLfFormulaParserParser.AND, LDLfFormulaParserParser.RPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==LDLfFormulaParserParser.NAME:
                    self.state = 207
                    self.match(LDLfFormulaParserParser.NAME)
                    self.state = 212
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [LDLfFormulaParserParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 213
                self.match(LDLfFormulaParserParser.TRUE)
                pass
            elif token in [LDLfFormulaParserParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 214
                self.match(LDLfFormulaParserParser.FALSE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





