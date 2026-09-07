# Abstraction
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


# Abstraction 02
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike Started")

b = Bike()
b.start()


# Class and Object
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Aditya")
print(s1.name)


# Constructor
class Car:
    def __init__(self, brand):
        self.brand = brand

c = Car("Toyota")
print(c.brand)


# Composition
class Engine:
    def start(self):
        print("Engine Started")

class Car:
    def __init__(self):
        self.engine = Engine()

c = Car()
c.engine.start()


# Encapsulation
class Bank:
    def __init__(self):
        self.__balance = 5000

    def show(self):
        print(self.__balance)

b = Bank()
b.show()


# Encapsulation 02
class Student:
    def __init__(self):
        self.__marks = 90

    def getMarks(self):
        return self.__marks

s = Student()
print(s.getMarks())


# Inheritance
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()


# Inheritance 02
class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    def bark(self):
        print("Barking")

d = Dog()
d.eat()
d.bark()


# Instance vs Static vs Class
class Demo:
    college = "MIT"

    def show(self):
        print("Instance Method")

    @staticmethod
    def display():
        print("Static Method")

    @classmethod
    def info(cls):
        print(cls.college)

d = Demo()
d.show()
Demo.display()
Demo.info()


# Instance vs Static
class Student:
    college = "MIT ADT"

    def __init__(self, name):
        self.name = name

s1 = Student("Aditya")
s2 = Student("Rugved")

print(s1.name)
print(Student.college)


# Magic Method
class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

s = Student("Aditya")
print(s)


# Polymorphism
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for animal in [Dog(), Cat()]:
    animal.sound()


# Polymorphism 02
class Bird:
    def sound(self):
        print("Chirp")

class Lion:
    def sound(self):
        print("Roar")

for obj in [Bird(), Lion()]:
    obj.sound()