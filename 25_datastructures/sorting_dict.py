numbers = {'first': 1, 'second': 2, 'third': 3, 'Fourth': 4}

# converting dictionary to list

lnum = list(numbers)

print(lnum)

# Sorting Python dictionaries by Keys

sorted_dict = sorted(numbers)

print(sorted_dict)

# Sorting Python dictionaries by Values

sort_values = sorted(numbers.values())
print(sort_values)


mydict = {'amit':40,
          'khan':2,
          'alen':1,
          'john':3}


# using collections

import collections
d = {2:3, 1:89, 4:5, 3:0}
od = collections.OrderedDict(sorted(d.items()))
print(od)


# using dict.items()
for k, v in d.items():
    print(k, v)

 











