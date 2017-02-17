#!/usr/bin/python

# import zlib module
import zlib
s = b'For applications that require data compression, the functions in this module allow compression and decompression,'
print("String :",s)
print("Length :", len(s))

t = zlib.compress(s)
 
print("length after compress : ", len(t))

print("String after decompress : ", zlib.decompress(t))

 

print("------------------------------------")

