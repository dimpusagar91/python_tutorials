#Variable length arguments
print("Example Program 3 - Variable length arguments:\n:")

# Function definition is here
def func(arg,*vartuple):
    # to print a passed string into function
    print("Output is: ")
    print(arg)
    for var in vartuple:
        print(var)
    return


# Now you can call user defined function
func(100)
func(70,80,90)
