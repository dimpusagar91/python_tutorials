#!/usr/bin/python

# the list is having values within the specific range 1 to 100
print(list(range(1,100)))

# sets in python
# A set is an unordered collection with no duplicate elements
basket = {'apple','orange','apple','pear','orange','banana'}

#to print the complete set
print("set :", basket )

# fast membership testing
print("'orange' in basket : ", 'orange' in basket )
print("'crabgrass' in basket : ", 'crabgrass' in basket )

# dictionaries in python

#create a dictionary
dic = {"IBM":630.34,"INTEL":123.12}

#print the dictionary
print("dic :" , dic)

# to append another value with key as 'CISCO'
dic['CISCO'] =456.45

# print the dictionary
print("dic :", dic)

#print  the specific value for the key IBM
print("dic['IBM'] : ", dic['IBM'])

# to delete the 'INTEL' key and value pair from dictionary
del dic['INTEL']

# check the dictionary
print("dic : ", dic)

# to find the key in the dictioary
print("'IBM' in dic :", "IBM" in dic )

#check the 'key' is not in the dictionary
print("'CISCO' not in dic :", 'CISCO' not in dic )


      
