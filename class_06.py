"""
Assingment
1) write a project for oops concept
OOP concepts
1)class
2)Abstraction
3)Encapsulation
4)Inheritance
5)Polymorphism

"""
# 1) class

class ClassName(object):

    """
     class level doc string
    """
    def __init__(self, name):
        self.name = name

    def my_function(self):
        print(F"Hello my function {self.name}")

    def my_function_2(self):
        print(F"Hello{self.name}")
        """

        :return:
        """


print('===================')
_class = ClassName(name="abhi")
_class.my_function()
_class.name = "hie how are u"
_class.my_function_2()
_class.my_function()

print('====================')
_class2 = ClassName(name="abhiii").my_function()

print('=======================')
_class3 = ClassName(name="abhishek").my_function()

# i have 2 doubts in hackerrank challange 1 is "finding the percentage" and 2 is " split string and join"


