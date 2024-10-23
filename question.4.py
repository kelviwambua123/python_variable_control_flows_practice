# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))  # Convert the input to a float
num2 = float(input("Enter the second number: "))  # Convert the input to a float

# Ask the user to input an operation (+, -, *, /)
operation = input("Enter an operation (+, -, *, /): ")  # Store the operator as a string

# Perform the operation based on the user input
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")  # Perform addition
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")  # Perform subtraction
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")  # Perform multiplication
elif operation == '/':
    if num2 != 0:  # Check if the denominator is not zero
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")  # Perform division
    else:
        print("Error: Division by zero is not allowed.")  # Handle division by zero
else:
    print("Invalid operation. Please enter one of +, -, *, /.")  # Handle invalid operator input
