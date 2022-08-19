import json

fav_number = input("What is your favorite number ? ")
filename = 'favnumber.json'
with open(filename, 'w') as file_object:
    json.dump(fav_number, file_object)
    print("Thanks I will remembered")



