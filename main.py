import json

def load_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except:
        pass

def save_data(updated_data):
    with open('users.json', 'w') as file:
        json.dump(updated_data, file, indent=4)

def register():
    # > STEP 1: LOAD THE DATAAA
    users = load_data()

    # > STEP 2: Input user info
    username = input("Enter username: ")

    if username in users: 
        print("""
     |---------------------------|         
     |  Username already exists  |
     |---------------------------|
              """)
        return
    
    password = input("Enter password: ")
    name = input("Enter your name: ")

        # > basically, hahapanin niyan yung users[username],
        # > pero di pa siya exists (username exist validation above),
        # > so iwri-write niya yund data instead of edit
    users[username] = {     
        "password": password,
        "name": name,
        "bio": "",
        "posts": []
    }

    # > STEP 3: Saving
    save_data(users)
    print("""
    |---------------------------------|    
    |    Registration successful!     |
    |---------------------------------|
    """)

def login():
    # > Step 1: Load data
    users = load_data()
    username = input("Enter username: ")
    password = input("Enter password: ")
    if ((username in users) and ((users[username]["password"] == password))):
        print("Login successful!")
        profile_menu(username)
    else:
        print("""
    |----------------------------------|    
    |   Invalid username or password.  |
    |----------------------------------|    
    """)

def menu():
    print("""
    |---------- Menu -----------|
    |    1  |      Register     |
    |    2  |      Login        |
    |---------------------------|
    |  enter 'quit' to exit     |
    |---------------------------|
    """)

# > Menu after user logged in
def profile_menu(username):
    while True:
        print(f"""\n
    |-- Welcome to Fakebook CLI-----|
           User: {username} 
    |     1    |    View Profile    |
    |     2    |    Update Bio      |
    |     3    |    Create Post     |
    |     4    |    View Posts      |
    |     5    |    Logout          |
    |-------------------------------|
 """)

        choice = input("Enter your choice: ")

        if choice == '1':
            view_profile(username)
        elif choice == '2':
            update_bio(username)
        elif choice == '3':
            create_post(username)
        elif choice == '4':
            view_posts(username)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

def view_profile(username):
    users = load_data()
    user = users[username] # > the specific user na naka-login

    print(f"""
    |----------------------------------|    
            Name: {user['name']}
            Bio: {user['bio']}
    |----------------------------------|
 """)


def update_bio(username):
    users = load_data()

    new_bio = input("Enter your new bio: ")
    users[username]["bio"] = new_bio
    save_data(users)
    print("""
    |----------------------------------|    
    |    Bio updated successfully!     |
    |----------------------------------|    
    """)

def create_post(username):
    users = load_data()
    post = input("Enter your post: ")
    users[username]["posts"].append(post)
    save_data(users)
    print("""
    |----------------------------------|    
    |    Post created successfully!    |
    |----------------------------------|    
          """)

def view_posts(username):
    users = load_data()
    posts = users[username]["posts"]
    if posts:
        print("\nYour Posts:")
        for i, post in enumerate(posts, 1):
            print(f"{i}. {post}")
    else:
        print("""
    |----------------------------------|        
    |       You have no posts yet.     |
    |----------------------------------|    
""")
    

def main():
    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == 'quit':
            print("""
    |------------- Bye -------------|
    |    Pls, don't forget your     |
    |     username and password     |
    |-------------------------------|
                  """)
            break
        else:
            print("""
    |----------------------------------|    
    |          Invalid choice          |
    |----------------------------------|    
    """)

main()