#!/usr/bin/python

print("\nExample program\n")

# to create a compressed GZIP file
import gzip
data = b"welcome to python programming"
with gzip.open('example.txt.gz','wb') as file:
      file.write(data)

file.close()

# to read a compressed file
with gzip.open('example.txt.gz','rb') as file:
      filecontent = file.read()
      print("File content : ", filecontent)
file.close()


# to GZIP compress an existing file
with open('example.txt','rb') as filein:
      with gzip.open('example.txt.gz','wb') as fileout:
          fileout.writelines(filein)

filein.close()
filein.close()

# to GZIP compress a binary string

inputString = b"Lots of content here"
outputString = gzip.compress(inputString)
print(" Input :", inputString)
print(" Output:", outputString)

    
      
      
