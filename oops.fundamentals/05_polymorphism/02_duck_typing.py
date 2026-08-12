"""
Topic: Polymorphism - Duck Typing
Author: Ishita Jain
Description: Demonstrates duck typing in Python.
             Different classes can be used interchangeably
             as long as they provide the required method.
"""


# ==========================================================
# Duck Typing
# ==========================================================

# Duck Typing is a form of polymorphism in Python.

# Python does not check the type of an object.
# Instead, it checks whether the required method exists.

# If an object has the required method,
# Python allows it to be used.

# "If it walks like a duck and quacks like a duck,
# treat it as a duck."


# ==========================================================
# Program 1 - Duck Typing
# ==========================================================

class Dog:

    def sound(self):
        return "Bhaayu Bhaayu"


class Cat:

    def sound(self):
        return "Miyaau Miyaau"


# This function accepts ANY object.
# The only requirement is that the object
# must have a sound() method.
def make_sound(animal):
    print(animal.sound())


d1 = Dog()
c1 = Cat()

make_sound(d1)
make_sound(c1)


# Output
# Bhaayu Bhaayu
# Miyaau Miyaau


# ==========================================================
# Key Notes
# ==========================================================

# 1. Duck Typing does NOT require inheritance.

# 2. Different classes can be used with the
#    same function if they provide the required method.

# 3. Python focuses on an object's behaviour,
#    not on its type.

# 4. If the required method is missing,
#    Python raises an AttributeError.

# 5. Duck Typing is one of Python's most
#    important polymorphism concepts.
