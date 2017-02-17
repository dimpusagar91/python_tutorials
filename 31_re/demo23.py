import re

m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())                      # entire match

print(m.groups())

print(m.group(1))                     # subgroup 1

print(m.group(2))                     # subgroup 2

print(m.groups())                     # all subgroups

m = re.match('ab', 'ab')       # no subgroups
print(m.group())                      # entire match

print(m.groups())                     # all subgroups


m = re.match('(ab)', 'ab')     # one subgroup
print("Entire match",m.group())                      # entire match

print("1st group",m.group(1))                     # subgroup 1

print("All groups",m.groups())                     # all subgroups

m = re.match('(a)(b)', 'ab')   # two subgroups
print(m.group())                      # entire match
print(m.group(1))                     # subgroup 1
print(m.group(2))                     # subgroup 2
print(m.groups())                     # all subgroups

m = re.match('(a(b))', 'ab')         # two subgroups
print(m.group())                      # entire match

print(m.group(1))                     # subgroup 1
print(m.group(2))                     # subgroup 2
print(m.groups())                     # all subgroups
