rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_int = input("Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user = int(user_int)
ascii = [rock,paper,scissors]

if user>=3 or user<0:
    print("You typed an Invalid number,You lose")
else:
  print(ascii[user])
  comp = random.randrange(0, 3)
  print("Computer Chose:")
  print(ascii[comp])


if (user == 0) and (comp == 2): 
    print(rock, "You win")
elif (user == 0) and (comp == 0):
    print(rock, "It's draws")
elif(comp>user):
  print(rock,"You lose")
elif (user == 1) and (comp == 0):
      print(paper, "You win")
elif (user == 1) and (comp == 1):
    print(paper, "The match is draw")
elif(comp<user):
    print("You lose")

elif(user == 2)and(comp == 1):
  print(scissors, "You win")
elif (user == 2) and (comp == 2):
    print(scissors, "The match is draw")
elif(comp<user):
    print("You lose")

