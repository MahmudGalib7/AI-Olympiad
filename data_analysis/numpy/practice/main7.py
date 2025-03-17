import seaborn as sns
from numpy import random
from matplotlib import pyplot as plt
from numpy.random import poisson
from seaborn import histplot

# Distribution

# arr = [1,2,3,4,5,6,7,8,9,10]
# arr2 = [[1,2,3],[4,5,6]]
# arr3 = [[[1,2],[3,4]],[[5,6],[7,8]]]
#
# y = random.normal(loc=50,scale=5,size=1000)
# sns.histplot(y,color="blue")

# Binomial Distribution

# x = random.binomial(10, 0.5, size=1000)
# sns.histplot(x, bins=10, kde=False, color="red")
#
# plt.title("Normal Distribution vs Binomial Distribution", fontsize=16)
# plt.xlabel("Number of success", fontsize=16)
# plt.ylabel("Probability", fontsize=16)

# plt.show()

# Poisson Distribution

# z = random.poisson(lam=2, size=1000)
# sns.histplot(z, bins=10, kde=False, color="red")
# plt.show()

# Probability Distribution

# a = random.uniform(1,100,size=(10,8))
# print(a)
# sns.histplot(a, bins=10, kde=False)
# plt.show()