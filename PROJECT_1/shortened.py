'''
1 for snake
-1 for water
0 for gun
'''

import random # importing the random module to generate random choices for the computer

computer = random.choice([1, -1, 0]) # random.choice() selects a random element from the list
youstr = input("Enter your choice (snake, water, gun): ").strip().lower() # .strip() removes leading and trailing whitespace, lower() converts the input to lowercase
youDict = {"s": 1, "snake": 1, "w": -1, "water": -1, "g": 0, "gun": 0}
reverseYouDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict.get(youstr) # .get() returns None if the key is not found in the dictionary

if you is None:
   print("Invalid choice. Please enter snake, water, or gun.")
   raise SystemExit

print(f"you chose {reverseYouDict[you]} and computer chose {reverseYouDict[computer]}") # f-string is used to format the output string with the values of you and computer


if(computer == you):
    print("It's a tie! No one wins.")

# Logic on the basis of the difference between computer and you
else:
    if(computer - you == 1 or computer - you == -2):  # if(computer - you == -1 or computer - you == 2) you lose 
        print("You win!")
    else:
        print("You lose!")

''' 
else:
 if(computer == -1 and you == 1):
    print("You win! Snake drinks water.")

 elif(computer == 1 and you == -1):
    print("You lose! Snake drinks water.")

 elif(computer == 0 and you == 1):
    print("You lose! Gun kills snake.")

 elif(computer == 1 and you == 0):
    print("You win! Gun kills snake.")

 elif(computer == 0 and you == -1):
    print("You win! Water damages gun.")

 elif(computer == -1 and you == 0):
    print("You lose! Water damages gun.")
 else:
    print("Something went wrong! Please try again.")
'''