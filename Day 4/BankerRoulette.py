# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

num_of_people = len(names)  #Get the number of names in the list

random_number = random.randint(0, num_of_people - 1)  # Get a random int up between 0 and the num of people

person_paying_for_meal = names[random_number]  # Choose a name

print(f"{person_paying_for_meal} is buying the meal today. ")