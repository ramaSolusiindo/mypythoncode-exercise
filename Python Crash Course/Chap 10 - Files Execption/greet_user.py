import json

filename = 'usernamex.json'

with open(filename) as file_object:
    username = json.load(file_object)
    print(f"Welcome back, {username}")
