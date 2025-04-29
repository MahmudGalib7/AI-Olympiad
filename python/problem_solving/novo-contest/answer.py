"""Problem 1"""

# def solveMeFirst(a,b):
# 	return a + b


# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)


"""Problem 2"""
# number = int(input())
# number_english = {
#     1: 'one',
#     2: 'two',
#     3: 'three',
#     4: 'four',
#     5: 'five',
#     6: 'six',
#     7: 'seven',
#     8: 'eight',
#     9: 'nine',
# }

# if number in number_english:
#     print(number_english.get(number))
# else:
#     print("Greater than 9")

"""Problem 2 Alt"""

# n = int(input())
# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and n in range(2,6):
#     print("Not Weird")
# elif n % 2 == 0 and n in range(6,21):
#     print("Weird")
# else:
#     print("Not Weird")

"""Problem 3"""
# n = int(input())
# arr = list(map(int, input().split()))
# print(sum(arr))

"""Problem 4"""

# t = int(input())
# for i in range(t):
#     a = input()
#     def calculate_similarity(s):
#         total_similarity = 0
#         z = [0] * len(s)
#         l, r, k = 0, 0, 0
#         for i in range(1, len(s)):
#             if i > r:
#                 l, r = i, i
#                 while r < len(s) and s[r] == s[r - l]:
#                     r += 1
#                 z[i] = r - l
#                 r -= 1
#             else:
#                 k = i - l
#                 if z[k] < r - i + 1:
#                     z[i] = z[k]
#                 else:
#                     l = i
#                     while r < len(s) and s[r] == s[r - l]:
#                         r += 1
#                     z[i] = r - l
#                     r -= 1
#         total_similarity = len(s) + sum(z)
#         return total_similarity

#     print(calculate_similarity(a))

"""problem 5"""

#tree related problem
"""
add = (a1+z*d1) * (a2+z*d2) * r^z
"""

n ,r = map(int, input().split())
for i in range(n):
    x, y = map(int, input().split())

u, q = map(int, input().split())    
updated_node = list(map(int, input().split()))
for i in range(q):
    i, j = map(int, input().split())