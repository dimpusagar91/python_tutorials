fobj = open("demo.txt", "r")
for line in fobj:
    print (line.rstrip())
fobj.close()
