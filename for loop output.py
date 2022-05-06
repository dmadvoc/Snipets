# For Loop
mylist=[2 ,3, 4, 5]
out= []
for i in mylist:
    value=i *10
    out.append(value)
print(out)   

# elif for a single value
temp = 8 
if temp < 4:
    desc = 'cold'
elif temp < 7:
    desc = 'warm'
elif temp < 9:
    desc = 'hot'
else:
    desc='boiling'
print(temp, desc)

# elif looping through an array
import numpy as np    
temp =  np.arange(1, 11, 1)
out=[]
for i in temp:
    if i < 4:
        desc='cold'
    elif i < 7:
        desc='warm'
    elif i < 9:
        desc='hot'
    else:
        desc='boiling'
    out.append([i, desc])
print(out)