#!/usr/bin/python

# Function definition is here
def changeme( *mylist1 ):
   "This changes a passed list into this function"
   print("Inside function",mylist1)
   return

# Now you can call changeme function
mylist = [10,20,30];
changeme(mylist);
print("Values outside the function: ", mylist)
