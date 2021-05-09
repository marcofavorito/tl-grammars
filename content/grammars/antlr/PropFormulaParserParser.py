# Generated from PropFormulaParser.g4 by ANTLR 4.9
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3\33")
        buf.write("\13\3\3\4\3\4\3\4\7\4 \n\4\f\4\16\4#\13\4\3\5\3\5\3\5")
        buf.write("\7\5(\n\5\f\5\16\5+\13\5\3\6\3\6\3\6\7\6\60\n\6\f\6\16")
        buf.write("\6\63\13\6\3\7\3\7\3\7\7\78\n\7\f\7\16\7;\13\7\3\b\5\b")
        buf.write(">\n\b\3\b\3\b\5\bB\n\b\3\b\3\b\3\b\3\b\5\bH\n\b\3\t\7")
        buf.write("\tK\n\t\f\t\16\tN\13\t\3\t\3\t\5\tR\n\t\3\t\2\2\n\2\4")
        buf.write("\6\b\n\f\16\20\2\2\2V\2\22\3\2\2\2\4\24\3\2\2\2\6\34\3")
        buf.write("\2\2\2\b$\3\2\2\2\n,\3\2\2\2\f\64\3\2\2\2\16G\3\2\2\2")
        buf.write("\20Q\3\2\2\2\22\23\5\4\3\2\23\3\3\2\2\2\24\31\5\6\4\2")
        buf.write("\25\26\7\6\2\2\26\30\5\6\4\2\27\25\3\2\2\2\30\33\3\2\2")
        buf.write("\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33\31\3\2")
        buf.write("\2\2\34!\5\b\5\2\35\36\7\7\2\2\36 \5\b\5\2\37\35\3\2\2")
        buf.write("\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"\7\3\2\2\2#!\3\2")
        buf.write("\2\2$)\5\n\6\2%&\7\b\2\2&(\5\n\6\2\'%\3\2\2\2(+\3\2\2")
        buf.write("\2)\'\3\2\2\2)*\3\2\2\2*\t\3\2\2\2+)\3\2\2\2,\61\5\f\7")
        buf.write("\2-.\7\t\2\2.\60\5\f\7\2/-\3\2\2\2\60\63\3\2\2\2\61/\3")
        buf.write("\2\2\2\61\62\3\2\2\2\62\13\3\2\2\2\63\61\3\2\2\2\649\5")
        buf.write("\16\b\2\65\66\7\n\2\2\668\5\16\b\2\67\65\3\2\2\28;\3\2")
        buf.write("\2\29\67\3\2\2\29:\3\2\2\2:\r\3\2\2\2;9\3\2\2\2<>\7\13")
        buf.write("\2\2=<\3\2\2\2=>\3\2\2\2>?\3\2\2\2?H\5\20\t\2@B\7\13\2")
        buf.write("\2A@\3\2\2\2AB\3\2\2\2BC\3\2\2\2CD\7\f\2\2DE\5\2\2\2E")
        buf.write("F\7\r\2\2FH\3\2\2\2G=\3\2\2\2GA\3\2\2\2H\17\3\2\2\2IK")
        buf.write("\7\3\2\2JI\3\2\2\2KN\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MR\3\2")
        buf.write("\2\2NL\3\2\2\2OR\7\4\2\2PR\7\5\2\2QL\3\2\2\2QO\3\2\2\2")
        buf.write("QP\3\2\2\2R\21\3\2\2\2\f\31!)\619=AGLQ")
        return buf.getvalue()


class PropFormulaParserParser ( Parser ):

    grammarFileName = "PropFormulaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NAME", "TRUE", "FALSE", "DOUBLEIMPLY", 
                      "IMPLY", "XOR", "OR", "AND", "NOT", "LPAREN", "RPAREN", 
                      "WS" ]

    RULE_propositionalFormula = 0
    RULE_doubleImplicationProp = 1
    RULE_implicationProp = 2
    RULE_xorProp = 3
    RULE_orProp = 4
    RULE_andProp = 5
    RULE_notProp = 6
    RULE_atom = 7

    ruleNames =  [ "propositionalFormula", "doubleImplicationProp", "implicationProp", 
                   "xorProp", "orProp", "andProp", "notProp", "atom" ]

    EOF = Token.EOF
    NAME=1
    TRUE=2
    FALSE=3
    DOUBLEIMPLY=4
    IMPLY=5
    XOR=6
    OR=7
    AND=8
    NOT=9
    LPAREN=10
    RPAREN=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PropositionalFormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def doubleImplicationProp(self):
            return self.getTypedRuleContext(PropFormulaParserParser.DoubleImplicationPropContext,0)


        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_propositionalFormula

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPropositionalFormula" ):
                listener.enterPropositionalFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPropositionalFormula" ):
                listener.exitPropositionalFormula(self)




    def propositionalFormula(self):

        localctx = PropFormulaParserParser.PropositionalFormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_propositionalFormula)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
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
                return self.getTypedRuleContexts(PropFormulaParserParser.ImplicationPropContext)
            else:
                return self.getTypedRuleContext(PropFormulaParserParser.ImplicationPropContext,i)


        def DOUBLEIMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(PropFormulaParserParser.DOUBLEIMPLY)
            else:
                return self.getToken(PropFormulaParserParser.DOUBLEIMPLY, i)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_doubleImplicationProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoubleImplicationProp" ):
                listener.enterDoubleImplicationProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoubleImplicationProp" ):
                listener.exitDoubleImplicationProp(self)




    def doubleImplicationProp(self):

        localctx = PropFormulaParserParser.DoubleImplicationPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_doubleImplicationProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.implicationProp()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropFormulaParserParser.DOUBLEIMPLY:
                self.state = 19
                self.match(PropFormulaParserParser.DOUBLEIMPLY)
                self.state = 20
                self.implicationProp()
                self.state = 25
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
                return self.getTypedRuleContexts(PropFormulaParserParser.XorPropContext)
            else:
                return self.getTypedRuleContext(PropFormulaParserParser.XorPropContext,i)


        def IMPLY(self, i:int=None):
            if i is None:
                return self.getTokens(PropFormulaParserParser.IMPLY)
            else:
                return self.getToken(PropFormulaParserParser.IMPLY, i)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_implicationProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImplicationProp" ):
                listener.enterImplicationProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImplicationProp" ):
                listener.exitImplicationProp(self)




    def implicationProp(self):

        localctx = PropFormulaParserParser.ImplicationPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_implicationProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.xorProp()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropFormulaParserParser.IMPLY:
                self.state = 27
                self.match(PropFormulaParserParser.IMPLY)
                self.state = 28
                self.xorProp()
                self.state = 33
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
                return self.getTypedRuleContexts(PropFormulaParserParser.OrPropContext)
            else:
                return self.getTypedRuleContext(PropFormulaParserParser.OrPropContext,i)


        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(PropFormulaParserParser.XOR)
            else:
                return self.getToken(PropFormulaParserParser.XOR, i)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_xorProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterXorProp" ):
                listener.enterXorProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitXorProp" ):
                listener.exitXorProp(self)




    def xorProp(self):

        localctx = PropFormulaParserParser.XorPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_xorProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.orProp()
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropFormulaParserParser.XOR:
                self.state = 35
                self.match(PropFormulaParserParser.XOR)
                self.state = 36
                self.orProp()
                self.state = 41
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
                return self.getTypedRuleContexts(PropFormulaParserParser.AndPropContext)
            else:
                return self.getTypedRuleContext(PropFormulaParserParser.AndPropContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PropFormulaParserParser.OR)
            else:
                return self.getToken(PropFormulaParserParser.OR, i)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_orProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrProp" ):
                listener.enterOrProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrProp" ):
                listener.exitOrProp(self)




    def orProp(self):

        localctx = PropFormulaParserParser.OrPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_orProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.andProp()
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropFormulaParserParser.OR:
                self.state = 43
                self.match(PropFormulaParserParser.OR)
                self.state = 44
                self.andProp()
                self.state = 49
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
                return self.getTypedRuleContexts(PropFormulaParserParser.NotPropContext)
            else:
                return self.getTypedRuleContext(PropFormulaParserParser.NotPropContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PropFormulaParserParser.AND)
            else:
                return self.getToken(PropFormulaParserParser.AND, i)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_andProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndProp" ):
                listener.enterAndProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndProp" ):
                listener.exitAndProp(self)




    def andProp(self):

        localctx = PropFormulaParserParser.AndPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_andProp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.notProp()
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==PropFormulaParserParser.AND:
                self.state = 51
                self.match(PropFormulaParserParser.AND)
                self.state = 52
                self.notProp()
                self.state = 57
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
            return self.getTypedRuleContext(PropFormulaParserParser.AtomContext,0)


        def NOT(self):
            return self.getToken(PropFormulaParserParser.NOT, 0)

        def LPAREN(self):
            return self.getToken(PropFormulaParserParser.LPAREN, 0)

        def propositionalFormula(self):
            return self.getTypedRuleContext(PropFormulaParserParser.PropositionalFormulaContext,0)


        def RPAREN(self):
            return self.getToken(PropFormulaParserParser.RPAREN, 0)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_notProp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotProp" ):
                listener.enterNotProp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotProp" ):
                listener.exitNotProp(self)




    def notProp(self):

        localctx = PropFormulaParserParser.NotPropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_notProp)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PropFormulaParserParser.NOT:
                    self.state = 58
                    self.match(PropFormulaParserParser.NOT)


                self.state = 61
                self.atom()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==PropFormulaParserParser.NOT:
                    self.state = 62
                    self.match(PropFormulaParserParser.NOT)


                self.state = 65
                self.match(PropFormulaParserParser.LPAREN)
                self.state = 66
                self.propositionalFormula()
                self.state = 67
                self.match(PropFormulaParserParser.RPAREN)
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
                return self.getTokens(PropFormulaParserParser.NAME)
            else:
                return self.getToken(PropFormulaParserParser.NAME, i)

        def TRUE(self):
            return self.getToken(PropFormulaParserParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(PropFormulaParserParser.FALSE, 0)

        def getRuleIndex(self):
            return PropFormulaParserParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = PropFormulaParserParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PropFormulaParserParser.NAME, PropFormulaParserParser.DOUBLEIMPLY, PropFormulaParserParser.IMPLY, PropFormulaParserParser.XOR, PropFormulaParserParser.OR, PropFormulaParserParser.AND, PropFormulaParserParser.RPAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PropFormulaParserParser.NAME:
                    self.state = 71
                    self.match(PropFormulaParserParser.NAME)
                    self.state = 76
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [PropFormulaParserParser.TRUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.match(PropFormulaParserParser.TRUE)
                pass
            elif token in [PropFormulaParserParser.FALSE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.match(PropFormulaParserParser.FALSE)
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





