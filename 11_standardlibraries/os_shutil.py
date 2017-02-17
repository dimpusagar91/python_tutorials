#!/usr/bin/python

 
# the shutil module provides a higher
#level interface that is easier

import shutil
shutil.copyfile('data.txt','archive.txt')
shutil.move('C://tempDir//test','temp')

# change the current directory

os.chdir('c://Python33//Demo//')


# import glob module
import glob
#A function for making file lists from directory wildcard searches
print(glob.glob('*.py'))
