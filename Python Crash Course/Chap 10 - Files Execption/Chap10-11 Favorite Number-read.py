import json

filename = 'favnumber.json'
with open(filename) as file_object:
    userfavnum = json.load(file_object)

print(f"I know your favorite number! It's {userfavnum}")





