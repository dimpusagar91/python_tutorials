#number of lines of a file

filePath = "demo.txt"

lineCount =  len(open(filePath, 'r').readlines())
print("File %s has %d lines." % (filePath,lineCount))
