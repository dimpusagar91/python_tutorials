import re

text = 'I am pythonist in python programming world learning python language'

pattern = 'python'
count = 0
for match in re.findall(pattern, text):
    count = count + 1

print(pattern, "exists for", count)    
