# Generated from LDLfFormulaParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LDLfFormulaParserParser import LDLfFormulaParserParser
else:
    from LDLfFormulaParserParser import LDLfFormulaParserParser


# This class defines a complete listener for a parse tree produced by LDLfFormulaParserParser.
class LDLfFormulaParserListener(ParseTreeListener):

    # Enter a parse tree produced by LDLfFormulaParserParser#start.
    def enterStart(self, ctx:LDLfFormulaParserParser.StartContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#start.
    def exitStart(self, ctx:LDLfFormulaParserParser.StartContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#expression.
    def enterExpression(self, ctx:LDLfFormulaParserParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#expression.
    def exitExpression(self, ctx:LDLfFormulaParserParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#doubleImplicationTemp.
    def enterDoubleImplicationTemp(self, ctx:LDLfFormulaParserParser.DoubleImplicationTempContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#doubleImplicationTemp.
    def exitDoubleImplicationTemp(self, ctx:LDLfFormulaParserParser.DoubleImplicationTempContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#implicationTemp.
    def enterImplicationTemp(self, ctx:LDLfFormulaParserParser.ImplicationTempContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#implicationTemp.
    def exitImplicationTemp(self, ctx:LDLfFormulaParserParser.ImplicationTempContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#orTemp.
    def enterOrTemp(self, ctx:LDLfFormulaParserParser.OrTempContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#orTemp.
    def exitOrTemp(self, ctx:LDLfFormulaParserParser.OrTempContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#andTemp.
    def enterAndTemp(self, ctx:LDLfFormulaParserParser.AndTempContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#andTemp.
    def exitAndTemp(self, ctx:LDLfFormulaParserParser.AndTempContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#ldlfBox.
    def enterLdlfBox(self, ctx:LDLfFormulaParserParser.LdlfBoxContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#ldlfBox.
    def exitLdlfBox(self, ctx:LDLfFormulaParserParser.LdlfBoxContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#ldlfDiamond.
    def enterLdlfDiamond(self, ctx:LDLfFormulaParserParser.LdlfDiamondContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#ldlfDiamond.
    def exitLdlfDiamond(self, ctx:LDLfFormulaParserParser.LdlfDiamondContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#notTemp.
    def enterNotTemp(self, ctx:LDLfFormulaParserParser.NotTempContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#notTemp.
    def exitNotTemp(self, ctx:LDLfFormulaParserParser.NotTempContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#ldlfAtom.
    def enterLdlfAtom(self, ctx:LDLfFormulaParserParser.LdlfAtomContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#ldlfAtom.
    def exitLdlfAtom(self, ctx:LDLfFormulaParserParser.LdlfAtomContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#regularExpression.
    def enterRegularExpression(self, ctx:LDLfFormulaParserParser.RegularExpressionContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#regularExpression.
    def exitRegularExpression(self, ctx:LDLfFormulaParserParser.RegularExpressionContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#alternation.
    def enterAlternation(self, ctx:LDLfFormulaParserParser.AlternationContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#alternation.
    def exitAlternation(self, ctx:LDLfFormulaParserParser.AlternationContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#concatenation.
    def enterConcatenation(self, ctx:LDLfFormulaParserParser.ConcatenationContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#concatenation.
    def exitConcatenation(self, ctx:LDLfFormulaParserParser.ConcatenationContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#star.
    def enterStar(self, ctx:LDLfFormulaParserParser.StarContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#star.
    def exitStar(self, ctx:LDLfFormulaParserParser.StarContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#test.
    def enterTest(self, ctx:LDLfFormulaParserParser.TestContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#test.
    def exitTest(self, ctx:LDLfFormulaParserParser.TestContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#propositionalFormula.
    def enterPropositionalFormula(self, ctx:LDLfFormulaParserParser.PropositionalFormulaContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#propositionalFormula.
    def exitPropositionalFormula(self, ctx:LDLfFormulaParserParser.PropositionalFormulaContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#doubleImplicationProp.
    def enterDoubleImplicationProp(self, ctx:LDLfFormulaParserParser.DoubleImplicationPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#doubleImplicationProp.
    def exitDoubleImplicationProp(self, ctx:LDLfFormulaParserParser.DoubleImplicationPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#implicationProp.
    def enterImplicationProp(self, ctx:LDLfFormulaParserParser.ImplicationPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#implicationProp.
    def exitImplicationProp(self, ctx:LDLfFormulaParserParser.ImplicationPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#xorProp.
    def enterXorProp(self, ctx:LDLfFormulaParserParser.XorPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#xorProp.
    def exitXorProp(self, ctx:LDLfFormulaParserParser.XorPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#orProp.
    def enterOrProp(self, ctx:LDLfFormulaParserParser.OrPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#orProp.
    def exitOrProp(self, ctx:LDLfFormulaParserParser.OrPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#andProp.
    def enterAndProp(self, ctx:LDLfFormulaParserParser.AndPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#andProp.
    def exitAndProp(self, ctx:LDLfFormulaParserParser.AndPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#notProp.
    def enterNotProp(self, ctx:LDLfFormulaParserParser.NotPropContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#notProp.
    def exitNotProp(self, ctx:LDLfFormulaParserParser.NotPropContext):
        pass


    # Enter a parse tree produced by LDLfFormulaParserParser#atom.
    def enterAtom(self, ctx:LDLfFormulaParserParser.AtomContext):
        pass

    # Exit a parse tree produced by LDLfFormulaParserParser#atom.
    def exitAtom(self, ctx:LDLfFormulaParserParser.AtomContext):
        pass



del LDLfFormulaParserParser