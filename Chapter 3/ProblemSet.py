# 1.
name = input("Enter your name please: ")
print(f"Good Afternoon {name}!") # f-string used here to place variable inside the string!

#2. 

letter = ''' Dear <|Name|>, 
                        You are selected! 
            
            - <|Date|> '''

print(f"{letter.replace("<|Name|>","Robinn").replace("<|Date|>","18th August, 2024")}") # Two replace commands are merged by using dot

# 3. 

print(f"The number of times Double space occured in the 'name' & 'letter' variables are {name.count("  ")} & {letter.count("  ")} respectively!")

# 4.

print(f"{letter.replace("  "," ")}") # Double spaces are replaced with single space.

# 5.

letter = "Dear Harry, \nThis python course is nice. \nThanks!"
print(letter)