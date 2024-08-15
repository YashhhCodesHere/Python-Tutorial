Set = {1,2,3,"Robinn"} # Creates a set
print(Set, type(Set))

emptySet = set() # Syntax to create an empty set
print(emptySet)
emptySet.add(24) 
print(emptySet)

# Union of Sets:

s = {5,19,20,38,11}
u = {1,10,31,52, 11}

print("Union are:",s.union({9,100,5,18,20})) # Prints all the elements present in both the sets

print("Intersections are:",s.intersection(u)) # Prints the common elements present in both the sets