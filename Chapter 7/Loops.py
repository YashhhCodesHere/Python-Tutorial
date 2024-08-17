# While Loop:

i = 1
while(i<=50):
    print(i)
    i+=0.5

# Printing contents of list using 'while' loop:-

list = ["Yash", "Robinn", "Harsh", "Utkarsh"]
x = 0
while(x < len(list)):
    print(list[x])
    x+=1

# For Loop:-

for i in range(0,5):  # Here in for loop last index is excluded-'4'
    print(f"Robinn-{i}th")

else:
    print("Done!") # This gets printed when the loop exhausts!

# Printing items in tupples using for loop:-

tup = (100, 2109, 'Yoyo', True)

for i in tup:
    print(i)
else:
    print("All the elements of tupples is now printed!!")

