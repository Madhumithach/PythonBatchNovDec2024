"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php

"""
principal_balance=1000
rate_of_interest=0.2
time=2
SI=principal_balance*(1+rate_of_interest*time)
print("Simple interest :",SI)








# Assignment
# 1. Compound Interest Calculation
#     ref: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php
#A=p(1+r/n)nt
n=5
CI=principal_balance*(1+rate_of_interest/n)**(n*time)
print(CI)