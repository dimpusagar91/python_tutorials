# Python Program to convert temperature in celsius to fahrenheit 
# Input is provided by the user in degree celsius

# take input from the user
celsius = float(input('Enter degree Celsius: '))

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))
