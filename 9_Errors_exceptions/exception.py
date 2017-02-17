'''
#But what about division by zero?
a = int(input('First number, please: '))
b = int(input('Second number: '))
print('Your result is ', a/b)
'''

'''
#Let's do a simple try-except block.
try:
    a = int(input('First number, please: '))
    b = int(input('Second number: '))
    print('Your result is ', a/b)
except ZeroDivisionError:
    print('Error: Division by zero will not work.')
'''

'''
# multi-exception handler
try:
    a = float(input('First number, please: '))
    b = float(input('Second number: '))
    print('Your result is ', a/b)
except ZeroDivisionError:
    print('Error: Division by zero will not work.')
except ValueError:
    print('Error: You used an incorrect data type.')
'''

'''
#catching multiple exceptions at once
try:
    a = float(input('First number, please: '))
    b = float(input('Second number: '))
    print('Your result is ', a/b)
except (ZeroDivisionError, ValueError, TypeError): #tuple
    print('Error: Invalid input provided.')
'''

'''
#print more dynamic exception message text
try:
    a = float(input('First number, please: '))
    b = float(input('Second number: '))
    print('Your result is ', a/b)
except (ZeroDivisionError, ValueError, TypeError) as e:
    print('Error: ', e)
'''

'''
#let's keep the program running after an exception
while True: #remember that break/continue req. a loop
    try:
        a = float(input('First number, please: '))
        b = float(input('Second number: '))
        print('Your result is ', a/b)
    except:
        print('Invalid input. Please retry.')
    else:
        break
'''

#Using finally to clean up after an exception


'''
def divlog(x, y):
    try:
        f = open('C:/files/divlog.txt', 'a')
        f.write('{0:g} / {1:g} = {2:g}\n'.format(x, y, (x/y)))
    except ZeroDivisionError:
        f.write('Error: Zero division not allowed\n')
        raise
    finally:
        f.close()
'''


