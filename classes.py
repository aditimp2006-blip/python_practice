# practice classes
# Classes, objects, methods, and inheritance

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def greet(self):
        print(f"Hello, my name is {self.name}. I study {self.course}.")

# Inheritance example
class CollegeStudent(Student):
    def __init__(self, name, age, course, college):
        super().__init__(name, age, course)
        self.college = college

    def greet_college(self):
        print(f"{self.name} studies at {self.college}.")

s1 = Student("Aditi", 19, "ENTC")
s1.greet()

s2 = CollegeStudent("Aditi", 19, "ENTC", "MIT College")
s2.greet_college()
