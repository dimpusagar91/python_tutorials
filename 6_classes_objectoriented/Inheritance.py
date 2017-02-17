#!/usr/bin/env python

class Person(object):
    def __init__(self,name):
        print("Calling person constructor")
        self.name = name

    def getDetails(self):
        print("Calling Person Details method")
        return self.name

class Student(Person):
    def __init__(self,name,branch,year):
        print("Calling student constructor")
        Person.__init__(self,name)
        self.branch = branch
        self.year = year

    def getDetails(self):
        print("Calling student constructor")
        return "%s studies %s and in %s year." %(self.name,self.branch,self.year)

class Teacher(Person):
    def __init__(self,name,papers):
        print("Calling teacher constructor")
        Person.__init__(self,name)
        self.papers = papers

    def getDetails(self):
        print("Calling Teacher Details method")
        return "%s teaches %s " % ( self.name ,','.join(self.papers))

person1 = Person('Tyler')
print(person1.getDetails())
student1 = Student('Ryan','computer science',2013)

#getDetails calls overridden method
print(student1.getDetails())
teacher1 =  Teacher('Giridhar',['C','C++'])

# getDetails calls overridden method
print(teacher1.getDetails())
