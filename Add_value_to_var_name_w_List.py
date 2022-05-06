# Add a number to a variable name
import numpy as np
out=[]
list=np.arange(5, 30, 5)
for i in list:
    Flat_Divisor= i
    globals()["var_"+str(i)]=1+Flat_Divisor
    print('var_'+str(i) , '=', 1+i)
    out.append(globals()["var_"+str(i)]) 
    
print('The out.append function writes out an array:' + '\n', out)
