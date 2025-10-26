import json

# Example JSON string
json_data = '{"name": "Alice", "age": 30, "isStudent": false, "courses": ["Math", "Science"]}'

# Parsing JSON string to Python dictionary
python_dict = json.loads(json_data)
print(f"Parsed Python dictionary: {python_dict}")
print(f"Name: {python_dict['name']}")

# Encoding Python dictionary to JSON string
new_data = {"city": "New York", "population": 8000000}
json_output = json.dumps(new_data, indent=4) # indent for pretty printing
print(f"\nEncoded JSON string:\n{json_output}")

# Writing to a JSON file
with open("data.json", "w") as f:
    json.dump(python_dict, f, indent=4)