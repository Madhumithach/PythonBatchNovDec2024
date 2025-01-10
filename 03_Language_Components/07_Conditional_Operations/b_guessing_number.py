"""
Purpose: Number Guessing Game
"""
lucky_number=77
guess_number=int(input("Enter your guessing number"))
#method1
#with if
# if(lucky_number==guess_number):
#     print("You guessed it correct!!")

# method2
# with if else
# if(lucky_number== guess_number):
#     print("you guessed it correct")
# else:
#     print("Please try again")

#method-3 with if-else ladder
if(guess_number == lucky_number):
    print("You guessed it correct")
elif (guess_number > lucky_number):
    print("Please try again by decreasing the guessing number")
elif(guess_number < lucky_number):
    print("Please try again by increasing the guessing number")