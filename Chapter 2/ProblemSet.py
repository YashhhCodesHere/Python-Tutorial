# 1.

a = int(input("Enter the first number: "))

b = int(input("Enter the second number: "))

print("\nThe sum of your entered numbers are: ", a+b)

# 2. 

c = int(input("Enter your number: "))
z = int(input("Enter the number you divide the above number with: "))
d = '''This is gonna remains to be a string type variable untill and 
unless it's get typecasted!'''

print("The remainder when your 1st number is divided by 2nd one: ", c % z)

# 3. 

# CHECKING THE TYPE OF VARIABLES:

print("The datatype of variable 'a' is: ", type(a))
print("The datatype of variable z is: ", type(z))
print("The datatype of variable d is: ", type(d))

# 4. 

x = 34
y = 80

print("a is greater than b : ", x>y)

# 5.

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))

print("Average of your both given numbers are: ", ((m+n)/2))

# 6.

p = int(input("Enter your number which you wanted to be squarred: "))

print("The square of your given number are: ", p**2) # '**' is used to for square

w = None
print("The value in 'w' is:", w , "as it stores None datatype!")