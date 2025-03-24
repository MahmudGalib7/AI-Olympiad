import seaborn as sns
from numpy import random
from matplotlib import pyplot as plt

# Normal Distribution

normal = random.normal(loc=4,scale=2,size=1000) # loc -> highest value in the graph, scale -> determines how flat the graph distribution should be, size -> the size of the variable
sns.distplot(normal, hist=False)
# plt.show()

# Binomial Distribution

