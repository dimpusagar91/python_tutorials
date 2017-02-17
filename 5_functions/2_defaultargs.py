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
