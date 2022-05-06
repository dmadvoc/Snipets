# Generate and sample random numbers and arrays

import random
import numpy as np
import matplotlib.pyplot as plt

# Samples n integrs within the selected range
print("Print two random numbers between 10 & 30", "\n", random.sample(range(10, 30), 2))

# Create a random float value between a range
print("Print a float between 0 to 10", "\n",random.uniform(0, 10))

# Randomly sample float numbers between 0 and 1
# The seed forces the same random value in successive trials
random.seed(5)
print("Print a random value beween 0 to 1 using a seed", "\n",random.random())

# Randomly sample from a list using "choice"
# Can be integers, floats or strings
list_int=[1,2,3,4,5,6,7,8,9,10]
list_flt=[1.2,1.2,1.3,1.4,1.5]
string='David Advocate'
print(random.choice(list_int))
print(random.choice(list_flt))
print(random.choice(string))

#Generate array of random uniform float values
print(np.random.uniform(low=0, high=10, size=(20)))

# Test to see if randint honors min and max values
# THE HIGH IS INDEXED, IE. N-1
ints = np.random.randint(low = 0,high=11,size=100000)
print(np.min(ints), np.max(ints))

#Generate array of random uniform float values
print(np.random.uniform(low=0, high=10, size=(5)))

# np.random.normal(mu, sigma, size)
np.random.seed(seed=10)
norm=np.random.normal(0,1,10000)
print(np.mean(norm))
plt.hist(norm, bins=30)
plt.show()




