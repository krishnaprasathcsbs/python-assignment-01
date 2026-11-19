# Q1: Username Validation System

# Accept the username from the user
username = input("Enter a username: ")

# Rule 2 is checked first so a spaces-only input gets the most accurate reason
if username.strip() == "":
    # strip() removes spaces; if nothing is left, the username was only spaces
    print("Invalid username: it must not contain only spaces.")
elif len(username) < 5:
    # Rule 1: at least 5 characters
    print("Invalid username: it must contain at least 5 characters.")
elif username.lower() == "admin":
    # Rule 3: compare in lowercase so "admin", "ADMIN", "Admin" are all rejected
    print("Invalid username: 'admin' is not allowed (case-insensitive).")
else:
    print("Valid username.")
