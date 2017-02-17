import re
fobj = open("client_info.txt","r")

for line in fobj:
    if re.search("^perl",line.rstrip()):
        print(line.rstrip())
fobj.close()
