"""
 Exercise write a program that prompt the user for their name and write their name to a file
 called guest.txt
"""


filename = '../Chap 9 - Class/guest_book.txt'
print("Type 'quit' if you want finished")
while True:
    username = input('Please type your name : ')
    if username == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{username.title()} \n")
            print(f"Greeting {username.title()}, your name has been added")


"""
with open(filename, 'w') as file_object:
    while username is True:
        print(f"Greeting {username.title()}")
        file_object.write(username)
        break
    else:
        print("Please retype your name")


"""