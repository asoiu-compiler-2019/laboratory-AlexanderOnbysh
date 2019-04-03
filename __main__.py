import pydot

from compiler.lexical_analysis.lexer import Lexer, EOF
from compiler.semantic_analysis.analyzer import SemanticAnalyzer
from compiler.syntax_analysis.parser import Parser
from compiler.compiler.compiler import Compiler
from utils.genastdot import ASTVisualizer

program = open('examples/example_1.c').read()

# Lexer
# lexer = Lexer(program)
# token = lexer.get_next_token
# while token.type != EOF:
#     # print(token)
#     token = lexer.get_next_token
#
# # Syntax
# lexer = Lexer(program)
# parser = Parser(lexer)
# viz = ASTVisualizer(parser)
# content = viz.gendot()
# (graph,) = pydot.graph_from_dot_data(content)
# graph.write_png('test.png')
# #
# # # Semantic
# lexer = Lexer(program)
# parser = Parser(lexer)
# tree = parser.parse()
# SemanticAnalyzer.analyze(tree)


# compiler 
compiler = Compiler()
compiler.run(program)
