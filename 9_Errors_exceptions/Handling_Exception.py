#!/usr/bin/python

#It is possible to write programs that handle selected exceptions
#when executing the code, which asks the user for input until a valid integer
#has been entered, but allows the user to interrupt the program
#(using Control-C), note that a user-generated interruption is signaled by
#raising the KeyboardInterrupt exception


print("\nExample program 1\n")
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("No!  That was no valid number. Try again ...")



print("\nExample program 2\n")
# import sys module
import sys

try:
    # open file info.txt having string content
    file = open('c:\python33\info.txt')
    #read a line and assigned to str
    str = file.readline()
    #convert the string to integer
    vara = int(str.strip())
    #print an error message and then re-raise the exception
except OSError as err :
    print("OS error : {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise



print("\nExample program 3\n")
#Exception handlers don't just handle exceptions
#if they occur immediately in the try clause, but
#also if they occur inside functions that are called
#(even indirectly) in the try clause


def this_fails():
    vara = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:',err)
