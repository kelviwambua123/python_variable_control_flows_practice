# Function to check the type of triangle based on the lengths of its sides
#8. Day of the Week Checker
def triangle_type(side1, side2, side3):
    # Check if the sides can form a triangle
    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        # Determine the type of triangle
        if side1 == side2 == side3:
            return "Equilateral"  # All sides are equal
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"  # Two sides are equal
        else:
            return "Scalene"  # All sides are different
    else:
        return "Not a triangle"  # The sides do not form a valid triangle

# Ask the user to enter the lengths of the three sides
side1 = float(input("Enter the length of the first side: "))  # Convert input to float
side2 = float(input("Enter the length of the second side: "))  # Convert input to float
side3 = float(input("Enter the length of the third side: "))  # Convert input to float

# Get the type of triangle based on the lengths of its sides
triangle_result = triangle_type(side1, side2, side3)

# Print the result
print("The triangle is:", triangle_result)
