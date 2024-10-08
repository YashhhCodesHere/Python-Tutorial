#1.

with open("Poem.txt", "r") as f:
    content = f.read().lower()
    if("Twinkle".lower() in content):
        print("It contains Twinkle!")
    else:
        print("It contains Twinkle!")

#2.

import random

def game():
    print('''You're Playing a game...
Your score is: ''', end="")
    score = random.randrange(0, 100)
    print(score)
    return score

result = game()

try:
    with open("Hi-score.txt", "r") as f:
        content = f.read()
        if content.strip():  # Check if content is not empty or only whitespace
            high_score = int(content)
        else:
            high_score = 0
except FileNotFoundError:
    high_score = 0  # If file doesn't exist, treat high score as 0

if result > high_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(result))  # Write the new high score
    print(f"New high score: {result}")
else:
    print(f"Your score of {result} did not beat the high score of {high_score}")

#3.

def Generate_Table(num):
    table = ""
    for j in range(1,11):
        table += (f"{num} * {j} = {num*j} \n")
    return table
        

for i in range(2,21):
    with open(f"Table{i}.txt", "w") as f:
        f.write(Generate_Table(i))

#4. 

word = "Donkey".lower()

with open("Censored.txt", "r") as f:
    # f.write("Actually, you're a Donkey... I'm not a donkey! Okay donkey!!")
    content = f.read().lower()

new_content = content.replace(word, "######")

with open("Censored.txt", "w") as f:
    f.write(new_content)