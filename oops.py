
# 1. Classes and Objects
class Vehicle:
    def __init__(self, name):
        self.name = name

car = Vehicle("Car")
print("Name of the vehicle:", car.name) 

# 2. Inheritance
class Car(Vehicle):
    def __init__(self, name, brand):
        super().__init__(name)
        self.brand = brand

car1 = Car("SUV", "Toyota")
print("Name of the car:", car1.name)    
print("Brand of the car:", car1.brand)  

# 3. Encapsulation
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

account = BankAccount()
account.deposit(100)
print("Account balance:", account.get_balance())  

# 4. Polymorphism
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def make_sound(animal):
    return animal.speak()

dog = Dog()
cat = Cat()
print("Dog says:", make_sound(dog))  
print("Cat says:", make_sound(cat))  

# 5. Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print("Area of the circle:", circle.area())  
