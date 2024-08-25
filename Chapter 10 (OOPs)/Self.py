class Employee:
        name = 'Yash'
        age = 19
        salary = 96000

        def get_details(self):
                print(f"Name is: {self.name}, whose age is: {self.age}")

        def greet(self):
                print("Hello, Good Morning!")

        @staticmethod   # This will avoid the use of self here... This is a decorator!
        def intro():
                print("Heyyy! I'm Yash...")

Employee001 = Employee()

Employee001.get_details() # 1st syntax to call the 'get_details' function

Employee.get_details(Employee001) # 2nd syntax to call the 'get_details' function

Employee001.greet()