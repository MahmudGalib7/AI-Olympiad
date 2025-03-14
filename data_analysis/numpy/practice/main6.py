import seaborn as sns
from numpy import random
from matplotlib import pyplot as plt

x = random.randint(1,100) # takes a random number from the value of low-high
# print(x)

y = random.rand()
# print(y) # provides the value from 0-1

x_1 = random.randint(100, size=(3,5,2)) # size can create 1-d,2-d,3-d array's based on the values of each parameter
# print(x_1)

x_2 = random.rand(2,5) # creates array's with the values from 0-1
# print(x_2)

x_3 = random.choice([1,2,3,4,5], size=(3,5)) # takes a random index & creates a array based on the size
# print(x_3)

x_4 = random.random_sample((2,5)) # returns float from 0-1 in the size of the array's index provided
# print(x_4)

x_5 = random.binomial(12, 0.5) # idk what its doing!
# print(x_5)

x_6 = random.bytes(10) # this thing Returns random bytes
# print(x_6)

x_7 = random.ranf() # same as rand()
# print(x_7)

# x_8 = random.random_integers(1, 1991) # gets a value of random int, but radiant is more recommendable
# print(x_8)

x_9 = random.choice([1,2,3,4,5], p=[0.0,0.1,0.2,0.3,0.4], size=(5,5))
# print(x_9)

x_10 = [1,6,7,8,9,10]
random.shuffle(x_10) # shuffle changes the original array, so we don't need an alternative one
# print(x_10)

random.permutation(x_10) # permutation doesn't change the original array, so we need an alternative one
# print(x_10)

arr = [1,2,3,4,5,6,7,8,9,10]
arr2 = [[1,2,3],[4,5,6]]
arr3 = [[[1,2],[3,4]],[[5,6],[7,8]]]

sns.distplot(arr, hist=False)
plt.show()