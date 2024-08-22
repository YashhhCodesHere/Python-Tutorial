f = open("Robinn.txt", "r") # Open file in read mode

text_data = f.read() # Read the file
print(text_data) # Print the file

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
f.close() # Close the file


print(f.readlines())

files = open("new.txt", "w")

strings = "Hey everyone...  Yash is a good boy!"

files.write(strings)

files.close()

f = open("new.txt")
text = f.read()
print(text)
f.close()

f = open("Robinn.txt", "r")

line = f.readline()
while(line != ""):
    print(line, type(line))
    line = f.readline()