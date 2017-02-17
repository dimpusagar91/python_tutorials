#!/usr/bin/python

# '!a' (apply ascii()), '!s' (apply str()) and '!r' ( apply repr()) can be
# used to convert the value before it is formatted

print("\nExample program 1 - Using format() convert the values\n")
import math

print('The value of PI is aproximately {}.'.format(math.pi))
print('The value of PI is aproximately {!r}.'.format(math.pi))


#An optional ':' and format specifier can follow the field name.
#This allows greater control over how the value is formatted.
#rounds Pi to three places after the decimal.

print("\nExample program 2 - Using format() control over the value\n")
print('The value of PI is approximately of {0:.3f}.'.format(math.pi))

table = {'Lauren':2000,'Nick':4000,'Andrew':3000}
for name,ECode in table.items():
    print('{0:10} ==> {1:10d}'.format(name,ECode))



#If you have a really long format string that you don't want to split up
# it would be nice if you could reference
#the variables to be formatted by name instead of by position.
#This can be done by simply passing the dict and using square brackets [] to access



print("\nExample program 3 - Values formatted by name instead of position\n")
table = {'Lauren':2000 , 'Nick':4000 , 'Andrew':30000}
print('Nick: {0[Nick]:d} ; Lauren: {0[Lauren]:d}; '
      'Andrew: {0[Andrew]:d}'.format(table))



#The % operator can also be used for string formatting
#It interprets the left argumetn like a sprint() - style format string
#to be applied to the right argument, and returns the string
#resulting from this formatting operation.

print("\nExample program 4 - String formatting using % operator\n")
print('The value of PI is approximately %5.3f.' % math.pi)
