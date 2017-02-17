#!/usr/bin/python

# function definition is here
def func(str):
    # to print a passed string into function
    print(str)
    return

# Now you can call user defined function

# Required arguments -- will show error
# func()

func("Python programming")



# Default arguments
# Example program2  - default values to parameters
# Function definition is here

def func(subject, marks=100):
    # to print a passed string into function
    print("Subject Name : ", subject)
    print("Marks :", marks)
    return

# Now you can call user defined function

print("Example program2 - Using keyword arguments:\n")
func("Science",80)

func( marks=90, subject="Chemistry")
print("Use Default Value:\n")
func(subject="Mathematics")

#Variable length arguments
print("Example Program 3 - Variable length arguments:\n:)

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

