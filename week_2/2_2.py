"""
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within
12 months. By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year
"""


def balance_one_year_payoff(balance, annual_interest_rate, minimum_fix_monthly_payment=10):
    # save original balance for sub-sequence recursive calls
    original_balance = balance

    # this is actually never change
    monthly_interest_rate = annual_interest_rate / 12.0

    # calculate balance after 1 year for current minimum_fix_monthly_payment
    for month in range(12):
        monthly_unpaid_balance = balance - minimum_fix_monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    # recursive steps
    if balance > 0:
        return balance_one_year_payoff(original_balance, annual_interest_rate, minimum_fix_monthly_payment+10)

    # balance is <= 0, we're done
    return minimum_fix_monthly_payment

print('Lowest Payment:', balance_one_year_payoff(1715.98, 0.6))
