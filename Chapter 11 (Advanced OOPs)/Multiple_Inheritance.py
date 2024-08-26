class A:
    def method_a(self):
        print("This is method A")

class B:
    def method_b(self):
        print("This is method B")

class C(A, B):
    def method_c(self):
        print("This is method C")

# Creating an instance of class C
Object_C = C()

# Calling methods from class A
Object_C.method_a()

# Calling methods from class B
Object_C.method_b()

# Calling method from class C
Object_C.method_c()

# Here we can call all the methods or attributes from class 'C' as it contains inheritance of class 'A' & 'B'