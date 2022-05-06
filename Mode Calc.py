#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 06:39:56 2022

@author: davidadvocate
"""
######################################################
# Two methods: 1st find the mode from a Histogram
# 2nd method: find the maxima (mode) from a PDF
#####################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

######################################################
# Histogram Method
#####################################################
# Top 100 HC Fields USA, from IEA
oeb=[238050,99787,79080,47259,62046,29487,15833,19996,23703,27346,19587,11665,25793,18291,28766,25494,1187,8492,
   17587,19396,15880,12922,35280,8930,13801,24808,23832,5452,3782,7825,307,4912,11793,5335,13496,6424,4051,5498,
   4011,7106,23360,8186,14306,7277,3694,10242,2476,5755,6116,3519,4407,7229,8808,8294,3737,5115,3441,4930,2348,
   4820,8226,3925,4308,3223,2563,6730,7484,21206,3093,3586,5660,5044,10421,2032,3516,3187,2415,3464,5111,4024,4131,
   2733,3840,4010,8247,3378,1790,1937,2270,3319,2251,6151,3325,2326,2096]
koeb=np.array(oeb)

# Find the mode (ml) using a detailed histogram
n, bins, patches=plt.hist(koeb, bins=500, edgecolor='gray', density=True, alpha=.2)
# plt.close()
mode_index = n.argmax()
mode=(bins[mode_index] + bins[mode_index+1])/2
print('Mode: ', np.round(mode))
plt.hist(oeb)

######################################################
# PDF Method
#####################################################
# Find the mode value from a PDF
from scipy.stats import beta

amin = 25  # Set parameters for 2nd distribution
bml =  35  # Try making both populations symmetrical
cmax = 80 
L=10     # Lambda variable controls the variance of the distribution
size=100    # Try different sample sizes, default=30

# Set the shape parameters for the Beta distributions
a= 1 + L * (bml-amin) / (cmax-amin)
b= 1 + L * (cmax-bml) / (cmax-amin)

# by = beta.pdf(bx, a, b, loc=amin, scale=cmax-amin)

# Generate the random Beta values
bvals = beta.rvs(a, b, loc=amin, scale=cmax-amin, size=size, random_state=None)
x = np.linspace(np.min(bvals)-5, np.max(bvals)+5, 1000)
y = beta.pdf(x, a, b, loc=amin, scale=cmax-amin)
plt.plot(x,y)

# Find the X value for the KDE maxima
maxima = x[np.argmax([y])]
print('X value of Mode: ', np.round(maxima,3))

plt.plot(x,y, lw=3)
plt.scatter(maxima, np.max(y), s=250, c='r')

