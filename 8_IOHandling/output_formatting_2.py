#!/usr/bin/python

# format() method
print("\nExample program 1 - Using format()\n")
print('{} to {} Programming'.format('welcome','Python'))

# The brackets and characters within them ( called format fields)
# are replaced with the objects passed into the str.format() method
# A number in hte brackets can be used to refer to the position of
# the object passed into the str.format() method.

print("\nExample program 2 - Using format() - A number in the brackets\n")
print('{0} and {1}'.format('Input','Output'))
print('{1} and {0}'.format('Input','Output'))

# If keyword arguments are used in the str.format() method
# their values are referred to by using the name of the argument.


print("\nExample program 3 - Using format() - referred by argument\n")
print('This {movie} is {adjective}.'.format(movie='Gladiator is',adjective='fantastic'))



# Positional and keyword arguments can be arbitrarily combined:
print("\nExample program 4 - Using format() - positional and keyword arguments\n")
print('The story of {0},{1} and {other}.'.format('Giridhar','S',other='Senior'))













