import re

fh = open("techinfo.txt")
for line in fh:
    if re.search("python|perl",line):
        print(re.group())
fh.close()
