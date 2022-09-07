import random
name_string = "Angela, Ben, Jenny, Michael, Chloe"
# print(name_string)
names = name_string.split(", ")
person = names[random.randint(0, len(names)-1)]


# names_string = names[random.randint(0, (len(names) - 1))]
print(f"{person} is going to buy the meal today!")
