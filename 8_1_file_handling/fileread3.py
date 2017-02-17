fobj = open("employyyyyee.log","r")
mylist = fobj.readlines()

print("Object type :",type(mylist))
#print(mylist)
for element in mylist:
    print(element.rstrip())

fobj.close()
