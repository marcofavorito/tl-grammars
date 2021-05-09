# Generated from LTLfFormulaParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LTLfFormulaParserParser import LTLfFormulaParserParser
else:
    from LTLfFormulaParserParser import LTLfFormulaParserParser


# This class defines a complete listener for a parse tree produced by LTLfFormulaParserParser.
class LTLfFormulaParserListener(ParseTreeListener):

    # Enter a parse tree produced by LTLfFormulaParserParser#start.
    def enterStart(self, ctx:LTLfFormulaParserParser.StartContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#start.
    def exitStart(self, ctx:LTLfFormulaParserParser.StartContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#expression.
    def enterExpression(self, ctx:LTLfFormulaParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#expression.
    def exitExpression(self, ctx:LTLfFormulaParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#doubleImplicationTemp.
    def enterDoubleImplicationTemp(self, ctx:LTLfFormulaParserParser.DoubleImplicationTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#doubleImplicationTemp.
    def exitDoubleImplicationTemp(self, ctx:LTLfFormulaParserParser.DoubleImplicationTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#implicationTemp.
    def enterImplicationTemp(self, ctx:LTLfFormulaParserParser.ImplicationTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#implicationTemp.
    def exitImplicationTemp(self, ctx:LTLfFormulaParserParser.ImplicationTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#xorTemp.
    def enterXorTemp(self, ctx:LTLfFormulaParserParser.XorTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#xorTemp.
    def exitXorTemp(self, ctx:LTLfFormulaParserParser.XorTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#orTemp.
    def enterOrTemp(self, ctx:LTLfFormulaParserParser.OrTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#orTemp.
    def exitOrTemp(self, ctx:LTLfFormulaParserParser.OrTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#andTemp.
    def enterAndTemp(self, ctx:LTLfFormulaParserParser.AndTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#andTemp.
    def exitAndTemp(self, ctx:LTLfFormulaParserParser.AndTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#release.
    def enterRelease(self, ctx:LTLfFormulaParserParser.ReleaseContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#release.
    def exitRelease(self, ctx:LTLfFormulaParserParser.ReleaseContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#weakUntil.
    def enterWeakUntil(self, ctx:LTLfFormulaParserParser.WeakUntilContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#weakUntil.
    def exitWeakUntil(self, ctx:LTLfFormulaParserParser.WeakUntilContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#strongRelease.
    def enterStrongRelease(self, ctx:LTLfFormulaParserParser.StrongReleaseContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#strongRelease.
    def exitStrongRelease(self, ctx:LTLfFormulaParserParser.StrongReleaseContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#until.
    def enterUntil(self, ctx:LTLfFormulaParserParser.UntilContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#until.
    def exitUntil(self, ctx:LTLfFormulaParserParser.UntilContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#globally.
    def enterGlobally(self, ctx:LTLfFormulaParserParser.GloballyContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#globally.
    def exitGlobally(self, ctx:LTLfFormulaParserParser.GloballyContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#eventually.
    def enterEventually(self, ctx:LTLfFormulaParserParser.EventuallyContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#eventually.
    def exitEventually(self, ctx:LTLfFormulaParserParser.EventuallyContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#weakNext.
    def enterWeakNext(self, ctx:LTLfFormulaParserParser.WeakNextContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#weakNext.
    def exitWeakNext(self, ctx:LTLfFormulaParserParser.WeakNextContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#next_.
    def enterNext_(self, ctx:LTLfFormulaParserParser.Next_Context):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#next_.
    def exitNext_(self, ctx:LTLfFormulaParserParser.Next_Context):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#notTemp.
    def enterNotTemp(self, ctx:LTLfFormulaParserParser.NotTempContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#notTemp.
    def exitNotTemp(self, ctx:LTLfFormulaParserParser.NotTempContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#ltlfAtom.
    def enterLtlfAtom(self, ctx:LTLfFormulaParserParser.LtlfAtomContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#ltlfAtom.
    def exitLtlfAtom(self, ctx:LTLfFormulaParserParser.LtlfAtomContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#propositionalFormula.
    def enterPropositionalFormula(self, ctx:LTLfFormulaParserParser.PropositionalFormulaContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#propositionalFormula.
    def exitPropositionalFormula(self, ctx:LTLfFormulaParserParser.PropositionalFormulaContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#doubleImplicationProp.
    def enterDoubleImplicationProp(self, ctx:LTLfFormulaParserParser.DoubleImplicationPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#doubleImplicationProp.
    def exitDoubleImplicationProp(self, ctx:LTLfFormulaParserParser.DoubleImplicationPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#implicationProp.
    def enterImplicationProp(self, ctx:LTLfFormulaParserParser.ImplicationPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#implicationProp.
    def exitImplicationProp(self, ctx:LTLfFormulaParserParser.ImplicationPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#xorProp.
    def enterXorProp(self, ctx:LTLfFormulaParserParser.XorPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#xorProp.
    def exitXorProp(self, ctx:LTLfFormulaParserParser.XorPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#orProp.
    def enterOrProp(self, ctx:LTLfFormulaParserParser.OrPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#orProp.
    def exitOrProp(self, ctx:LTLfFormulaParserParser.OrPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#andProp.
    def enterAndProp(self, ctx:LTLfFormulaParserParser.AndPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#andProp.
    def exitAndProp(self, ctx:LTLfFormulaParserParser.AndPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#notProp.
    def enterNotProp(self, ctx:LTLfFormulaParserParser.NotPropContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#notProp.
    def exitNotProp(self, ctx:LTLfFormulaParserParser.NotPropContext):
        pass


    # Enter a parse tree produced by LTLfFormulaParserParser#atom.
    def enterAtom(self, ctx:LTLfFormulaParserParser.AtomContext):
        pass

    # Exit a parse tree produced by LTLfFormulaParserParser#atom.
    def exitAtom(self, ctx:LTLfFormulaParserParser.AtomContext):
        pass



del LTLfFormulaParserParser