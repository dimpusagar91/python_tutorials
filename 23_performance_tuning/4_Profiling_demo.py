#!/usr/bin/python

#The dis module can be used to disassemble python functions, methods
# and classes into low-level interpreter instructions

import dis
def sum():
    varSubject1 = 90
    varSubject2 = 95
    varSubject3 = 85

    sum = varSubject1 + varSubject2 + varSubject3
#   print("Subject1:  ",varSubject1)
#   print("Subject2:  ",varSubject2)
#   print("Subject3:  ",varSubject3)


# call dis function for the function
dis.dis(sum)
