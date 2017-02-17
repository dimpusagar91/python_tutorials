#!/usr/bin/python

#import io module
import io

print("StringIO:")
f= open("myfile.txt","r",encoding="utf-8")
f=io.StringIO("some initial text data")
print("Get Value :", f.getvalue())
f.close()


import time
print("strftime with gmtime :", time.strftime("%a, %d %b %H:%M:%S", time.gmtime()))
print("strptime :", time.strptime("30 Nov 00", "%d %b %y"))
