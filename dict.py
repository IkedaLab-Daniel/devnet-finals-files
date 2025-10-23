my_dict = {
    'name': ['ice', 'daniel', 'mark', 'callejas'],
    'school': 'MCC',
    'age': 20
    }
# print(my_dict['name'], my_dict['name'][1])
# print(my_dict['school'])
# print(my_dict['age'])

for i, name in enumerate(my_dict["name"], start=1):
    print(f"{i}. Name: ", name)

# how to print: ('name', ['ice', 'daniel', 'mark', 'callejas'])
print(('name', my_dict['name']))

# Create a dictionary
persons = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}  

print(persons)
print("\n---- 1 - keys:")
for i, person in enumerate(persons, start=1):
    print(f"Key {i}: {person}")

print("\n---- 2 - keys:")
keys = persons.keys()
for i, key in enumerate(keys, start=1):
    print(f"Key {i}: {key}")
print(keys)
