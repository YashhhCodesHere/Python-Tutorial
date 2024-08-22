# f = open("this.txt", "w") 
# f.write("this is nice") 
# f.close

# The same can be done with the use of with statement:

with open("file.txt", "w") as file:
    file.write("Heyyy! Good Morning everyone...")
    print(file,'\n')     # Print type/data of file created

# We don't have to close the file here eplicitly

file = open("file.txt")
print(file.read())