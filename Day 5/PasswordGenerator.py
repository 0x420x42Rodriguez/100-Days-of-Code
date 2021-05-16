#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

pass_letters = []
pass_symbols = []
pass_numbers = []

#  Create list of random letters
for letter in range(1, nr_letters + 1):
    random_letter = random.randint(0, len(letters) - 1)
    pass_letters.append(letters[random_letter])


#  Create list of random numbers
for number in range(1, nr_numbers + 1):
    random_number = random.randint(0, len(numbers) - 1)
    pass_numbers.append(numbers[random_number])


#  Create list of random symbols
for symbol in range(1, nr_symbols + 1):
    random_symbol = random.randint(0, len(symbols) - 1)
    pass_symbols.append(symbols[random_symbol])

#  Print generated password
password_chars = pass_letters + pass_symbols + pass_numbers
user_password = ""

#  Iterate through all the lists and add to new string variable
for char in password_chars:
    user_password += char

print(user_password)

