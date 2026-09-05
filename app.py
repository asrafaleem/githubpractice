def welcome():
    print("Welcome to my application")


VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"



def login(username, password):
    if username == "admin" and password == "1234":
        print("Login successful")
    else:
        print("Invalid username or password")


welcome()
login("admin", "1234")