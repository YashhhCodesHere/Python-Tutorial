class Employee:     # Base Class
    company = "ITC"
    def show(self,name, salary):
        self.salary = salary
        self.name = name
        print(f"The name is {self.name} & salary is {self.salary}.")
        
class Programmer(Employee):    # Derived Class or Child Class 
    company = "ITC Infotech"    # It will gonna contain all the properties of Employee class 

    # We can add some other methods or attributes to it!

a = Employee()
a.show("Harsh", 196000)
b = Programmer()
b.show("Yash", 152000)
