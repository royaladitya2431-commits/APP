class Student:
    def __init__(self):
        self.__marks = 90

    def getMarks(self):
        return self.__marks

s = Student()
print(s.getMarks())