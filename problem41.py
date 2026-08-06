#Check if a triangle is valid given three sides (sum of any two sides > third side), and if valid, check if it's equilateral, isosceles, or scalene.

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: ")) 
side3 = float(input("Enter the third side of the triangle: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The triangle is not valid.") 
    