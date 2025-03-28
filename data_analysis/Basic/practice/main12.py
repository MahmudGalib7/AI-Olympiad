import math
from math import log
import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

pd.options.display.max_rows = 1000

data = pd.read_csv('Dataset/data.csv')
# print(data)

loc = {
    "place" : {'0':"tokyo", '1': "dhaka", '2': "new york", '3': "chattogram"},
    "ratings": {'0': 9,'1': 8,'2': 7,'3': 5}
}
dic = pd.DataFrame(loc)
# print(dic)

# print(data.head(10))
# print(data.tail(10))

# print(data.info())

# print(data)

# new_data = data.dropna()
# print(new_data)

# x = data['Calories'].mean()
# x = data['Calories'].median()
# x = data['Calories'].mode()[0]
#
# new_data = data['Calories'].fillna(x)
# print(new_data)

dataset = pd.read_csv('Dataset/new_data.csv')

dataset['Date'] = pd.to_datetime(dataset['Date'], format='mixed')

dataset.dropna(inplace=True, subset=['Date'])

dataset.fillna(dataset['Calories'].mode()[0], inplace=True)

dataset.loc[7, 'Duration'] = dataset['Duration'].mode()[0]



for x in dataset.index:
    if dataset.loc[x, 'Duration'] > 55:
        dataset.drop(x, inplace=True)

print(dataset)