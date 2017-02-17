

newdict = {"US":"Washington","Canada":"Ottawa" }
#print(newdict)

for i in newdict:
    print("{country}:{capital}".format(country=i,capital =newdict[i]))
    
