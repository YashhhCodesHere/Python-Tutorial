#1.

translation = {
    "mai" : "me",
    "tum" : "you",
    "hum" : "we",
    "aaj" : "today"
}
a = input("Enter the word in hindi to see it's english translation: ")
print("English translation of your given word is:",translation.get(a))

#2.

nums = set()

nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
nums.add(int(input("Enter your number:")))
print("All the unique numbers you entered are:", nums)

#3.

b = {18,"18"}
print(b)

#4.

s = set() 
s.add(20) # Here the value of 20 == 20.0 (same)
s.add(20.0) 
s.add('20') # length of s after these operations?
print(s,len(s))

#5.

o = {} # It's dictationary! Not sets! 
p = set() # Null set
print(type(o),type(p))

#6.

favLang = {}

favLang.update({input("Enter your name: "): input("Enter you fav language: ")})
favLang.update({input("Enter your name: "): input("Enter you fav language: ")})
favLang.update({input("Enter your name: "): input("Enter you fav language: ")})
favLang.update({input("Enter your name: "): input("Enter you fav language: ")})
print(favLang)

#9.

s = {8, 7, 12, "Harry", [1,2]} # List can be stored in a set
