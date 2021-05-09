#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from antlr4 import *
from LDLfFormulaParserLexer import LDLfFormulaParserLexer
from LDLfFormulaParserParser import LDLfFormulaParserParser
from LTLfFormulaParserLexer import LTLfFormulaParserLexer
from LTLfFormulaParserParser import LTLfFormulaParserParser 

class LDLfFormulaListener(ParseTreeListener):
    def enterStart(self, ctx):
        pass
    def exitStart(self, ctx):
        pass
 
class StartPrinter(LDLfFormulaListener):

    def enterStart(self, ctx):
        print("Oh, a start! enter", ctx)

    def exitStart(self, ctx):
        print("Oh, a start!", ctx)

    def exitLtlfAtom(self, ctx):
        print("Oh, a name!", ctx)




def main(argv):
    input_stream = FileStream(argv[1])
    # lexer = LDLfFormulaParserLexer(input_stream)
    lexer = LTLfFormulaParserLexer(input_stream)
    stream = CommonTokenStream(lexer)
    # parser = LDLfFormulaParserParser(stream)
    parser = LTLfFormulaParserParser(stream)
    tree = parser.start()

    printer = StartPrinter()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

 
if __name__ == '__main__':
    main(sys.argv)

