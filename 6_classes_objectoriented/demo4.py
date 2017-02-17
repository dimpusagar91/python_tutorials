class Robot:

    def SayHello(self):
        print("Hello, I'm " + self.name)

    def SetName(self, name):
         self.name = name
#        print(name)

if __name__ == "__main__": 
    x = Robot()
    x.SetName("Python")
    x.SayHello()
