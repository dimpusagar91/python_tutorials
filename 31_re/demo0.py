import re
line = "I love ruby programmings"
x = re.search("(python|ruby|unix)",line)
if x :
    print("pattern exists in the string")
else:
    print("pattern doesn't exist")



