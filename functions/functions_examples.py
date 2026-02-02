"""
This file demonstrates Python functions:
- Defining functions
- Arguments and return values
- Default arguments
- *args and **kwargs
- Simple utility functions
"""

def greet(name):
    """Returns a greeting message."""
    return f"Hello, {name}!"

def add(a, b):
    """Returns sum of two numbers."""
    return a + b

def calculate_area(radius, pi=3.14159):
    """Calculates area of a circle with default argument."""
    return pi * radius * radius

def print_numbers(*args):
    """Accepts variable number of arguments."""
    print("Numbers received:", args)

def student_info(**kwargs):
    """Accepts keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# Testing functions
if __name__ == "__main__":
    print(greet("Aditi"))
    print("Sum:", add(5, 10))
    print("Area of circle:", calculate_area(7))
    print_numbers(1, 2, 3, 4, 5)
    student_info(name="Aditi", branch="Engineering", year=2)
