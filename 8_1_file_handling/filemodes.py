#!/usr/bin/python

# Open a file
fo = open("demo.txt", "r")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)
fo.close()

if fo.closed :
    print("File is already closed")

 
