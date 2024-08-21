#1.

def greatest(x,y,z):
    if(x>y and x>z):
        return (f"{x} is the greatest number")
    elif(y>x and y>z):
        return (f"{y}  is the greatest number")
    else:
        return (f"{z} is the greatest number")

print(greatest(13,102,100))

#2.

''' c/5 = (f-32)/9''' # Formula of celcius to fahrenheit or vice-versa

celsius_Input = int(input("Enter the temperature: "))

def convert_temperature(celsius):
    fahrenheit = (celsius * (9/5) + 32)
    return float(fahrenheit)

out=convert_temperature(celsius_Input)

print(round(out,2))     

#3.

print("Hello World", end= " ")
print("Hey")

#4.

num = int(input("Enter the value of n: "))

def sum_till_n(n):
    if(n == 1):     # Base condition is defined here to NOT to make the recursion be performed infinte times here!
        return 1    
    return n + sum_till_n(n-1)

print(sum_till_n(num))

#5.

def star_pattern(n):
    for i in range(0,n):
        print("*" * n)
        n-=1
    
n = int(input("Enter the number of lines you want the pattern of: "))
star_pattern(n)

#6. 

''' 1 inch = 2.54 cm'''

inch = int(input("Enter the inches: "))

def inch_to_cm(inches):
    cm = (inches * 2.54)
    return cm

print(f"{inch} inches in centimeter is {inch_to_cm(inch)} cm!")

#8.

m = int(input("Enter the you want the multiplication table of: "))
i = 1
def table(m,i):
    if i == 11:
        return None     # Base Condition!
    
    print(f"{m} * {i} = {i*m}")
    return table(m, i+1)

table(m,i)