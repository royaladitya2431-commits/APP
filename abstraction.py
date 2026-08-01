from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

s = Square()
s.area()