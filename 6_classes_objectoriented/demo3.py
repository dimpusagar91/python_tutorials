class Robot:

    def SayHello(self):
        print("Hello, I'm " + self.name)

    def SetName(self, name):
        self.name = name


if __name__ == "__main__":
    x = Robot()
    x.SetName("Marvin")
    x.SayHello()
