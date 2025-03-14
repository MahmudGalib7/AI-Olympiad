import seaborn as sns
from numpy import random
from matplotlib import pyplot as plt
# Distribution

arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = [[1,2,3],[4,5,6]]
arr3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

sns.distplot(arr, hist=False)
plt.show()
