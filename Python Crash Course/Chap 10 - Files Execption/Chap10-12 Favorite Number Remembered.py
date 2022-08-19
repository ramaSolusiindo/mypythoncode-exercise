"""
 Exercise json load and dump data parsing
"""
import json

filename = 'favnumber.json'

try:
    with open(filename) as file_object:
        favnumber = json.load(file_object)
except Exception:
    with open(filename, 'w') as file_object:
        favnumber = input("What is your favorite number ? ")
        json.dump(favnumber, file_object)
        print("Thanks I will remembered")
else:
    print(f"Hi, your number already stored, this is the {favnumber}")




