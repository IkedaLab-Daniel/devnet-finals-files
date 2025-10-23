from colored import Fore, Style

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
    print(f"{Fore.green}Key {i}: {person}{Style.reset}")

print("\n---- 2 - keys:")
keys = persons.keys()
for i, key in enumerate(keys, start=1):
    print(f"Key {i}: {key}")
print(keys)

# > ---------------- Changing a Value -----------------------------------------
print(f"\n{Fore.green}")
new_dict = {
    'name': ['daniel']
}

print(f"\nStart List:")
print(new_dict)

name = new_dict["name"][0]
print(name)

new_dict['name'] = 'ice' # > Change value
changed_name = new_dict['name']  # > GET changed value
print(changed_name) # > print

print(f"\nUpdated List:")
print(new_dict)

print(f"{Style.reset}")

# > ---------------- Changing a Key -----------------------------------------

another_new_dict = {
    'name': 'ice'
}

print(f"\n{Fore.blue}Start dict")
print(another_new_dict)

another_new_dict['first_name'] = another_new_dict.pop('name')  # > Change key
print("\nNew dict")
print(another_new_dict)
