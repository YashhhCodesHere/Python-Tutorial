# def average():
#     _1st = float(input("Enter your 1st number: "))
#     _2nd = float(input("Enter your 2nd number: "))
#     _3rd = float(input("Enter your 3rd number: "))

#     avg = ((_1st+_2nd+_3rd)/3)

#     print(int(avg))

# average()


# Function Definition!
def greet(name = "User"):   # "User" is a Default Parameter Value
    print(f"Good Day, {name}")

greet(input("Enter your name: "))  # Function Call!

def birthday(month):
    if(month.lower() == "august"):
        print("Hurray! This is your Birthday month!")
    else:
        print("This isn't your birthday month!")

    return "The function worked well!"  # Return value of the function!

print(birthday("August"))

