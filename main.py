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

import random

cpu_answer = random.randint(0, 2)
user_answer = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors\n"))

if user_answer >= 3 or user_answer < 0:
  print("You chose an invalid number. Please try again")
else:
  game_images = [rock, paper, scissors]
  print(game_images[user_answer])
  print("Computer chose:")
  print(game_images[cpu_answer])

  if user_answer == cpu_answer:
    print("Draw")
  elif user_answer > cpu_answer:
    print("You win!")
  elif user_answer < cpu_answer:
    print("You lose")