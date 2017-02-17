#!/usr/bin/python

#The finally clause is executed in any event
print("\nExample program 1\n")
def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is :", result)
    finally:
        print("executing finally clause")



#The TypeError raised by dividing two strings is not handled by the except clause
#therefore re-raised after the finally clause has been executed.
#In real world applications, the finally clause is useful for releasing exter
#regardless of whether the use of the  resource was successful

divide(6,2)
divide(2,0)

print("\nExample program 2\n")
#Clean up Actions

#The try statement has another optional clause which is intended
# to define clean up actions that must be executed under all circumstances.


try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
    
