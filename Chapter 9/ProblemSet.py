# #1.

# with open("Poem.txt", "r") as f:
#     content = f.read().lower()
#     if("Twinkle".lower() in content):
#         print("It contains Twinkle!")
#     else:
#         print("It contains Twinkle!")

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
