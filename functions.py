# practice functions
# Functions with return values and parameters

# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Testing the functions
print("Factorial of 5:", factorial(5))
print("Is 17 prime?", is_prime(17))
print("Is 18 prime?", is_prime(18))
