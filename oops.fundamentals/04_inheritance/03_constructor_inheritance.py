"""
Topic: Inheritance - Constructor Inheritance
Author: Ishita Jain
Description: Demonstrates how a child class can 
inherit the constructor and attributes of a parent class.
"""


# ======================================
# Program 3 - Constructor Inheritance
# ======================================


# Parent Class / Base Class
# Contains a constructor that initializes attributes.
class Parent:

    def __init__(self, address, city):

        # Creating instance attributes
        self.address = address
        self.city = city


# Child Class / Derived Class
# Since Student does not have its own constructor,
# it automatically uses the constructor of Parent class.
class Student(Parent):
    pass


# Creating object of child class
# Parent constructor will be called automatically.
s1 = Student("123", "Delhi")


# Accessing attributes inherited from Parent class
print(s1.address, s1.city) 

"""
Topic: Inheritance - Child Class Extending Parent
Author: Ishita Jain
Description: Demonstrates how a child class can inherit parent attributes and add its own attributes.
"""


class Parent:

    def __init__(self, address, city):
        self.address = address
        self.city = city


class Student(Parent):

    def student_details(self, name, section):
        self.name = name
        self.section = section


s1 = Student("123", "Delhi")

s1.student_details("Ishita", "B")

print(s1.address, s1.city, s1.name, s1.section)
