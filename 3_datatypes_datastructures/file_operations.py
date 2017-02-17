#!/usr/bin/python

# open a file
file = open("example.txt","w")

print("Name of the file : ", file.name )

file.write("Welcome to Python. \n Hello world!!\n")

# close opened file
file.close()

# file read operation

file = open("example.txt","r")
#read the file
for line in file:
	print(line, end= '')

file.close()


# import os module
import os

# rename a file from example.txt to example1.txt

os.rename("example.txt","example1.txt")
file = open("example1.txt","r")
print("Name of the file : ", file.name)

# After renamed of the file example1.txt will be not available
# so, error will occur.

file = open("example.txt","r")
print("Name of the file : ", file.name)