import re

##finditer() returns an iterator that produces Match instances instead of the strings returned by findall().


text = 'I am pythonist in python programming world learning python language'

pattern = 'python'

for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print ('Found "%s" at %d:%d' % (text[s:e], s, e))
