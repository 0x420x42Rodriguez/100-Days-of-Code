print("Welcome to the tip calculator.")
bill_total = float(input("What was the total bill? $"))  # Get bill total as int
tip_percentage = int(input("What percentage would you like to tip? "))  # Get desired tip percentage as int
number_of_people = int(input("How many people are splitting the bill? "))  # Get number of people splitting the bill as int

total_tip = bill_total * (tip_percentage / 100)  # find the tip for the bill

bill_with_tip = total_tip + bill_total  # Add tip to bill

personal_bill = bill_with_tip / number_of_people  # Split bill and tip evenly

final_amount = "{:.2f}".format(personal_bill)  # Format result to 2 decimal places

print(f"Each person should pay: ${final_amount}") 
