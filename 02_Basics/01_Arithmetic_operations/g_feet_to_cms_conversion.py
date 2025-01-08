"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results
"""
feet=int(input("Enter number of feet"))
inches=12*feet
centi=2.54*inches
print("Inches=",inches)
print("centimeters=",centi)