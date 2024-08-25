# #1. 

# class Programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, city):
#         self.name = name
#         self.salary = salary
#         self.city = city
#         # return (name, city, salary)

# Yash = Programmer("Yash", 150000, "Patna")
# print(Yash.name, Yash.company, Yash.salary)
# Harsh = Programmer("Harsh", 120000, "Gaziabad")
# print(Harsh.name, Harsh.company, Harsh.salary)

# # print(Programmer.__init__())

# #2.

# class Calculator:
    
#     @staticmethod
#     def greet():
#         print("Hello!")

#     def __init__(self, number , operation):
#         if(operation.lower() == "square"):
#             print(f"Square of {number} is: {number**2}")
#         elif(operation.lower() == "cube"):
#             print(f"Square of {number} is: {number**3}")
#         elif(operation.lower() == "root"):
#             print(f"Square of {number} is: {number**(1/2)}")
#         else:
#             print("You entered wrong entry!")

# num = int(input("Enter your number: "))
# Oper = input("Square/Cube/Root 'CHOOSE & TYPE ANY ONE': "+ '\n')
# tries = Calculator(num, Oper)

# tries.greet()

#5.
import random

class Train:
    train_name = "Rajdhani"
    booking_methods = "Online", "Offline"

    def __init__(self, train_no, From, To):
        self.train_no = train_no
        self.From = From
        self.To = To

        print(f"You can book your ticket in {self.train_no} from {self.From} to {self.To}!")
        print(f"Current seat available is: {random.randint(0, 155)}!")
        print(f"Price of your fare is: Rs.{random.randrange(1200, 2500)}")

Ticket = Train(12321, "Delhi", "Jaipur")
print(f"\nShowing status of {Ticket.train_name}({Ticket.train_no}) ")
