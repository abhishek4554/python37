# """
# 1)Anonymous Lambda Function
# 2)Iterator
# 3)Generator
# 4)Generator vs Iterator
# 5)Recursive Function
# """
# # ##################################
# # 1) LAMBDA
# # ##################################
# """
# Lambda
# lambda object : operation/expression
# MAP(lambda object : ope/exp, iteratable object)
# """
#
# _add_func = lambda ele_1, ele_2, ele_3: (ele_1 + ele_2) * ele_3
# print(_add_func(34, 45, 1))
#
# _sq = list(map(lambda x: x * x, [1, 2, 3, 4, 5]))
# print(_sq)
#
#
# # #######################################
# # 2)Iterator
# # #######################################
#
# class MyRange():
#     """
#     my range function
#     """
#
#     def __init__(self, n):
#         self.i = 0
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         if self.i <= self.n:
#             i = self.i
#             self.i += 1
#             return i
#         else:
#             raise StopIteration()
#
#
# data = MyRange(5)
# print(data.next())
# print(data.next())
# print(data.next())
# print(data.next())


# #############################
# 3)Generator
# #############################

# def simple_generator():
#     yield 1
#     yield 2
#     yield 3
#
# for item in simple_generator():
#     print(item)
# for item in range(1, 4):
#     print(item)
# def fib(limit):
#     a, b = 0, 1
#     while a < limit:
#         break
#     a, b = b, a + b
#     print('++++', a, b)
#
# def fib(limit):
#     numbers = []
#     a = 0
#     b = 1
#
#     while True:
#         if a > limit:
#             break
#             a, b =b, a+b
#             print('++++', a, b)
#             numbers.append(a)
#     return numbers

# def factorial(limit):
#     output = 1
#     initial = 1
#     while initial <= limit:
#         yield initial * output
#         output, initial = output * initial, initial+1
# for i in factorial(5):
#     print(i)

_prime = list(

)







