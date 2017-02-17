#!/usr/bin/python

code = compile('a + 5','file.py','eval')
a=5

print("code : ", eval(code))


# import parser module
import parser

st = parser.expr('b + 5')
code = st.compile('file.py')
b = 15

print("Parser code : ", eval(code))

# import systable module  - access to the  compilers symbol table

import symtable
table = symtable.symtable("def func(): pass", "string","exec")

print("func : ", table.lookup("func").is_namespace())
