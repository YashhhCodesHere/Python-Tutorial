# #1.

# table = int(input("Enter the number you want the table of: "))

# for i in range(1,11):
#     print(f"{table} x {i} = {table*i}")
# else:
#     print("Your table is now printed!")

# #2.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith(("s", "S"))):
#         print(f"Hello, {name}!")

# #3.

# Table = int(input("Enter the number: "))
# i = 1
# while(i<=10):
#     print(f"{Table} x {i} = {(Table*i)}")
#     i+=1

# #4.

# import math

# n = int(input("Enter the number you want to check is it Prime: "))
# if (n == 1 or n == 0):
#         print(f"\n{n} is Neither Prime Nor Composite!\n")

# elif (n < 0):
#         print("\nEnter whole number to check either it's prime or not!\n")

# for i in range(2, n):
#     if ((n%i) == 0):
#         print(f"\n{n} is NOT prime!\n")
#         break
#     else:
#         print(f"\n{n} is a Prime Number!")

# #5.

# n = int(input("Enter your number: "))
# i = 1
# sum = 0
# while(i<=n):
#     sum += i
#     i+=1
# else:
#     print(sum)

# #6.

# n = int(input("Enter your number: "))
# fact = 1
# for i in range(1,(n+1)):
#     fact = fact * i
# else:
#     print(f"The factorial of your given number is: {fact}")

# #7.

# n = int(input("Enter your number: "))
# k = 1
# for i in range(1,(n+1)):
#     print(" "*(n-1) + "*"*k)
#     n-=1
#     k+=2

# #8.

# n = int(input("Enter your number: "))

# for i in range(1,(n+1)):
#     print("*" * i)

#9.

n = 8
i = 10
while(i>0):
    print(f"{n} x {i} = {(n*i)}")
    i-=1
