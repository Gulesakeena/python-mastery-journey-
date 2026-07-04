'''
🏦 Banking Interest Calculator

Build a console application that:

Takes:
Customer Name
Account Number
Principal Amount
Annual Interest Rate
Time (Years)

Calculates:

Simple Interest
Total Amount
Monthly Interest
Daily Interest

Output Example:

========== BANK REPORT ==========
Customer : Gule
Account  : 12345678

Principal : 100000
Interest  : 12000
Total     : 112000

Monthly Interest : 1000
Daily Interest   : 32.87
=================================
'''


# -----------------------------------------
# Simple Interest Calculator
# -----------------------------------------

print("=" * 50)
print("        BANK INTEREST CALCULATOR")
print("=" * 50)

# Customer Information
customer_name = input("Enter Customer Name: ")
account_number = input("Enter Account Number: ")

# Financial Details
principal_amount = float(input("Enter Principal Amount: "))
annual_interest_rate = float(input("Enter Annual Interest Rate (%): "))
time_years = float(input("Enter Time (Years): "))

# Calculations
simple_interest = (
    principal_amount * annual_interest_rate * time_years
) / 100

total_amount = principal_amount + simple_interest

monthly_interest = simple_interest / (time_years * 12)

daily_interest = simple_interest / (time_years * 365)

# Output
print("\n" + "=" * 50)
print("            CUSTOMER DETAILS")
print("=" * 50)

print(f"Customer Name        : {customer_name}")
print(f"Account Number       : {account_number}")
print(f"Principal Amount     : {principal_amount:.2f}")
print(f"Interest Rate        : {annual_interest_rate}%")
print(f"Time                 : {time_years} Years")

print("\n" + "=" * 50)
print("         INTEREST CALCULATION")
print("=" * 50)

print(f"Simple Interest      : {simple_interest:.2f}")
print(f"Total Amount         : {total_amount:.2f}")
print(f"Monthly Interest     : {monthly_interest:.2f}")
print(f"Daily Interest       : {daily_interest:.2f}")

print("=" * 50)

