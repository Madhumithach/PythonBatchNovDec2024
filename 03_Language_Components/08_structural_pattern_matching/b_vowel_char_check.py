"""
Purpose: To check largest of give two numbers
"""
num1=int(input("Enter number1:"))
num2=int(input("Enter number2:"))
match num1>num2:
    case True:
        print(f"{num1} is the largest number")
    case False:
        print(f"{num2} is the largest number")

letter = input("Enter any character:").strip()


if letter in "aeiou":
    print(f"{letter} is a LOWER VOWEL CHARACTER")
elif letter in "AEIOU":
    print(f"{letter} is a UPPER VOWEL CHARACTER")
else:
    print(f"{letter} may be a CONSONANT")

# match letter:
#     case (letter in "aeiou"):
#         print(f"{letter} is a LOWER VOWEL CHARACTER")
#     case (letter in "AEIOU"):
#         print(f"{letter} is a UPPER VOWEL CHARACTER")
#     case _:
#         print(f"{letter} may be a CONSONANT")

# NOTE: in operator wont work in match condition check
