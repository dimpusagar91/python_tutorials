#!/usr/bin/python

print("\nExample program :\n")

# to import tempfile module
import tempfile

#create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Helo world!')

# read data from file
fp.seek(0)
info = fp.read()
print("Reading from file : ", info)
#close the file, it will be removed
fp.close()



# create a temporary file using a context manager

with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    print("reading: ",fp.read())



# file is now closed and removed
# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('Created temporary directory: ', tmpdirname)

#get temporary directory

print("get temporary directory:", tempfile.gettempdir())

