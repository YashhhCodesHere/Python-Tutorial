age = int(input("Enter you age here: "))

# if elif else ladder:-

if(age>=18):
    print("Congratulation! You're eligible to vote...")

elif(age<=0):
    print('''Your entered age is invalid... 
Please try again!!!''')

else:
    print("Sorry! Your age must be greater than 18 yrs to vote...")

print("\nWe're out of the conditional statement!!!\n\nSecond if-statement: ")

# If elif:-

if(age%2==0):
    print("Your age is Even!")
elif(age%2==1):
    print("Your age is Odd!")