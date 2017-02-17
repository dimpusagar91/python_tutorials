import re

fh = open("techinfo.txt")
for line in fh:
    if re.search("(python|perl|ruby)",line):
        print(line.rstrip())
fh.close()
