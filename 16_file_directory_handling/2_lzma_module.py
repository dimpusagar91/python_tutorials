#!/usr/bin/python

print("\nExample program: \n")

#Creating a compressed file
import lzma
data = b"Welcome to Python"
with lzma.open("example.xz", "w") as file:
    file.write(data)
file.close()


# reading in a compressed file
with lzma.open("example.xz") as file:
    filecontent = file.read()
    print("\nContent in the file : ", filecontent)
file.close()    


# compressing data in memory
data_in = b"welcome to python"
data_out = lzma.compress(data_in)
print("\nbefore compress :", data_in)
print("\nafter compress :", data_out)

#incremental compression
lzcompression = lzma.LZMACompressor()
out1 =  lzcompression.compress(b"Some data\n")
out2 = lzcompression.compress(b"Another piece of data\n")
out3 = lzcompression.compress(b"Even more data\n")
out4 = lzcompression.flush()

# concatenate all the partial results
result = b"".join([out1,out2,out3,out4])
print("\nresults:", result)

data = b"This data will be compressed\n"

#writing compressed data to an already-open file
with open("example.xz","wb") as file:
    with lzma.open(file,"w") as lzfile:
        lzfile.write(data)

