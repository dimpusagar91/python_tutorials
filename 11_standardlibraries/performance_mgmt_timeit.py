#!/usr/bin/python

#import timeit module
from timeit import Timer

print("performance of Timer('temp=a;a=b;b=temp',a=1;b=2'): ",Timer('temp=a;a=b;b=temp','a=1;b=2').timeit())

print("performance of Timer('a,b = b,a','a=1;b=2'):", Timer('a,b = b,a','a=1;b=2').timeit())
