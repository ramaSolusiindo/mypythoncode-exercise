import json

filename = 'username.json'


def userinput():
    username = input("What is your name? ")
    with open(filename, 'w') as file_object:
        # store data
        json.dump(username, file_object)
        print(f"We will remember you when you came back, {username} !")


def greet_user():
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except json.decoder.JSONDecodeError:
        userinput()
    except FileNotFoundError:
        userinput()
    else:
        print(f"Welcome back, {username}!")

greet_user()
