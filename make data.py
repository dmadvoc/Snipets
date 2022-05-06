import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# The multi-dimensional array produces 2 rows
ar0=np.array([[1,2,3],['a','b','c'] ])
print('Two rows of data: '+'\n', ar0)

# This is how to create two colums
ar1=np.array([1,2,3])
ar2=np.array([4,5,6])
ar3=np.column_stack((ar1,ar2))
print('Two columns of data: '+'\n', ar3)

# Convert arry to DataFrame
df = pd.DataFrame(ar3, columns =['C1', 'C2'])
display(df)

# Add column to DataFrame and reorganize colums
# Array data can be np.array or a list
ar4=['x','y','z']
df['C3']=ar4
df = df.reindex(['C3','C2','C1'], axis=1)
print(df)
plt.scatter(ar1, ar2)

%whos
