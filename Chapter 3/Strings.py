name = "Yash Kumar"
alphabets = "abcdefghijklmnopqrstuvwxyz"

# String slicing:-

surname = name[-6:] # last index is always excluded!

print("Your surname is:", surname) 

# Slicing with skipping values with equal intervals:-

print(name[0:8:3]) # Every third alphabets will be printed including 1st one!

# Length of String:

print(len(name))
print(len(alphabets))

# Checking string starts or ends with:   (This function is case sensitive!)

print(name.endswith("ar"))
print("Alphabets string starts with abcb:", alphabets.startswith("abcb "))

# Counting character:

print(name.count("a"))

# Find word's index:-

print(f"The word 'Kumar' is at",name.find("Kumar"),"th index")

# Replacing words in the string:

replaced_word = name.replace("Kumar", "Singh Rajput")
print(replaced_word)