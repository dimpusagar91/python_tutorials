#!/usr/bin/python
import doctest
#import doctest module

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([40,60,140]))
    80.0
    """
    return sum(values) / len(values)



# automatically validate the embedded tests
print("automatically validate the embedded tests: ", doctest.testmod())

 
