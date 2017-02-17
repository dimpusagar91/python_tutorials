import re

pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

print(re.search.__doc__)

print(match)

