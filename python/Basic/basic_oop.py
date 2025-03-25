# Basic OOP

# class car:
#     def __init__(self, name, model, color):
#         self.name = name
#         self.model = model
#         self.color = color

#     def display(self):
#         print(f"Name: {self.name}\nModel: {self.model}\nColor: {self.color}")


# car1 = car("BMW", "X5", "White")
# print(car1.display())

# Encapsulation (DATA HANDLING)

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number  # Public
#         self._bank_name = "XYZ Bank"  # Protected
#         self.__balance = balance  # Private

#     def deposit(self, amount):
#         self.__balance += amount

#     def get_balance(self):  # Public method to access private attribute
#         return self.__balance

# account = BankAccount("12345", 1000)
# print(account.account_number)  # ✅ Allowed
# print(account._bank_name)  # ✅ Allowed (but not recommended)
# # print(account.__balance)  # ❌ Error (Private)
# print(account.get_balance())  # ✅ Accessing private variable via method


# Inheritance (Code Reusability)

# Basic


# class Parent:
#     # Constructor
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f"Name: {self.name}")
#
#
# # Child class inherits from Parent
# class Child(Parent):
#     pass  # No new code, but it inherits everything
#
#
# child_obj = Child("Alice")
# child_obj.show()  # ✅ Works because Child inherits show() from Parent

# Single Inheritance

# class Animal:
#     def speak(self):
#         print("This animal makes a sound")
#
#
# class Dog(Animal):
#     def bark(self):
#         print("Woof!")
#
#
# dog = Dog()
# dog.speak()  # Output: This animal makes a sound
# dog.bark()  # Output: Woof!

# Multiple Inheritance

# class Engine:
#     def engine_type(self):
#         return "V8 Engine"
#
#
# class Wheels:
#     def wheel_count(self):
#         return 4
#
#
# class Car(Engine, Wheels):  # Inheriting from Engine and Wheels
#     def car_type(self):
#         return "Sedan"
#
#
# my_car = Car()
# print(my_car.engine_type())  # ✅ From Engine class
# print(my_car.wheel_count())  # ✅ From Wheels class
# print(my_car.car_type())  # ✅ From Car class

# Multilevel Inheritance (Parent → Child → Grandchild)

# class Animal:
#     def eat(self):
#         print("This animal eats food.")
#
#
# class Mammal(Animal):  # Mammal inherits from Animal
#     def warm_blooded(self):
#         print("Mammals are warm-blooded.")
#
#
# class Dog(Mammal):  # Dog inherits from Mammal
#     def bark(self):
#         print("Dog barks!")
#
#
# dog = Dog()
# dog.eat()  # ✅ From Animal
# dog.warm_blooded()  # ✅ From Mammal
# dog.bark()  # ✅ From Dog

# Hierarchical Inheritance (One Parent, Multiple Children)

# class Animal:
#     def speak(self):
#         print("Animals can make sounds.")
#
#
# class Cat(Animal):  # Cat inherits from Animal
#     def meow(self):
#         print("Cat says: Meow!")
#
#
# class Dog(Animal):  # Dog inherits from Animal
#     def bark(self):
#         print("Dog says: Woof!")
#
#
# cat = Cat()
# dog = Dog()
#
# cat.speak()  # ✅ Inherited from Animal
# cat.meow()  # ✅ Cat's own method
#
# dog.speak()  # ✅ Inherited from Animal
# dog.bark()  # ✅ Dog's own method

# Hybrid Inheritance (Combination)

# class Vehicle:
#     def general_info(self):
#         print("Vehicles are used for transportation.")
#
#
# class Car(Vehicle):
#     def car_info(self):
#         print("Cars have 4 wheels.")
#
#
# class Electric:
#     def battery(self):
#         print("Runs on battery.")
#
#
# class Tesla(Car, Electric):  # Hybrid: Inherits from both Car & Electric
#     def autopilot(self):
#         print("Tesla has autopilot mode.")
#
#
# tesla = Tesla()
# tesla.general_info()  # ✅ From Vehicle
# tesla.car_info()  # ✅ From Car
# tesla.battery()  # ✅ From Electric
# tesla.autopilot()  # ✅ From Tesla

# super() function

# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f"Parent Name: {self.name}")
#
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)  # Calls Parent's __init__()
#         self.age = age
#
#     def show(self):
#         super().show()  # Calls Parent's show()
#         print(f"Child Age: {self.age}")
#
#
# child = Child("Alice", 10)
# child.show()

# Polymorphism (Different Behavior for the Same Method)

# Method Overriding

# class Bird:
#     def sound(self):
#         return "Chirp"
#
#
# class Crow(Bird):
#     def sound(self):
#         return "Caw Caw"
#
#
# bird = Bird()
# print(bird.sound())  # Output: Chirp
#
#
# crow = Crow()
# print(crow.sound())  # Output: Caw Caw (Overridden method)

# Method Overloading (Not Built-in, but Achievable)


# class MathOperations:
#     def add(self, a, b, c=0):  # c is optional
#         return a + b + c
#
#
# math_op = MathOperations()
# print(math_op.add(2, 3))  # Uses 2 arguments
# print(math_op.add(2, 3, 4))  # Uses 3 arguments

# Abstraction (Hiding Implementation Details)

#  Abstract Classes and Methods (Using ABC module)

# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):  # Abstract class
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Circle(Shape):  # Concrete class
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return 3.14 * self.radius ** 2
#
#
# circle = Circle(5)
# print(circle.area())  # Output: 78.5

# Special Methods (Dunder Methods)

# __str__() – String Representation

# class Car:
#     def __init__(self, name, model):
#         self.name = name
#         self.model = model
#
#     def __str__(self):
#         return f"{self.name} {self.model}"
#
#
# car = Car("Tesla", "Model 3")
# print(car)  # Output: Tesla Model 3
#
# # __eq__(), __lt__(), __gt__() – Operator Overloading
#
# class Box:
#     def __init__(self, volume):
#         self.volume = volume
#
#     def __lt__(self, other):  # Less than
#         return self.volume < other.volume
#
#
# box1 = Box(10)
# box2 = Box(20)
#
# print(box1 < box2)  # Output: True

# Advance OOP

# Class Methods vs Static Methods

# @staticmod

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# print(Math.add(5, 3))  # ✅ Output: 8

# # @classmethod

#
# class Dog:
#     count = 0  # Class variable
#
#     def __init__(self, name):
#         self.name = name
#         Dog.count += 1  # Increment the number of dogs
#
#     @classmethod
#     def total_dogs(cls):  # Works with class variables
#         return cls.count
#
#
# dog1 = Dog("Rex")
# dog2 = Dog("Buddy")
#
# print(Dog.total_dogs())  # ✅ Output: 2

# @property

# class Person:
#     def __init__(self, name):
#         self._name = name  # Protected variable (_name)
#
#     @property
#     def name(self):  # Getter (acts like an attribute)
#         return self._name
#
#
# p = Person("John")
# print(p.name)  # ✅ Output: John

# @name.setter

# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):  # Getter
#         return self._name
#
#     @name.setter
#     def name(self, value):  # Setter
#         if len(value) < 3:
#             raise ValueError("Name must be at least 3 characters long!")
#         self._name = value
#
#
# p = Person("John")
# p.name = "Doe"  # ✅ Works fine
#
# p.name = "Al"  # ❌ ERROR! Name too short

# @name.deleter

# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         return self._name
#
#     @name.deleter
#     def name(self):  # Deletes _name
#         print("Deleting name...")
#         del self._name
#
#
# p = Person("John")
# del p.name  # ✅ Output: Deleting name...
