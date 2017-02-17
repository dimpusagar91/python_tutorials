x = set("A Python Tutorial")
print(x)

x = set(["Perl", "Python", "Java"])
print(x)

# set operations

# add

colours = {"red","green"}
colours.add("yellow")
print(colours)

# clear

cities = {"Stuttgart", "Konstanz", "Freiburg"}
cities.clear()
print(cities)

#copy

more_cities = {"Winterthur","Schaffhausen","St. Gallen"}
cities_backup = more_cities.copy()
more_cities.clear()
print(cities_backup)

