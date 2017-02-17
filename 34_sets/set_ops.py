
# set is the function used to convert   any object into set object
x = set("A Python Tutorial")
print(x)

 
x = set(["Perl", "Python", "Java"])
print(x)



cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print(cities)


# adding element to list
cities = set(["Frankfurt", "Basel","Freiburg"])
cities.add("Strasbourg")

print(cities)






#frozensets
cities = frozenset(["Frankfurt", "Basel","Freiburg"])
#cities.add("Strasbourg")





# Other way of defining the set
#We can define sets (since Python2.6) without using the built-in set function.
#We can use curly braces instead:


 
adjectives = {"cheap","expensive","inexpensive","economical"}
print(adjectives)



# set operations
# add operation
colours = {"red","green"}
colours.add("yellow")
print(colours)




# clear
more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()

print(more_cities)


 

#difference()
x = {"a","b","c","d","e"}
y = {"b","c"}
z = {"c","d"}
print("Difference :",x.difference(y))
print("Difference :",x-y)

print("Difference :",x.difference(y).difference(z))
print("Difference :",x-y-z )

 
#Instead of using the method difference, we can use the operator "-":
print(x-y)
print(x - y - z)


#The method difference_update removes all elements of another set from this set.
#x.difference_update() is the same as "x = x - y"

x = {"a","b","c","d","e"}

y = {"b","c"}
x.difference_update(y)
print("Elements of x",x)
x = {"a","b","c","d","e"}
y = {"b","c"}
x = x - y
print("After difference update",x)

 

#discard(el)
#An element el will be removed from the set, if it is contained in the set.
#If el is not a member of the set, nothing will be done.

x = {"a","b","c","d","e"}
x.discard("a")
print("Discard example:",x)
x.discard("z")
print(x)



#remove(el)
#works like discard(), but if el is not a member of the set,
#a KeyError will be raised.


x = {"a","b","c","d","e"}
#x.remove("q")
print("Remove example:",x)
x.remove("b")
print("After removing B ", x)

 

#intersection(s)
#Returns the intersection of the instance set and the set s as a new set.
#In other words: A set with all the elements which are contained
#in both sets is returned.

x = {"a","b","c","d","e"}
y = {"c","d","e","f","g"}
x = { "c","d","e" ,"d"}
print("Intersection example:",x.intersection(y))
print("Intersection example:",x.intersection(y).intersection(z))

 
#pop()
x = {"a","b","c","d","e","q"}
print("Pop example",x.pop())
print("Pop example",x.pop())
print("Pop example",x.pop())
print("Pop example",x.pop())
print("Pop example",x.pop())

print(x)

 
#issubset()
x = {"a","b","c","d","e"}
y = {"c","d"}
print(x.issubset(y))   # false
print(y.issubset(x))   # true

    
 
''' 
