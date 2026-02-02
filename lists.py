# practice lists
# Lists and basic operations

fruits = ["apple", "banana", "cherry", "orange"]
print("Original list:", fruits)

# Add elements
fruits.append("mango")
print("After append:", fruits)

# Insert at index
fruits.insert(1, "grapes")
print("After insert:", fruits)

# Remove element
fruits.remove("banana")
print("After remove:", fruits)

# Loop through list
for fruit in fruits:
    print("Fruit:", fruit)

# List comprehension: squares
squares = [x**2 for x in range(1, 6)]
print("Squares 1-5:", squares)
