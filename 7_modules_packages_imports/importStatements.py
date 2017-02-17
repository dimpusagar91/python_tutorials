#!/usr/bin/python

# import the module

import fibonacci

print("fibonacci.fibo(x): ")
# Using the module name you can access the functions
fibonacci.fibo(50)
print("fibonacci.fibolist(80):", fibonacci.fibolist(80))

#imports all name except those beginning with an underscore (_)
print("fibonacci.__name__ : ", fibonacci.__name__ )


# import the module using from
from fibonacci import fibo, fibolist

print("fibo(50): ")
# using the module name you can access the functions
fibo(50)
print("fibolist(80) : ", fibolist(80))


# import all the modules using from
from fibonacci import *

print("fibo(50) :")
#using the module name you can access the functions
fibo(50)
print("fibolist(80) : ", fibolist(80))

#dir()

fib = fibonacci.fibo
# The builtin function dir() is used to find out
# which  names a module defines
# It returnsa sorted list of strings
print("dir(fib) : ", dir(fib))

print("\n")
# without arguments, dir() lists the names you
# have defined currently
print("dir() : ",dir())

# It lists all types of names : variables
# modules,functions etc


