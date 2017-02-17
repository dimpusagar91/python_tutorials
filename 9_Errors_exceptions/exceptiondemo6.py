 
#let's keep the program running after an exception
# infinite loop

while True:  
    try:
        a = float(input('First number, please: '))
        b = float(input('Second number: '))
        print('Your result is ', a/b)
    except :
        print('Invalid input. Please retry.')
    else:
        break

print("Outside the loop")
 
