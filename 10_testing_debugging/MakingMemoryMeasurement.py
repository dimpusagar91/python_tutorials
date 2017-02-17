#!/usr/bin/python

#Import sys module
import sys

#The getsizeof() function is only going to give you a rough idea of overall memory use for various objects

print("sys.getsizeof(1)",sys.getsizeof(1))
print("sys.getsizeof(\"Hello World\"):", sys.getsizeof("Hello world"))
print("sys.getsizeof([1,2,3,4]) :",sys.getsizeof([1,2,3,4]))

#The reported size of the list [1,2,3,4] is actually smaller than
#the space required for four integers
#( which are 24 bytes each )

print("sum(sys.getsizeof(x) for x in [1,2,3,4]) :",sum(sys.getsizeof(x) for x in [1,2,3,4]))
      
