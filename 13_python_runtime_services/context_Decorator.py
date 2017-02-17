#!/usr/bin/python

# import contextlib module - Utilities for with-statement contexts

from contextlib import ContextDecorator

Class mycontext(ContextDecorator):
    def __enter__(self):
        print('Starting')
        return self

    def __exit__(self,*exc):
        print('Finishing')
        return False

#decorator
@mycontext()
def function():
    print('The bit in the module')

print("Calling decorator:", function())

with mycontext():
    print("The bit in the middle using my context")
