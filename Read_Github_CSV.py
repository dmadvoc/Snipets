#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 15:28:16 2022

@author: davidadvocate
"""
# See article below:
# https://medium.com/towards-entrepreneurship/importing-a-csv-file-from-github-in-a-jupyter-notebook-e2c28e7e74a5

import pandas as pd
import requests
import io
    
# Downloading the csv file from your GitHub account
# To get the url, click on the CSV file in your Github site,
# then click the raw button. Copy the like below:

url = "https://raw.githubusercontent.com/dmadvoc/PDFs/main/Test_Data.csv" # Make sure the url is the raw version of the file on GitHub
download = requests.get(url).content

# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# Printing out the first 5 rows of the dataframe

print (df.head())

