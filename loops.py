# Loop practice
# Demonstrates for and while loops

# For loop example: print numbers 1 to 5
for i in range(1, 6):
    print("For loop:", i)

# While loop example: print numbers 1 to 5
count = 1
while count <= 5:
    print("While loop:", count)
    count += 1
  
# nested loops
# multiplication table
print("Multiplication table 1-5")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()
