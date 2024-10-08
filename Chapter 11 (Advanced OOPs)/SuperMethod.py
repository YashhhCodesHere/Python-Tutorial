class Grandparent:
    def __init__(self):
        print("Grandparent constructor")
        super().__init__()

class Parent(Grandparent):
    def __init__(self):
        # super().__init__()     # This will not gonna call the Grandparent class constructor because super() is commented
        print("Parent constructor")

class Child(Parent):
    def __init__(self):
        super().__init__()      # This will call the Parent class constructor
        print("Child constructor")

# Creating an instance of the Child class
child = Child()
# print(Child)


# Super method is used to call the constructor of the parent class to the child class. 



# Ex of Function of super method:-

class Parent:
    def __init__(self):
        print("Parent class initialized")

class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls the constructor of the Parent class
        print("Child class initialized")

# Creating an instance of Child
child_instance = Child()
