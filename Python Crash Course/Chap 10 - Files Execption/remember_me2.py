import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as fileobject:
            username = json.load(fileobject)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as file_object:
            # store data
            json.dump(username, file_object)
            print(f"We will remember you when you came back, {username} !")


greet_user()
