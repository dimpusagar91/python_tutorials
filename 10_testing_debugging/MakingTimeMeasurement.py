#!/usr/bin/python

#Import time module
import time
start_cpu = time.clock()
start_real = time.time()

#The first argument to timeit() is the code you want to benchmark
#The second argument is a statement that gets executed in order to
#set up the execution environment
# The timeit() function runs the supplied  statement
# one million  times and reports the execution time.

from timeit import timeit
timeit('math.sqrt(2.0)','import math')
timeit('sqrt(2.0)','from math import sqrt')

#The number of repetitions can be changed by supplying a number=count keyword argument to timeit()
#Using sqrt(2.0) instead of math.sqrt(2.0) represents a speedup of 0.20388/0.14494 or about 1.41
#Sometimes this gets reported as a percentage by saying the speedup is about 41 percent.


from timeit import repeat
repeat('math.sqrt(2.0)','import math')
end_cpu = time.clock()
end_real = time.time()

tmp2 = end_cpu - start_cpu
tmp1 = end_real - start_real
print("%f Real Seconds" %(tmp1))
print("%f CPU seconds" %(tmp2))
