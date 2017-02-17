import os

path = "C:\\scripts"

# Check current working directory.
retval = os.getcwd()
print ("Current working directory %s" % retval)

# Now change the directory
os.chdir(path)

# Check current working directory.
retval = os.getcwd()

print ("Directory changed successfully %s" % retval)
