import json

filename = 'text.json'

my_dict = {
    "name": "sample",
    "age": 0
}

with open(filename, 'w') as file:
    json.dump(my_dict, file, indent=4)

with open(filename, 'r') as file:
    data = json.load(file)
    print(data)