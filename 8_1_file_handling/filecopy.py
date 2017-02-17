
# file copy
fobj_in = open("demo.txt","r")
fobj_out = open("democopy.txt","w")
i = 1
for line in fobj_in:
    print(line.rstrip())
    if line.find("python"):
        fobj_out.write(str(i) + ": " + line)
    i = i + 1
fobj_in.close()
fobj_out.close()

