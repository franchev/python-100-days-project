# rock paper scissors
# rules
#0 Rock wins against scissors.
#1 Paper wins against rock.
#2 Scissors win against paper.
# 0 > 2, 1 > 0, 2> 1

import random

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

image_list = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choice = random.randint(0,2)

if human_choice > 2 or human_choice < 0:
    print("This is not a valid option")
else:
    print(image_list[human_choice])
    print("Computer Choose: %s" % image_list[computer_choice])
    if human_choice == 0 and computer_choice == 2:
        print("You win")
    elif human_choice == 1 and computer_choice == 0:
        print("You win")
    elif human_choice == 2 and computer_choice == 1:
        print("You win")
    else:
        print("You lose")
