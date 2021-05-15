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

print("Welcome to Rock, Paper, Scissors. ")
user_choice = input("Type 'rock' 'paper' or 'scissors' to make your choice! ").lower()

computer_choice = random.randint(1, 3)  # Get random number for computer choice

if computer_choice == 1:  # Get computer input to print ASCII art
    print(f"The computer chose \n {paper}")
elif computer_choice == 2:
    print(f"The computer chose \n {paper}")
else:
    print(f"The computer chose \n {scissors}")

if user_choice == "rock":
    print(rock)
    if computer_choice == 1:
        print("It's a tie!")
    elif computer_choice == 2:
        print("Paper beats rock, you lose!")
    else:
        print("Rock beats scissors, you win!")

if user_choice == "paper":
    print(paper)
    if computer_choice == 1:
        print("Paper beats rock, you win!")
    elif computer_choice == 2:
        print("It's a tie!")
    else:
        print("Scissors beat paper, you lose!")

if user_choice == "scissors":
    print(scissors)
    if computer_choice == 1:
        print("Rock beats scissors, you lose!")
    elif computer_choice == 2:
        print("Scissors beat paper, you win!")
    else:
        print("It's a tie!")        