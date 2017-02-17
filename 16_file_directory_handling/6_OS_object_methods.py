#!/usr/bin/python
print("\nExample program :\n")

import os,sys,stat

# assuming  example.txt exists and has read/write permissions

#to test the existence of path
returnValue = os.access("example.txt",os.F_OK)
print("F_OK - return value %s" % returnValue)

# to test the readability of the path
returnValue = os.access("example.txt",os.R_OK)
print("R_OK - return value %s"  %returnValue)

# to test the writability of path
returnValue = os.access("example.txt", os.W_OK)
print("W_OK - return value %s" %returnValue)

#to test the executability of path
returnValue = os.access("example.txt",os.X_OK)
print("X_OK - return value %s" %returnValue)



# assuming example.txt exists, set a file execute by the group
os.chmod("example.txt",stat.S_IXGRP)

 
#set a file write by others
os.chmod("example.txt", stat.S_IWOTH)
print("Changed mode successfully to allow others to write!!")

os.chmod("example.txt",stat.S_IWRITE)
print("Changed mode successfully to allow write access only to the owner!!")


 
# first to the current directory
os.chdir("../mydir")

#print current working directory
print("current working dir : %s" %os.getcwd())



