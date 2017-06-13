"""
Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment
required by the credit card company each month.

The following variables contain values as described below:
1. balance - the outstanding balance on the credit card
2. annualInterestRate - annual interest rate as a decimal
3. monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months,
print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy
"""


def balance_one_year(balance, annual_interest_rate, monthly_payment_rate):
    # this is actually never change
    monthly_interest_rate = annual_interest_rate / 12.0

    # calculate balance after 1 year
    for month in range(12):
        minimum_monthly_payment = monthly_payment_rate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
    return round(balance, 2)

print('Remaining balance:', balance_one_year(42, 0.2, 0.04))
