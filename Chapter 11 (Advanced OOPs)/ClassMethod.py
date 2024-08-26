class Worker:
    salary = 10000

    def show(self):
        print(f"The salary of the {self.name} is {self.salary}!")

    @classmethod
    def update(cls):
        print(f"The salary of Ankur is {cls.salary}")

Ankur = Worker()
Ankur.name = "Ankurr"
Ankur.salary = 15000

print(Ankur.show())     # This will print the salary of Ankur on the basis of instance variable
print(Ankur.update())   # This will print the salary of Ankur on the basis of class variable