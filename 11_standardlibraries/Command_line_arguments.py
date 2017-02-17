#!/usr/bin/python

# Import sys module

import sys
# Common utility scripts often need to process command line arguments
print(sys.argv)

print('\n---------------------------\n')
for arg in sys.argv:
    print(arg)

# The sys module has attributes for stdin, stdout and stderr
print('----- sys.stderr.write-----\n')
sys.stderr.write('Warning, log file not found starting a new one\n')
