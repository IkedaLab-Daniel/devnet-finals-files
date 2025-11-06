import json

def load_data():
    with open(USER_DATA, 'r') as file:
        data = json.load(file)
        return data

# > append data 
def save_data(username ,data_to_add):
    with open(f"{username}.json", 'x') as file:
        pass

    with open(f"{username}.json", 'w') as file:
        json.dump(data_to_add, file)


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    bio = input("Enter bio: ")

    to_add = {
        f"{username}": {
            "password": f"{password}",
            "bio": f"{bio}",
            "posts": []
        }
    }   
    print(to_add)
    save_data(username ,to_add)

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    data = load_data()
    if username in data and data[username] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

def view_profile():
    pass

def update_bio():
    pass

def create_post():
    pass

def view_user_post():
    pass

def main():
    while True:
        print("""
        |----- Welcome to FakeBook -----|
        |      1      |   Login         |
        |      2      |   Register      |
        |--------------------------------
        |        'quit' to exit         |
        |-------------------------------|
        """)
        
        choice = input('Choose: ')
        if choice == '1':
            login()
        elif choice == '2':
            register()
        elif choice == 'quit':
            break
        else:
            print("Invalid input")


main()