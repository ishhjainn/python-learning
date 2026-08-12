"""
Topic: Polymorphism - Built-in Polymorphism
Author: Ishita Jain
Description: Demonstrates built-in polymorphism in Python.
             The same built-in function or operator behaves
             differently depending on the type of object.
"""


# ==========================================================
# Built-in Polymorphism
# ==========================================================

# Built-in polymorphism means that Python's built-in
# functions and operators can work with different types
# of objects while performing different behaviours.

# The function or operator remains the same,
# but the result depends on the object it is working with.


# ==========================================================
# Program 1 - len() Function
# ==========================================================

print(len("Hello"))
print(len([10, 20, 30]))
print(len((1, 2, 3, 4)))
print(len({"name": "Ishita", "age": 19}))


# Output
# 5
# 3
# 4
# 2


# String      -> Counts characters.
# List        -> Counts elements.
# Tuple       -> Counts elements.
# Dictionary  -> Counts keys.


# ==========================================================
# Program 2 - max() Function
# ==========================================================

print(max(2, 5, 8))
print(max([10, 20, 30]))
print(max("Python"))


# Output
# 8
# 30
# y


# Numbers -> Returns the largest number.
# List    -> Returns the largest element.
# String  -> Returns the character with the highest
#            Unicode value.


# ==========================================================
# Program 3 - '+' Operator
# ==========================================================

print(10 + 20)

print("Hello " + "World")

print([1, 2] + [3, 4])


# Output
# 30
# Hello World
# [1, 2, 3, 4]


# Numbers -> Performs addition.
# Strings -> Performs concatenation.
# Lists   -> Merges two lists.


# ==========================================================
# Key Notes
# ==========================================================

# 1. Built-in polymorphism is achieved using Python's
#    built-in functions and operators.

# 2. The function or operator does not change.
#    Only its behaviour changes based on the object.

# 3. Common examples of built-in polymorphism are:
#
#       len()
#       max()
#       min()
#       sum()
#       + operator

# 4. Different object types provide their own
#    implementations for these operations internally.

# 5. Built-in polymorphism is one of the reasons
#    Python code is simple, flexible, and reusable.