try:
    a = float(input('First number, please: '))
    b = float(input('Second number: '))
    print('Your result is ', a/b)
except ZeroDivisionError:
    print('Error: Division by zero will not work.')
except ValueError:
    print('Error: You used an incorrect data type.')
