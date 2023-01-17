"""
Optional bonus. See course site for details.

Jim Crivello
1/16/2023
In this module, we provide an introduction to programming and basic descriptive analytics. We explore the world of data 
analytics and configure our environment with professional tools and begin to explore the foundations of programmatically 
analyzing data.  

"""

import random

# Fix the code below to print the name using an f-string
# Right now, the user choses wolf everytime.
# Modify the code so the user is asked to
# enter wolf, eagle, or snake.
# Hint: use the input() function
#user_choice = "wolf"
# Change the name below to a name of your choice

name = "ForestMaster"

print()
print("Hello, I'm", (f'{name}'), "your gamebot.")
print("Let's play an animal guessing game!")
print("There are 3 animals: wolf, eagle, snake (a Python of course).")
print("The wolf scares the eagle.")
print("The eagle grabs the snake.")
print("The snake bites the wolf.")
print("I'll pick one and you pick one and we'll see who wins.")
print()

# System prompts the user for an animal
user_choice = input("Your turn to pick. Type in wolf, eagle, or snake.  ")
# Now the bot will pick one
buddy_choice = random.choice(["wolf", "eagle", "snake"])

# Report the choices
print()
print(f"You said {user_choice}.")
print(f"I said {buddy_choice}.")
print()

# Now we need to compare the choices and determine the winner
# Complete the logic to
# compare the choices and print who won
# In Python, indentation is important!

# Evaluate all scenarios and display who won
if user_choice == buddy_choice:
    print("We tied!")
if user_choice == "wolf" and buddy_choice == "eagle":
    print("You win this round!")
if buddy_choice == "wolf" and user_choice == "eagle":
    print("I win this round!")
if user_choice == "eagle" and buddy_choice == "snake":
    print("You win this round!")
if buddy_choice == "eagle" and user_choice == "snake":
    print("I win this round!")
if user_choice == "snake" and buddy_choice == "wolf":
    print("You win this round!")
if buddy_choice == "snake" and user_choice == "wolf":
    print("I win this round!")
print()
print()
# When you finish,
# right-click on the code and select "Format Document"

# Run the code, and play the game a few times.
# Copy the output from the terminal and paste it into the
# docstring comment below.
# --------------------------------------------------------------------
"""

PS C:\Users\JMC\Documents\datafun-01-getting-started> & C:/Users/JMC/anaconda3/python.exe c:/Users/JMC/Documents/datafun-01-getting-started/xtra_p1.py

Hello, I'm ForestMaster your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
I'll pick one and you pick one and we'll see who wins.

Your turn to pick. Type in wolf, eagle, or snake.  eagle

You said eagle.
I said snake.

You win this round!


PS C:\Users\JMC\Documents\datafun-01-getting-started> & C:/Users/JMC/anaconda3/python.exe c:/Users/JMC/Documents/datafun-01-getting-started/xtra_p1.py

Hello, I'm ForestMaster your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
I'll pick one and you pick one and we'll see who wins.

Your turn to pick. Type in wolf, eagle, or snake.  snake

You said snake.
I said wolf.

You win this round!


PS C:\Users\JMC\Documents\datafun-01-getting-started> & C:/Users/JMC/anaconda3/python.exe c:/Users/JMC/Documents/datafun-01-getting-started/xtra_p1.py

Hello, I'm ForestMaster your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
I'll pick one and you pick one and we'll see who wins.

Your turn to pick. Type in wolf, eagle, or snake.  wolf

You said wolf.
I said snake.

I win this round!

PS C:\Users\JMC\Documents\datafun-01-getting-started> & C:/Users/JMC/anaconda3/python.exe c:/Users/JMC/Documents/datafun-01-getting-started/xtra_p1.py

Hello, I'm ForestMaster your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
I'll pick one and you pick one and we'll see who wins.

Your turn to pick. Type in wolf, eagle, or snake.  wolf

You said wolf.
I said eagle.

You win this round!

PS C:\Users\JMC\Documents\datafun-01-getting-started> & C:/Users/JMC/anaconda3/python.exe c:/Users/JMC/Documents/datafun-01-getting-started/xtra_p1.py

Hello, I'm ForestMaster your gamebot.
Let's play an animal guessing game!
There are 3 animals: wolf, eagle, snake (a Python of course).
The wolf scares the eagle.
The eagle grabs the snake.
The snake bites the wolf.
I'll pick one and you pick one and we'll see who wins.

Your turn to pick. Type in wolf, eagle, or snake.  wolf

You said wolf.
I said wolf.

We tied!


PS C:\Users\JMC\Documents\datafun-01-getting-started> 


"""
