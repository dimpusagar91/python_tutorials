#!/usr/bin/python



# Function definition is here
def printme( number1,number2 ):
   """This prints a passed string into this function"""
   print("Number inside funciton is " ,number1,number2)
   print("Simple function");
   return ;




# Now you can call printme function
mystring = "I'm first call to user defined function!"
printme(10,20);
print("In between two functions...")



print("Documentation :",printme.__doc__)
 


