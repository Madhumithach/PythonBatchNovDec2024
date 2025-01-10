#!/usr/bin/python3
"""
Purpose: Temperature Conversions
    - celsius to fahrenheit , or vice versa


user input : 23c
output     : xF

user input : 23F
output     : xC

23c, 23C, 23F, 23f
23C, 23F
23 C
23C
"""
temp=input("Enter temperature").lower().strip()

if temp.endswith("c"):
    celsius=int(temp[:-1])
    fahrenheit=(celsius*9/5)+32
    print(f"{fahrenheit}f")
elif temp.endswith("f"):
    fahrenheit=int(temp[:-1])
    celsius=(fahrenheit-32)*5/9
    print(f"{celsius}c")