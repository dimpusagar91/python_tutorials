#!/usr/bin/python

print("\nExample program: \n")

#importing the path module
from pathlib import Path

# listing subdirectories
pathVariable = Path('.')
[item for item in pathVariable.iterdir() if item.is_dir()]
print("Display path of the directories :", [item for item in pathVariable.iterdir() if item.is_dir()])

#listing python source files in this directory tree
list(pathVariable.glob('*.py'))
print("\nDisplay path of the files :", list(pathVariable.glob('*.py')))

#navigating inside a directory tree
pathVariable = Path('c:/python33/demo')
fileVariable = pathVariable /'Module12'/'..'
print("\nDisplay path of the current file : ", fileVariable)

# to resovle symlinks and eliminate ".." components
print("\nDisplay path of the current file eliminated ..", fileVariable.exists())

#return True if hte path points to a directory
#False if it points to another kind of file

print("\nWhether the path points to a directory : ", fileVariable.is_dir())     
