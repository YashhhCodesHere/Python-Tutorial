class Animal:
    a = 1
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    b = 2
    def bark(self):
        print(f"{self.name} is barking.")

class Bulldog(Dog):
    c = 3
    def guard(self):
        print(f"{self.name} is guarding.")

# Creating an instance of Bulldog
obj = Dog("Leo")
bulldog = Bulldog("Rocky")

# Calling methods from different levels of inheritance

bulldog.eat()
bulldog.bark()
bulldog.guard()

print(bulldog.c)

print(obj.b)
# print(obj.c)      This will gonna throws an error