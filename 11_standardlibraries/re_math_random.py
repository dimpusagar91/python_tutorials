#!/usr/bin/python

# import re module
import re
print("find all : ", re.findall(r'\bf[a-z]*','which foot or hand fell fastest'))

print("sub string: ", re.sub(r'(\b[a-z]+) \1',r'\1','cat in the hat'))

print("replace: ", 'tea for too'.replace('too','two'))



# import math module
import math
print("Cos of pi/4  :", math.cos(math.pi/4))
print("Log of 1024  :", math.log(1024,2))



# import random module
import random
print("Random choice first: ",random.choice(['one','two','three','four','five','six','seven']))
print("Random choice second: ", random.choice(['one','two','three','four','five','six','seven']))
print("Sampling without replacement: ", random.sample(range(100),10))
print("Random float with random() : ", random.random())
print("Random integer chosen from range(4) :", random.randrange(4))
print("Random choice third: ", random.choice(['one','two','three','four','five','six','seven']))
