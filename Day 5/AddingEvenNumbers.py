# Add all even numbers together between 1 and 100

accumulator = 0

for number in range(1, 101):
    if number % 2 == 0:
        accumulator += number
        
print(accumulator)