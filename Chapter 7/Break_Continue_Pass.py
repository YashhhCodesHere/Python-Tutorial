# Break:-

for i in range(0,100):  # i += 1 isn't needed in for loop as it also increase the iterate with the step size!
    print(i)
    if(i == 77):
        break   # This will exit the loop!

# Continue:-

for i in range(1,21):
    print(i)
    if(i==15 or i==18):
        continue    # This will skip the current iteration (Present value of i)
else:
    print("15 and 18 is skipped using continue statement here!")

# Pass:-

for i in range(1,10):
    pass   # Blank loop will throw an error, hence Pass is used!
else:
    print("For loop is executed with doing anything with the help of pass statement!")