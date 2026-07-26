"""
Topic: Encapsulation - Setter with Validation
Author: Ishita Jain
Description: Demonstrates how setter methods can validate data before updating private attributes.
"""


# ======================================
# Program 5 - Setter Method with Validation
# ======================================


class Gmail:

    def __init__(self, gmail_id, gmail_pass):

        # Public attribute
        # This attribute can be accessed directly outside the class.
        self.gmail_id = gmail_id

        # Private attribute
        # This attribute cannot be accessed directly outside the class.
        self.__gmail_pass = gmail_pass


    # Setter Method with Validation
    # Setter is used to update the value of a private attribute.
    # Validation ensures that only valid data is stored.
    def set_password(self, new_password):

        # Checking password length before updating the private attribute.
        if len(new_password) >= 6:

            # Updating private attribute only when validation is successful.
            self.__gmail_pass = new_password

            return self.__gmail_pass

        else:

            # Returning an error message if validation fails.
            return "Invalid password"


# Creating an object
s1 = Gmail("ishitajain@gmail.com", "xyzqphsj")


# Public attribute can be accessed directly.
print("Gmail ID:", s1.gmail_id)


# Trying to update password using setter method.
# Password will only update if it satisfies the validation condition.
print("Password Status:", s1.set_password("pytho"))