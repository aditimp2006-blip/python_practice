# practice strings
# String operations, formatting, and methods

text = "Hello Python Programming"

# Length, uppercase, lowercase
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# Split string
words = text.split()
print("Words:", words)

# Join list into string
joined_text = "-".join(words)
print("Joined with hyphen:", joined_text)

# Substring check
print("Contains 'Python'?", "Python" in text)

# String formatting
name = "Aditi"
age = 19
print(f"My name is {name} and I am {age} years old.")
