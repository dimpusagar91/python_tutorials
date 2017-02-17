#!/usr/bin/python

# import os module
import os
def sample():
    if os.access("myfile.txt",os.R_OK):
        with open("myfile.txt") as fp:
            return fp.read()
    return "some default data"

print("output :",sample())



def samplenew():
    try:
        fp = open("myfile.txt")
    except PermissionError:
        return "some default data"
    else:
        with fp:
            return fp.read()

print("New output: ", samplenew())

statinfo = os.stat("myfile.txt")
print("statinfo: ", statinfo)

#size of file in bytes
print("statinfo.st_size : ", statinfo.st_size)





