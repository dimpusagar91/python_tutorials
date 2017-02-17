import os, sys

# listing directories
print ("The dir is: %s"%os.listdir(os.getcwd()))

# renaming directory ''tutorialsdir"
#os.rename("tutorialsdir","tutorialsdirectory")

print "Successfully renamed."

# listing directories after renaming "tutorialsdir"
print ("the dir is: %s" %os.listdir(os.getcwd()))
