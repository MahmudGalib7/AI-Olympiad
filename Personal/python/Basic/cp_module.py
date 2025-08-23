import sys
from collections import deque, defaultdict, Counter

size_int = sys.getsizeof(int(12))
size_float = sys.getsizeof(float(12.01234))
size_str = sys.getsizeof(str("h"))

a = [1, 2, 3, 4, 5]
size_list = sys.getsizeof(a)

total_size = size_list + sum(sys.getsizeof(i) for i in a)

# print(size_int, size_float, size_str, size_list)
# print(total_size)

x = [i for i in range(1000)]
y = tuple(i for i in range(1000))
z = set(i for i in range(1000))
a = 10000 ^ 100000000000
b = 12389257259450948350438509438268.5435348593453495834905830495
c = "hello" * 1000
d = {i: i for i in range(1000)}


def size_of(obj):
    if isinstance(obj, dict):
        return sys.getsizeof(obj) + sum(sys.getsizeof(k) + sys.getsizeof(v) for k, v in obj.items())
    elif isinstance(obj, (list, tuple, set)):
        return sys.getsizeof(obj) + sum(sys.getsizeof(i) for i in obj)
    else:
        return sys.getsizeof(obj)


# print(f"{type(x)} : {size_of(x)}")
# print(f"{type(y)} : {size_of(y)}")
# print(f"{type(z)} : {size_of(z)}")
# print(f"{type(a)} : {size_of(a)}")
# print(f"{type(b)} : {size_of(b)}")
# print(f"{type(c)} : {size_of(c)}")
# print(f"{type(d)} : {size_of(d)}")

# deque

de = deque(range(1000))
# # print(size_of(de))
# # print(size_of(x))
#
# l = [1,2,3,4,5]
# de_l = deque(l)
# # print(size_of(de_l))
# # print(de_l)
# # print(type(de_l))
# de_l.append(10)
# de_l.appendleft(100)
# de_l.insert(1, 1000)
# print(de_l)
# de_l.pop()
# de_l.popleft()
# de_l.remove(1000)
# print(de_l)
# # de_l.rotate(3)
# # print(de_l)
# de_l.extend([6,7,8,9,10])
# print(de_l)
# de_l.extendleft([11,12,13,14,15])
# print(de_l)

# DefaultDict

dd = defaultdict(int)
st = 'The Bangladesh the country known as Bangladesh for its own country and its own name is Bangladesh for its country'.lower()
# for i in 'MMMoooonnnnsssstteeeeeeerr':
#     dd[i] += 1
# new_s = s.split()
# for i in new_s:
#     dd[i] += 1
# print(dd)
# info = [
#     ('a',10),
#     ('b',20),
#     ('c',30),
#     ('a',40),
#     ('b',50),
#     ('c',60),
#     ('a',70),
#     ('d',90),
# ]
#
# dl = defaultdict(list)
# for key, value in info:
#     dl[key].append(value)
# print(dl)

name = [
    'Albert',
    'Ace',
    'Albedo',
    'Ben',
    'BenDover',
    'Catfish',
    'Romeo',
    'Dove',
    'Dover',
    'Eren',
    'G',
]

# name_dict = defaultdict(list)
# for i in name:
#     y = len(i)
#     name_dict[y].append(i)
# print(name_dict)

name_dict = defaultdict(list)
name_count = defaultdict(int)

for i in name:
    first_letter = i[0].upper()
    name_count[first_letter] += 1

# print(name_dict)
# print(name_count)

# nested_dict = defaultdict(lambda: defaultdict(int))
# nested_dict['Rahim']['Math'] += 1
# nested_dict['Karim']['English'] += 1
# nested_dict['Johan']['Law'] += 1
# nested_dict['Aizen']['Philosophy'] += 1
# nested_dict['Newton']['Physics'] += 1
# nested_dict['Albert']['Quantum Mechanics'] += 1
# for k,v in enumerate(nested_dict):
#     print(f"{k} : {v}")
# print(nested_dict)

# nested_dict = defaultdict(lambda: defaultdict(int))
#
# l = [
#     ('A', 'Math'),
#     ('B', 'Math'),
#     ('C', 'Math'),
#     ('D', 'Bangla'),
#     ('E', 'English'),
#     ('A', 'Bangla'),
#     ('B', 'Chemistry'),
#     ('C', 'Physics'),
#     ('F', 'Chemistry'),
#     ('A', 'Physics'),
#     ('C', 'Biology'),
#     ('B', 'Biology'),
#     ('B', 'Physics')
# ]
#
# for char, sub in l:
#     nested_dict[char][sub] += 1
# print_nested_dict = {k:dict(v) for k,v in nested_dict.items()}
# print(print_nested_dict)

scores = [
    ('A', '100'),
    ('B', '100'),
    ('C', '100'),
    ('D', '99'),
    ('E', '99'),
    ('F', '98'),
]

dl = defaultdict(list)

for char, score in scores:
    dl[score].append(char)
# print(dict(dl))

# Counter
numbers = [1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,1,1,2,3]
s = "My countries name is Bangladesh because this is the name people choose and The Bangladesh the country known as Bangladesh for its own country and its own name is Bangladesh for its country".lower()
stg = "Bangladesh"
new_s = s.split()

# print(dict(Counter(new_s)))

count_stg = Counter(stg)
count_str = Counter(new_s)
# print(count_str.most_common())
# print(list(count_stg.elements()))
# count_str.subtract(count_stg)
# print(count_str)
# count_str.update(count_stg)
# print(count_str)

# s1 = "cork"
# s2 = "rock"
#
# if Counter(s1) == Counter(s2):
#     x = True
# else:
#     x = False
# print(x)

l1 = ["listen", "silent", "enlist", "hello", "below", "elbow", "cat", "act"]

ld = defaultdict(list)
for i in l1:
    p = "".join(sorted(i))
    ld[p].append(i)
print(list(ld.values()))
