#!/usr/bin/python

# User defined exception
print("\nExample program 1\n")
# Programs may name their own exceptions by creating a
# new exception class. Exceptions should typically be derived from
# the Exception class, either directly or indirectly


class MyError(Exception):
    def __init__(self,value):
        self.value = value


try:
    raise MyError(10*10)
except MyError as e:
    print('My own defined exception occurred, value:', e.value)



# Raising exception
print("\nExample program 2\n")
# The raise statement allows the programmer to
# force a specified exception to occur

# If you need to determine whether an exception was raised but don't intend to have a
# simpler form of the raise statement allows you to re-raise the exception

try:
    raise NameError('Hi There')
except NameError as e:
    print('An exception flew by!',e)
    raise
