# promt the user to enter any number
number = int(input("Enter a number: "))  # Convert input to an integer

# Check if the number is even or odd using modulus operator (%)
if number % 2 == 0:
    print("The number is even.")  # If the remainder is 0, the number is even
else:
    print("The number is odd.")  # If the remainder is not 0, the number is odd
