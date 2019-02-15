# 1)
_random = list()

_random = [i for i in range(56, 85) if i % 2 == 0]
print(_random)

# 2)
# _prime = list()
#
# _prime = [i for i in range(2, 11) if i % 2 == 1]
# print(_prime)
for num in range(2, 24):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if prime:
     print(num)


# 3)
info = []

data = ['name', 'Job', 'Company', 'Experience', 'salary']

user_01 = ['XY', 'Developer', 'aws', '3 yrs', '40k']
for user in [user_01]:
    _user = {}
    for index in range(0, 5):
        _user[data[index]] = user[index]
    info.append(_user)
print(info)

# 4.1)

