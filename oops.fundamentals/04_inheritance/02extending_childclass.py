"""
Topic: Inheritance - Extending Child Class
Author: Ishita Jain
Description: Demonstrates how a child class can 
inherit methods from a parent class and also add its own methods.
"""


# ======================================
# Program 2 - Child Class Adding Its Own Methods
# ======================================


# Parent Class / Base Class
# Contains common methods that can be inherited by child classes.
class Animal:

    def eat(self):
        return "Animals can eat"


# Child Class / Derived Class
# Inherits methods from Animal class and adds its own functionality.
class Dog(Animal):

    def bark(self):
        return "Dogs can bark"


# Creating an object of child class
dog1 = Dog()


# Accessing inherited method from Parent class
print(dog1.eat())


# Accessing child class's own method
print(dog1.bark())

"""
Topic: Inheritance - Using Parent Class Methods
Author: Ishita Jain
Description: Demonstrates how a child class can
 inherit and use methods from a parent class.
"""


# ======================================
# Program 3 - Child Class Using Parent Method
# ======================================


# Parent Class / Base Class
# Contains a method that creates and stores attributes.
class Parent:

    def house(self, address, city):

        # Creating instance attributes using method
        self.address = address
        self.city = city

        return "The city is:", city, "The address is:", address


# Child Class / Derived Class
# Inherits methods from Parent class.
class Student(Parent):
    pass


# Creating object of child class
s1 = Student()


# Calling inherited method from Parent class
# This method creates address and city attributes.
s1.house("123", "Delhi")


# Accessing attributes created by the inherited method
print(s1.address, s1.city)

