#!/usr/bin/python


def countdown(n):
    while n > 0:
        yield "Countdown number : %d\n" %n
        n -=1
    yield "Good Bye!\n"

print("\nExample - Yield\n")
# Open a file
file = open("example.txt","w")

count = countdown(5)
file.writelines(count)

file.close()

print("\nExample - File read\n")
file = open("example.txt","r")
# read the file
for line in file:
      print(line,end= '')
file.close()      
