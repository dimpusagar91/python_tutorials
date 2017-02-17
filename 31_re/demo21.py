import re

s = '100 BROAD' 
print (re.sub('ROAD', 'RD', s)) 
print (re.sub('\bBROAD$', 'RD.', s))             


#syntax
#=======
#re.sub(pattern,replacement,originalstr)
