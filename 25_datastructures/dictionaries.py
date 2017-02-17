my_dict={
'a':{'b':10,'c':20},
'd':{'b':30,'c':40}
}
 
print(my_dict)

print(my_dict['a'])
#print(my_dict['b'])
print(my_dict['d'])

print (my_dict['a']['b'] ) #10
print (my_dict['a']['c'] ) # 20
print (my_dict['d']['c'] ) # 40
print (my_dict['d']['b'] ) #30
 

dictA = {"one": 1, "two": 2, "three": 3 }
dictB = {"England": "EN", "Poland": "PL" }
cookieMonster = {"Numbers": dictA}
print(cookieMonster)
cookieMonster.update({"Languages": dictB})
print(cookieMonster)
#print("The Poland language code is %s; England: %s" % (cookieMonster['Languages']['Poland'], cookieMonster['Languages']['England']) )
 









