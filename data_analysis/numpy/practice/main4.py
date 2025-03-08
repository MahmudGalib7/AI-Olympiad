# n = int(input("Enter the number of element: "))
# l = []
#
# for i in range(n):
#     x = int(input("Enter an element: "))
#     if x not in l:
#         l.append(x)
#
# print(list(set(l)))

# x = {2,4,6,8,10}
# y = {1,2,3,4,5}
# z = {1,3,5,6,7}

# x.intersection_update(y)
# print(x)
#
# union_x_y_z = x.union(y,z)
# intersection_x_y = x.intersection(y)
# print(union_x_y_z)
# print(intersection_x_y)

set1 = {"a","b","c"}
set2 = {"c","d","e"}

# set3 = set1 - set2
# set3 = set1.difference(set2)
# set3 = set1.symmetric_difference(set2)
set1.symmetric_difference_update(set2)
print(set1)