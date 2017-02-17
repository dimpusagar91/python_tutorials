"""
this is the documentation of the program itself
"""


fobj = open("demo.txt", "r")
for line in fobj:
    print (line)
fobj.close()
