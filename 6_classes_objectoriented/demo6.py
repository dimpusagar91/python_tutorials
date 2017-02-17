class Robot:

    def __init__(self, name):
        self.name = name

    def SayHello(self):
        print("Hello, I'm " + self.name)

    def SetName(self, name):
        self.name = name
        print(self.name)
        self.name = "I am in love with Python"
        print(self.name)
        


if __name__ == "__main__":
    x = Robot("Python")
    x.SayHello()
    x.SetName("Python programming")


    y = Robot("Perl")
    y.SayHello()
    y.SetName("perl programming")




    
