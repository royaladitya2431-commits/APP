class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

s1 = Student("Aditya")
s2 = Student("Rugved")

print(s1.name)
print(Student.college)