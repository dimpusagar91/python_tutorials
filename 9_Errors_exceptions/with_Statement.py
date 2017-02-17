#!/usr/bin/python

#The script tries to open a file and print its contents to the screen
print("Example program 1 \n")
for line in open("myfile.txt"):
    print(line,end="")


#The problem with this code is that is leaves the file open for an indetermat
#amount of time after this part of the code has finished executing.
#This is not an issue in simple scripts, but can be a problem for larger applications


#The with statement allows objects like files to be used in a way that ensures
#they are always cleaned up promptly and correctly.
print("\nExample program 2\n")
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")

#After the statement is executed, the file f is always closed, even if a problem
#was encountered while processing the lines. Objects which, like files,
#provide predefined clean up actions will indicate this in their documentation


#The with statement allows objects like files to be used in a way that ensures
#they are always cleaned up promptly and correctly.
