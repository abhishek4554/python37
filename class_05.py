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

