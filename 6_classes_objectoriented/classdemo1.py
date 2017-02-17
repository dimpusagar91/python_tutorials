class Robot:
    ''' document string example '''
    print("Executed directy")
    # self attribute contains the object 
    def SayHello(self,name):
        self.name =  name
        print("Hello " + self.name)
        

# creating object to a class
# Object initialization 
x = Robot()
y= Robot()
z = Robot()
x.SayHello("Perl" )
y.SayHello("Python")
z.SayHello("Ruby")
print("You are executing this module directly")

 
