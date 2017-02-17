class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def SayHello(self):
        print("Hi, I'm " + self.name)


    def GetBuildYear(self):
        return str(self.build_year)

# __name__  ==  __main__  only if this program executed directly

if __name__ == "__main__":
    x = Robot("Python", 1991)
    y = Robot("Perl", 1987)
    for rob in [x, y]:
        rob.SayHello()
        print("I was built in the year " + rob.GetBuildYear() + "!")
