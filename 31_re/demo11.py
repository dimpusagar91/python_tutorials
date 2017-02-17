#!/usr/bin/python
import re

phone = "2004-959-559 # This is Phone Number"

print("Phone Num : ", phone)

# Delete Python-style comments
phone = re.sub('Number', "new number", phone)
print("Phone Num : ", phone)

