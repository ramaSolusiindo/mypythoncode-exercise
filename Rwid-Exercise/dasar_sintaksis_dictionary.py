users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}

print(users["name"])
print(users["address"]["street"])
print(users["address"]["geo"]["lat"])

import json

filename = 'dump.json'

with open(filename, 'w') as file_object:
    result = json.dumps(users)
    file_object.write(result)

with open('dump_2.json', 'w') as file_object:
    json.dump(users, file_object)

