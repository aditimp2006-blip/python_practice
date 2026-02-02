# Try-except examples and raising exceptions

try:
    num = int(input("Enter a number: "))
    reciprocal = 1 / num
    print("Reciprocal:", reciprocal)
except ValueError:
    print("Invalid input! Please enter an integer.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Raise an exception manually
def check_positive(n):
    if n < 0:
        raise ValueError("Number must be positive!")
    return True

try:
    check_positive(-5)
except ValueError as e:
    print("Error:", e)
