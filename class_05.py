# """
# 10/02/2019
# Assingments
"""
1)Write list comprehension to create 15 random numbers.
2)Write list comprehension to create Prime numbers till user defined number.
3)Write Dictionary comprehension with 5 key value pair.
4)Convert all pattern assingments in user defined function.
"""
# 1) Comprehension
# 2) User defined function
# """
# # Two types of comprehension
# # 1.lIST comprehension
#
# _odd = list()
#
# for i in range(1, 10, 2):
#     _odd.append(i)
# print(_odd)
#
# _odd = [i for i in range(1, 10, 2)]
# print(_odd)
#
# for i in range(1, 10):
#     if i % 2 == 1:
#         _odd.append(i)
#
# _odd = [i for i in range(1, 10) if i % 2 == 1]
# print(_odd)
#
# # Dictionary Comprehension
#
sqrt = {}

numbers = [2, 4, 6, 8, 9, 11]

for num in numbers:
    sqrt[num] = num * num

print(sqrt)
#
# _sqrt = {num: num * num for num in numbers}
#
# print(_sqrt)
#
# op = []
# lables = ['Name', 'Age', 'Contact_no']
#
# user_1 = ['Ab', '10', 9513571234]
# user_2 = ['Cd', '12', 7894561230]
# user_3 = ['Ef', '22', 4565556562]
#
# for user in [user_1, user_2, user_3]:
#     _user = {}
#     for index in range(0, 3):
#         _user[lables[index]] = user[index]
#     op.append(_user)
# print(op)
#
# output = [
#
#     {
#         label: user[index] for index, label in enumerate(lables)
#     }for user in [user_1, user_2, user_3]
#
# ]
# print(output)

# User defined function
'''
def<function_name>():
   <statement1>
   <statement2>
   .
   .
   .
   <statement n>
# this is to create new function after indentation new line starts for new function,fun always starts with def   
'''


# def greetings():
#     """
#     This is greetung function
#     :return:
#     """
#     print("HELLO WORLD")
#     # next line is jst for calling the function.
#     greetings()
#
#
# def arg_greetings(name):
#     """
#     This is greetings fun with argument
#     :param name:
#     :return:
#     """
#     print(F"hello {name}")
#
#     arg_greetings(name="Ab")
#
#
# def arg_return_greetings(name):
#     """
#     with return argument
#     :param name:
#     :return:
#     """
#     message = F"Hello {name}"
#     return message
#
#
# resp = arg_return_greetings(name="AB")
# print(resp)
#
# _name = input("Enter your name:")
# resp = arg_return_greetings(name=_name)
# print(resp)

"""
ASSINGMENT 1
_random = list()
for i in range(1,15):
    _random.append(i)
    
print(_random)
"""


# if u want to pass default variable then just put it in argument parenthesis as blank "*"

def wild_card_args_function(*args):
    """

    :param args:
    :return:
    """
#     print(args[0], args[1])
#
#
# wild_card_args_function(*['test', 'test2'])
#
# def wild_card_Kwargs_function(**kwargs):
#     """
#
#     :param kwargs:
#     :return:
#     """
#     for key, values in kwargs.items():
#
#      print(key, ": ", values)
#
# user1 = {"Name": "AB", "Age": "19", "Contact no": 9673453049}
# wild_card_args_function(**user1)
