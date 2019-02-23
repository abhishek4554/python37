# ## if
"""
if <Condition>:
    statement
"""
number_01 = 6
number_02 = 4
number_03 = 4
"""
if number_01 < number_02:
     print("Number 02 is greater then Number 01.")
"""
# if else
"""
if number_01 > number_02:
     print("Number 01 is greater then Number 02.")
else:
     print("Number 02 is greater then Number 01.")
"""
# if elif else

if number_01 > number_02:
    print("Number 02 is greater then Number 01.")

elif number_02 < number_03:
    print("Number 03 is greater then Number 02.")

else:
    print("Number 02 is greater then Number 00s1.")

# Nested if else

# if number_01 > number_02:
#     if number_01 > number_03:
#         print("01 Number 01 is max")
#     else:
#         print("02 Number 03 is max")
#
# else:
#     if number_02 > number_03:
#         print("03 Number 02 is max")
#     else:
#         print("04 Number 03 is max")


# if number_01 < number_02 < number_03:
#     print("05 Number 03 is max")
#
# elif number_01 < number_02 and number_02 > number_03:
#     print("06 Number 02 is max")
#
# elif number_01 > number_02 and number_01 > number_03:
#     print("07 Number 01 is max")
#
# else:
#     print("08 Numbers are same")