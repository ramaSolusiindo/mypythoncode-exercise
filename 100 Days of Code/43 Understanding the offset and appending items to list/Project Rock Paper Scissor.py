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

# Write your code below this line 👇
import random

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer = random.randint(0, 2)
random_comp = [rock, paper, scissors]
result = None

if choose == 0:
    print(choose, rock)
    print("VS")
    if computer == 0:
        print(random_comp[0])
        result = "Draw"
        print(result)
    elif computer == 1:
        print(random_comp[1])
        result = "You Loose"
        print(result)
    elif computer == 2:
        print(random_comp[2])
        result = "You Win"
        print(result)
elif choose == 1:
    print(paper)
    print("VS")
    if computer == 0:
        print(random_comp[0])
        result = "You Win"
        print(result)
    elif computer == 1:
        print(random_comp[1])
        result = "Draw"
        print(result)
    elif computer == 2:
        print(random_comp[2])
        result = "You loose"
        print(result)
elif choose == 2:
    print(scissors)
    print("VS")
    if computer == 0:
        print(random_comp[0])
        result = "You loose"
        print(result)
    elif computer == 1:
        print(random_comp[1])
        result = "You Win"
        print(result)
    elif computer == 2:
        print(random_comp[2])
        result = "Draw"
        print(result)
else:
    print("Please choose 0,1,2")

user_choice = 0
computer_choice = 0

if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number")
else:
    if user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice == 0 and user_choice == 2:
        print("You loose")
    elif computer_choice > user_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")