# 1.

print('''The poem going to be starts from now:- 


Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!
Twinkle Twinkle, Little Star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle Twinkle Little Star
How I wonder what you are!\n''')

# 2.

# import pyttsx3
# engine = pyttsx3.init()
# engine.say("I will speak this text")
# engine.runAndWait()

# 4.

import os

directory = '.'  # Change this to the path of the directory you want to list
print('\n'.join(os.listdir(directory)))
