"""
Topic: Polymorphism - Method Overriding
Author: Ishita Jain
Description: Demonstrates how polymorphism is achieved
             using method overriding in Python.
"""


# ==========================================================
# Polymorphism
# ==========================================================

# Polymorphism means "one interface, many forms".
# The same method can behave differently depending on
# the object that calls it.

# Method overriding is one way to achieve polymorphism.


# ==========================================================
# Program 1 - Basic Method Overriding
# ==========================================================

class Animal:

    def sound(self):
        return "Some Animal Sound"


class Dog(Animal):

    # Overriding the parent method
    def sound(self):
        return "Bhaayu Bhaayu"


class Cat(Animal):

    # Overriding the parent method
    def sound(self):
        return "Miyaau Miyaau"


d1 = Dog()
c1 = Cat()

print(d1.sound())
print(c1.sound())


# Output
# Bhaayu Bhaayu
# Miyaau Miyaau


# ==========================================================
# Program 2 - Child Does Not Override
# ==========================================================

# A child class is NOT required to override a method.
# If it does not define its own implementation,
# Python automatically searches in the parent class.

class Animal:

    def sound(self):
        return "Some Animal Sound"


class Dog(Animal):

    def sound(self):
        return "Bhaayu Bhaayu"


# Cat does not override sound().
# Python automatically uses Animal's sound() method.
class Cat(Animal):
    pass


d1 = Dog()
c1 = Cat()

print(d1.sound())
print(c1.sound())


# Output
# Bhaayu Bhaayu
# Some Animal Sound


# ==========================================================
# Program 3 - Same Method, Same Output
# ==========================================================

# Polymorphism does NOT require different outputs.
# Different objects can still respond to the same
# method call with the same result.


class Animal:

    def sound(self):
        return "Some Animal Sound"


class Dog(Animal):

    def sound(self):
        return "Bhaayu Bhaayu"


class Cat(Animal):

    # Same implementation as Dog
    def sound(self):
        return "Bhaayu Bhaayu"


d1 = Dog()
c1 = Cat()

print(d1.sound())
print(c1.sound())


# Output
# Bhaayu Bhaayu
# Bhaayu Bhaayu


# ==========================================================
# Key Notes
# ==========================================================

# 1. Polymorphism means "one interface, many forms."

# 2. Method overriding is one way to achieve polymorphism.

# 3. Different objects can respond to the same method call.

# 4. Different outputs are NOT mandatory.
#    Polymorphism depends on the object receiving
#    the method call, not on whether the returned
#    value is different.

# 5. A child class does not have to override a method.
#    If it does not, Python automatically uses the
#    inherited method from the parent class.