#!/usr/bin/python

# to write a table of squares and cubes using range(), repr() and rjust()
print("\nExample program 1 - Using repr() and rjust():\n")
for x in range(1,11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end = ' ')
    # Note use of 'end' on previous line

    # The str.rjust() method of string objects, which right-justifies a string in
    # it with spaces on the left.
    print(repr(x*x*x).rjust(4))

print("\nExample program 2 - Using format() \n")
# To write a tabe of squares and cubes using range(), format()
for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

# str.zfill(), which pads a numeric string on the left with zeros
# It understands about plus and minus signs.

print("\nExample program 3 - zfill()\n")
print('\'90\'.zfill(6)) : ', '90'.zfill(6))
print('\'-3.14\'.zfill(8) : ', '-3.14'.zfill(8))
print()

