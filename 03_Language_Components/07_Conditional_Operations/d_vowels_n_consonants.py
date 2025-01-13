#!/usr/bin/python3
"""
Purpose: To check whether the given character
        is vowels or consonant

        vowels - aeiou

in operator  works with any iterable object

Algorithm:
============
1) is it empty 
2) is it alphabet 
3) is it vowel or not 

NOTE: handle case-sensitivity 
"""
##method-1
# alphabet=input("Enter a letter").upper()
# if(alphabet==""):
#     print("String is Empty")
# elif(alphabet=="a"or alphabet=="e" or alphabet=="i"  or alphabet=="o" or alphabet=="u"):
#     print(f"{alphabet} is an vowel")
# else:
#     print(f"{alphabet} is a consonant")
alphabet=input("Enter a letter").upper()
if(alphabet==""):
    print("string is Empty")
elif(alphabet in ["a","e","i","o","u"]):
    print(f"{alphabet} is an vowel")
else:
    print(f"{alphabet} is a consonant")