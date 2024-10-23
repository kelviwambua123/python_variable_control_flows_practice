# Ask the user to enter a number representing the day of the week
#8. Day of the Week Checker
day_number = int(input("Enter a number (1 to 7) to get the corresponding day of the week: "))  # Convert input to an integer

# Check the entered number and print the corresponding day
if day_number == 1:
    print("Day 1: Sunday")  # 1 corresponds to Sunday
elif day_number == 2:
    print("Day 2: Monday")  # 2 corresponds to Monday
elif day_number == 3:
    print("Day 3: Tuesday")  # 3 corresponds to Tuesday
elif day_number == 4:
    print("Day 4: Wednesday")  # 4 corresponds to Wednesday
elif day_number == 5:
    print("Day 5: Thursday")  # 5 corresponds to Thursday
elif day_number == 6:
    print("Day 6: Friday")  # 6 corresponds to Friday
elif day_number == 7:
    print("Day 7: Saturday")  # 7 corresponds to Saturday
else:
    print("Invalid input. Please enter a number between 1 and 7.")  # Handle invalid input
