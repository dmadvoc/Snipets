#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:45:59 2022

@author: davidadvocate
"""
import pandas as pd
import numpy as np

# Create some data (Note that 2021-08-03 is duplicated)
#dates = ['2021-08-01', '2021-08-02', '2021-08-03','2021-08-03']
dates = ['2021/08/01', '2021/08/02', '2021/08/03','2021/08/03']
df = pd.DataFrame({'StartDate': dates})
#df.info()

# Convert Dates from an object to a datetime
df['StartDate'] = pd.to_datetime(df['StartDate'])
#df.info()

# Extact Year, Month, Day
df['yyyy'] = pd.to_datetime(df['StartDate']).dt.year
df['mm'] = pd.to_datetime(df['StartDate']).dt.month
df['dd'] = pd.to_datetime(df['StartDate']).dt.day
print('This is the data')
print(df , '\n')

#Extract the first occurrence of StartDate
gb = df.groupby(['StartDate', 'yyyy', 'mm', 'dd'])['StartDate'].first()
print(gb)

pd.DataFrame({'x' : df.groupby(['StartDate', 'yyyy', 'mm', 'dd'])['StartDate'].first()}).reset_index()

