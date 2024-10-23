# Ask the user to input a score between 0 and 100
# 4. Simple Calculator with Conditionals
score = int(input("Enter your score (0-100): "))  # Convert the input to an integer

# Grade categorization based on the score
if 90 <= score <= 100:
    print("Your grade is: A")  # Score between 90 and 100
elif 80 <= score < 90:
    print("Your grade is: B")  # Score between 80 and 89
elif 70 <= score < 80:
    print("Your grade is: C")  # Score between 70 and 79
elif 60 <= score < 70:
    print("Your grade is: D")  # Score between 60 and 69
elif 0 <= score < 60:
    print("Your grade is: F")  # Score below 60
else:
    print("Invalid score. Please enter a number between 0 and 100.")  # Handle invalid inputs
