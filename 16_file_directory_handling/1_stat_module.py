#!/usr/bin/python

print("\nExample program using stat module:\n")

#import moduel os,sys, stat
import os,sys
from stat import *


def dirtree(top,callback):
    '''
    recursively descend the directory tree rooted at top
    calling the callback function for each regular file
    '''
    
    for f in os.listdir(top):
        pathname = os.path.join(top,f)
        mode = os.stat(pathname).st_mode
        
        #return non-zero if the mode is from a directory
        if S_ISDIR(mode):
            #it's a directory, recurse into it
            dirtree(pathname,callback)
        #retun non-zero if the mode is from a regular file
        elif S_ISREG(mode):
            #it's a file, call the visitfile function
            callback(pathname)
        else:
            # if unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    print('visiting',file)

# execute from command prompt with directory name as an argument

if __name__ == '__main__':
    dirtree(sys.argv[1],visitfile) 
