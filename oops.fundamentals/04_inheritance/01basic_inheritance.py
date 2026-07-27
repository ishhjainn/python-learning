"""
Topic: Inheritance - Basic Inheritance
Author: Ishita Jain
Description: Demonstrates how a child class can inherit attributes and methods from a parent class.
"""


# ======================================
# Program 1 - Basic Inheritance
# ======================================


# Parent Class / Base Class
# This class contains common properties and methods.
class Parent:

    def eat(self):
        # This method will be inherited by child classes.
        return "They eat"


# Child Class / Derived Class
# Child class inherits all accessible methods of Parent class.
class Child(Parent):
    pass


# Creating an object of child class
child1 = Child()


# Child object can access the parent class method
# because of inheritance.
print(child1.eat())


