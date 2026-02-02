"""
File: loops.py
Description:
This file demonstrates different types of loops in Python with examples.
Covers:
- for loop
- while loop
- break, continue
- nested loops
"""

# 1. for loop example
print("For Loop Example:")
for i in range(1, 6):
    print("Number:", i)

print("-" * 30)

# 2. while loop example
print("While Loop Example:")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("-" * 30)

# 3. break statement
print("Break Example:")
for i in range(1, 10):
    if i == 5:
        print("Breaking at", i)
        break
    print(i)

print("-" * 30)

# 4. continue statement
print("Continue Example:")
for i in range(1, 8):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

print("-" * 30)

# 5. Nested loops (Pattern Printing)
print("Pattern Printing:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
