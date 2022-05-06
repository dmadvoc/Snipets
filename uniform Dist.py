#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:52:12 2022

@author: davidadvocate
"""
# Good Reference: https://www.alphacodingskills.com/scipy/scipy-uniform-distribution.php
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform

# Input random values ranging from umin to umax
umin=5
umax=30

#np.random.seed(10)

#creating bin - ranging above and below will give the pdf a better shape
ux = np.arange(umin-100,umax+100,1) 
uvals1 = uniform.rvs(umin, umax, 10000) #uniformly distributed random numbers
uy = uniform.pdf(ux, umin, umax) # Create the PDF

uvals2 = uniform.rvs(umin, umax, 10000)
uvals3 = uniform.rvs(umin, umax, 10000)
uvals=uvals1*uvals2*uvals3
print("min, max, mean:", round(np.min(uvals),1), round(np.max(uvals),1), round(np.mean(uvals),1))


fig,ax = plt.subplots()
ax.plot(ux, uy, c='r', lw=3)
ax2=ax.twinx()
ax2.hist(uvals, bins=30, edgecolor='blue', alpha=.3) 
#plt.xlim(umin-5,umax+10)
plt.show()