def fact(n):
    if(n == 0 or n == 1):
        return 1
    return n * fact(n-1)

n = int(input("Enter your number of which you want the factorial of: "))
print(f"The factorial of your entered number is: {fact(n)}")