"""
Topic: Encapsulation - Private Attributes
Author: Ishita Jain
Description: Demonstrates the concept of private attributes in Python and shows that they cannot be accessed directly outside the class.
"""

# ======================================
# Program 1 - Private Attributes
# ======================================

class Gmail:
    def __init__(self, gmail_id, gmail_pass):
        # Public attribute
        self.gmail_id = gmail_id

        # Private attribute
        self.__gmail_pass = gmail_pass


# Creating an object
s1 = Gmail("ishh.jain@gmail.com", "hello2hi")

# Public attributes can be accessed directly.
print("Gmail ID:", s1.gmail_id)

# Private attributes cannot be accessed directly.
# Attempting to access them raises an AttributeError.

try:
    print("Password:", s1.gmail_pass)
except AttributeError as e:
    print("Error:", e)