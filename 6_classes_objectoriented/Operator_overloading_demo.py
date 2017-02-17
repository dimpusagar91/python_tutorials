#!/usr/bin/env python
# Operator Overloading

class Marks:
    def __init__(self,marks,subject):
        print("Inside constructor ( __init__) ")
        self.marks = marks
        self.subject = subject

    def __str__(self):
        print("Inside constructor (  __str__) ")
        return 'Total marks %d obtained in %s ' %(self.marks,self.subject)

    def __add__(self,other):
        print("Inside constructor ( __add__) ")
        return Marks(self.marks + other.marks,self.subject + ',' +  other.subject)



m1 = Marks(80,"Maths")
m2 = Marks(85,"Science")
m3 = Marks(75,"English")
m4 = Marks(83,"French")
m5 = Marks(82,"Geography")

print( m1 + m2 + m3 + m4 + m5 )

# Data hiding

class Person(object):
    __secretCount = 0
    def getDetails(self):
        print("Calling person details method")
        self.__secretCount +=1
        print(self._Person__secretCount)

person1 = Person()
person1.getDetails()
person1.getDetails()
person1.getDetails()
person1.getDetails()
person1.getDetails()
person1.getDetails()
    

