import re

pattern = 'python'
text = 'There are many languages in which Python is the best'

if re.search(pattern,  text, re.I):
    print('found a match!')
else:
    print('I am sorry')
