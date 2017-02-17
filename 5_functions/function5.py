#!/usr/bin/python

number = 1992
name = "Python"

print("%s was developed in the year %d" %(name,number))

line = "%s was developed in the year %d"

print(line %(name,number))

### python style

print("{number} was developed in the year {name}".format(number=10,name="test"));
