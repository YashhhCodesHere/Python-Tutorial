#1.

num = []
num.append(int(input("Enter the number: ")))
num.append(int(input("Enter the number: ")))
num.append(int(input("Enter the number: ")))
num.append(int(input("Enter the number: ")))

maximum = max(num)

print("Max of your entered number is:",max(num))

#2.

sub1 = int(input("Enter the English marks: "))
sub2 = int(input("Enter the Maths marks: "))
sub3 = int(input("Enter the Science marks: "))
tot = (sub1+sub2+sub3)
print("\n")

if(sub1>100 or sub2>100 or sub3>100):
    print("Please enter the marks in the range of 0-100!")
elif(tot>=120) and (sub1>=33 and sub2>=33 and sub3>=33):
    print("You're PASSED!")
else:
    print("You're FAILED!")

#3.

spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"

text = input("Enter your message: ")

# Way 1:
if(text==spam1 or text==spam2 or text==spam3 or text==spam4):
    print("ALERT! This message is Spam.\n")

# Way 2:
if(spam1 in text or spam2 in text or spam3 in text or spam4 in text):
    print("This is Fraud!!")
else:
    print("This is Safe message.")

#4.

userName = input("Enter your username please: ")

if(len(userName)<10):
    print("Your username is less than 10 characters!")
else:
    print("Your username is greater than 10 characters!")

#5.

ls = ["Yash","Harsh","Tutu","Munu"]
name = input("Enter your name:")

if(name in ls):
    print("Your name found!")
else:
    print("Your name doesn't exists in the list!")

#6.

mark = int(input("Enter your marks: "))

if(mark<=100 and mark>90):
    print("Excellent! A+")
elif(mark<=90 and mark>80):
    print("A")
elif(mark<=80 and mark>70):
    print("B")
elif(mark<=70 and mark>60):
    print("C")
elif(mark<=60 and mark>50):
    print("D")
elif(mark<=50 and mark>0):
    print("F")
elif(mark>100 and mark<0):
    print("Invalid marks entered!")
else:
    print("Enter your marks carefully!")