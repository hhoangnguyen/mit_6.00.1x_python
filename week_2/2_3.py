"""
Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within
12 months. By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year
Using Bisection Search to Make the Program Faster and get accurate monthly payment to the cent
"""


def balance_one_year_payoff_bisection_search(balance, annual_interest_rate, monthly_payment_lower_bound=0.0, monthly_payment_upper_bound=0.0):
    # save original balance for sub-sequence recursive calls
    original_balance = balance

    # this is actually never change
    monthly_interest_rate = annual_interest_rate / 12.0

    # calculate lower and upper bound if needed
    if monthly_payment_upper_bound <= 0:
        monthly_payment_lower_bound = balance / 12
    if monthly_payment_upper_bound <= 0:
        monthly_payment_upper_bound = (balance * (1 + monthly_interest_rate)**12) / 12.0
    minimum_fix_monthly_payment = (monthly_payment_lower_bound + monthly_payment_upper_bound) / 2

    # calculate balance after 1 year for current minimum_fix_monthly_payment
    for month in range(12):
        monthly_unpaid_balance = balance - minimum_fix_monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

    # base case, return if balance within 1 cent
    if balance <= 0.01 and balance >= -0.01:
        return round(minimum_fix_monthly_payment, 2)

    # recursive steps
    # still have balance left meaning we need to pay more, so replace lower_bound = minimum_fix
    if balance > 0:
        return balance_one_year_payoff_bisection_search(original_balance, annual_interest_rate, minimum_fix_monthly_payment, monthly_payment_upper_bound)
    # negative balance meaning we need to pay to much, so replace upper_bound = minimum_fix
    if balance < 0:
        return balance_one_year_payoff_bisection_search(original_balance, annual_interest_rate, monthly_payment_lower_bound, minimum_fix_monthly_payment)

print('Lowest Payment:', balance_one_year_payoff_bisection_search(999999, 0.18))
