# Precision handling of numbers
import math
a=1.5555555555
print('value; ', a)
print('trunc: ', math.trunc(a))
print('ceil:  ', math.ceil(a))
print('floor: ', math.floor(a))

# Format the number to 2 decimal places
print ('using % :    ', '%.2f'%a) 
print ('using fromat:', "{0:.2f}".format(a)) 

# roundingnnumbers using Pythons built-in round functions
print('round to a specified number of decimals:')
print('round the number: ', a)
print('round to 0 decimals: ', round(a))     
print('round to 1 decimals: ', round(a, 1))  
print('round to 2 decimals: ', round(a, 2)) 

# How to round to nearest whole number
b = 55.555  
print('round the value: ', b) 
print('round to the nearest 1:    ',  round(b, 0))
print('round to the nearest 10:   ',  round(b, -1))
print('round to the nearest 100:  ',  round(b, -2))
print('round to the nearest 1000: ',  round(b, -3))
