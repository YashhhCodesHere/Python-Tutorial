marksList = {
    "Yash" : 100 ,
    "Robinn" : 99.5 , 
    "Harsh" : 100 ,
    "Abhay" : 88,
    "Ankur" : 95,
    "Tushar" : 34
}
print(f"The type of marks list is {type(marksList)} & it's Key-Value is {marksList}")

print(f"Yash & Abhay having mark are \'{marksList['Yash']}\' & \'{marksList['Abhay']}\' respectively...")

print(f'{marksList.items()}') # They will gonna return keys along with their values in tuple value!

print(marksList.keys()) # They will gonna return values in tuple value!

marksList.update({"Yash" : 101, "Aniket" : 100}) # Key of 'Yash' get updated & of 'Aniket' get added as it wasn't there in the dict.

print(marksList) 

# print(marksList.get("Robin")) - This will gonna show 'None' value if that key isn't exists in the dict.

# print(marksList["Robin"]) - This will gonna show an error if that key isn't exists in the dict.

print(f"The marks of Robinn are: {marksList.pop("Robinn")}") # Remove the key and return it's value
print(marksList)
