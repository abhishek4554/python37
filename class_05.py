"""
10/02/2019
1) Comprehension
2) User defined function
"""
# Two types of comprehension
# 1.lIST comprehension

_odd = list()

for i in range(1, 10, 2):
    _odd.append(i)
print(_odd)

_odd = [i for i in range(1, 10, 2)]
print(_odd)

for i in range(1, 10):
    if i % 2 == 1:
        _odd.append(i)

_odd = [i for i in range(1, 10) if i % 2 == 1]
print(_odd)

# Dictionary Comprehension

sqrt = {}

numbers = [2, 4, 6, 8, 9, 11]

for num in numbers:
    sqrt[num] = num * num

print(sqrt)

_sqrt = {num: num*num for num in numbers}

print(_sqrt)
