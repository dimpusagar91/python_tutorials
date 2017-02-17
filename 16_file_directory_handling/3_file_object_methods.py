#!/usr/bin/python

print("\nExample program 1:\n")
#open a file
file = open("example.txt","a")
print("Name of the file :", file.name)

 

#fileno method returns the integer file descriptor
fileid = file.fileno()
print("File Descriptor :", fileid)

 

print("\nExample program 2 : \n")
file.write("Welcome to Python.\nHello world!\n")
sequence = ["This is 6th line\n","This is 7th line"]
#write lines at the end of the file
 
line = file.writelines(sequence)
file.write("again new line")
file.close()
 
 

file = open("example.txt","r")

# returns the next input line, or raises StopIteration when EOF is hit
for index in range(3):
    row = file.__next__()
    print("Line no %d - %s" %(index, row))

readLine = file.readline()
print("Read Line %s" %(readLine))


#number of bytes to be read from the file
readLine = file.readline(5)
print("Read 5 bytes : %s" %(readLine))
file.close()


file = open("example.txt","r")
readLines = file.readlines()
print("\nRead Lines : %s" %(readLines))

readLines = file.readlines(15)
print("\nRead Lines approximately 15 bytes : %s" %(readLines))


#current position of the file
position = file.tell()
print("Current Position: %d " % (position))


# set the pointer to the beginning
file.seek(0,0)
print("After setting the pointer to the beginning by using seek: ")
readLines = file.readlines(15)
print("Read Lines approximately 15 bytes : %s" %(readLines))

file.close()


 
