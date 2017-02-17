class A:
    
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"
        print(self.__priv)        


# public    : all the members defined with public can be accessible
#             anywhere in the program
# private   : member defined with private(__) can be accessible only
#             inside the class
# protected : any member defined with protected(_) can be accessed
#             in other classes as well


obj = A()

print(obj.pub)
print(obj._prot)
print(obj.__priv)
