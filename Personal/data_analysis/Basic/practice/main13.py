import math
from math import log
import numpy as np
from numpy import *
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt


pd.options.display.max_rows = 1000

data = pd.read_csv('Dataset/data.csv')
dataset = pd.read_csv('Dataset/new_data.csv')

# for i in data.index:
#     if data.loc[i, 'Duration'] > 45:
#         data.drop(i, inplace=True)

# print(data.drop_duplicates())


print(data.corr())

dataset['Date'] = pd.to_datetime(dataset['Date'], format='mixed')
print(dataset.corr())

