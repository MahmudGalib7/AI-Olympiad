import seaborn as sns
from numpy import random
from matplotlib import pyplot as plt
from numpy.random import poisson
from seaborn import histplot

# Distribution

# arr = [1,2,3,4,5,6,7,8,9,10]
# arr2 = [[1,2,3],[4,5,6]]
# arr3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

y = random.normal(loc=50,scale=5,size=1000)
# sns.histplot(y,color="blue")

# Binomial Distribution

x = random.binomial(10, 0.5, size=1000)
# sns.histplot(x, bins=10, kde=False, color="red")
#
# plt.title("Normal Distribution vs Binomial Distribution", fontsize=16)
# plt.xlabel("Number of success", fontsize=16)
# plt.ylabel("Probability", fontsize=16)

# plt.show()

# Poisson Distribution

z = random.poisson(lam=2, size=1000)
# sns.histplot(z, bins=10, kde=False, color="red")
# plt.show()

# Probability Distribution

a = random.uniform(1,100,size=(10,8))
# print(a)
# sns.histplot(a, bins=10, kde=False)
# plt.show()

# Logistic Distribution

b = random.logistic(loc=1, scale=2, size=1000)
# sns.histplot(b, bins=10, kde=False)
# plt.show()

# multinomial Distribution

c = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6], size=1000)
# sns.histplot(c, bins=10, kde=False)
# plt.show()

# Exponential Distribution

d = random.exponential(scale=2,size=1000)
# sns.distplot(d, hist=False, label="Exponential Distribution")
# plt.show()

# Chi-square Distribution

e = random.chisquare(df=1, size=1000)
# sns.distplot(e, hist=False, label="Chi-square distribution")
# plt.show()

# Rayleigh Distribution

f = random.rayleigh(size=1000)
# sns.distplot(f, hist=False, label="Rayleigh distribution")
#
# plt.show()

# Pareto Law Distribution

# g = random.pareto(a=2 ,size=1000)
# sns.distplot(g, hist=False, kde=False)
# plt.show()

# Zipf's Law

h = random.zipf(a=2, size=1000)
sns.distplot(h[h<15], hist=True, kde=False)
plt.show()
