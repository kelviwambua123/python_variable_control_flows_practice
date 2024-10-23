# Ask the user to enter a password
#6. Password Validator

password = input("Enter your password: ")  # Get the password input from the user

# Check if the entered password is correct
if password == "python123":
    print("Access granted.")  # Password is correct
else:
    print("Access denied.")  # Password is incorrect
