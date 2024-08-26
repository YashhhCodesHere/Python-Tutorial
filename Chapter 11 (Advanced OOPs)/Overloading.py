class Number:
    def __init__(self, n):
        self.x = n
        print(f"{self.x}")

    def __add__(self, num):
        return self.x + num.x

a = Number(2)
b = Number(3)

print("The sum is:", a+b)