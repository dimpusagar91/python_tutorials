#!/usr/bin/python

# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)
   print("Tuple inside function", vartuple)
   for var in vartuple:
      print ("value from tuple is ", var)
   return;

# Now you can call printinfo function
printinfo( 10 );
printinfo( 70, 60, 50 );
