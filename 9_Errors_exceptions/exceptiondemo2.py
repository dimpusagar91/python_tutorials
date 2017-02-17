

try:
    a = int(input('First number, please: '))
    b = int(input('Second number: '))
    print('Your result is ', a/b)
except ZeroDivisionError:
    print('Error: Division by zero will not work.')
except ValueError:
    print('Error: Incorrect value given')
except IOError:
    print('Error:  Input output error occured')
else:
    print("got executed finally")    
finally:
    print("At last") 
