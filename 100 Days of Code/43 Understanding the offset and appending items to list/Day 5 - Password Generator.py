# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


panjang = len(letters)
panjang_num = len(numbers)
panjang_sym = len(symbols)
# randow_test = letters[random.randint(0, panjang)]


# letter_pass = ""
# for i in range(0, nr_letters):
#     letter_pass += letters[random.randint(0, panjang)]
#
# number_pass = ""
# for i in range(0, nr_numbers):
#     # number_pass += numbers[i]
#     number_pass += numbers[random.randint(0, panjang_num - 1)]
#
# symbols_pass = ""
# for i in range(0, nr_symbols):
#     symbols_pass += symbols[random.randint(0, panjang_sym)]
#
# new_pass = [letter_pass, number_pass, symbols_pass]
# print(f"{rand_newpass}")

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
# for char in range(1, nr_letters + 1):
#     password += random.choice(letters)
# for symbol in range(1, nr_symbols + 1):
#     password += random.choice(symbols)
# for number in range(1, nr_numbers + 1):
#     password += random.choice(numbers)

#print(password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_in_list = []
for char in range(1, nr_letters + 1):
    password_in_list.append(random.choice(letters))
for symbol in range(1, nr_symbols + 1):
    password_in_list += random.choice(symbols)
for number in range(1, nr_numbers + 1):
    password_in_list += random.choice(numbers)

# print(password_in_list)
random.shuffle(password_in_list)
for char in password_in_list:
    password += char
print(f"Your password is : {password}")
print(f"Total character is : ", len(password))
