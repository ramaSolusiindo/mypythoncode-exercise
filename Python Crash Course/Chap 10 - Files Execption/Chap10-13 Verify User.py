import json


def load_user():
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            content = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return content



def get_new_username():
    filename = 'username.json'
    user_input = input("Please enter your name : ")
    with open(filename, 'w') as file_object:
        json.dump(user_input, file_object)
        print("Thanks your name has been record")
    return user_input


try:
    with open(filename) as file_object:
        content = json.load(file_object)
        askuser = input(f"Is this your username '{content}' ?")

except FileNotFoundError:
    get_new_username()
else:
    greet_user()

