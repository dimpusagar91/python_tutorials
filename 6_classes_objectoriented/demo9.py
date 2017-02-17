# using class variable
# All the instances can access the class variable
# class variable is defined inside the class, but outside of methods

class Employee:
   'Common base class for all employees'
   empCount = 0   # class object (or) class variable # this variable will be shared across all objects

   def __init__(self, name, salary):
      self.name = name          # instance objects
      self.salary = salary
      Employee.empCount += 1    # shared variable
 

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

if __name__ == "__main__":
    print (Employee.__doc__) 
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    emp1.displayEmployee()
    emp2.displayEmployee()
    print ("Total Employees %d" % Employee.empCount)
    
