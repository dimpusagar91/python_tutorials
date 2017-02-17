#!/usr/bin/python
import re

line = "perl";
## Cat (or) Catss (or) Catssss (or) Cats
searchObj = re.search( '^perl$', line,re.I)
if searchObj:
   print ("search --> searchObj.group() : ", searchObj.group())
else:
   print ("Nothing found!!")
