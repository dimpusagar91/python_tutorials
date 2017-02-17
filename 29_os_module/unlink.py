import os, sys

# listing directories
print ("The dir is: %s" %os.listdir(os.getcwd()))

#os.unlink("aa.txt")

# listing directories after removing path
print ("The dir after removal of path : %s" %os.listdir(os.getcwd()))
