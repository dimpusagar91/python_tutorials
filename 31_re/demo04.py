import re
mo = re.search("python", "I love python programming")
if mo:
    print(mo.group())
    print("Start and end",mo.span())
    print("Starting position",mo.start())
    print("Ending position", mo.end())
else:
    print("doesn't exist")
    
