class Students:
    programming_language = "Python" # This is a class attribute
    salary = 120000

# Object instantiation:- 

Harsh = Students() # Creating an object of the class Students

Harsh.programming_language = "C++" # Here we changed class attribute to instance attribute (Property of the particular object or instance)

print(f"Language used: '{Harsh.programming_language}', Salary: {Harsh.salary}") # Accessing the attributes of the class Students

Robinn = Students()

Robinn.name = "Robin" # This is a instance attribute

print(Robinn.name, Robinn.salary, Robinn.programming_language)

# print(type(objects))
