import re

# Pre-compile the patterns
regexes = [ re.compile(p) for p in [ 'this','that'] ]
print(regexes)

