## read in on go
## reading all the lines at a time
fobj = open("demo.txt","r")
output = fobj.read()
print(output)
print("Object type :", type(output))
fobj.close()

     
