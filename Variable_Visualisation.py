# -*- coding: utf-8 -*-
"""Untitled65.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kvkjknGx16WNUbiRXgEJVzMVVwpf2ckM

**Importing the Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""Dataset is about population of countries each year from 1960 to 2022

**Importing the dataset**
"""

dataset=pd.read_csv('visualisation_dataset.csv')

"""**Creating a new variable 'Total Population' to plot the population factor in graph**"""

columns_to_exclude=['Country Name','Country Code','Indicator Name','Indicator Code']
new_row = dataset[dataset.columns.difference(columns_to_exclude)].cumsum().iloc[-1]
dataset = dataset.append(new_row, ignore_index=True)

print(dataset)

"""**Plot of Total Population of all countries year wise**"""

plt.figure(figsize=(12, 6))
plt.plot(dataset.iloc[-1,4::10],marker='o')
plt.title('Total population - year wise plot')

"""Insights : The population appears to exhibit exponential growth as it progresses through the years.

**Creating a new feature Average Population of a country from 1960 to 2022**
"""

dataset['Average Population']=np.mean(dataset.iloc[:,4:6],axis=1)

"""**Sort it in terms of average population**"""

dataset = dataset.sort_values(by='Average Population', ascending=False)

"""**Plotting the top 5 countries with higher average population**"""

plt.figure(figsize=(10, 6))
plt.plot(dataset.iloc[1:6,0],dataset.iloc[1:6,-1],marker='o')
plt.title('Plot of top 5 countries with high average population')