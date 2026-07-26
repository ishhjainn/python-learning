"""
Topic: Encapsulation - Getter and Setter Methods
Author: Ishita Jain
Description: Demonstrates how getter and setter methods provide controlled access to private attributes.
"""

# ======================================
# Program 4 - Getter and Setter Methods
# ======================================


class Gmail:

    def __init__(self, gmail_id, gmail_pass):
        # Public attribute
        self.gmail_id = gmail_id

        # Private attribute
        self.__gmail_pass = gmail_pass


    # Getter Method
    # A getter method is used to access/read the value of a private attribute.
    # It provides controlled access instead of directly accessing private data.
    def get_password(self):
        return self.__gmail_pass


    # Setter Method
    # A setter method is used to modify/update the value of a private attribute.
    # Instead of changing private data directly, we update it through a method.
    # This provides controlled modification of private data.
    def set_password(self, new_password):
        self.__gmail_pass = new_password



# Creating an object
s1 = Gmail("ishh.jain@gmail.com", "hello2hi")


# Accessing private attribute using getter method
print("Old Password:", s1.get_password())


# Updating private attribute using setter method
s1.set_password("python123")


# Accessing updated value using getter method
print("New Password:", s1.get_password())