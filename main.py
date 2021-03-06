import sundanase_lexer
import sundanase_parser
import sundanase_interpreter

from sys import *

#DENGAN MASUKAN
lexer = sundanase_lexer.SundanaseLexer()
parser = sundanase_parser.SundanaseParser()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    sundanase_interpreter.SundanaseExecute(tree, env)
