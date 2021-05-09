# Generated from PropFormulaParser.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PropFormulaParserParser import PropFormulaParserParser
else:
    from PropFormulaParserParser import PropFormulaParserParser

	package generatedParsers;


# This class defines a complete listener for a parse tree produced by PropFormulaParserParser.
class PropFormulaParserListener(ParseTreeListener):

    # Enter a parse tree produced by PropFormulaParserParser#propositionalFormula.
    def enterPropositionalFormula(self, ctx:PropFormulaParserParser.PropositionalFormulaContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#propositionalFormula.
    def exitPropositionalFormula(self, ctx:PropFormulaParserParser.PropositionalFormulaContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#doubleImplicationProp.
    def enterDoubleImplicationProp(self, ctx:PropFormulaParserParser.DoubleImplicationPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#doubleImplicationProp.
    def exitDoubleImplicationProp(self, ctx:PropFormulaParserParser.DoubleImplicationPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#implicationProp.
    def enterImplicationProp(self, ctx:PropFormulaParserParser.ImplicationPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#implicationProp.
    def exitImplicationProp(self, ctx:PropFormulaParserParser.ImplicationPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#xorProp.
    def enterXorProp(self, ctx:PropFormulaParserParser.XorPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#xorProp.
    def exitXorProp(self, ctx:PropFormulaParserParser.XorPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#orProp.
    def enterOrProp(self, ctx:PropFormulaParserParser.OrPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#orProp.
    def exitOrProp(self, ctx:PropFormulaParserParser.OrPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#andProp.
    def enterAndProp(self, ctx:PropFormulaParserParser.AndPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#andProp.
    def exitAndProp(self, ctx:PropFormulaParserParser.AndPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#notProp.
    def enterNotProp(self, ctx:PropFormulaParserParser.NotPropContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#notProp.
    def exitNotProp(self, ctx:PropFormulaParserParser.NotPropContext):
        pass


    # Enter a parse tree produced by PropFormulaParserParser#atom.
    def enterAtom(self, ctx:PropFormulaParserParser.AtomContext):
        pass

    # Exit a parse tree produced by PropFormulaParserParser#atom.
    def exitAtom(self, ctx:PropFormulaParserParser.AtomContext):
        pass



del PropFormulaParserParser