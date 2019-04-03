import pydot
import sys

from compiler.compiler.compiler import Compiler


with open(sys.argv[1]) as f:
    file = f.read()

compiler = Compiler()
Compiler.interpret(file)


