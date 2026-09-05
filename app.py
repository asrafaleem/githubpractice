def welcome():
    print("Welcome to my application")


def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid username or password")


welcome()
login("admin", "1234")