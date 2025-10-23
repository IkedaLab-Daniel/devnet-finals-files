
# Create a dictionary
person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New York"
}

# Access dictionary values
print(f'First Name: {person["first_name"]}')
print(f'Age: {person["age"]}')

# Add a new key-value pair
person["email"] = "john.doe@example.com"

# Update a value
person["age"] = 31

# Remove a key-value pair
del person["city"]

# Iterate through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
