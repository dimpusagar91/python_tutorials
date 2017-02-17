#!/usr/bin/python

print("\nExample program1 - File open\n")
# open a file
file = open("example.txt","w")
print("Name of the file :", file.name)
print("closed or not :", file.closed)
print("Opening mode :", file.mode)

print("\nExample program 2 - file write and close\n")
file.write("Welcome to Python.\nhello world!\n")

file.close()

print("\nExample program3 - File read\n")
file = open("example.txt","r")
#read the file
for line in file:
    print(line,end='')
file.close()


print("\nExample program4 - file rename\n")
import os
# rename a file from example.txt to example1.txt
os.rename("example.txt","example1.txt")
print("Name of the file :", file.name)

print("\nExample program5 - Access to read old file \n")
#After renamed program 5 - Access to read old file \n")
#so error will occur

file = open("exapmle.txt","r")
print("Name of the file:", file.name)
