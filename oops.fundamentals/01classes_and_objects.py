"""
Topic: Classes and Objects
Author: Ishita Jain
Description: Basic implementation of classes, objects, methods, class variables, and instance variables.
"""

# ==========================================================
# Program 1: Creating a Class, Object and Calling a Method
# ==========================================================

class Student:
    # Class is created which acts as the blueprint/design.

    def show(self):
        # Method to display a simple message.
        print("My first basic OOP program")


# Creating an object
s1 = Student()

# Calling the method using the object
s1.show()


# ==========================================================
# Program 2: Class Variables and Instance Variables
# ==========================================================

class Students:

    # Class Variable (shared by all objects)
    college_name = "VIPS College"

    def details(self, name, age, result):

        # Instance Variables (different for every object)
        self.name = name
        self.age = age
        self.result = result


# First Object
s2 = Students()
s2.details("Ishita", 19, 8.95)

print("Name:", s2.name)
print("Age:", s2.age)
print("College:", Students.college_name)
print("Result:", s2.result)

print()


# Second Object
s3 = Students()
s3.details("Naysha", 19, 8.5)

print("Name:", s3.name)
print("Age:", s3.age)
print("College:", Students.college_name)
print("Result:", s3.result)