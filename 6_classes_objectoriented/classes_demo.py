#!/usr/bin/python

print("\n Example Program -1 : Classes and Instances\n")
class Student:
    'Common base class for all student'
    studentCount = 0
    def __init__(self,name,fee,age):
        self.name = name
        self.fee = fee
        self.age = age
        Student.studentCount += 1

    def displayCount(self):
        print("Total Students %d" % Student.studentCount )

    def displayStudent(self):
        print("Name : ", self.name , ", Fee : ", self.fee)

    def displayAge(self):
        print("Name : ", self.name , ",Age: ", self.age )

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed")


student1 = Student("Ebby",2500,17)
student1.displayStudent()
student1.displayAge()

print("\n Example Program -2 : Accessing attributes\n")
print("hasattb: ", hasattr(student1,'age')) # returns true if 'age' attribute exists
print("getattb: ", getattr(student1,'age')) # returns value of you can add, rem
print("setattb: ", setattr(student1,'age',19)) # set attribute 'age' to 19
print("getattr after setattr with new value: ", getattr(student1, 'age'))

print("\n Example Program -3 : Built-in class attributes\n")
print("Student.__doc__:",Student.__doc__)
print("Student.__name__:",Student.__name__)
print("Student.__module__ :",Student.__module__)
print("Student.__bases__ :", Student.__bases__)
print("Student.__dict__ :", Student.__dict__)

print("Total students %d " % Student.studentCount)

print("\n Example Program -4 : Destroying objects(Garbage collection) \n")
print("Object id :", id(student1))

del student1

# You can add, remove or modify attributes of classes and objects at any time
# student1 = Student("Giri",2500,17)
# student1.department = "Computer science"  # Add a depatment attribute
# student1.department = "Chemistry"         # Modify department attribute
# del student1.department                   # Delete department attribute
