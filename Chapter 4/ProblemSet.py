# 1.

fruits = [] # Null List created

print("Enter your fruit name: ",)
fruits.append(input())
print("Enter your fruit name: ")
fruits.append(input())
print("Enter your fruit name: ")
fruits.append(input())
print("Enter your fruit name: ")
fruits.append(input())
print("Enter your fruit name: ")
fruits.append(input())
print("Enter your fruit name: ")
fruits.append(input())

print(fruits)

# 2.

marks = []

marks.append(int(input("Enter the marks of the first student: ")))
marks.append(int(input("Enter the marks of the second student: ")))
marks.append(int(input("Enter the marks of the third student: ")))
marks.append(int(input("Enter the marks of the fourth student: ")))
marks.append(int(input("Enter the marks of the fifth student: ")))
marks.append(int(input("Enter the marks of the sixth student: ")))

marks.sort()
print(f"The given marks of 6 students in increasing order are as follows: {marks}")

# 3.

tup = (7,10,29)
print(type(tup))
# tup[2] = 100  - Here it shows tuples can't be modified!
print(tup.count())

# 4. 

ls = [132,311,495,911]
add = ls[1] + ls[2] + ls[3] + ls[0] # Making sum with the help of indexing
print(add)
print(sum(ls)) # making sum with help of sum function

# 5.

a = (7, 0, 8, 0, 0, 9)

print(f"The number of time zero occurs in the given tuples are: {a.count(0)}")