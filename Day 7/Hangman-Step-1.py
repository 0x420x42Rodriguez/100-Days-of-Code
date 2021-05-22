# A game of Hangman built with Python
import random


#  Set a wordlist
word_list = ["aardvark", "baboon", "camel"]

#  Pick random word
chosen_word = random.choice(word_list)

#  Get a letter from user
print("Welcome to Hangman. ")
print("_" * len(chosen_word))

#TODO1
user_answer = []  # List to put user guess into

#TODO2
guess = input("Please guess a letter: ").lower()

#TODO3

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")