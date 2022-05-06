# array 2 Data frame
import pandas as pd
import numpy as np
a=np.array([[1,2,3], [4,5,6]])
           
Divisor=np.array([0.5, 0.75])

df = pd.DataFrame(a, columns =['C1', 'C2', 'C3'])

df['Divisor']=Divisor
df = df.reindex(['Divisor','C1','C2','C3'], axis=1)
display(df)