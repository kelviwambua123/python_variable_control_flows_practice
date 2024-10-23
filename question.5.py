# Ask the user to input their age
#5. Simple Age Checker
age = int(input("Enter your age: "))  # Convert the input to an integer

# Age categorization based on the user's input
if age < 18:
    print("You are a minor.")  # Age is less than 18
elif 18 <= age <= 65:
    print("You are an adult.")  # Age is between 18 and 65 (inclusive)
elif age > 65:
    print("You are a senior.")  # Age is greater than 65
else:
    print("Invalid age. Please enter a positive number.")  # Handle invalid input like negative ages
