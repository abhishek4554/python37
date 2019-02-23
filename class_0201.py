# # Assingments
# # create 5 variable of each datatype
# # create 5 list variable with 3 elements like name, add, contact no.
# integer_variable = 3
# print("integer")
#
# print(integer_variable, id(integer_variable))
#
# # string
# string_variable = "This is my single line string."
# string_variable_2 = "This is my"\
#                      "multi line string. "
# string_variable_3 = """
# this is mt next multi variable string
# i can write anything in it
# thank you"""
# print('string')
# print(string_variable)
# print(string_variable_2)
# print(string_variable_3)
#
# # Boolean
# true_flag = True
# false_flag = False
#
# # None
# none_variable = None
# print('string variable 2', type(string_variable_2), id(string_variable_2))
# print('string variable 3', type(string_variable_3))
#
# # Data Structure
#
# # ###List
#
# list_variable = [
#     'abhiii', 'Ghar', 9767332523, 7.56, True
# ]
# print(list_variable)
# print(type(list_variable[2]))
# print(list_variable.index(7.56))
#
# print(len(list_variable))
# print(list_variable.count('abhiii'))
#
# integer_list = [1, 2, 3, 60, 55, 6]
# print(sorted(integer_list))
# integer_list.sort(reverse=True)
# print(integer_list)
#
# list_nested = [
#     "abhiii", ["Satara", "pune", [169, 78]]
# ]

# print(list_nested[1])
# print(list_nested[1][2][0])

list_nested_02 = [
    ['test_1', ['test_2', 'test_3', ['test_4']], 'test_05', ['test_6', 'test_7'], 'test_8', ['test_9', ['test_10']]]
]

print(list_nested_02[0][4])
print(list_nested_02[0][5][1][0])



