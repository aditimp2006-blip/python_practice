# practice dictionaries
# Dictionary operations and loops

student = {
    "name": "Aditi",
    "age": 19,
    "course": "ENTC",
    "marks": {"Math": 95, "Physics": 88}
}

# Access value
print("Name:", student["name"])
print("Marks in Math:", student["marks"]["Math"])

# Add new key-value
student["grade"] = "A"
print("Updated student:", student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)

# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("Squares dictionary:", squares)
