"""
Topic: Encapsulation - Getter Method
Author: Ishita Jain
Description: Demonstrates how getter methods provide controlled access to private attributes.
"""

# ======================================
# Program 3 - Getter Method
# ======================================

class Gmail:
    def __init__(self, gmail_id, gmail_pass):
        # Public attribute
        self.gmail_id = gmail_id

        # Private attribute
        self.__gmail_pass = gmail_pass


    # Getter Method
    # A getter is a public method used to access the value of a private attribute.
    # It provides controlled access to private data instead of accessing it directly.
    def get_password(self):
        return self.__gmail_pass


# Creating an object
s1 = Gmail("ishh.jain@gmail.com", "hello2hi")


# Public attribute can be accessed directly.
print("Gmail ID:", s1.gmail_id)


# Private attribute cannot be accessed directly:
# print(s1.__gmail_pass)  ❌

# Using getter method to access private attribute:
print("Password:", s1.get_password())