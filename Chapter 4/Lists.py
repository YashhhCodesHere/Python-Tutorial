friends = ["Yash", "Robinn", "Patna", "James Bond 007", 117, True]
nums = [12, 94, 192, 1, 31, 88]

print(type(friends))

# List Indexing:

print(f"1st Index is {friends[1]} & 2nd index is {friends[3]} in friends list!")

friends[1] = "Robin Singh Rajput" # List index modification i.e., they are mutable

print(friends)
print(friends[1:5])

# List Methods:

friends.append("Baatu Titan") # Adds Baatu Titan at the last of the list
print(friends)

nums.sort() # Sort the list in increasing form
print(nums)
nums.reverse() # Sort the list in decreasing form
print(nums)

friends.insert(1, "Leo Leo") # Insert Leo Leo at 1st index in friends list
print(friends)

nums.pop(3) #Deletes 3rd index value
print(nums)

nums.remove(192) # Delete specifically 192 from the list
print(nums)