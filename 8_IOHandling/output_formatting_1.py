#!/usr/bin/python

print('\n Output formatting - str() and repr() \n ')
print('\n Example 1 - Convert values to strings \n')
# Assign the value

var_str = 'Hello, world.'

# Convert values to strings using repr() and str()

print('str(var_str)', str(var_str))
print('repr(var_str)',repr(var_str))
print('str(22/7): ', str(22/7))

# repr()  is to generate representations which can be read by the interpreter
# It will force a Syntaxerror if there is no equivalent syntax
# str() is to return representations of values which are fairly human-readable


print('\n Example 2 - Concatenation strings\n')
var_a = 20 * 3.14
var_b = 150 * 150
var_str = 'The value of var_a is '+  repr(var_a) + ', and var_b is ' + repr(var_b) + '...'
print(var_str)


# The repr() of a string adds string quotes and backslashes
print('\n Example 3 - The string can be read by the interpreter\n')
var_str = 'Hello, world.\n'
var_c = repr(var_str)
print('repr(var_str) : ', var_c )

print('\n Example 4 - The argument to repr method\n')
# The argument to repr() may be any Python object
print('repr((var_a,var_b),(\'Python\',\'Programming\'))):', repr((var_a, var_b ,('Python','Programming'))))
