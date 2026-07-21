"""
Topic: Constructors (__init__)
Author: Ishita Jain
Description: Demonstrates the use of constructors (__init__) to initialize object attributes and calculate the average marks of a student.
"""

# ==========================================================
# Program 1: Student Average Using Constructor
# ==========================================================

class Student:

    # Constructor to initialize the marks of three subjects
    def __init__(self, chemistry, physics, maths):
        self.chemistry = chemistry
        self.physics = physics
        self.maths = maths

    # Method to calculate and return the average marks
    def calculate_average(self):
        average = (self.chemistry + self.physics + self.maths) / 3
        return average


# Creating an object
s1 = Student(100, 100, 100)

# Displaying the marks
print("Marks Obtained:")

print("Chemistry :", s1.chemistry)
print("Physics   :", s1.physics)
print("Mathematics:", s1.maths)

# Displaying the average
print("\nAverage Marks:", s1.calculate_average())