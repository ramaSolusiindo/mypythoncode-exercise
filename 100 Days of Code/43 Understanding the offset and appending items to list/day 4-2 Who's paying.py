import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

names_string = names[random.randint(0, (len(names) - 1))]
print(f"{names_string} is going to buy the meal today!")
