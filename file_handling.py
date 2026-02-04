# file_handling
# Reading and writing files

# Writing to a file
with open("sample.txt", "w") as f:
    f.write("Hello Python\n")
    f.write("File handling practice\n")

# Reading the file
with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:\n", content)

# Appending to a file
with open("sample.txt", "a") as f:
    f.write("Appending new line\n")

# Reading lines one by one
with open("sample.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
