"""
Topic: Encapsulation - Name Mangling
Author: Ishita Jain
Description: Demonstrates Python's name mangling mechanism and shows how private attributes can still be accessed using their mangled names.
"""

# ======================================
# Program 2 - Name Mangling
# ======================================
# Private attributes in Python are not completely inaccessible.
# Python internally changes the name of a private attribute to prevent accidental direct access.
# This process is called Name Mangling.

# Although name mangling allows access to private attributes,
# it is not considered proper encapsulation because it bypasses
# the controlled access provided by getter and setter methods.
class Gmail:
    def __init__(self, gmail_id, gmail_pass):
        # Public attribute
        self.gmail_id = gmail_id

        # Private attribute
        self.__gmail_pass = gmail_pass


# Creating an object
s1 = Gmail("ishh.jain@gmail.com", "hello2hi")

# Accessing the public attribute
print("Gmail ID:", s1.gmail_id)

# Accessing the private attribute using Python's name mangling.
# Although this works, it is not the recommended way to access private data.

print("Password:", s1._Gmail__gmail_pass)
