"""
Purpose: Check even-ness of a given number, in runtime.
"""
# Alogorithm: determining odd/even status using the modulus arithmetic operator

number = 33
print(f"{number             = }")
print(f"{number / 2         = }")
print(f"{number % 2         = }")
print(f"{number % 2 == 0    = }")

if number:
    print(f"{number} is a non-zero number")
else:
    print("It is zero")

"""
It can evaluate that
    number != None and
    number != False and
    number != 0 and
    number != ""
"""
if (number%2==0):
    print(f"{number} is a even number")

if number%2 :
    print(f"{number} is a odd number")

#------
# Assignment: Generate even numbers between 45 & 137
# loop values between limits, test eveness for each number
# and display, if it is even

# TIP - range, if condition within it, print function

for num in range(45,137):
    if(num%2==0):
        print(f"{num} is an even number")

